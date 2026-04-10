import os
import re
import sys
import time
import json
import unicodedata
import markdown
from datetime import datetime, timezone
from notion_client import Client
from dotenv import load_dotenv

TEST_MODE = "--test" in sys.argv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))

RAICES = {
    "290477bc-d0eb-8013-a785-d8784b2f8210": "notas-gcp",
    "290477bc-d0eb-807e-a377-f5b7cbbf8b9e": "notas-git",
    "332477bc-d0eb-8042-be0a-f27c6d6a2013": "notas-ia",
    "290477bc-d0eb-80c5-9a9a-f3e74d79a73f": "notas-bash",
}

CAT_LABELS = {
    "notas-gcp": "Google Cloud Platform",
    "notas-git": "Git & GitHub",
    "notas-ia": "Claude",
    "notas-bash": "Bash & Shell",
}

_DIR          = os.path.dirname(os.path.abspath(__file__))
BASE_MD       = os.path.join(_DIR, "../content")
BASE_HTML     = os.path.join(_DIR, "../docs")
TEMPLATE_PATH = os.path.join(_DIR, "../assets/note_template.html")

# Notion usa nombres de lenguaje distintos a los que esperan los parsers de markdown
LANGUAGE_MAP = {
    "plain text": "",
    "plain_text": "",
    "shell":      "bash",
    "zsh":        "bash",
    "sh":         "bash",
}

try:
    import _imagenes as _img
    _IMG_ENABLED = True
except ImportError:
    _IMG_ENABLED = False

stats = {"actualizadas": 0, "saltadas": 0, "fallidas": 0, "huerfanas": 0}
notas_procesadas = []
archivos_generados = set()
archivos_md_generados = set()

# ────────────────────────────────────────────
# Utilidades
# ────────────────────────────────────────────

def slugify(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r'[^\w\s-]', '', texto)
    texto = re.sub(r'[\s_]+', '-', texto)
    return texto

def notion_fechas(page_id):
    page = notion.pages.retrieve(page_id=page_id)
    modificacion = datetime.fromisoformat(page["last_edited_time"].replace("Z", "+00:00"))
    creacion = page["created_time"]
    return modificacion, creacion

def local_fecha(ruta_html):
    if not os.path.exists(ruta_html):
        return None
    ts = os.path.getmtime(ruta_html)
    return datetime.fromtimestamp(ts, tz=timezone.utc)

def md_to_html(titulo, contenido_md, categoria, grupo):
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()
    cuerpo = markdown.markdown(
        contenido_md,
        extensions=['pymdownx.superfences', 'tables', 'codehilite']
    )
    return (template
        .replace("{{titulo}}", titulo)
        .replace("{{categoria}}", CAT_LABELS.get(categoria, categoria))
        .replace("{{grupo}}", grupo)
        .replace("{{contenido}}", cuerpo))

# ────────────────────────────────────────────
# Huérfanos
# ────────────────────────────────────────────

def recolectar_html_existentes(base):
    existentes = set()
    for raiz, _, archivos in os.walk(base):
        for archivo in archivos:
            if archivo.endswith(".html"):
                existentes.add(os.path.abspath(os.path.join(raiz, archivo)))
    return existentes

def recolectar_md_existentes(base):
    existentes = set()
    for raiz, _, archivos in os.walk(base):
        for archivo in archivos:
            if archivo.endswith(".md"):
                existentes.add(os.path.abspath(os.path.join(raiz, archivo)))
    return existentes

def limpiar_huerfanos(existentes, generados):
    huerfanos = existentes - generados
    for ruta in huerfanos:
        os.remove(ruta)
        print(f"🗑️  Eliminado huérfano: {ruta}")
        stats["huerfanas"] += 1

# ────────────────────────────────────────────
# Convertidor de bloques
# ────────────────────────────────────────────

def rich_text_a_md(rich_texts):
    resultado = ""
    for rt in rich_texts:
        texto = rt.get("plain_text", "")
        annotations = rt.get("annotations", {})
        if annotations.get("code"):
            texto = f"`{texto}`"
        if annotations.get("bold"):
            texto = f"**{texto.strip()}**"
        if annotations.get("italic"):
            texto = f"*{texto}*"
        resultado += texto
    return resultado

