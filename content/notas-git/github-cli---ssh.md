**¿Qué es SSH?**
SSH (Secure Shell) es un protocolo de comunicación segura. En el contexto de Git/GitHub, se usa para autenticarte sin contraseñas ni tokens — usando un par de llaves matemáticamente relacionadas.



**El par de llaves:**

`🔑 Llave privada  → se queda en tu equipo (nunca sale)
🔓 Llave pública  → la subes a GitHub (puede verse)`

Cuando haces un `git push`, GitHub verifica que tu llave privada corresponde con la pública que tienes registrada — si coinciden, acceso concedido.



**Lo que vamos a hacer ahora (pasos):**

1. **Generar el par de llaves** en tu equipo con `ssh-keygen`

1. **Agregar la llave privada al agente SSH** de Windows — para no tener que escribir nada cada vez

1. **Subir la llave pública a GitHub** — una sola vez

1. **Configurar gh para usar SSH** en vez de HTTPS

1. **Verificar** que todo funciona



## **Paso 0 — Verificar **

mac

```bash
#Verificar cuántos pares de SSH tienes:
ls ~/.ssh

#cada par de keys tiene dos archivos:
#- id_ed25519 — clave privada (nunca compartas esto)
#- id_ed25519.pub — clave pública (esta es la que subes a GitHub)

#Verificar si GitHub reconoce tu llave:
ssh -T git@github.com
```

windows

```bash
#Verificar cuántos pares de SSH tienes:
dir C:\Users\TU_USUARIO\.ssh

#Cada par de keys tiene dos archivos:
#- id_ed25519 — clave privada (nunca compartas esto)
#- id_ed25519.pub — clave pública (esta es la que subes a GitHub)

Verificar si GitHub reconoce tu llave:
ssh -T git@github.com
```



## **Paso 1 — Generar el par de llaves:**

```bash
ssh-keygen -t ed25519 -C "angelgarciadatablog@gmail.com"
```

Cuando te pregunte:

- **Dónde guardarla** → presiona Enter (usa la ruta por defecto `~/.ssh/id_ed25519`)

- **Passphrase** → te recomiendo ponerle una contraseña, agrega una capa extra de seguridad. Si alguien roba tu llave privada, sin la passphrase no puede usarla.

⚠️ Si creas una passphrase, el agente SSH se resetea al reiniciar el Mac y te la pedirá cada vez que hagas push.

**Solución** → Configurar `~/.ssh/config`:

```bash
cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
```

La primera vez que uses la llave te pedirá la passphrase, la ingresas y Mac la recuerda permanentemente.



**¿Por qué ****`ed25519`****?**

Es el algoritmo moderno recomendado para generar llaves SSH — más seguro y eficiente que el antiguo `RSA`

Resultado:

```bash
Your identification has been saved in C:\Users\Lenovo/.ssh/id_ed25519
Your public key has been saved in C:\Users\Lenovo/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:b3qu1K88zcM12735vX4DPLI+gnesbJS6G8EtdDkMcPo angelg@reechai.com
The key's randomart image is:
+--[ED25519 256]--+
|     ..o         |
|      o o .      |
|     . . =       |
|      + o .      |
|       ES.. .    |
|        o= . +o  |
|       .= =+o.o+.|
|       +oBo*= ..*|
|       oB*O+o..=O|
+----[SHA256]-----+
```

Perfecto, las llaves se generaron correctamente:

windows

- **Llave privada:** `C:\Users\Lenovo\.ssh\id_ed25519` → se queda aquí, nunca la compartas

- **Llave pública:** `C:\Users\Lenovo\.ssh\id_ed25519.pub` → esta la subiremos a GitHub



mac

- Privada: `/Users/angelgarciachanga/.ssh/id_ed25519 `→ se queda aquí, nunca la compartas

- Pública: `/Users/angelgarciachanga/.ssh/id_ed25519.pub `→ esta la subiremos a GitHub



## **Paso 2 — Activar el agente SSH:**

mac

```bash
# Iniciar el agente SSH (opcional, usualmente ya corre solo en mac)
eval "$(ssh-agent -s)"

# Agregar tu llave al agente
ssh-add ~/.ssh/id_ed25519
```



windows

```bash
# Iniciar el agente SSH
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent

# Agregar tu llave al agente
ssh-add C:\Users\Lenovo\.ssh\id_ed25519
```

Te pedirá tu passphrase 

Repuesta:

```bash
Identity added: C:\Users\Lenovo\.ssh\id_ed25519 (angel@gmail.com)
```

```bash
Identity added: /Users/nombredeusuario/.ssh/id_ed25519 (angelgarciadatablog@gmail.com)
```





## **Paso 3 — Subir la llave pública a GitHub:**

Primero copia el contenido de tu llave pública:

Mac

```bash
cat /Users/nombredeusuario/.ssh/id_ed25519.pub
```



windows:

```bash
Get-Content C:\Users\Lenovo\.ssh\id_ed25519.pub
```



## **Ahora súbela a GitHub:**

1. Ve a **github.com** → inicia sesión con `angel-reechai`

1. Clic en tu foto → **Settings**

1. En el menú izquierdo → **SSH and GPG keys**

1. Clic en **New SSH key**

1. Rellena:

```bash
tu llave pública
```

1. Clic en **Add SSH key**





## **Paso 5 — Configurar gh para usar SSH:**

```bash
gh config set git_protocol ssh
```

Luego verifica:

```bash
gh config get git_protocol
```

Debería responder `ssh`.