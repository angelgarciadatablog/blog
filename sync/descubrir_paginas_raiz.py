#!/usr/bin/env python3
"""
Script para descubrir páginas raíz (categorías) en Notion.
Solo muestra páginas que tengan la estructura: RAIZ → Carpetas → Notas
"""

import os
import sys
import time
import signal
from notion_client import Client
from dotenv import load_dotenv

# ════════════════════════════════════════════════════════════════════════════════════
# ⚠️  MANEJO DE INTERRUPCIÓN (Ctrl+C / SIGINT)
# ════════════════════════════════════════════════════════════════════════════════════
#
# Este script puede ser interrumpido con Ctrl+C, lo que enviará la señal SIGINT.
#
# ⚠️  ADVERTENCIA IMPORTANTE SOBRE INTERRUMPIR PROCESOS:
# No siempre es seguro interrumpir procesos a la mitad. Conceptos técnicos relacionados:
#
# • ATOMICIDAD: Una operación atómica debe completarse en su totalidad o no ejecutarse.
#   Si interrumpimos un proceso en mitad de una operación atómica, violamos este principio.
#   El sistema queda en un estado inconsistente.
#
# • TRANSACCIONES (ACID): En bases de datos, las transacciones garantizan que si algo
#   falla, se hace ROLLBACK automático (se revierten todos los cambios). Sin esto,
#   cambios parciales quedan en el sistema.
#
# • CONSISTENCIA DE DATOS: Interrumpir puede dejar datos en estado inconsistente.
#   Ejemplo: Si se estaba escribiendo un archivo de 100MB y se interrumpe a los 50MB,
#   el archivo queda corrupto y no es utilizable.
#
# • CLEANUP/LIMPIEZA DE RECURSOS: Algunos procesos necesitan ejecutar código de
#   limpieza (cerrar conexiones de BD, liberar memoria, eliminar archivos temporales).
#   Si se interrumpe bruscamente, esto no ocurre y quedan resources "huérfanos".
#
# • ESTADO CONSISTENTE vs INCONSISTENTE: Una operación puede dejar cambios parciales.
#   Ej: "transferencia bancaria" - si se interrumpe después de débito pero antes de
#   crédito, el dinero desaparece. El estado es INCONSISTENTE.
#
# PARA ESTE SCRIPT ESPECÍFICAMENTE:
# Solo hacemos lecturas (queries SELECT a Notion). No hay escrituras, no hay actualizaciones,
# no hay operaciones críticas que requieran completarse. Si interrumpimos a mitad de una
# búsqueda, simplemente no obtenemos el resultado completo, pero los datos de Notion
# no sufren daño. Es seguro interrumpir.
#
# ════════════════════════════════════════════════════════════════════════════════════

def handle_sigint(sig, frame):
    """Maneja la interrupción con Ctrl+C (SIGINT)"""
    print("\n\n⏹️  Proceso interrumpido por usuario (Ctrl+C)")
    print("   (No hay daño: este script solo hace consultas de lectura, no escrituras)\n")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Leer RAICES actuales directamente desde descargar_notas.py (evita hardcoding)
try:
    import descargar_notas
    current_raices = descargar_notas.RAICES
except ImportError:
    print("❌ Error: No se pudo importar descargar_notas.py")
    print("   Asegúrate de ejecutar este script desde la carpeta 'sync/'")
    sys.exit(1)

def get_page_title(page_id):
    """Obtiene el título de una página"""
    try:
        page = notion.pages.retrieve(page_id=page_id)
        if "properties" in page:
            for prop_name, prop_value in page["properties"].items():
                if prop_value.get("type") == "title":
                    if prop_value.get("title"):
                        return "".join(
                            t.get("plain_text", "")
                            for t in prop_value["title"]
                        )
        return "(sin título)"
    except:
        return "(no se pudo obtener título)"

def has_child_pages(page_id):
    """Verifica si una página tiene child_pages"""
    try:
        children = notion.blocks.children.list(block_id=page_id)
        return any(b["type"] == "child_page" for b in children.get("results", []))
    except:
        return False

def is_valid_root(page_id):
    """
    Verifica si una página es una RAIZ válida:
    - Tiene child_pages (carpetas)
    - Al menos una de esas carpetas tiene child_pages (notas)
    """
    try:
        children = notion.blocks.children.list(block_id=page_id)
        child_pages = [b for b in children.get("results", []) if b["type"] == "child_page"]

        if not child_pages:
            return False

        # Verificar que al menos una carpeta tiene notas dentro
        for child in child_pages[:3]:  # Revisar las primeras 3 carpetas
            time.sleep(0.1)
            if has_child_pages(child["id"]):
                return True

        return False
    except:
        return False

print("🔍 Buscando páginas raíz (categorías que empiezan con 'notas-')...\n")

# Buscar solo páginas cuyo nombre empiece con "notas-" (patrón de búsqueda)
try:
    response = notion.search(
        query="notas-",
        sort={"direction": "descending", "timestamp": "last_edited_time"}
    )
    all_pages = [r for r in response.get("results", []) if r["object"] == "page"]
    print(f"📄 Analizando {len(all_pages)} páginas encontradas con patrón 'notas-'...\n")

    root_pages = {}

    for i, page in enumerate(all_pages):
        page_id = page["id"]
        page_title = get_page_title(page_id)

        # Skip si ya está en RAICES
        if page_id in current_raices:
            continue

        print(f"[{i+1}/{len(all_pages)}] Verificando: {page_title}...", end=" ")

        if is_valid_root(page_id):
            print("✅ CANDIDATA")
            root_pages[page_id] = page_title
        else:
            print("⏭️")

        time.sleep(0.1)

    print("\n" + "="*60)
    print("🎯 POSIBLES NUEVAS RAICES (no están en RAICES actual):")
    print("="*60 + "\n")

    if root_pages:
        for page_id, title in root_pages.items():
            print(f"  • {title}")
            print(f"    ID: {page_id}\n")
    else:
        print("  (ninguna encontrada)\n")

except Exception as e:
    print(f"❌ Error: {e}\n")

# Mostrar RAICES actuales
print("="*60)
print("✅ RAICES actuales en descargar_notas.py:")
print("="*60 + "\n")

for raiz_id, category in current_raices.items():
    print(f"  • {category}")
    print(f"    ID: {raiz_id}\n")
