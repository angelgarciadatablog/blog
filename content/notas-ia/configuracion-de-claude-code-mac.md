# 1. ¿Qué es /config?

`/config` es una interfaz visual que te permite cambiar configuraciones sin tocar ningún archivo. Es como un panel de control.



# **2. Dónde guarda cada cosa:**

Cuando cambias algo en `/config`, Claude guarda el cambio en distintos lugares dependiendo del tipo de configuración:

| Tipo de cambio | Se guarda en |
| --- | --- |
| Preferencias de interfaz  | `/Users/tu_usuario/.claude.json` — NO editar manualmente |
| Preferencias personales del proyecto | `/mi_proyecto/.claude/settings.local.json` |
| Configuración global personal | `/Users/tu_usuario/.claude/settings.json` |
| Configuración del proyecto settings.json | `/mi_proyecto/.claude/settings.json` |



# 3. Los archivos de configuración

Antes de entrar a `/config`, hay que entender dónde vive cada configuración:



| Archivo | Qué contiene | ¿Se edita manualmente? | ¿Se crea automáticamente? |
| --- | --- | --- | --- |
| `/Users/tu_usuario/.claude.json` | Estado interno, caché, preferencias de interfaz | ❌ No — Claude lo gestiona solo | ✅ Sí |
| `/Users/tu_usuario/.claude/settings.json` | Configuración global personal — aplica a todos tus proyectos | ✅ Sí | ✅ Vacío al primer uso |
| `/mi_proyecto/.claude/settings.json` | Configuración del proyecto settings.json — se commitea a git | ✅ Sí | ❌ No, Lo creas tú manualmente |
| `/mi_proyecto/.claude/settings.local.json` | Preferencias personales del proyecto | ✅ Sí |   |

⚠️ `~/.claude.json` y `~/.claude/settings.json` son archivos distintos aunque sus nombres se parezcan. El primero nunca se toca manualmente.



# 4. /config explicado

Para abrir el panel de configuración, primero debes estar dentro de una sesión de Claude Code:

```bash
# Entra a cualquier directorio de proyecto
cd /Users/tu_usuario/mi_proyecto

# Inicia Claude Code
claude

# Una vez dentro, abre la configuración
/config
```

Verás una pantalla como esta:

```bash
  Status   Config   Usage   Stats

  ╭─────────────────────────────────────╮
  │ ⌕ Search settings…                  │
  ╰─────────────────────────────────────╯

    Auto-compact                    true
    Show tips                       true
    ...
```

Navegación:

- `↑` `↓` → moverse entre opciones
- `Espacio` → cambiar el valor
- `Esc` → cerrar



## 4.1 Opciones que van a `.claude.json` (NO editar manualmente)

| Opción | Por defecto | Qué hace |
| --- | --- | --- |
| `Show turn duration` | `true` | Muestra cuánto tardó Claude en responder. Ej: `⏱ Cooked for 1m 6s` |
| `Terminal progress bar` | `true` | Barra de progreso mientras Claude trabaja. Solo en terminales compatibles: Ghostty 1.2+, iTerm2 3.6.6+ |
| `Editor mode` | `normal` | Modo de teclas (`normal` o `vim`) |
| `Auto-connect to IDE` | `false` | Conecta automáticamente con VS Code o JetBrains |

> ⚠️ Estas opciones solo deben cambiarse desde `/config`. Si intentas editarlas en `settings.json` Claude Code dará error de validación.

## 4.2 Todas las opciones disponibles

| Opción | Por defecto | Qué hace |
| --- | --- | --- |
| `Auto-compact` | `true` | Compacta automáticamente el contexto cuando se acerca al límite |
| `Show tips` | `true` | Muestra sugerencias mientras Claude trabaja |
| `Reduce motion` | `false` | Reduce animaciones de la interfaz |
| `Thinking mode` | `true` | Activa el modo de razonamiento extendido |
| `Rewind code (checkpoints)` | `true` | Guarda puntos de restauración antes de cambios |
| `Verbose output` | `false` | Muestra más detalle de lo que hace Claude internamente |
| `Terminal progress bar` | `true` | Barra de progreso. Solo en terminales compatibles |
| `Show turn duration` | `true` | Muestra cuánto tardó Claude en responder |
| `Default permission mode` | `Default` | Cómo Claude pide permisos para ejecutar acciones |
| `Respect .gitignore in file picker` | `true` | Excluye archivos del `.gitignore` al buscar con `@` |
| `Always copy full response` | `false` | Al copiar, copia la respuesta completa sin selector |
| `Auto-update channel` | `latest` | `latest` → versión más reciente. `stable` → ~1 semana de antigüedad, sin bugs críticos |
| `Theme` | `Dark mode` | Tema visual |
| `Notifications` | `Auto` | Notificaciones del sistema |
| `Output style` | `default` | Estilo de respuesta de Claude |
| `Language` | `Default (English)` | Idioma de la interfaz de Claude Code |
| `Editor mode` | `normal` | Modo de teclas (`normal` o `vim`) |
| `Show PR status footer` | `true` | Muestra estado de PR en el pie de pantalla |
| `Model` | `Default (recommended)` | Modelo de Claude a usar |
| `Auto-connect to IDE` | `false` | Conecta automáticamente con VS Code o JetBrains |
| `Claude in Chrome enabled` | `true` | Habilita integración con Chrome |
| `Enable Remote Control` | `default` | Control remoto desde claude.ai |

# 5 — /Users/tu_usuario/.claude/settings.json — configuración global personal

Aplica a **todos tus proyectos**. Se crea vacío `{}` al primer uso. Solo lo editas cuando quieres configurar algo globalmente.

```bash
# Ver tu configuración global actual
cat /Users/tu_usuario/.claude/settings.json
```

