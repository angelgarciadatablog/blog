Cuando trabajas con Google Cloud desde tu máquina local, existen **dos mecanismos distintos de autenticación** que suelen confundirse:

- Autenticación del CLI (`gcloud`)

- Application Default Credentials (ADC) usadas por librerías de Google Cloud

Entender esta diferencia evita errores de permisos, cuotas y warnings.

---

## 🟢 1️⃣ Autenticación de `gcloud` (CLI Identity)

Se configura con:

```bash
gcloud auth login
```

### ¿Qué hace?

- Abre el navegador

- Permite iniciar sesión con tu cuenta Google

- Guarda un token OAuth localmente

- Permite que el SDK (`gcloud`) ejecute comandos contra GCP

### Se guarda en:

Mac/Linux:

```plain text
~/.config/gcloud/
```

Windows:

```plain text
C:\Users\TU_USUARIO\AppData\Roaming\gcloud
```

### Se usa para:

- `gcloud functions deploy`

- `gcloud projects list`

- `gcloud scheduler create`

- Cualquier comando del SDK

---

## 🔵 2️⃣ Autenticación de librerías Python (Application Default Credentials — ADC)

Se configura con:

```bash
gcloud auth application-default login
```

Y se puede alinear el proyecto de cuotas con:

```bash
gcloud auth application-default set-quota-project TU_PROJECT_ID
```

### ¿Qué es ADC?

Es el mecanismo estándar que usan las librerías oficiales de Google Cloud para autenticarse automáticamente.

Por ejemplo, cuando en un notebook haces:

```python
from google.cloudimport bigquery

client = bigquery.Client()
```

La librería no usa directamente `gcloud auth login`.

Usa ADC.

---

## 📁 Dónde se guarda ADC

Mac/Linux:

```plain text
~/.config/gcloud/application_default_credentials.json
```

Windows:

```plain text
C:\Users\TU_USUARIO\AppData\Roaming\gcloud\application_default_credentials.json
```

---

## 🎯 Diferencia clave

Son sistemas relacionados pero distintos.

---

## ⚠️ Problema común: “quota project mismatch”

Puede ocurrir que:

- Cambies el proyecto activo con:

```bash
gcloud configset project nuevo-proyecto
```

Pero ADC siga apuntando al proyecto anterior.

Eso genera el warning:

```plain text
Your active project doesnotmatch the quota projectin yourlocal ApplicationDefault Credentials file.
```

La solución es:

```bash
gcloud auth application-default set-quota-project nuevo-proyecto
```