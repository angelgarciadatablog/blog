# angelgarciadatablog · Docs

Documentación técnica personal exportada desde Notion y publicada como sitio estático en GitHub Pages. El contenido vive en Notion como fuente de verdad, se sincroniza mediante un script Python y se despliega automáticamente a través de GitHub Pages.

---

## Por qué existe esto

El objetivo era tener una documentación técnica personal accesible desde cualquier lugar, versionada en Git y con un diseño limpio orientado a la lectura. Se evaluaron varias opciones antes de llegar a esta solución.

### Por qué Notion y no Obsidian

Obsidian fue la primera opción considerada, pero presentó problemas concretos:

- **Imágenes rotas**: Obsidian almacena las imágenes como archivos locales vinculados con rutas relativas. Al mover notas entre carpetas o al exportar, los links se rompen con frecuencia.
- **Multi-ordenador sin fricción**: Actualmente el trabajo se realiza en dos ordenadores (Mac y Windows). Con Obsidian + Git habría que hacer `git pull` cada vez que se cambia de máquina y `git push` al terminar — un paso manual que interrumpe el flujo de trabajo. Con Notion, la sincronización entre dispositivos es automática e instantánea.
- **Flujo de exportación**: Exportar desde Obsidian a HTML o a un sitio web requería plugins externos con resultados inconsistentes.

Notion resuelve todos estos problemas: sincroniza automáticamente entre dispositivos, gestiona las imágenes en su propia infraestructura y expone una API oficial que permite extraer el contenido de forma estructurada.

---

## Estructura del contenido

### Categorías

Una **categoría** es un tema principal. Cada categoría corresponde a una página raíz en Notion y a una carpeta en el repositorio (`content/notas-gcp/`, `content/notas-git/`). Actualmente existen dos:

| Categoría | Label | ID en Notion |
|-----------|-------|--------------|
| `notas-gcp` | Google Cloud Platform | `290477bc-d0eb-8013-a785-d8784b2f8210` |
| `notas-git` | Git & GitHub | `290477bc-d0eb-807e-a377-f5b7cbbf8b9e` |

Las categorías se gestionan directamente en el script (`RAICES` en `sync/descargar_notas.py`). Agregar una nueva categoría implica crear una página raíz en Notion, obtener su ID y añadirla al diccionario.

### ⚠️ Al agregar una nueva categoría hay que actualizar 3 lugares

`CAT_LABELS` está definido en **dos sitios distintos** — uno para el backend (Python) y otro para el frontend (JavaScript). Olvidar cualquiera de los dos hace que el label no se muestre correctamente:

| Archivo | Qué actualizar |
|---------|---------------|
| `sync/descargar_notas.py` | Añadir entrada en `RAICES` y en `CAT_LABELS` |
| `assets/app.js` | Añadir entrada en `CAT_LABELS` (línea 1) |

Ejemplo para una nueva categoría `notas-ia`:

```python
# sync/descargar_notas.py
RAICES = {
    ...
    "332477bc-d0eb-8042-be0a-f27c6d6a2013": "notas-ia",
}
CAT_LABELS = {
    ...
    "notas-ia": "Inteligencia Artificial",
}
```

```javascript
// assets/app.js
const CAT_LABELS = {
  ...
  'notas-ia': 'Inteligencia Artificial',
};
```

### Carpetas (grupos)

Dentro de cada categoría existen **carpetas** (llamadas internamente "grupos"), que representan subtemas. Por ejemplo, dentro de `notas-gcp` existe la carpeta "CLI de google cloud - SDK". Estas carpetas son páginas hijo de la página raíz en Notion y agrupan notas relacionadas.

### Notas

Las **notas** son páginas hijo dentro de una carpeta. Son la unidad mínima de contenido. Cada nota se exporta como:
- Un archivo Markdown en `content/{categoria}/{slug}.md`
- Un archivo HTML en `docs/{categoria}/{slug}.html`
- Una entrada en `notes.json`

---

## Gestión de la API de Notion

### API Key y acceso

Las categorías disponibles, así como la API Key, se gestionan desde el portal de integraciones de Notion:

👉 [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)

Desde ahí se crea una integración, se obtiene el token (`NOTION_TOKEN`) y se comparten con ella las páginas raíz de cada categoría. El token se almacena en un archivo `.env` local (no versionado):

```
NOTION_TOKEN=secret_xxxxxxxxxxxx
```

### Librerías utilizadas

| Librería | Uso |
|----------|-----|
| `notion-client` | Cliente oficial de la API de Notion |
| `markdown` | Conversión de Markdown a HTML |
| `pymdown-extensions` | Extensión `superfences` para bloques de código dentro de listas |
| `python-dotenv` | Carga del token desde `.env` |
| `Pillow` | Descarga y conversión de imágenes a WebP |
| `requests` | Descarga de imágenes desde URLs de Notion |

