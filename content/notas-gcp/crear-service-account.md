# 📍 Paso 1 — Crear Service Account

Puedes hacerlo desde la interfaz (recomendado para que veas todo visualmente):

☰ → IAM & Admin → Service Accounts → Create Service Account

![](img/30a477bcd0eb80c79e9fcdf79a751cbf.webp)

![](img/30a477bcd0eb80ed9fa5c884382a64e0.webp)



Nombre:

```
youtube-pipeline-sa
```

ID sugerido (automático):

```
youtube-pipeline-sa
```

Descripción:

```
Service accountfor YouTubedata pipeline Cloud Functions
```

---

# 📍 Paso 2 — Asignar roles mínimos

Añade estos roles:

### 1️⃣ BigQuery Data Editor

Permite escribir en tablas.

### 2️⃣ BigQuery Job User

Permite ejecutar queries (DELETE snapshot, etc).

### 3️⃣ Storage Object Admin

Para cuando exportes JSON a Cloud Storage.

### 3️⃣ Cloud Run Invoker

Para cuando usemos cloud scheduler



No agregues Owner.

No agregues Editor.

No agregues roles innecesarios.

Arquitectura limpia desde el inicio.

---









# 🧠 Por qué no usamos credenciales JSON

En producción con Cloud Functions:

- No necesitas descargar claves
- No necesitas service account keys
- No necesitas JSON local

La función se ejecuta con esa Service Account automáticamente.

Eso es más seguro.