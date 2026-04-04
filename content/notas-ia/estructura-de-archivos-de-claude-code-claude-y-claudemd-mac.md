# **1. ¿Por qué entender esto?**

Cuando trabajas con Claude Code, los archivos y carpetas que se generan no son aleatorios. Cada uno tiene un propósito específico y vive en un lugar determinado. Entender esta estructura te evita confusiones, te ayuda a depurar problemas y te permite sacarle el máximo provecho.



# 2. usuario/.claude/ (en la carpeta global)

Es un directorio oculto que guarda **configuraciones, credenciales y datos persistentes** que usa Claude en tu sistema, para que funcione correctamente.

## **2.1 ¿Cuándo se crea?**

Se crea en **dos momentos distintos**, no de golpe:

```bash
Durante la instalación de Claude Code:
usuario/.claude/
├── backups/
├── cache/
└── downloads/
```

```bash
Al ejecutar claude por primera vez (desde cualquier directorio):
usuario/.claude/ agrega:
├── history.jsonl
├── mcp-needs-auth-cache.json
├── plugins/
├── projects/
├── sessions/
└── settings.json
```

> 💡 Claude Code nunca toca tu proyecto sin que se lo pidas. Todo lo que genera automáticamente vive en `usuario/.claude/`, nunca en tu proyecto.



## 2.2 Estructura completa con el uso

Con el tiempo, a medida que usas más funcionalidades, aparecen carpetas adicionales:

```bash
~/.claude/
├── backups/              ← instalación
├── cache/                ← instalación
├── downloads/            ← instalación
├── history.jsonl         ← primer uso
├── mcp-needs-auth-cache.json ← primer uso
├── plugins/              ← primer uso
├── projects/             ← primer uso
├── sessions/             ← primer uso
├── settings.json         ← primer uso
├── debug/                ← cuando hay errores o modo debug
├── file-history/         ← historial de archivos editados
├── ide/                  ← cuando conectas un IDE
├── plans/                ← cuando usas modo plan
├── session-env/          ← snapshots del entorno por sesión
├── shell-snapshots/      ← estado del shell en cada interacción
├── skills/               ← cuando creas o usas skills
├── statsig/              ← métricas de uso
├── telemetry/            ← datos de telemetría
└── todos/                ← cuando usas tareas
```

> 💡 Las carpetas que aparecen con el uso no se crean vacías — se crean cuando hay algo que guardar en ellas. Cada una se explica en detalle en su bloque correspondiente.



## 2.3 ¿Qué contiene cada carpeta base?

| Carpeta/Archivo | Qué contiene |
| --- | --- |
| `backups/` | Respaldos automáticos de archivos antes de editarlos |
| `cache/` | Caché general de Claude Code |
| `downloads/` | Archivos descargados durante sesiones |
| `history.jsonl` | Historial de todos los comandos ejecutados |
| `mcp-needs-auth-cache.json` | Caché de servidores MCP que necesitan autenticación |
| `plugins/` | Plugins instalados globalmente |
| `projects/` | Sesiones e historial de conversaciones por proyecto |
| `sessions/` | Datos de sesiones activas |
| `settings.json` | Configuración global de Claude Code |

### Una por usuario

`~/.claude/` es personal — cada usuario de Mac tiene la suya:

```bash
Tu Mac
├── Usuario angel
│   └── ~/.claude/    ✅ su propia carpeta global
│
└── Usuario datablog
    └── ~/.claude/    ✅ su propia carpeta global, independiente
```





# 3. proyecto/.claude/ (dentro del proyecto)

A diferencia de `usuario/.claude/` que se crea durante la instalación, la carpeta `.claude/` dentro de un proyecto **se crea bajo demanda** — solo cuando hay algo que persistir.

## 3.1 ¿Cómo se genera?

No existe un comando que la cree explícitamente. Se genera de forma implícita:

