

# PASO 1 — Verificación del entorno

Abre **PowerShell** (no necesita ser administrador por ahora) y ejecuta estos comandos uno por uno, dime el output de cada uno:

**1.1 — ¿Tienes Git?**

**Git** es el sistema de control de versiones. Registra los cambios de tu código, permite trabajar en equipo y es la base de todo. Sin Git, nada más funciona.

```bash
git --version
```

**1.2 — ¿Tienes SSH?**

**OpenSSH** es el protocolo de autenticación segura. Le dice a GitHub *"esta persona es quien dice ser"* sin usar usuario y contraseña cada vez. Es la llave con la que entras.

```bash
ssh -V
```

**1.3 — ¿Tienes GH?**

**GitHub CLI (****`gh`****)** es una herramienta opcional que te permite interactuar con GitHub (crear repos, abrir PRs, etc.) directamente desde la terminal. No reemplaza a Git, lo complementa — Git maneja tu código local, `gh` maneja la plataforma GitHub.

```bash
gh --version
```


🔗 **Relación entre los tres:** Git necesita SSH para autenticarse con GitHub de forma segura. `gh` usa esa misma autenticación SSH por debajo. Los tres trabajan juntos, ninguno se pisa con otro.





# PASO 2 — Instalar Git: opciones disponibles

| Método | Comando / Fuente | Pros | Contras |
| --- | --- | --- | --- |
| **winget** | `winget install --id Git.Git -e` | Nativo de Windows 10/11, sin descargar nada extra, actualizable con `winget upgrade` | Requiere winget activo (viene por defecto en W11, en W10 puede faltar) |
| **Instalador oficial** | git-scm.com | Control total de opciones durante instalación, más visual para principiantes | Manual, hay que ir al navegador y elegir bien las opciones |
| **Chocolatey** | `choco install git` | Popular en entornos DevOps, gestiona muchas herramientas juntas | Requiere instalar Chocolatey primero si no lo tienes |
| **Scoop** | `scoop install git` | Instalaciones limpias sin tocar el registro de Windows | Requiere instalar Scoop primero |

---

**Recomendación:**

- Si ya tienes `winget` → **Opción 1**, es lo más directo
- Si es un equipo de desarrollo que ya usa Chocolatey → **Opción 3**
- Si quieres la experiencia más visual y controlada → **Opción 2**



# PASO 3 — Instalar Git con winget

Primero verifica que winget esté disponible:

```bash
winget --version
```

Si responde `no reconocido`, significa que tu Windows no lo tiene. 

Si sí responde, instala Git:

```bash
winget install --id Git.Git -e --source winget
```

Durante la instalación verás progreso en la terminal. Cuando termine:

⚠️ **Cierra y vuelve a abrir PowerShell** antes de verificar

```bash
git --version
```

---



# PASO 4 — Elegir método de autenticación con GitHub

Tienes 3 opciones para conectarte con GitHub:

| Método | Pros | Contras |
| --- | --- | --- |
| **SSH** | Se configura una vez, nunca más pide credenciales, estándar profesional | Requiere generar y registrar una llave |
| **HTTPS + Token** | Rápido de configurar, sin instalar nada extra | El token expira, hay que renovarlo y gestionarlo |
| **GitHub CLI (****`gh`****)** | Guiado paso a paso, maneja SSH o HTTPS por debajo automáticamente | Requiere instalar `gh` primero |

> 🔗 **Nuestra ruta:** configuraremos **SSH** ahora (Paso 5) e instalaremos `gh` al final como herramienta complementaria.



# PASO 5 — Configurar SSH

## 5.1 — Instalar OpenSSH Client

Solo ejecuta este paso si el comando anterior (`ssh -V`) no fue reconocido.

Tienes dos opciones:

| Método | Pros | Contras |
| --- | --- | --- |
| **Windows Capability** | Nativo de Windows, sin dependencias | Solo funciona desde PowerShell Admin |
| **winget** | Consistente con cómo instalamos Git, actualizable | Requiere tener winget activo |

**Opción 1 — Windows Capability** (PowerShell como Administrador):

```bash
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

**Opción 2 — winget:**

```bash
winget install --id Microsoft.OpenSSH.Beta -e --source winget
```

Verifica que se instaló correctamente:

```bash
ssh -V
```



## 5.2— Verificar/Activar OpenSSH en Windows

OpenSSH viene incluido en Windows 10/11 pero puede no estar activo. Abre **PowerShell como Administrador** y verifica. Este comando también se ejecuta solo una vez para verificar si OpenSSH está instalado en ese usuario/equipo:

```bash
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

```bash
#Verás algo como:

Name  : OpenSSH.Client~~~~0.0.1.0
State : Installed        

Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent
```

Solo necesitas `OpenSSH.Client`. El `OpenSSH.Server` no es necesario aquí.

Si `OpenSSH.Client` dice `NotPresent`, instálalo:

```bash
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

Verifica:

```bash
ssh -V
```

---

## 5.3 — Configurar ssh-agent como servicio permanente

Esto es lo más importante. Sin este paso, tu llave SSH se olvida cada vez que reinicias.
Este bloque solo necesitas ejecutarlo una vez por usuario de Windows para dejar `ssh-agent` configurado como servicio automático.

```bash
# Configurar para que arranque automáticamente con Windows
Set-Service -Name ssh-agent -StartupType Automatic

# Iniciarlo ahora mismo
Start-Service -Name ssh-agent

# Verificar
Get-Service -Name ssh-agent | Select-Object Name, Status, StartTyp
```

Toda esa sección se ejecuta una sola vez por usuario de Windows. Una vez que `ssh-agent` queda en `Automatic`, seguirá arrancando solo cada vez que inicies sesión.

```bash
Esperado:

Name      Status  StartType
----      ------  ---------
ssh-agent Running Automatic
```

> ⚠️ Si dice `Manual` en lugar de `Automatic`, el primer comando no se ejecutó correctamente. Verifica que PowerShell esté abierto como Administrador.



---

## 5.4 — Generar tu llave SSH (sin sobrescribir la existente)

En **PowerShell normal** (ya no necesitas admin):

```bash
ssh-keygen -t ed25519 -C "angelg@reechai.com" -f $HOME\.ssh\id_ed25519_lenovo_reechai
```

- `t ed25519` → usa el algoritmo moderno recomendado
- `C "angelg@reechai.com"` → agrega una etiqueta para identificar la llave
- `f $HOME\.ssh\id_ed25519_reechai` → guarda la llave con otro nombre para no sobrescribir la llave personal existente

**`Importante`**: si ya tienes una llave personal en `id_ed25519`, no presiones Enter para usar la ruta por defecto, porque la reemplazarías.

**`Importante`**:  Una misma cuenta de GitHub puede tener varias llaves SSH al mismo tiempo. De hecho es lo normal cuando usas la misma cuenta en varios equipos o varios usuarios de Windows.

Al ejecutar el comando te pedirá:

```bash
Enter passphrase (empty for no passphrase):
```

Puedes:

- presionar Enter para dejarla vacía (de preferencia para poder automatizar los push)
- o ingresar una contraseña si quieres mayor seguridad

Si la dejas vacía, no tendrás que escribir una contraseña cada vez que hagas `git push`.

Deberías ver un mensaje similar a:

```bash
Your identification has been saved in C:\Users\TU_USUARIO\.ssh\id_ed25519_reechai
Your public key has been saved in C:\Users\TU_USUARIO\.ssh\id_ed25519_reechai.pub
```

Verifica que se crearon los archivos:

```bash
Get-ChildItem $HOME\.ssh
```

```bash
#Esperado:
id_ed25519        ← llave privada (nunca la compartas ni la subas a ningún lado)
id_ed25519.pub    ← llave pública (esta es la que se sube a GitHub)

#`known_hosts` almacena las huellas digitales de los servidores SSH a los que ya te has conectado (por ejemplo, GitHub) para verificar su identidad en futuras conexiones. `known_hosts.old` es una copia de respaldo generada automáticamente. Estos archivos no contienen tus llaves SSH ni credenciales, por lo que normalmente no necesitas modificarlos ni eliminarlos.
# agent es una carpeta creada por el servicio ssh-agent de OpenSSH en Windows. Guarda información temporal de las claves cargadas mientras el agente está funcionando.
```

Agrega la llave al agente:

```bash
ssh-add $HOME\.ssh\id_ed25519_lenovo_reechai
```

**`Importante`**: Utilizar el nombre de la llave

Verificar:

```bash
ssh-add -l
```

Mostrar la llave pública para copiarla a GitHub:

```bash
Get-Content $HOME\.ssh\id_ed25519_lenovo_reechai.pub
```

**`Importante`**: Utilizar el nombre de la llave

## 5.5 — Agregar la llave pública a GitHub

Copia tu llave pública al portapapeles:

```bash
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | clip
```

Luego en GitHub:

1. Ve a 👉 https://github.com/settings/keys
1. Clic en **New SSH key**
1. **Title:** algo descriptivo como `Windows - Mi PC`
1. **Key type:** `Authentication Key`
1. **Key:** pega el contenido (ya está en tu portapapeles)
1. Clic en **Add SSH key**

Verifica que la conexión funciona:

```bash
ssh -T git@github.com
```

```bash
#Esperado:
Hi tuusuario! You've successfully authenticated, but GitHub does not provide shell access.
```





# PASO 6 — Clonar el repositorio

## 6.1 — Navegar a la carpeta donde quieres clonar

Primero decide dónde quieres guardar el proyecto. Algunos ejemplos comunes:

```bash
#Raíz del sistema
cd /

# Si tienes una carpeta de proyectos
cd C:\Users\TuUsuario\Projects

# O en el escritorio
cd C:\Users\TuUsuario\Desktop

# O crear una carpeta nueva y entrar
mkdir C:\Projects
cd C:\Projects
```

El `git clone` creará automáticamente una carpeta con el nombre del repositorio dentro de donde estés parado. No necesitas crear la carpeta del proyecto manualmente.

## 6.2 — Clonar

```bash
git clone git@github.com:Reech-Team/obsidian-atrapalo-argentina.git
```

## 6.3 — Verificar

```bash
# Entrar al repositorio
cd obsidian-atrapalo-argentina

# Ver el estado
git status
# Esperado: On branch main, nothing to commit, working tree clean

# Ver la conexión con GitHub
git remote -v
# Esperado:
# origin  git@github.com:Reech-Team/obsidian-atrapalo-argentina.git (fetch)
# origin  git@github.com:Reech-Team/obsidian-atrapalo-argentina.git (push)
```