### El archivo `notes.json`

El script genera `notes.json` en la raíz del repositorio. Este archivo es consumido por el frontend (SPA) para construir el índice, el sidebar y la sección de notas recientes. Cada entrada tiene la siguiente estructura:

```json
{
  "title": "Instalar librería Google Cloud",
  "slug": "notas-gcp/instalar-libreria-google-cloud",
  "category": "notas-gcp",
  "catLabel": "Google Cloud Platform",
  "grupo": "Libreria de google cloud",
  "fecha_modificacion": "2025-01-15T10:23:00+00:00",
  "fecha_creacion": "2024-11-01T08:00:00.000Z"
}
```

---

## El script de sincronización

**Archivo principal:** `sync/descargar_notas.py`

### Estados de las notas

Durante cada ejecución, el script compara la fecha de última modificación en Notion con la fecha del archivo HTML local:

| Estado | Símbolo | Descripción |
|--------|---------|-------------|
| Actualizada | ✅ | La nota cambió en Notion desde el último sync. Se re-exporta. |
| Sin cambios | ⏭️ | La nota no cambió. Se omite para ahorrar llamadas a la API. |
| Fallida | ❌ | Ocurrió un error al procesar la nota. Se registra y se continúa. |
| Huérfana eliminada | 🗑️ | El archivo HTML existe localmente pero la nota ya no existe en Notion. Se elimina. |

### Cómo se manejan los cambios estructurales

| Acción en Notion | Comportamiento del script |
|------------------|--------------------------|
| Modificar contenido de una nota | Se re-exporta en el siguiente sync |
| Borrar una nota | Su HTML queda huérfano y se elimina automáticamente |
| Borrar una carpeta | Todas sus notas quedan huérfanas y se eliminan |
| Renombrar una nota | Se genera un nuevo slug → nuevo HTML. El anterior queda huérfano y se elimina. |
| Renombrar una carpeta | Solo afecta al label visible, no al slug de las notas |
| Renombrar una categoría | **No gestionado automáticamente.** Requiere actualizar `RAICES` y `CAT_LABELS` en el script manualmente |

### Mecanismos anti-error implementados

- **`LANGUAGE_MAP`**: Notion usa nombres de lenguaje no estándar (`"plain text"`, `"shell"`, `"zsh"`). El mapa los convierte a identificadores válidos de Markdown (`""`, `"bash"`, `"bash"`). Sin esto, los bloques de código mal identificados nunca cierran su delimitador y rompen el renderizado de todo el contenido siguiente.
- **`pymdownx.superfences`**: La librería estándar `markdown` de Python no soporta bloques de código dentro de listas numeradas. Esta extensión lo resuelve correctamente según el estándar CommonMark.
- **`dentro_de_lista`**: Parámetro que controla el join de bloques hijo. Dentro de un ítem de lista se usa `\n` en lugar de `\n\n` para evitar que el parser interprete cada línea como una lista nueva (lo que causaba que todos los ítems numerados aparecieran como "1.").
- **`TEST_MODE`**: Flag `--test` que procesa solo 3 notas y omite la limpieza de huérfanos. Útil para probar cambios sin afectar el contenido completo.

---

## Reglas para escribir notas en Notion

El script soporta los siguientes tipos de bloque. Usarlos correctamente garantiza una exportación sin errores:

### Bloques soportados

| Bloque en Notion | Resultado en Markdown |
|------------------|-----------------------|
| Párrafo | Texto plano |
| Heading 1 / 2 / 3 / 4 | `#` / `##` / `###` / `####` |
| Bulleted list | `- ítem` |
| Numbered list | `1. ítem` |
| Code block | ` ```lenguaje ... ``` ` |
| Quote / Callout | `> texto` |
| Divider | `---` |
| Image | Descargada localmente como WebP |
| Table | Tabla Markdown estándar |

### Reglas importantes

1. **Listas numeradas con código dentro**: Se puede incluir un bloque de código como hijo de un ítem numerado, pero debe ser el **último elemento** del ítem. Si se añade contenido después del bloque de código dentro del mismo ítem, el renderizado puede romperse.

2. **No anidar listas después de contenido mixto**: Se pueden tener sublistas (viñetas dentro de numeradas o viceversa), pero solo si están al final del ítem padre, sin mezclar con párrafos intermedios.

3. **Lenguajes de código**: Usar siempre un lenguaje reconocido (`bash`, `python`, `sql`, `javascript`, etc.). Evitar "Plain text" — el script lo convierte a bloque sin lenguaje, lo cual es correcto, pero no tendrá syntax highlighting.

