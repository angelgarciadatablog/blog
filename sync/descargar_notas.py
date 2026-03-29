import os
import re
import time
import json
import unicodedata
import markdown
from datetime import datetime, timezone
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))

RAICES = {
    "290477bc-d0eb-8013-a785-d8784b2f8210": "notas-gcp",
    "290477bc-d0eb-807e-a377-f5b7cbbf8b9e": "notas-git",
}

CAT_LABELS = {
    "notas-gcp": "Google Cloud Platform",
    "notas-git": "Git & GitHub",
}

BASE_MD    = "../content"
BASE_HTML  = "../docs"

stats = {"actualizadas": 0, "saltadas": 0, "fallidas": 0, "huerfanas": 0}
notas_procesadas = []
archivos_generados = set()

CSS = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
  :root {
    --bg: #0f0f0f;
    --bg-side: #141414;
    --border: #242424;
    --text: #c9c9c9;
    --text-dim: #555;
    --text-head: #e8e8e8;
    --accent: #4a90d9;
    --code-bg: #1a1a1a;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    font-size: 15px;
    line-height: 1.7;
    padding: 48px 60px;
    max-width: 860px;
    margin: 0 auto;
  }
  .topbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 48px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    padding: 0 32px;
    gap: 16px;
    z-index: 100;
  }
  .topbar a { color: var(--text-dim); text-decoration: none; font-size: 13px; }
  .topbar a:hover { color: var(--text); }
  .topbar .sep { color: var(--border); }
  .note-content { margin-top: 72px; }
  h1 { font-size: 26px; font-weight: 600; color: var(--text-head); margin-bottom: 24px; letter-spacing: -0.02em; }
  h2 { font-size: 18px; font-weight: 600; color: var(--text-head); margin: 36px 0 12px; }
  h3 { font-size: 15px; font-weight: 500; color: var(--text-head); margin: 24px 0 8px; }
  p { margin-bottom: 16px; }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  code {
    font-family: 'Fira Code', monospace;
    background: var(--code-bg);
    border: 1px solid var(--border);
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 13px;
    color: #e2e8f0;
  }
  pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 16px 20px;
    overflow-x: auto;
    margin: 16px 0;
  }
  pre code { background: none; border: none; padding: 0; font-size: 13px; line-height: 1.6; }
  blockquote { border-left: 3px solid var(--accent); padding: 8px 16px; margin: 16px 0; color: var(--text-dim); font-style: italic; }
  table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; }
  th { text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--border); color: var(--text-dim); font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.06em; }
  td { padding: 10px 12px; border-bottom: 1px solid var(--border); }
  tr:last-child td { border-bottom: none; }
  ul, ol { padding-left: 20px; margin-bottom: 16px; }
  li { margin-bottom: 6px; }
  img { max-width: 100%; border-radius: 6px; margin: 16px 0; }
  hr { border: none; border-top: 1px solid var(--border); margin: 32px 0; }
</style>
"""

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
    """Obtiene fecha de modificación y creación en una sola llamada."""
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
    cuerpo = markdown.markdown(
        contenido_md,
        extensions=['fenced_code', 'tables', 'codehilite']
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo} · Angel García</title>
  {CSS}
</head>
<body>
  <div class="topbar">
    <a href="../../index.html">← Inicio</a>
    <span class="sep">|</span>
    <a href="../../index.html">{CAT_LABELS.get(categoria, categoria)}</a>
    <span class="sep">|</span>
    <span style="color: var(--text-dim); font-size: 13px;">{grupo}</span>
  </div>
  <div class="note-content">
    <h1>{titulo}</h1>
    {cuerpo}
  </div>
</body>
</html>"""

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

def exportar_pagina(page_id):
    try:
        bloques = notion.blocks.children.list(block_id=page_id)
    except Exception as e:
        return f"❌ Error obteniendo bloques: {e}"

    lineas = []

    for bloque in bloques["results"]:
        tipo = bloque["type"]
        data = bloque.get(tipo, {})
        rich = data.get("rich_text", [])
        texto = rich_text_a_md(rich)

        if tipo == "paragraph":
            lineas.append(texto if texto else "")
        elif tipo == "heading_1":
            lineas.append(f"# {texto}")
        elif tipo == "heading_2":
            lineas.append(f"## {texto}")
        elif tipo == "heading_3":
            lineas.append(f"### {texto}")
        elif tipo == "heading_4":
            lineas.append(f"#### {texto}")
        elif tipo == "callout":
            lineas.append(f"> {texto}")
        elif tipo == "quote":
            lineas.append(f"> {texto}")
        elif tipo == "bulleted_list_item":
            lineas.append(f"- {texto}")
        elif tipo == "numbered_list_item":
            lineas.append(f"1. {texto}")
        elif tipo == "code":
            lenguaje = data.get("language", "")
            codigo = "".join(rt.get("plain_text", "") for rt in rich)
            lineas.append(f"```{lenguaje}\n{codigo}\n```")
        elif tipo == "divider":
            lineas.append("---")
        elif tipo == "image":
            url = data.get("file", {}).get("url", "") or data.get("external", {}).get("url", "")
            caption = rich_text_a_md(data.get("caption", []))
            lineas.append(f"![{caption}]({url})")
        else:
            pass

        time.sleep(0.1)

    return "\n\n".join(lineas)

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

    try:
        fecha_notion, fecha_creacion = notion_fechas(page_id)
        fecha_local  = local_fecha(ruta_html)

        if fecha_local and fecha_local >= fecha_notion:
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

for page_id, categoria in RAICES.items():
    print(f"\n📁 Procesando {categoria}...")
    procesar_categoria(page_id, categoria)

limpiar_huerfanos(html_existentes, archivos_generados)
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