| Acción | Qué crea |
| --- | --- |
| Cambiar una preferencia personal en `/config` | `.claude/settings.local.json` |
| Cambiar una configuración del equipo en `/config` | `.claude/settings.json` |
| Agregar reglas | `.claude/rules/` |
| Agregar skills del proyecto | `.claude/skills/` |
| Agregar agentes | `.claude/agents/` |

## 3.2 settings.json vs settings.local.json

Al cambiar configuraciones en `/config`, Claude Code decide inteligentemente dónde guardar cada cambio:

| Archivo | Para qué | ¿Se commitea a git? |
| --- | --- | --- |
| `settings.json` | Configuración compartida con el equipo | ✅ Sí |
| `settings.local.json` | Preferencias personales del proyecto | ❌ No, es personal |

**Ejemplo real:** al cambiar `Show tips` a `false` en `/config`, Claude lo guardó en `settings.local.json` porque es una preferencia personal:

```bash
{
  "spinnerTipsEnabled": false
}
```

`settings.local.json `Es el archivo para tus preferencias personales dentro de un proyecto específico. Lo que lo hace especial:

- **No se comparte** con el equipo
- **Debe agregarse al****`.gitignore`** para evitar subirlo accidentalmente
- Claude Code lo crea automáticamente cuando cambias preferencias personales en `/config`

## 3.3 No genera toda la estructura de golpe dentro de .claude (con varias carpetas)

```bash
~/test-claude/
├── CLAUDE.md
├── README.md
├── script.sh
└── .claude/
    └── settings.local.json    ← solo lo que se necesitó
```

💡 `.claude/` dentro del proyecto es bajo demanda. `usuario/.claude/` en cambio se crea durante la instalación con una estructura base.





# 4. CLAUDE.md

## 4.1 ¿Qué es?

Es un archivo markdown que le da a Claude **instrucciones persistentes** sobre tu proyecto. A diferencia de una conversación que Claude olvida al cerrar la sesión, el `CLAUDE.md` se lee automáticamente cada vez que inicias `claude` en ese directorio.

## 4.2 ¿Es lo mismo que `README.md`?

No, tienen propósitos distintos:

|   | `README.md` | `CLAUDE.md` |
| --- | --- | --- |
| **Para quién** | Humanos / equipo | Claude |
| **Qué contiene** | Descripción del proyecto, instalación, uso | Instrucciones y contexto para Claude |
| **Se actualiza** | Manualmente | Manualmente o con `/init` |
| **¿Se commitea?** | ✅ Sí | ✅ Sí |

## 4.3 ¿Cómo se genera?

Con el comando `/init` dentro de Claude Code:

```bash
cd ~/mi-proyecto
claude
/init
```

💡 `/init` no genera contenido genérico — analiza tu código real. En un proyecto vacío no puede generar nada útil.

### Los 4 escenarios de `/init`

| Escenario | Qué hace |
| --- | --- |
| Proyecto vacío | No genera nada, necesita código para analizar |
| Primera vez con código | Genera `CLAUDE.md` desde cero |
| `CLAUDE.md` existe y está actualizado | Confirma que está bien, no propone cambios |
| `CLAUDE.md` existe pero el código cambió | Muestra diff y propone solo los cambios necesarios |

### Flujo recomendado

```bash
1. Haces cambios en tu código
2. /init → Claude detecta cambios y propone actualizar CLAUDE.md
3. Confirmas los cambios
4. Le pides a Claude: "actualiza el README basándote en el CLAUDE.md"
5. Revisas el README antes de commitear
```

⚠️ Siempre revisa el README antes de commitear — está dirigido a humanos y Claude puede no saber qué tan técnica es tu audiencia.







# 5. Sesiones

## 5.1 ¿Qué es una sesión?

Es el historial de una conversación con Claude Code vinculada a un directorio específico. Se guarda automáticamente en `~/.claude/projects/` — nunca dentro de tu proyecto.

