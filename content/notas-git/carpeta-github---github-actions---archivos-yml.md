## 1️⃣ ¿Qué es `.github` y por qué empieza con punto?

En macOS / Linux:

- Las carpetas que empiezan con `.` son **ocultas**
- No es “misterio”, es solo convención

Ejemplos comunes:

- `.git` → info interna de Git
- `.env` → variables de entorno
- `.github` → **configuración especial para GitHub**

👉 O sea:

> `.github` NO es para tu código, es para decirle cosas a GitHub.

---



## 2️⃣ ¿Para qué sirve la carpeta `.github`?

GitHub **escanea automáticamente** esa carpeta cuando subes el repo.

Dentro de `.github` pueden vivir:

- workflows (automatizaciones)
- templates de issues
- templates de PRs
- config de seguridad

En tu proyecto, **sirve para usar:**

👉 **GitHub Actions**





## 3️⃣ ¿Qué es `.github/workflows` exactamente?

Esta ruta:

```
.github/workflows/
```

tiene un significado especial:

> 📌 **GitHub busca ahí los archivos****`.yml`****para ejecutar Actions**

Si no existe:

- GitHub Actions **no corre**
- Aunque tu YAML esté perfecto

Es una **ruta obligatoria**, no un gusto.

---

## 4️⃣ Qué significa este comando exactamente

```bash
mkdir .github/workflows
```

Se lee así (en español humano):

> “Crea una carpeta llamada `workflows` dentro de una carpeta llamada `.github`”

Y como `.github` es especial, GitHub sabe:

- “ah, aquí hay automatizaciones”

---

## 5️⃣ Analogía sencilla (para que no se olvide)

Piensa en el repo como una empresa:

```
youtube-data-pipeline/
│
├── scripts/        → trabajadores (Python)
├── sql/            → reglasdel negocio
├── data/           → almacén temporal
│
├──.github/
│   └── workflows/ → jefe que dice CUÁNDOy CÓMO trabajan
```

Sin `.github/workflows`:

- tienes trabajadores
- pero nadie los coordina