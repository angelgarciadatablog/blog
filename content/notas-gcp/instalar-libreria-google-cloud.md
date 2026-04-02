# 🔐 Configuración de credenciales locales para BigQuery (Desarrollo)

## 🎯 Objetivo

Permitir que los notebooks y scripts en Python se conecten a BigQuery desde el entorno local utilizando **Application Default Credentials (ADC)**.

Esta configuración es **solo para desarrollo local**.

En producción (GitHub Actions) se usará un Service Account.

---

## 🥇 Paso 1 — Instalar Google Cloud CLI (si no está instalado)

Verificar si ya está instalado:

```bash
gcloud --version
```

Si no está instalado



```sql
pip install google-cloud-bigquery
```

---

## 🥈 Paso 2 — Autenticación con Application Default Credentials

En la terminal (fuera de Jupyter), ejecutar exactamente:

```bash
gcloud auth application-default login
```

*Para poder ejecutar esto se debe tener Google Cloud SDK instalado previamente

![](img/306477bcd0eb801cb981d366f43ccae3.webp)



Esto abrirá una ventana en el navegador para autheticarte con tu cuenta de google. Al final conectará con tu cuenta y te redijirá a esta página: https://docs.cloud.google.com/sdk/auth_success?hl=es-419



⚠️ Importante:

No es:

```bash
gcloud auth login
```

No es:

```bash
gcloud init
```

Es específicamente:

```bash
gcloud auth application-default login
```

---



## 🧠 ¿Qué ocurre al ejecutar el comando?

1. Se abre el navegador.
1. Se inicia sesión con la cuenta Google.
1. Se genera un archivo local en:

```
~/.config/gcloud/application_default_credentials.json
```

Este archivo contiene las credenciales necesarias para que las librerías oficiales de Google Cloud (como `google-cloud-bigquery`) puedan autenticarse automáticamente.

Este archivo es usado automáticamente por la librería Python.



# 🧪 Paso  de validación en notebook

Ve a tu notebook y ejecuta:

```python
from google.cloudimport bigquery

client = bigquery.Client()print("Proyecto detectado:", client.project)

datasets =list(client.list_datasets())for datasetin datasets:print(dataset.dataset_id)
```

Debería imprimir:

```
Proyecto detectado:
prueba2-433703
dataset_youtube_v3
```

*Esto lista los proyectos actuales dentro de la cuenta de google



# 📦 Uso de la librería `google-cloud-bigquery`

## 🎯 Objetivo

Permitir que el pipeline interactúe con BigQuery desde Python:

- Crear tablas
- Ejecutar queries
- Insertar datos
- Cargar DataFrames

# 🥇 Instalación previa

Antes de importar la librería, debe estar instalada en el entorno virtual:

```bash
pip install google-cloud-bigquery
```

Dependencias recomendadas adicionales:

```bash
pip install pyarrow
pip install python-dotenv
```

---

# 🥈 Importación en Python

```python
from google.cloud import bigquery
```

---

# 🧠 ¿Qué hace esta importación?

Este módulo:

- Proporciona el cliente oficial de BigQuery para Python.
- Permite autenticación mediante Application Default Credentials.
- Permite interactuar con el Data Warehouse sin usar el CLI.

Es parte del SDK oficial de Google Cloud para Python.





Contenido del `.env`:

```
GCP_PROJECT=prueba2-433703
```



# 🏗 Creación del cliente

Después de importar:

```python
import os
from google.cloud import bigquery

PROJECT_ID = os.getenv("GCP_PROJECT")

client = bigquery.Client(project=PROJECT_ID)

print("Proyecto activo:", client.project)
```

El objeto `client` permite:

- Ejecutar queries SQL
- Crear tablas
- Cargar DataFrames
- Ejecutar DELETE
- Ejecutar MERGE
- Gestionar datasets

---



# 🐍 Crear cliente BigQuery usando esa variable

```python
from google.cloud import bigquery

client = bigquery.Client(project=PROJECT_ID)
print("Proyecto activo:", client.project)
```

Esto garantiza que:

- El proyecto está definido explícitamente
- No depende del SDK
- Es portable a otros entornos



