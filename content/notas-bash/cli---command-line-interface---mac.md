CLI viene de —Command Line Interface— o sea, una herramienta que

usas desde la terminal escribiendo comandos. (No tiene pantallas ni botones, solo texto.)

Un **CLI** es un archivo binario que puedes ejecutar desde la Terminal.



![](img/2e3477bcd0eb8034bce2dc3e1c25cad0.webp)





> Las 5 formas más comunes de instalar CLIs (o apps) en macOS

Tu Mac, por sí misma, **no sabe instalar cosas nuevas**.

Necesita “métodos de instalación”: herramientas o formatos que le digan *cómo descargar, descomprimir y colocar los archivos en su sitio correcto*.

Existen varios **tipos de instaladores**, cada uno pensado para cierto tipo de programas.



![](img/2e3477bcd0eb8060b3c0f4d66e48599b.webp)



Instalar un CLI **no basta** para poder usarlo.

Después de instalarlo, el sistema necesita **saber dónde quedó guardado** para poder ejecutarlo desde cualquier parte.

Ahí entra en juego el **`$PATH`**.





![](img/2e3477bcd0eb80e79c62f8794affc2e7.webp)



![](img/2e3477bcd0eb80c28b96c3cb90900cc7.webp)



Ejemplo:

![](img/2e3477bcd0eb80bca27cdf322233f5d0.webp)



![](img/2e3477bcd0eb800caaffc950913e0dd9.webp)



![](img/2e3477bcd0eb8080bf1afdb65693089f.webp)





ejemplo:

```bash
nombre_usuario@MacBook-Air-de-Angel ~ % echo $PATH | tr ':' '\n'
/Users/nombre_usuario/.nvm/versions/node/v20.19.4/bin:
/Users/nombre_usuario/.pyenv/shims:
/Users/nombre_usuario/.pyenv/bin:
/opt/homebrew/bin:
/opt/homebrew/sbin:
/usr/local/bin:
/System/Cryptexes/App/usr/bin:
/usr/bin:
/bin:
/usr/sbin:
/sbin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
```

*Rojo → Rutas creadas al instalar algo 

- homebrew es como una tienda de aplicaciones para Mac con chip M
- .nvm para instalar diferentes de versiones node.js 
- .pyenv para instalar diferentes versiones de pytho

*Verde → Rutas estándar de Unix/macOS





### En palabras simples:

> Tu $PATH es como una lista de “lugares VIP”.

Cada vez que escribes un comando, tu Mac recorre la lista de arriba hacia abajo hasta encontrarlo.

Si lo encuentra, lo ejecuta.

Si no lo encuentra en ninguno... te dice: command not found





### Nota importante:

Si instalas **dos versiones de un mismo CLI**, **el que esté primero en tu****`$PATH`****gana**.

Por ejemplo:

- Si `python` existe en Pyenv y también en `/usr/bin`, se usará el de Pyenv (porque aparece antes).
- Lo mismo pasa con `node` o `npm` si usas NVM.



> ¿qué pasa si se borra algún path?

![](img/2e3477bcd0eb807e88f4cadb8af9c246.webp)



> ¿Qué pasa si creo otro usuario en mi mac? 

Si creas un usuario nuevo y revisas el PATH dentro de la consola, solo aparecerán las rutas estándares en Mac (VERDE), sin embargo hay que tener en cuenta algunas consideraciones:

- Los path que dicen nombre_de_usuario solo están disponibles para el usuario que lo instaló
- Los path como homebrew y /Library/Frameworks/Python. si están instalados a nivel de sistema, pero el nuevo usuario no tendrá acceso a esos programas desde la consola, al menos que los agregue al path.

```bash
usuario_nuevo@MacBook-Air-de-Angel ~ % echo $PATH | tr ':' '\n'
/Users/nombre_usuario/.nvm/versions/node/v20.19.4/bin:
/Users/nombre_usuario/.pyenv/shims:
/Users/nombre_usuario/.pyenv/bin:
/opt/homebrew/bin:
/opt/homebrew/sbin:
/usr/local/bin:
/System/Cryptexes/App/usr/bin:
/usr/bin:
/bin:
/usr/sbin:
/sbin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
```



> Agregar al path rutas que solo están en un solo usuario

Aquí vamos a agregar homebrew al nuevo usuario del sistema, puesto que solo se instaló en el usuario principal

```bash
echo 'export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"' >> ~/.zshrc
```

*Puedes ejecutar `echo` desde cualquier carpeta en la consola Porque `~/.zshrc` es una ruta absoluta





# Resumen

### 🧩 1. **Programas con interfaz gráfica (GUI)**

- Son los que **ves y usas con el mouse**.
- Se instalan usualmente con un archivo `.pkg` o `.dmg`.
- Quedan visibles en el **Finder → Aplicaciones**.
- Ejemplos:
    - Visual Studio Code
    - Google Chrome
    - Slack
    - Node.pkg

📍**Se ejecutan con doble clic**, no desde la terminal.

---

### ⚙️ 2. **Programas sin interfaz gráfica (CLI o “de línea de comandos”)**

- No tienen ventanas ni íconos: funcionan **solo en la terminal**.
- Se instalan con gestores de paquetes (como **Homebrew** o **npm**) o mediante scripts.
- Suelen ubicarse en `/usr/local/bin` o `/opt/homebrew/bin`.
- Ejemplos:
    - `git` → control de versiones
    - `ffmpeg` → conversión de video/audio
    - `python3` → intérprete de Python
    - `brew` → el propio gestor de paquetes
    - `claude` → cliente CLI de IA

📍**Se ejecutan escribiendo un comando**, no haciendo clic.

---

### 🧠 En resumen

En macOS conviven **dos mundos**:

- El **mundo visual (GUI)** → apps con ventanas.
- El **mundo invisible (CLI)** → herramientas que trabajan en segundo plano o desde la terminal.

Ambos se instalan desde Internet, pero el **tipo de instalador** define **cómo accedes al programa** (por Finder o por Terminal).v