4. **Imágenes**: Insertarlas directamente en Notion (upload), no como links externos si se quiere que persistan. Las imágenes externas también se descargan, pero dependen de que el servidor externo las mantenga disponibles.

5. **Bloques no soportados** (columns, toggles, embeds, etc.): Son ignorados silenciosamente. Si un bloque tiene hijos, el script intentará exportar el contenido hijo, pero el contenedor en sí no tendrá representación visual.

---

## El Markdown generado

### Cómo llega desde Notion

La API de Notion devuelve el contenido como bloques con `rich_text` — objetos JSON que describen el texto con sus anotaciones (negrita, cursiva, código inline, etc.). El script convierte cada bloque a su equivalente en Markdown:

```
bold → **texto**
italic → *texto*
inline code → `texto`
```

### Ajustes personalizados aplicados

- **Numeración de listas**: Notion siempre devuelve `1` como número de ítem. El script también usa `1.` para todos los ítems, lo cual es válido en CommonMark (la mayoría de parsers renumeran automáticamente al renderizar).
- **Indentación de hijos**: Los bloques hijo de un ítem de lista se indentan con 2 espacios (viñetas) o 3 espacios (numeradas) para cumplir con CommonMark.
- **Join inteligente**: Entre bloques normales se usa `\n\n` (párrafos separados). Entre ítems de lista consecutivos se usa `\n`. Dentro de un ítem con hijos se usa `\n` para no romper el contexto de la lista.

### Qué tan estándar es

El Markdown generado es compatible con **CommonMark** y **GFM (GitHub Flavored Markdown)**, los dos estándares más adoptados. Es legible directamente en:
- GitHub (preview de archivos `.md`)
- Obsidian
- VS Code
- Cualquier parser moderno

Si en el futuro se quisieran combinar estas notas con Markdown de otras fuentes (por ejemplo, notas escritas manualmente en Obsidian), serían compatibles sin conversión, siempre que las otras fuentes también respeten CommonMark y no usen extensiones propietarias.

---

## Manejo de imágenes

### Flujo

1. Durante el sync, al encontrar un bloque `image`, el script llama a `sync/imagenes.py`
2. La imagen se descarga desde la URL de Notion (firmada por AWS S3, expira en ~1 hora)
3. Se convierte a formato WebP con calidad 85 usando Pillow
4. Se guarda en `img/{block_id_sin_guiones}.webp`
5. La URL de Notion en el Markdown se reemplaza por `img/{nombre}.webp`

### Naming por block ID

El nombre del archivo es el UUID del bloque de Notion sin guiones (32 caracteres hex). Esto garantiza:
- **Estabilidad**: Renombrar la nota no cambia el nombre de la imagen
- **Unicidad**: Cada bloque tiene un ID único en toda la plataforma de Notion
- **Idempotencia**: Si la imagen ya existe localmente, no se vuelve a descargar

### Limpieza de huérfanas

Al finalizar el sync, `limpiar_imagenes_huerfanas()` escanea todos los archivos `.md` en `content/` y construye la lista de imágenes referenciadas. Las imágenes en `img/` que no aparecen en ningún markdown son eliminadas. Esto cubre los casos de:
- Imagen eliminada en Notion
- Nota eliminada (y con ella sus imágenes)
- Imagen reemplazada (nuevo block ID → nueva imagen, la anterior queda huérfana)

### Posibles conflictos

| Situación | Comportamiento |
|-----------|----------------|
| Nota no re-sincronizada (sin cambios) | Sus imágenes ya existen localmente y son encontradas por el scanner de huérfanas |
| Imagen externa (no subida a Notion) | Se descarga igual; si el servidor externo la borra, fallará con ⚠️ y mantendrá la URL original |
| Pillow no instalado | `_IMG_ENABLED = False`, el script usa las URLs de Notion directamente (se rompen en ~1 hora) |
| Error al descargar | Se registra ⚠️ y se mantiene la URL original de Notion para esa imagen |

### Imágenes en el historial de git

Cada imagen se versiona en git como un archivo binario. Aunque se elimine una imagen y se haga commit, el archivo sigue existiendo en el historial, lo que hace crecer el tamaño del repositorio con el tiempo.

Con imágenes WebP a calidad 85 y un promedio de ~150KB por imagen, esta acumulación **no representa un problema real durante muchos años** para el volumen de notas técnicas de este blog. El repositorio puede crecer varios cientos de MB antes de que sea necesario intervenir.

Cuando el repositorio supere un tamaño manejable, la solución recomendada es **migrar las imágenes a un cloud storage externo** (Google Cloud Storage, Cloudinary, etc.) y que el script guarde la URL externa en lugar de la ruta local. Esta migración es posible sin romper el pipeline actual y puede hacerse en el futuro sin urgencia.

