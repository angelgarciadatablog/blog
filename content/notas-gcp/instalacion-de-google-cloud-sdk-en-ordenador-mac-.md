## Paso 1: Verificar si ya está instalado

Antes de instalar nada, comprueba si el SDK ya está en tu Mac.

```bash
gcloud --version
```

Si ya está instalado, verás algo como:

```bash
Google Cloud SDK 513.0.0
bq 2.1.11
core 2024.11.08
gsutil 5.31
```





## Paso 2: **Elegir método de instalación**

Hay tres formas de instalar el SDK en Mac. Elige la que mejor se adapte a ti:



### **2) Homebrew**: 

El método más limpio si ya usas terminal. Homebrew gestiona la instalación y actualizaciones automáticamente.







### **3) Script Interactivo:**

Descarga un script que te guía paso a paso con preguntas interactivas. Útil cuando quieres controlar exactamente dónde se instala.





## Paso 3: Revisar que componentes se instalaron

```bash
gcloud components list
```

`gcloud components list` muestra todos los componentes disponibles e instalados — útil para ver si necesitas agregar algo como `bq` (BigQuery) o `gsutil`.



### **Componentes del Google Cloud SDK ¿Qué es un componente?**

Un componente es una parte instalable del SDK. Puede ser una herramienta de línea de comandos (`gcloud`, `bq`, `gsutil`), un conjunto de comandos en niveles alpha o beta, o un paquete con dependencias internas. Google**Componentes que se instalan por defecto**
Al instalar el SDK con cualquiera de los tres métodos vistos, obtienes automáticamente estos cuatro componentes:


1. **`gcloud`** — La herramienta principal. Con ella interactúas con prácticamente todos los servicios de Google Cloud: Compute Engine, Cloud Run, IAM, redes, etc. Solo incluye comandos en nivel GA (General Availability), los más estables.


1. **`bq`** — La CLI de BigQuery. Permite crear datasets, cargar datos, ejecutar consultas SQL y administrar tablas directamente desde la terminal.


1. **`gsutil`** — La herramienta legacy de Cloud Storage. Sigue funcionando, pero Google recomienda usar `gcloud storage` en su lugar, que es más moderno y está incluido en el componente `gcloud`.


1. **`core`** — Librerías internas que usan el resto de herramientas. No lo usas directamente, pero sin él nada funciona.



### Instalar, actualizar y eliminar componentes

Instalar uno o varios componentes a la vez:

```bash
gcloud components install COMPONENTE_ID
gcloud components install kubectl cloud-sql-proxy beta
```

Actualizar todos los componentes instalados a la última versión:

```bash
gcloud components update
```

Eliminar un componente que ya no necesitas:

```bash
gcloud components remove COMPONENTE_ID
```



### Importante: Homebrew y el gestor de componentes

Si instalaste el SDK con **Homebrew**, el gestor de componentes de `gcloud` está deshabilitado. Esto significa que `gcloud components install` no funcionará. En ese caso, los componentes adicionales se instalan con Homebrew directamente:

```bash
brew install kubectl
```

Y las actualizaciones del SDK completo se hacen con:

```bash
brew upgrade --cask google-cloud-sdk
```

