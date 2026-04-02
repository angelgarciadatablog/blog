# Paso 1: Verificar si ya está instalado

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

# Paso 2: **Elegir método de instalación**

Hay tres formas de instalar el SDK en Mac. Elige la que mejor se adapte a ti:

## 1) Instalador .pkg: 

Descarga un instalador gráfico, como cualquier otra aplicación de Mac. Ideal si prefieres no usar la terminal para instalar.

  1. Ir a la página oficial y descargar el .pkg:
   ```bash
   https://cloud.google.com/sdk/docs/install#mac
   ```
  1. Abrir el .pkg descargado y seguir el asistente.
  1. Abrir una terminal nueva y verificar:
   ```bash
   gcloud version
   ```



## **2) Homebrew**: 

El método más limpio si ya usas terminal. Homebrew gestiona la instalación y actualizaciones automáticamente.



  1. Verificar que Homebrew esté instalado:
   ```bash
   brew --version
   ```
  1. Instalar el SDK:
   ```bash
   brew install --cask google-cloud-sdk
   ```
       - **`brew install`** instala herramientas de línea de comandos — programas que viven en la terminal y no tienen interfaz gráfica. Homebrew los descarga, compila si es necesario, y los deja disponibles como comandos.
       - **`brew install --cask`** instala aplicaciones que tienen una forma de distribución empaquetada, normalmente con un instalador propio (.pkg, .dmg o .app). El flag `--cask` le dice a Homebrew "esto no es una librería ni una CLI pura, es un paquete con su propio instalador, manéjalo diferente".



  1. Agregar al PATH (solo la primera vez):
   ```bash
   echo 'source "$(brew --prefix)/share/google-cloud-sdk/path.zsh.inc"' >> ~/.zshrc
   echo 'source "$(brew --prefix)/share/google-cloud-sdk/completion.zsh.inc"' >> ~/.zshrc
   source ~/.zshrc
   ```
  1. Abrir una terminal nueva y verificar:
   ```bash
   gcloud version
   ```
   *Con Homebrew, actualizar el SDK en el futuro es tan simple como brew upgrade --cask google-cloud-sdk.*



## **3) Script Interactivo:**

Descarga un script que te guía paso a paso con preguntas interactivas. Útil cuando quieres controlar exactamente dónde se instala.



  1. Descargar y ejecutar el instalador interactivo:
   ```bash
   curl https://sdk.cloud.google.com | bash
   ```
   *El script te preguntará dónde instalar y si quiere modificar tu shell. Responde según tus preferencias — puedes aceptar los valores por defecto.*
  1. Reiniciar la terminal:
   ```bash
   exec -l $SHELL
   ```
  1. Verificar:
   ```bash
   gcloud version
   ```
   *Este método instala el SDK en **`~/google-cloud-sdk`** por defecto. Las actualizaciones hay que hacerlas manualmente con **`gcloud components update`**.*



# Paso 3: Revisar que componentes se instalaron

```bash
gcloud components list
```

*`gcloud components list`** muestra todos los componentes disponibles e instalados — útil para ver si necesitas agregar algo como **`bq`** (BigQuery) o **`gsutil`**.*



## **Componentes del Google Cloud SDK ¿Qué es un componente?**

Un componente es una parte instalable del SDK. Puede ser una herramienta de línea de comandos (`gcloud`, `bq`, `gsutil`), un conjunto de comandos en niveles alpha o beta, o un paquete con dependencias internas. Google **Componentes que se instalan por defecto**
Al instalar el SDK con cualquiera de los tres métodos vistos, obtienes automáticamente estos cuatro componentes:


1. **`gcloud`** — La herramienta principal. Con ella interactúas con prácticamente todos los servicios de Google Cloud: Compute Engine, Cloud Run, IAM, redes, etc. Solo incluye comandos en nivel GA (General Availability), los más estables.

1. **`bq`** — La CLI de BigQuery. Permite crear datasets, cargar datos, ejecutar consultas SQL y administrar tablas directamente desde la terminal.

1. **`gsutil`** — La herramienta legacy de Cloud Storage. Sigue funcionando, pero Google recomienda usar `gcloud storage` en su lugar, que es más moderno y está incluido en el componente `gcloud`.

1. **`core`** — Librerías internas que usan el resto de herramientas. No lo usas directamente, pero sin él nada funciona.



## Instalar, actualizar y eliminar componentes

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



## Importante: Homebrew y el gestor de componentes

Si instalaste el SDK con **Homebrew**, el gestor de componentes de `gcloud` está deshabilitado. Esto significa que `gcloud components install` no funcionará. En ese caso, los componentes adicionales se instalan con Homebrew directamente:

```bash
brew install kubectl
```

Y las actualizaciones del SDK completo se hacen con:

```bash
brew upgrade --cask google-cloud-sdk
```

