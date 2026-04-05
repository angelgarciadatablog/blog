

| Comando | Qué hace |
| --- | --- |
| `/config` | Abre el panel de configuración visual → ver Bloque 4 |
| `/permissions` | Gestiona reglas de permisos allow, ask y deny |
| `/theme` | Cambia el tema visual |
| `/keybindings` | Abre o crea tu archivo de atajos de teclado personalizados |
| `/terminal-setup` | Activa Option+Enter para saltos de línea y visual bell |
| `/sandbox` | Configura el modo sandbox |

---



# 1. /config — Panel de configuración

Abre la interfaz visual para cambiar configuraciones de Claude Code. Ya lo explicamos en detalle en el **Bloque “**Configuración de Claude Code (/config) (Mac)”

```bash
/config
```



# 2. /permissions — Gestiona reglas de permisos 

Permite ver y gestionar las reglas de permisos de Claude Code para la sesión actual.

```bash
/permissions
```

Tiene 5 pestañas navegables con `←` `→`:

| Pestaña | Qué muestra |
| --- | --- |
| `Recently denied` | Acciones que Claude intentó ejecutar pero fueron bloqueadas |
| `Allow` | Herramientas y acciones que Claude puede usar sin pedir confirmación |
| `Ask` | Herramientas que siempre piden confirmación antes de ejecutarse |
| `Deny` | Herramientas y archivos bloqueados técnicamente |
| `Workspace` | Directorios a los que Claude tiene acceso |

---

## 2.1 Pestaña Recently denied

Muestra acciones que Claude intentó ejecutar pero el sistema bloqueó. Útil para detectar si alguna regla está siendo demasiado restrictiva o si hay intentos de acceso inesperados.

```bash
No recent denials. Commands denied by the auto mode classifier will appear here.
```

## 2.2 Pestaña Allow

Muestra las herramientas pre-aprobadas. Aquí aparecen las reglas de `permissions.allow` del `settings.json` y también herramientas de MCP conectados:

```bash
mcp__computer-use__left_click
mcp__computer-use__key
...
```

## 2.3 Pestaña Ask

Herramientas que siempre pedirán confirmación antes de ejecutarse, independientemente del modo de permiso activo.

```bash
Claude Code will always ask for confirmation before using these tools.
```

## 2.4 Pestaña Deny

Muestra los archivos y herramientas bloqueados técnicamente. Aquí se ven las reglas del `settings.json` del proyecto:

```bash
Read(./.env)
Read(./secretos.txt)
```

## 2.5 Pestaña Workspace

Muestra los directorios a los que Claude tiene acceso:

```bash
/Users/tu_usuario/mi_proyecto  (Original working directory)
```

> 💡 Puedes agregar nuevas reglas directamente desde `/permissions` sin editar manualmente el `settings.json` — selecciona `Add a new rule…` en cualquier pestaña.



## →Agregar una nueva regla desde /permissions

En lugar de editar manualmente el `settings.json`, puedes agregar reglas directamente desde la interfaz. Selecciona `Add a new rule…` en cualquier pestaña y verás:

```bash
Add deny permission rule

Permission rules are a tool name, optionally followed by a specifier in parentheses.
e.g., WebFetch or Bash(ls:*)

╭──────────────────────────────────────╮
│ Enter permission rule…               │
╰──────────────────────────────────────╯

Enter to submit · Esc to cancel
```

El formato de las reglas es:

| Formato | Ejemplo | Qué bloquea |
| --- | --- | --- |
| Solo herramienta | `WebFetch` | Todas las llamadas web |
| Con especificador | `Bash(rm *)` | Solo el comando `rm` |
| Archivo específico | `Read(./.env)` | Solo ese archivo |
| Patrón con wildcard | `Read(./secrets/*)` | Toda la carpeta secrets |
| Dominio específico | `WebFetch(domain:ejemplo.com)` | Fetch a ese dominio |
| Comando npm | `Bash(npm run *)` | Todos los scripts npm |
| Git específico | `Bash(git push *)` | Solo git push |
| Todas las ediciones | `Edit` | Cualquier edición de archivo |
| Edición específica | `Edit(./src/*)` | Solo ediciones en src/ |
| Agentes | `Agent` | Todos los subagentes |

> 💡 El formato general es `Herramienta(especificador)`. El `*` es un wildcard que coincide con cualquier valor. La lista completa de herramientas disponibles está en code.claude.com/docs/en/tools-reference.





# 3. /theme — Cambiar tema visual

```bash
/theme
```

Abre un selector con 6 opciones y una vista previa de código en tiempo real:

```bash
Theme

Choose the text style that looks best with your terminal

❯ 1. Dark mode ✔
  2. Light mode
  3. Dark mode (colorblind-friendly)
  4. Light mode (colorblind-friendly)
  5. Dark mode (ANSI colors only)
  6. Light mode (ANSI colors only)

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
 1  function greet() {
 2 -  console.log("Hello, World!");
 2 +  console.log("Hello, Claude!");
 3  }
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
Syntax theme: Monokai Extended (ctrl+t to disable)
```

| Opción | Para quién |
| --- | --- |
| `Dark mode` | La mayoría de usuarios — fondo oscuro |
| `Light mode` | Si prefieres fondo claro |
| `Dark/Light mode (colorblind-friendly)` | Paleta de colores adaptada para daltonismo |
| `Dark/Light mode (ANSI colors only)` | Terminales con soporte limitado de colores |