## Ejemplos de uso:

```bash
{
  "language": "spanish",
  "model": "claude-sonnet-4-6",
  "autoUpdatesChannel": "stable",
  "cleanupPeriodDays": 20
}
```

| Parámetro | Qué hace |
| --- | --- |
| `language` | Fuerza a Claude a responder siempre en español, independientemente del idioma en que le escribas |
| `model` | Define qué modelo usa Claude por defecto en todos tus proyectos |
| `autoUpdatesChannel` | `stable` → versión con ~1 semana de antigüedad, sin bugs críticos. `latest` → versión más reciente inmediatamente |
| `cleanupPeriodDays` | Días de inactividad antes de eliminar sesiones antiguas automáticamente. Por defecto son 30 días |

# 6 — proyecto/.claude/settings.json — configuración del proyecto

Este archivo **no se crea automáticamente** — lo creas tú manualmente cuando el proyecto lo necesita. Se commitea a git y aplica a todos los que trabajen en el proyecto.

```bash
# Crear el archivo manualmente
mkdir -p /Users/tu_usuario/mi_proyecto/.claude
cat > /Users/tu_usuario/mi_proyecto/.claude/settings.json << 'EOF'
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secretos.txt)"
    ]
  }
}
EOF
```



## 6.1 Lo que confirmamos en la práctica

Al agregar `permissions.deny` verificamos que:

- ✅ Claude intenta leer el archivo pero el sistema lo bloquea técnicamente
- ✅ Claude mismo informa que hay una regla activa bloqueando el acceso
- ✅ No puede saltárselo aunque le insistas — es un bloqueo técnico, no de comportamiento
- ⚠️ El `!` antes de un comando te permite a **ti** ejecutar comandos directamente — `permissions.deny` solo bloquea a Claude, no al usuario

```bash
# Esto SÍ funciona — tú puedes leerlo aunque Claude no pueda
! cat /Users/tu_usuario/mi_proyecto/.env
```



## 6.2 Los 10 parámetros más importantes

| Parámetro | Qué hace | Nivel recomendado |
| --- | --- | --- |
| `language` | Idioma de respuesta de Claude | Usuario o Proyecto |
| `model` | Modelo por defecto | Usuario |
| `permissions.deny` | Bloquear archivos o comandos — bloqueo técnico | Proyecto |
| `permissions.allow` | Permitir comandos sin confirmación | Proyecto |
| `permissions.ask` | Pedir confirmación antes de ejecutar | Proyecto |
| `autoUpdatesChannel` | Canal de actualizaciones (`latest` o `stable`) | Usuario |
| `env` | Variables de entorno para cada sesión | Proyecto |
| `cleanupPeriodDays` | Días antes de eliminar sesiones inactivas (default: 30) | Usuario |
| `attribution` | Personalizar texto de autoría en commits y PRs | Proyecto |
| `includeGitInstructions` | Incluir instrucciones de git en el system prompt | Proyecto |

> 💡 Hay más parámetros disponibles para casos avanzados. La referencia completa está en code.claude.com/docs/en/settings

### ⚠️ Sobre `language`

Verificamos en la práctica que `language` funciona como instrucción, no como restricción técnica — Claude puede ignorarlo si detecta que escribes en otro idioma y decide adaptarse. Para forzarlo estrictamente combínalo con una instrucción en `CLAUDE.md`:

```bash
## Idioma
Siempre responde en inglés sin excepción, independientemente del idioma en que te escriban.
```





# 7— proyecto/.claude/settings.local.json — preferencias personales del proyecto

Se crea automáticamente cuando cambias preferencias personales en `/config`. **Claude lo agrega al****`.gitignore`****automáticamente** cuando lo crea.

```bash
# Ver tus preferencias locales del proyecto
cat /Users/tu_usuario/mi_proyecto/.claude/settings.local.json
```

Ejemplo real generado automáticamente al cambiar una configuración utilizando el comando /config dentro de claude code:

```bash
{
  "spinnerTipsEnabled": false
}
```

## ¿Qué va aquí vs en `settings.json` del proyecto?

| `settings.local.json` | `settings.json` del proyecto |
| --- | --- |
| Preferencias visuales personales | Archivos protegidos del equipo |
| URLs locales de desarrollo | Comandos permitidos para todos |
| Configuraciones de tu máquina específica | Variables de entorno del proyecto |



# 8 — Los niveles de configuración

| Nivel | Nombre | Archivo | Alcance | ¿Se comparte? |
| --- | --- | --- | --- | --- |
| 1 (más alto) | Managed | `/Library/Application Support/ClaudeCode/managed-settings.json` | Todos los usuarios de la Mac | Solo empresas con IT — **no se usa en desarrollo individual** |
| 2 | Command line | No tiene archivo — se pasa al iniciar `claude` | Solo esa sesión | No |
| 3 | Local del proyecto | `/Users/tu_usuario/mi_proyecto/.claude/settings.local.json` | Solo tú, en ese proyecto | No |
| 4 | Proyecto | `/Users/tu_usuario/mi_proyecto/.claude/settings.json` | Todo el equipo | ✅ Sí, via git |
| 5 (más bajo) | Usuario | `/Users/tu_usuario/.claude/settings.json` | Solo tú, en todos tus proyectos | No |

> 

Command line: Se ejecuta al escribirlo directo en la terminal, por ejemplo: usar un modelo específico solo en esta sesión : claude --model claude-opus-4-6



Todo en Claude Code funciona en cascada. Cuando hay conflicto, el más específico gana:

💡 Para un desarrollador individual sin equipo, los niveles relevantes son **usuario** y **local**. Managed es solo para empresas con IT centralizado.

