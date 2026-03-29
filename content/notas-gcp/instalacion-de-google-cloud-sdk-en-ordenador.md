## Verificar si está instalado

```bash
gcloud --version
```



## Instalar CLI de google cloud

#### 1) Windows

En PowerShell escribe:

```bash
winget --version
```

Si responde con versión → perfecto.

Luego instala:

```bash
winget install Google.CloudSDK
```

Eso descarga e instala el SDK automáticamente.



#### 2) Mac

En macOS (que tú usas normalmente), lo ideal es Homebrew:

```bash
brew install --cask google-cloud-sdk
```



#### 3) Ubuntu

En Ubuntu el proceso se divide en varios pasos porque APT necesita que le digas manualmente de dónde descargar el SDK.

```bash
#Agregar llave de seguridad de Google:
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

#Agregar el repositorio de Google Cloud:
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list

#Actualizar catálogo de APT:
sudo apt update

#Instalar el SDK:
sudo apt install -y google-cloud-cli
```





---