def exportar_bloques(block_id, indent=0, dentro_de_lista=False):
    lineas = []
    tipos = []
    cursor = None

    while True:
        kwargs = {"block_id": block_id}
        if cursor:
            kwargs["start_cursor"] = cursor

        respuesta = notion.blocks.children.list(**kwargs)
        bloques = respuesta["results"]

        for bloque in bloques:
            tipo = bloque["type"]
            data = bloque.get(tipo, {})
            rich = data.get("rich_text", [])
            texto = rich_text_a_md(rich)

            if tipo == "paragraph":
                lineas.append(texto if texto else "")
                tipos.append(tipo)

            elif tipo == "heading_1":
                lineas.append(f"# {texto}")
                tipos.append(tipo)

            elif tipo == "heading_2":
                lineas.append(f"## {texto}")
                tipos.append(tipo)

            elif tipo == "heading_3":
                lineas.append(f"### {texto}")
                tipos.append(tipo)

            elif tipo == "heading_4":
                lineas.append(f"#### {texto}")
                tipos.append(tipo)

            elif tipo == "callout":
                lineas.append(f"> {texto}")
                tipos.append(tipo)

            elif tipo == "quote":
                lineas.append(f"> {texto}")
                tipos.append(tipo)

            elif tipo == "bulleted_list_item":
                prefix = "  " * indent
                contenido = f"{prefix}- {texto}"
                if bloque.get("has_children", False):
                    hijos = exportar_bloques(bloque["id"], indent + 1, dentro_de_lista=True)
                    hijos_indentados = "\n".join(
                        "  " + l if l.strip() else l
                        for l in hijos.split("\n")
                    )
                    contenido += "\n" + hijos_indentados.rstrip()
                lineas.append(contenido)
                tipos.append(tipo)
                continue

            elif tipo == "numbered_list_item":
                prefix = "  " * indent
                contenido = f"{prefix}1. {texto}"
                if bloque.get("has_children", False):
                    hijos = exportar_bloques(bloque["id"], indent + 1, dentro_de_lista=True)
                    hijos_indentados = "\n".join(
                        "   " + l if l.strip() else l
                        for l in hijos.split("\n")
                    )
                    contenido += "\n" + hijos_indentados.rstrip()
                lineas.append(contenido)
                tipos.append(tipo)
                continue

            elif tipo == "code":
                lenguaje = data.get("language", "")
                lenguaje = LANGUAGE_MAP.get(lenguaje, lenguaje)
                codigo = "".join(rt.get("plain_text", "") for rt in rich)
                lineas.append(f"```{lenguaje}\n{codigo}\n```")
                tipos.append(tipo)

            elif tipo == "divider":
                lineas.append("---")
                tipos.append(tipo)

            elif tipo == "image":
                url = data.get("file", {}).get("url", "") or data.get("external", {}).get("url", "")
                caption = rich_text_a_md(data.get("caption", []))
                if _IMG_ENABLED:
                    try:
                        url = _img.descargar_imagen(bloque["id"], url)
                    except Exception as e:
                        print(f"    ⚠️  Imagen no descargada: {e}")
                lineas.append(f"![{caption}]({url})")
                tipos.append(tipo)

            elif tipo == "table":
                filas = notion.blocks.children.list(block_id=bloque["id"])["results"]
                for i, fila in enumerate(filas):
                    celdas = fila.get("table_row", {}).get("cells", [])
                    contenido = " | ".join(
                        rich_text_a_md(celda) if celda else " "
                        for celda in celdas
                    )
                    lineas.append(f"| {contenido} |")
                    tipos.append("table_row")
                    if i == 0:
                        separador = " | ".join("---" for _ in celdas)
                        lineas.append(f"| {separador} |")
                        tipos.append("table_row")
                time.sleep(0.1)
                continue

            else:
                pass

            if bloque.get("has_children", False):
                hijos = exportar_bloques(bloque["id"], indent + 1)
                if hijos:
                    lineas.append(hijos)
                    tipos.append("children")

            time.sleep(0.1)

        if respuesta.get("has_more"):
            cursor = respuesta.get("next_cursor")
        else:
            break

    # Join inteligente según tipo de bloque
    es_lista = lambda t: t in ("bulleted_list_item", "numbered_list_item", "table_row")

    resultado = []
    for i, linea in enumerate(lineas):
        resultado.append(linea)
        if i < len(lineas) - 1:
            t_actual = tipos[i]
            t_siguiente = tipos[i + 1]
            if dentro_de_lista:
                resultado.append("\n")
            elif es_lista(t_actual) and es_lista(t_siguiente):
                resultado.append("\n")
            else:
                resultado.append("\n\n")

    return "".join(resultado)

