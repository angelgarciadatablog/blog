**¿Qué es un CLI?**
CLI = *Command Line Interface*. Es un programa que se usa desde la terminal escribiendo comandos, en lugar de hacer clic en botones. Por ejemplo, en vez de abrir GitHub en el navegador, escribes    `gh repo clone` y listo.



**Comando para revisar aplicaciones instaladas:**

```bash
ls /Applications
```

*En Mac todas las aplicaciones se guardan en la carpeta Applications



**Comando para revisar las CLIs instaladas con Homebrew**

```bash
brew list
```





**estores de paquetes en Mac:**

| Gestor | Para qué sirve | Cómo listar lo instalado |
| --- | --- | --- |
| **Homebrew** | CLIs y apps generales del sistema | `brew list` |
| **npm** | Paquetes de JavaScript/Node.js | `npm list -g --depth=0` |
| **nvm** | Versiones de Node.js | `nvm list` |
| **pyenv** | Versiones de Python | `pyenv versions` |
| **App Store** | Apps oficiales de Apple | Desde la UI |

💡 `brew list` solo muestra lo instalado con Homebrew. nvm, npm, pyenv se instalan por separado y gestionan sus propias versiones.



---

**Setup actual:**

| Gestor | Paquetes instalados |
| --- | --- |
| **Homebrew** | `gh`, `pyenv`, `gcloud-cli`, `ngrok`, `obsidian`, `postman` |
| **npm (via nvm)** | `n8n` |
| **Instalación nativa (web)** | `claude` |

---

**¿Cuáles requieren login?**
No todos los CLIs necesitan login — solo los que se conectan a un servicio externo con tu cuenta:

| CLI | Servicio | ¿Requiere login? |
| --- | --- | --- |
| Git | GitHub / GitLab / cualquier repo | ⚠️ Parcialmente (nombre y email) |
| GitHub CLI (`gh`) | GitHub | ✅ Sí |
| Google Cloud SDK (`gcloud`) | Google Cloud | ✅ Sí |
| npm | npmjs.com | ✅ Solo si publicas paquetes |
| Claude CLI | Anthropic | ✅ Sí |

**Los que NO necesitan login:**

- Python, Node.js, WinRAR, VLC, etc. — son herramientas locales que no se conectan a ningún servicio con tu cuenta.