💡 El tema se guarda en `~/.claude.json` — aplica en todos tus proyectos. También se puede cambiar desde `/config` → `Theme`.





# 4. /keybindings — Atajos de teclado personalizados

```bash
/keybindings
```

Si no existe el archivo, lo crea automáticamente con una plantilla completa y lo abre en tu editor:

```bash
Created /Users/tu_usuario/.claude/keybindings.json with template. Opened in your editor.
```

## 4.1 ¿Para qué sirve?

El archivo `keybindings.json` te permite **cambiar o crear atajos de teclado** para Claude Code. Por ejemplo, si quieres que `Ctrl+K` limpie la conversación en lugar de `Ctrl+L`, lo defines aquí.

El archivo usa JSON con esta estructura:

```bash
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "$docs": "https://code.claude.com/docs/en/keybindings",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+s": "chat:stash",
        "enter": "chat:submit"
      }
    }
  ]
}
```



## 4.2 ¿Qué es un contexto?

Un contexto es **la pantalla o modo en que estás** dentro de Claude Code en ese momento. El mismo atajo puede hacer cosas distintas dependiendo de dónde estés:

```bash
Estás escribiendo en el chat    → contexto: Chat
Estás en el selector de tema    → contexto: ThemePicker
Estás viendo un diff            → contexto: DiffDialog
Estás en cualquier lugar        → contexto: Global
```

Por ejemplo `Escape` hace cosas distintas según el contexto:

- En `Chat` → cancela lo que Claude está haciendo
- En `Autocomplete` → descarta las sugerencias
- En `Settings` → cierra la configuración

---

## **4.3 ¿Cómo crear un atajo personalizado?**

```bash
{
  "context": "Chat",
  "bindings": {
    "ctrl+k": "chat:cancel"   ← presionar Ctrl+K cancela el chat
  }
}
```

El formato es siempre:

```bash
"atajo": "contexto:acción"
```

---



Los atajos están organizados por **contexto** — cada contexto es una pantalla o modo diferente de Claude Code:

| Contexto | Cuándo aplica |
| --- | --- |
| `Global` | En cualquier parte de Claude Code |
| `Chat` | Dentro del chat principal |
| `Autocomplete` | Cuando aparecen sugerencias |
| `Settings` | Dentro de `/config` |
| `Confirmation` | Cuando Claude pide confirmación |
| `Tabs` | Navegando entre pestañas |
| `Transcript` | Viendo el historial |
| `ThemePicker` | Dentro de `/theme` |
| `Scroll` | Navegando el contenido |
| `ModelPicker` | Seleccionando modelo |
| `DiffDialog` | Viendo diffs de archivos |

⚠️ El archivo vive en `/Users/tu_usuario/.claude/keybindings.json` — aplica globalmente a todos tus proyectos.





# 5. /terminal-setup — Configuración del terminal

```bash
/terminal-setup
```

⚠️Configura automáticamente **Terminal.app** de Mac para una mejor experiencia con Claude Code. No muestra opciones ni pide confirmación — ejecuta los cambios **inmediatamente** al invocarlo.

## 5.1 ¿Qué cambia exactamente?

Verificamos en la práctica que modifica dos configuraciones en Terminal.app:

| Cambio | Dónde en Terminal.app | Para qué sirve |
| --- | --- | --- |
| `Usar Opción como tecla modificadora` | Preferencias → Perfiles → Teclado | Habilita `Option+Enter` para saltos de línea sin enviar el mensaje |
| `Aviso visual` | Preferencias → Perfiles → Avanzado → Aviso | Reemplaza el beep sonoro por un parpadeo visual |

---

## 5.2 ¿Qué significa cada cambio?

**`Usar Opción como tecla modificadora`**

Por defecto en Mac, la tecla `Option` escribe caracteres especiales (`∑`, `®`, `†`). Al activar esta opción, `Option` funciona como tecla `Meta` — lo que habilita atajos como:

```bash
Option + Enter  → salto de línea sin enviar el mensaje
Meta + P        → cambiar modelo en Claude Code
Meta + T        → activar/desactivar thinking mode
```

Sin esta configuración estos atajos no funcionarían.

```bash
Aviso visual
```

Normalmente cuando la terminal quiere alertarte emite un sonido (`beep`). Con aviso visual, en lugar del sonido la pantalla parpadea brevemente. Es más discreto especialmente en espacios compartidos.

### ⚠️ Advertencias importantes

> Debes **reiniciar Terminal.app** para que los cambios tomen efecto — abre una nueva ventana con `Cmd + N`.

> Si no quieres estos cambios, puedes revertirlos manualmente en `Terminal → Configuración → Perfiles` desactivando las opciones correspondientes.

> 💡 Solo funciona con **Terminal.app** nativa de Mac. Si usas iTerm2, Ghostty, Warp u otro terminal, debes configurar estas opciones manualmente en sus preferencias.





# 6. /sandbox — Modo sandbox

```bash
/sandbox
```

El sandbox aísla los comandos bash de Claude del resto de tu sistema — Claude puede ejecutar comandos pero con acceso limitado al filesystem y red.

📌 **Pendiente:** El sandbox tiene sentido en contextos más avanzados como automatizaciones, agentes autónomos y CI/CD. Lo documentamos en detalle cuando lleguemos a esos bloques donde su uso será más claro y relevante.