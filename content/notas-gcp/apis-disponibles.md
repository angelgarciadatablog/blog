# 🧠 Las 3 APIs de YouTube (qué hace cada una)

## 🟥 1️⃣ YouTube Data API v3 ✅ ← ESTA es tu base

👉 Es la API “pública” de datos estructurales de YouTube.

### Sirve para:

- Info de canales

- Lista de videos

- Metadata de videos

- Views, likes, comments (conteos públicos)

- Playlists

- Comentarios públicos

### Autenticación:

✔ API Key

✔ Fácil

✔ Perfecta para pipelines automáticos

### Ejemplo de preguntas que responde:

- ¿Cuántos videos tiene el canal?

- ¿Cuántas vistas tiene cada video?

- ¿Qué videos existen?

- ¿Cuándo se publicó cada video?

---

### 🚨 Limitaciones importantes

No trae:

- Retención de audiencia

- Watch time real

- CTR

- Ingresos

- Performance interna del canal

👉 Esto es normal. No es un bug.

---



## 🟡 2️⃣ YouTube Analytics API ⚠️ Solo si eres dueño del canal

👉 Es la API “interna” del rendimiento real del canal.

### Sirve para:

- Watch time

- Retención

- CTR

- Fuentes de tráfico

- Demografía

- Revenue

- Engagement profundo

### Autenticación:

❌ No usa API Key

✔ OAuth 2.0 (login real a tu cuenta)

👉 Es más compleja de automatizar.

---

### 🚨 Limitación clave

Solo puedes acceder a:

- Tu canal

- Canales donde tengas permisos

👉 No sirve para analizar canales externos.

---



## 🔵 3️⃣ YouTube Reporting API 🧠 Nivel empresa / batch

👉 No es para queries rápidas.

👉 Es para descargar **reportes masivos programados**.

### Sirve para:

- Reportes históricos grandes

- Descargas en CSV

- Jobs programados

- Data warehouse scenarios

### Ejemplo real:

- Descargar todos los datos históricos del canal

- Cargar a BigQuery

- Procesar offline