```bash
usuario/mi-proyecto/                          ← tu código vive aquí

usuario/.claude/projects/
└── Users-angel-mi-proyecto/            ← la sesión vive aquí
    └── [historial de conversaciones]
```

💡 Las sesiones de Claude Code son completamente independientes de las conversaciones de claude.ai — esas viven en los servidores de Anthropic, no en tu Mac.



## 5.2 Proyecto = ruta exacta

Para Claude Code, **proyecto es igual a ruta exacta**:

```bash
cd ~/proyecto-A        → sesión en projects/Users-angel-proyecto-A/
cd ~/proyecto-A/src    → sesión en projects/Users-angel-proyecto-A-src/
```

⚠️ Siempre entra desde la raíz de tu proyecto. Si entras desde un subdirectorio tendrás sesiones fragmentadas que no comparten historial. Esto lo desarrollamos en detalle en el próximo bloque.



## 5.3 Cómo retomar sesiones

```bash
# Continuar la sesión más reciente del directorio actual
claude -c

# Ver todas las sesiones y elegir cuál retomar
claude -r
```

Al ejecutar `claude -r` verás:

```bash
Resume Session
┌─────────────────────────────────────┐
│ ⌕ Search…                           │
└─────────────────────────────────────┘

❯ exits
  18 seconds ago · HEAD · 6.6KB

  Hola, quiero saber cómo...
  2 weeks ago · HEAD · 1.8MB
```

| Elemento | Qué significa |
| --- | --- |
| Primera línea | Primer mensaje de esa conversación |
| Tiempo | Hace cuánto fue la última actividad |
| `HEAD` | Branch de git en ese momento |
| Tamaño | Peso del historial de esa sesión |

### Atajos en la pantalla de sesiones

| Atajo | Acción |
| --- | --- |
| `Ctrl+A` | Ver sesiones de todos los proyectos |
| `Ctrl+B` | Filtrar por branch de git |
| `Ctrl+V` | Vista previa de la sesión |
| `Ctrl+R` | Renombrar la sesión |
| `Esc` | Cancelar |



## 5.4 Las sesiones crecen con el tiempo

```bash
# Ver cuánto ocupan tus sesiones
du -sh ~/.claude/projects/
```

⚠️ Cada conversación se guarda completa. En el largo plazo esto puede ocupar espacio considerable en tu Mac.

### Limpiar sesiones

```bash
# Eliminar sesiones de un proyecto específico
rm -rf ~/.claude/projects/nombre-del-proyecto/

# Eliminar TODAS las sesiones (no recuperable)
rm -rf ~/.claude/projects/
```

⚠️ No hay forma de recuperar sesiones eliminadas.



# 6. Resumen: Dos niveles de configuración

Todo en Claude Code funciona en dos niveles que se aplican en cascada:

```bash
~/.claude/                    ← nivel global (todos tus proyectos)
    +
~/mi-proyecto/.claude/        ← nivel proyecto (solo este proyecto)
    =
Configuración final aplicada
```

Si hay conflicto, el nivel proyecto tiene prioridad sobre el global.

|   | Global (`~/.claude/`) | Proyecto (`.claude/`) |
| --- | --- | --- |
| **CLAUDE.md** | `~/.claude/CLAUDE.md` instrucciones para todos tus proyectos | `./CLAUDE.md` instrucciones solo para este proyecto |
| **settings.json** | Configuración global | Configuración del equipo |
| **settings.local.json** | — | Preferencias personales del proyecto |
| **Skills** | Disponibles en todos los proyectos | Solo disponibles en este proyecto |
| **MCP servers** | Conectados en todos los proyectos | Solo conectados en este proyecto |
| **Reglas** | Aplican en todos los proyectos | Solo aplican en este proyecto |
| **Agentes** | Disponibles en todos los proyectos | Solo disponibles en este proyecto |

💡 Esto es muy poderoso — puedes tener tus preferencias personales globales y por encima de eso cada proyecto tiene sus propias reglas específicas.