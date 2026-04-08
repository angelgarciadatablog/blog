import os
import re
import requests
from PIL import Image
from io import BytesIO

_DIR    = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(_DIR, "../img")
IMG_WEB = "img"  # path relativo a la raíz del sitio (usado en HTML/markdown)


def descargar_imagen(block_id, url):
    """Descarga una imagen de Notion, la convierte a WebP y retorna el path local."""
    os.makedirs(IMG_DIR, exist_ok=True)

    nombre = f"{block_id.replace('-', '')}.webp"
    ruta   = os.path.join(IMG_DIR, nombre)

    if not os.path.exists(ruta):
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        img = Image.open(BytesIO(r.content))
        img = img.convert("RGBA") if img.mode in ("RGBA", "LA") else img.convert("RGB")
        img.save(ruta, "webp", quality=85)

    return f"{IMG_WEB}/{nombre}"


def limpiar_imagenes_huerfanas(base_md):
    """Elimina imágenes en assets/img/ que no están referenciadas en ningún markdown."""
    if not os.path.exists(IMG_DIR):
        return

    referenciadas = set()
    for raiz, _, archivos in os.walk(base_md):
        for archivo in archivos:
            if not archivo.endswith(".md"):
                continue
            with open(os.path.join(raiz, archivo), "r", encoding="utf-8") as f:
                contenido = f.read()
            for match in re.finditer(r'img/([^\s\)]+)', contenido):
                referenciadas.add(match.group(1))

    for archivo in os.listdir(IMG_DIR):
        if archivo not in referenciadas:
            os.remove(os.path.join(IMG_DIR, archivo))
            print(f"🗑️  Imagen huérfana: {archivo}")
