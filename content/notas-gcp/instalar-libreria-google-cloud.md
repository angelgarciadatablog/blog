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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/ce6dfcc3-d51f-47cf-a7c5-442ae1d3d8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P3CRDRI%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQComlWjw7gc1D45oIKcyGGBWSeSGyxOZZjBrpU50mLU0gIhAL%2B6mwci87AjN%2B6pwPCZ5AWg%2B14FJoT5itxknKELGuHtKv8DCAUQABoMNjM3NDIzMTgzODA1IgxsG6kAOO3jKFTo7ZMq3AO0nZc5bo2laqzyKf3xW2Kmff%2BBeBD%2FFBMyDpNjARRORbY%2BPxWEc2XWbN4AnLyd9w4TvuOCpUx2sZJehhbVG4FV7SjkqPa%2FZ%2BUuJgN6mWoFxvzSg9ytl5vPN1gBKpmlRAkZeveUBqe0VP%2F7PySb%2FgxRflzb%2FxsR3RcgAh%2FAlDIOMSXziiLREQNJoBNP4Lm8%2FM6u8dD0t044zTTsOIIFhpQVlDi2fd8lCqx7uqMO%2BbL6tn%2FacHfX%2FGOpC%2FqKOvT6jrX4WDPrEntKmYDlbKNLpvTOhwyd9Qt41EJ4mOFNyWmQQS4Vl0mYTad3lW5NLG5VKCDbFaYPnhGvxqOvvTg1WQJa6BCKN8Ohe46yegpI4LbnnPyo3dgqLzPKLh5NfC5XQXVuyFjpbSw9ff1NBYPU%2FInSt1Z%2FkKEeCo0tLj8JkdZgSz%2FoJspqCvOYED53b5i2z%2BQN16dsySdaOIHsfVilRpFkLg7pUWwzoYlfJ9DiuqmjgUSRs%2FscLDnedmAIDyel3wU3zL7lhhOxU3BkEVgpVTRMwV0cY7rC%2FUjq5xpptywlhWuQu5ChFhJa9ktgHGawNbqPKR60yeLJsohTkHnEc1rj8I6mwJJHpUhplB%2BoBlOhag7dmlTYRkfgNRDl0TC%2Bx6LOBjqkAflcxDAPN0YwnzgAG%2FoTW%2BR2CMSKIWDmoGlfcWeingscYkVNpua9%2FPN%2ByrYmwQtnHhhWajbpuqaO1O5krKadPC1vanEofs4bmsj%2F2fp%2FZ7Q1dKQLk%2BlOo7TER0XjgMf7VNkz6SPGy%2BElDWPviZ%2B%2FALCWHy0QA6c8Xdkdan5FaTCnsnBWdvN9HkoV7iWu%2F1srVh%2B%2FLWuXtXnHtLFupxFwC%2FNtRn6W&X-Amz-Signature=ca5fa042d56da1b61b2a4dbbe1e79d382019e9426d4bbd3040f1c2b65c2480bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



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

```plain text
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

```plain text
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

```plain text
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