def exportar_pagina(page_id):
    try:
        return exportar_bloques(page_id, indent=0)
    except Exception as e:
        return f"❌ Error obteniendo bloques: {e}"

# ────────────────────────────────────────────
# Procesamiento
# ────────────────────────────────────────────

def guardar_nota(page_id, titulo, grupo, categoria):
    carpeta_md   = os.path.join(BASE_MD, categoria)
    carpeta_html = os.path.join(BASE_HTML, categoria)
    os.makedirs(carpeta_md, exist_ok=True)
    os.makedirs(carpeta_html, exist_ok=True)

    slug      = slugify(titulo)
    ruta_md   = os.path.join(carpeta_md, slug + ".md")
    ruta_html = os.path.join(carpeta_html, slug + ".html")

    archivos_generados.add(os.path.abspath(ruta_html))
    archivos_md_generados.add(os.path.abspath(ruta_md))

    try:
        fecha_notion, fecha_creacion = notion_fechas(page_id)
        fecha_local  = local_fecha(ruta_html)

        if not TEST_MODE and fecha_local and fecha_local >= fecha_notion:
            print(f"  ⏭️  Sin cambios: {titulo}")
            stats["saltadas"] += 1
        else:
            contenido_md = exportar_pagina(page_id)

            with open(ruta_md, "w", encoding="utf-8") as f:
                f.write(contenido_md)

            html = md_to_html(titulo, contenido_md, categoria, grupo)
            with open(ruta_html, "w", encoding="utf-8") as f:
                f.write(html)

            print(f"  ✅ Actualizado: {titulo}")
            stats["actualizadas"] += 1
            time.sleep(0.35)

    except Exception as e:
        print(f"  ❌ Error en '{titulo}': {e}")
        stats["fallidas"] += 1
        return

    notas_procesadas.append({
        "title": titulo,
        "slug": f"{categoria}/{slug}",
        "category": categoria,
        "catLabel": CAT_LABELS.get(categoria, categoria),
        "grupo": grupo,
        "fecha_modificacion": fecha_notion.isoformat(),
        "fecha_creacion": fecha_creacion,
    })

def procesar_categoria(raiz_id, categoria):
    try:
        bloques = notion.blocks.children.list(block_id=raiz_id)
    except Exception as e:
        print(f"❌ Error accediendo a {categoria}: {e}")
        return

    for bloque in bloques["results"]:
        if bloque["type"] != "child_page":
            continue

        grupo_titulo = bloque["child_page"]["title"]
        grupo_id     = bloque["id"]
        print(f"\n  📁 {grupo_titulo}")

        try:
            subpaginas = notion.blocks.children.list(block_id=grupo_id)
        except Exception as e:
            print(f"  ❌ Error accediendo al grupo '{grupo_titulo}': {e}")
            continue

        for sub in subpaginas["results"]:
            if sub["type"] != "child_page":
                continue

            nota_titulo = sub["child_page"]["title"]
            nota_id     = sub["id"]
            guardar_nota(nota_id, nota_titulo, grupo_titulo, categoria)

            if TEST_MODE and stats["actualizadas"] >= 3:
                return

# ────────────────────────────────────────────
# Generar notes.json
# ────────────────────────────────────────────

def generar_notes_json():
    ruta = "../notes.json"
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(notas_procesadas, f, ensure_ascii=False, indent=2)
    print(f"\n📄 notes.json generado con {len(notas_procesadas)} notas.")

# ────────────────────────────────────────────
# Ejecución principal
# ────────────────────────────────────────────

html_existentes = recolectar_html_existentes(BASE_HTML)
md_existentes   = recolectar_md_existentes(BASE_MD)

try:
    for page_id, categoria in RAICES.items():
        print(f"\n📁 Procesando {categoria}...")
        procesar_categoria(page_id, categoria)
except KeyboardInterrupt:
    print("\n\n⚠️  Proceso interrumpido (SIGINT recibido). Guardando lo que se procesó hasta ahora...")

if not TEST_MODE:
    limpiar_huerfanos(html_existentes, archivos_generados)
    limpiar_huerfanos(md_existentes, archivos_md_generados)
    if _IMG_ENABLED:
        _img.limpiar_imagenes_huerfanas(BASE_MD)
generar_notes_json()

print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Resumen de sincronización
━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Actualizadas : {stats['actualizadas']}
⏭️  Sin cambios  : {stats['saltadas']}
❌ Fallidas     : {stats['fallidas']}
🗑️  Huérfanas   : {stats['huerfanas']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")