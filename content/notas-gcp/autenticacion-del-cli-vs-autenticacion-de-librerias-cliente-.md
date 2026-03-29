Cuando trabajas con Google Cloud desde tu máquina local, existen dos mecanismos distintos de autenticación que suelen confundirse.

# `1) gcloud auth login` — autenticación del CLI

Permite que el SDK ejecute comandos contra Google Cloud desde la terminal.

```bash
gcloud auth login
```

Se usa para cualquier comando del CLI:

```bash
gcloud projects list
gcloud functions deploy
bq query ...
```

*Las credenciales se guardan en: ~/.config/gcloud/credentials.db*



# `2) gcloud auth application-default login` — autenticación de librerías cliente (ADC)

Permite que las librerías oficiales de Google Cloud se autentiquen desde tu código.

```bash
gcloud auth application-default login
```

Se usa cuando tu código accede a Google Cloud directamente, por ejemplo:

```bash
from google.cloud import bigquery

client = bigquery.Client()
```

*La librería no usa las credenciales de `gcloud auth login` — usa ADC. Sin este comando, ese código fallará aunque el CLI funcione perfectamente. Las credenciales se guardan en: ~/.config/gcloud/application_default_credentials.json*



# Problema común: quota project mismatch

Ocurre cuando cambias el proyecto activo con `gcloud config set project` pero ADC sigue apuntando al proyecto anterior:

```plain text
Your active project does not match the quota project in your local Application Default Credentials file.
```

La solución:

```bash
gcloud auth application-default set-quota-project TU_PROJECT_ID
```

# Resumen:





