

## 📌 Documentación: Uso de rutas relativas para imágenes en Markdown

## 1️⃣ Contexto del problema

Al trabajar con archivos Markdown dentro de una estructura de carpetas, las imágenes no se muestran correctamente si la ruta no está bien definida.

En este proyecto la estructura es:

```
2-ecommerce-analytics-comercial/
│
├── analysis/
│   └── ecommerce-analytics-comercial-analysis.md
│
├── images/
│   ├── ecommerce-performance-cupones.png
│   ├── ecommerce-performance-mujer.png
│   ├── ecommerce-performance-caida-ventas.png
│   └── ecommerce-performance-tallas.png
```

El archivo `.md` se encuentra dentro de la carpeta `analysis`, mientras que las imágenes están en la carpeta `images`.

---

## 2️⃣ Concepto clave: Rutas relativas

En Markdown, las imágenes se insertan con la siguiente sintaxis:

```markdown
![Texto alternativo](ruta/de/la/imagen.png)
```

La ruta se interpreta **desde la ubicación del archivo Markdown**.

### Símbolos importantes:

- `.` → carpeta actual
- `..` → subir un nivel en la estructura
- `../images/` → subir un nivel y entrar en la carpeta `images`

---

## 3️⃣ Construcción de la ruta correcta

Como el archivo `.md` está dentro de:

```
analysis/
```

Y las imágenes están en:

```
images/
```

Es necesario:

1. Subir un nivel → `..`
1. Entrar a la carpeta `images`

La ruta correcta es:

```markdown
![Cupones](../images/ecommerce-performance-cupones.png)
```

---



## 🧠 Regla mental que debes recordar (muy importante)

Siempre piensa:

> ¿Desde dónde está parado mi archivo `.md`?

Luego:

- `.` → carpeta actual
- `..` → subir un nivel
- `../images/` → subir y entrar a images