---

## Diseño y comportamiento del blog

### Arquitectura SPA

El blog es una **Single Page Application** (SPA). Hay un único `index.html` que carga el contenido dinámicamente mediante JavaScript. Al abrir una nota, el script fetch-ea el HTML correspondiente de `docs/`, extrae el contenido de `.note-content` y lo inyecta en el visor sin recargar la página. Esto hace la navegación instantánea.

**Implicación importante**: El botón "atrás" del navegador (especialmente en móvil) no funciona como navegación interna — para el navegador solo hay una página. El botón "← Volver" del blog lleva siempre a la categoría padre de la nota actual.

### Preferencias de diseño adoptadas

- **Tema oscuro** con fondo `#0f0f0f` y texto `#c9c9c9`
- **Fuente**: Inter (texto) + Fira Code (código)
- **Accent color**: `#4a90d9` (azul) para links, sidebar activo y TOC
- **Inline code**: fondo rojo translúcido `rgba(235,87,87,0.15)` con texto `#f28b82`, inspirado en Notion dark mode
- **Bloques de código bash**: todo el texto en rojo `#f28b82` (sin syntax highlighting de palabras clave, ya que bash tiene mínimos built-ins)
- **Python, SQL y otros lenguajes**: syntax highlighting via highlight.js con tema `github-dark`
- **Headings**: espaciado superior generoso (H1: 72px, H2: 48px, H3: 36px) para separar secciones visualmente
- **TOC (Table of Contents)**: panel lateral derecho visible solo en pantallas ≥ 1200px. Se construye dinámicamente con los headings de cada nota y resalta la sección visible mientras se hace scroll via `IntersectionObserver`

### Responsive

- En mobile, el sidebar se oculta y aparece un botón de menú hamburguesa
- El TOC desaparece en pantallas < 1200px
- Los links del topbar se ocultan en mobile
- El padding del contenido se reduce en pantallas pequeñas

---

## Script principal a detalle

**`sync/descargar_notas.py`**

```
Estructura:
├── Constantes (RAICES, CAT_LABELS, LANGUAGE_MAP, rutas)
├── Utilidades (slugify, fechas, md_to_html)
├── Huérfanos (recolectar_html_existentes, limpiar_huerfanos)
├── Convertidor de bloques (rich_text_a_md, exportar_bloques)
├── Procesamiento (guardar_nota, procesar_categoria)
├── Generador de notes.json
└── Ejecución principal
```

El flujo completo al ejecutar `python sync/descargar_notas.py`:

1. Carga el token de `.env`
2. Recolecta todos los HTML existentes en `docs/`
3. Para cada categoría en `RAICES`, recorre sus carpetas y notas
4. Por cada nota: compara fecha de modificación Notion vs local
5. Si cambió: exporta bloques → Markdown → HTML → guarda ambos
6. Al finalizar: elimina HTML huérfanos, descarga imágenes huérfanas, regenera `notes.json`

**Módulo de imágenes:** `sync/imagenes.py` — completamente aislado. Si falla la importación (Pillow no instalado), el script principal continúa sin descargar imágenes.

### Automatización pendiente

Actualmente el sync se ejecuta manualmente. Está pendiente integrarlo en uno de estos mecanismos:

- **GitHub Actions**: workflow que se ejecute con un schedule (cron) o manualmente desde GitHub
- **Cloud Function**: función en GCP que ejecute el script periódicamente via Cloud Scheduler

Por ahora se mantiene manual para validar que el pipeline sea estable y no rompa nada antes de automatizarlo.

---

## Pendientes

### Redirecciones entre notas

En Notion es posible mencionar otras páginas con `@NombreDePágina`. La API devuelve estas menciones en el `rich_text` como tipo `mention` con el `page_id` de la página referenciada. Está pendiente implementar la conversión de estas menciones a links internos del blog que apunten al slug correspondiente.

### Botón atrás en móvil

El botón atrás del navegador en móvil sale del blog porque la URL nunca cambia (SPA sin History API). La solución es implementar `history.pushState()` al navegar y escuchar `popstate` para manejar el retroceso. Está pendiente por el riesgo de introducir bugs en la lógica de navegación actual.

### Colorear comandos personalizados

Los comandos como `git`, `gcloud`, `curl`, `brew` no son built-ins de bash y ningún highlighter estándar los colorea. Está pendiente implementar un grammar personalizado en highlight.js que los trate como keywords.

---

## Ejecutar el sync

```bash
# Instalación de dependencias (primera vez)
pip install -r requirements.txt

# Sync completo
python sync/descargar_notas.py

# Sync de prueba (solo 3 notas, sin limpiar huérfanos)
python sync/descargar_notas.py --test
```
