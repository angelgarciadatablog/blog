| Comando | Qué hace |
| --- | --- |
| `/context` | Visualiza el uso actual del contexto como una grilla de colores |
| `/clear` | Borra el historial de la conversación actual en memoria |
| `/compact` | Limpia el historial pero guarda un resumen en contexto |
| `/memory` | Edita los archivos de memoria de Claude |
| `/plan` | Activa el modo plan o muestra el plan de la sesión actual |
| `/tasks` | Lista y gestiona tareas en segundo plano |

---

# 1. /context — Contexto actual

El comando `/context` muestra cuántos tokens está usando la sesión actual y cómo están distribuidos.

Verás una pantalla como esta:

```bash
Context Usage
⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛀ ⛀ ⛁   Sonnet 4.6
                       claude-sonnet-4-6

⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛶ ⛶ ⛶   29.4k/200k tokens (15%)

⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Estimated usage by category
                       ⛁ System prompt: 6.2k tokens (3.1%)
⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System tools: 8.5k tokens (4.2%)
                       ⛁ Memory files: 164 tokens (0.1%)
⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Skills: 545 tokens (0.3%)
                       ⛁ Messages: 15.8k tokens (7.9%)
⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛶ Free space: 147.8k (73.9%)
                       ⛝ Autocompact buffer: 21k tokens (10.5%)

Memory files · /memory
└ CLAUDE.md: 164 tokens

Skills · /skills
User
└ datablog-design-v1: 69 tokens
```

---

## 1.1 ¿Qué significa cada categoría?

| Categoría | Qué contiene | ¿Quién lo controla? | ¿Crece durante la sesión? |
| --- | --- | --- | --- |
| `System prompt` | Instrucciones base de Claude Code | Anthropic — no se puede tocar | ❌ Fijo |
| `System tools` | Herramientas disponibles para Claude | Anthropic — no se puede tocar | ❌ Fijo |
| `Memory files` | Tus archivos `CLAUDE.md` | ✅ Tú — cuánto escribes en el `CLAUDE.md` | ❌ Fijo |
| `Skills` | Skills que tienes instaladas | ✅ Tú — cuántas skills tienes activas | ❌ Fijo |
| `Messages` | La conversación actual | Se genera solo | ✅ Crece con cada mensaje |
| `Free space` | Espacio disponible | — | ✅ Decrece con cada mensaje |
| `Autocompact buffer` | Reserva para comprimir automáticamente | Anthropic | ❌ Fijo |

---

## 1.2 Los porcentajes son sobre el total del modelo

Todos los porcentajes son sobre los **200k tokens totales** del modelo, no sobre el porcentaje usado:

```bash
Total del modelo: 200k tokens = 100%

System prompt:  6.2k = 3.1%  ┐
System tools:   8.5k = 4.2%  │
Memory files:    164 = 0.1%  ├── Total usado: 29.4k = 15%
Skills:          545 = 0.3%  │
Messages:      15.8k = 7.9%  ┘

Free space:   147.8k = 73.9%
Autocompact:    21k  = 10.5%
```

---

## 1.3 /context vs Usage en /config

Son dos medidores completamente distintos:

|   | `/context` | `/config` → Usage |
| --- | --- | --- |
| **Qué mide** | Tokens de la conversación actual | Cuota de tu plan Pro |
| **Total** | 200k tokens por sesión | Tu límite mensual/semanal |
| **Se recarga** | Al hacer `/clear` o `/compact` | Automáticamente según tu plan |
| **Para qué sirve** | Saber cuándo necesitas compactar | Saber si te quedas sin créditos |

---

## 1.4 Lo que crece con la conversación

Al ejecutar `/context` dos veces en la misma sesión vimos:

```bash
Primera vez:  21.7k tokens → Messages: 8.9k
Segunda vez:  29.4k tokens → Messages: 15.8k
```

Solo `Messages` creció — todo lo demás es fijo. Esto confirma que **System prompt, System tools, Memory files y Skills se cargan una vez al inicio y no cambian**.

---



## 1.5 El impacto de skills y CLAUDE.md en el contexto

Los componentes que tú controlas consumen tokens fijos en cada sesión:

```bash
Sin skills ni CLAUDE.md:
→ Sistema ocupa ~15k tokens
→ Disponible para mensajes: ~164k tokens

Con 50 skills globales (~500 tokens c/u = 25k) + CLAUDE.md extenso (2k):
→ Sistema ocupa ~42k tokens
→ Disponible para mensajes: ~137k tokens
```

> ⚠️ Las **skills globales** (~/.claude/skills/) se cargan en **todos tus proyectos** sin excepción. Las **skills del proyecto** (.claude/skills/) solo en ese proyecto. Por eso es importante no acumular skills globales que no usas.

> 💡 El `CLAUDE.md` solo afecta al proyecto actual — no es global a menos que crees uno en `~/.claude/CLAUDE.md`.

---





# 2. /clear — Limpiar la conversación actual

Borra el historial de la conversación actual en memoria. Claude ya no recuerda lo que hablaron, pero **la sesión sigue guardada** en `/Users/tu_usuario/.claude/projects/` — puedes retomar con `/resume`.

```bash
/clear
```

💡 Piénsalo como limpiar la pizarra — el borrador queda en el archivo, pero Claude empieza con la mente en blanco.



# 3. /compact — Compactar manteniendo el contexto

Limpia el historial pero guarda un resumen en el contexto. A diferencia de `/clear`, Claude sigue recordando lo esencial de la conversación.

```bash
# Compactar sin instrucciones
/compact

# Compactar indicando qué conservar
/compact enfócate en los cambios de la API que hicimos
```

## /clear vs /compact

|   | `/clear` | `/compact` |
| --- | --- | --- |
| ¿Qué hace? | Borra todo el historial en memoria | Borra el historial pero guarda un resumen |
| ¿Claude recuerda algo? | ❌ No | ✅ Sí, el resumen |
| ¿Cuándo usarlo? | Cuando quieres empezar de cero | Cuando el contexto está lleno pero quieres continuar |



# 4. /memory — Gestión de memoria

El comando `/memory` te permite ver y editar los archivos de memoria que Claude usa en cada sesión.

Verás esta pantalla:

```bash
Memory

  Auto-memory: on
  Auto-dream: off · never

❯ 1. Project memory    Saved in ./CLAUDE.md
  2. User memory       Saved in ~/.claude/CLAUDE.md
  3. Open auto-memory folder

Learn more: https://code.claude.com/docs/en/memory
```

---

## 4.1 ¿Qué hace cada opción?

| Opción | Qué hace | Dónde guarda |
| --- | --- | --- |
| `1. Project memory` | Abre el `CLAUDE.md` del proyecto actual en tu editor | `/Users/tu_usuario/mi_proyecto/CLAUDE.md` |
| `2. User memory` | Crea (si no existe) y abre el `CLAUDE.md` global en tu editor | `/Users/tu_usuario/.claude/CLAUDE.md` |
| `3. Open auto-memory folder` | Abre en Finder la carpeta donde Claude guarda sus notas automáticas | `/Users/tu_usuario/.claude/projects/-Users-tu_usuario-mi_proyecto/memory/` |

---

### **—Auto-dream**

Aparece en la pantalla de `/memory` como `Auto-dream: off · never`. Es una función experimental que permite a Claude generar reflexiones y conexiones entre sesiones de forma autónoma — como si "soñara" con lo que aprendió.

### —Auto-memory

Cuando está activado (`Auto-memory: on`), Claude guarda notas automáticamente sobre tus preferencias y patrones de trabajo a lo largo de las sesiones. Por ejemplo:

- Comandos que usas frecuentemente
- Convenciones de código que prefieres
- Patrones que Claude detecta en tu forma de trabajar

Estas notas viven en la carpeta `memory/` del proyecto y se cargan al inicio de cada sesión. En proyectos nuevos la carpeta empieza vacía y se va llenando con el uso.

💡 La carpeta `memory/` es diferente al `CLAUDE.md` — el `CLAUDE.md` lo escribes tú, el `memory/` lo escribe Claude solo.

---

### —User memory — `~/.claude/CLAUDE.md`

Al seleccionar `2. User memory` por primera vez, Claude crea el archivo vacío y lo abre en tu editor. Este archivo es el equivalente global del `CLAUDE.md` de proyecto — aplica a **todos tus proyectos**.

```bash
# Ejemplo de ~/.claude/CLAUDE.md

## Mis preferencias globales
- Siempre responde en español
- Usa type hints en Python
- Prefiero async/await sobre callbacks
- Siempre incluye manejo de errores
```

> ⚠️ Todo lo que escribas aquí consume tokens en **cada sesión de todos tus proyectos**. Mantenlo conciso.

---

### —¿Qué va en `CLAUDE.md` del proyecto vs `~/.claude/CLAUDE.md`?

| `CLAUDE.md` del proyecto | `~/.claude/CLAUDE.md` |
| --- | --- |
| Stack y arquitectura del proyecto | Preferencias personales globales |
| Comandos específicos del proyecto | Estilo de código que usas siempre |
| Convenciones del equipo | Idioma de respuesta |
| Archivos importantes del proyecto | Herramientas que siempre usas |

---

### —¿Cuántos tokens consume cada archivo?

Ambos archivos se cargan en el contexto y consumen tokens:

| Archivo | Cuándo se carga | Impacto |
| --- | --- | --- |
| `./CLAUDE.md` del proyecto | Solo cuando estás en ese proyecto | Local — afecta solo ese proyecto |
| `/Users/tu_usuario/.claude/CLAUDE.md` global | En **todos** tus proyectos | ⚠️ Global — afecta todas tus sesiones |

Puedes verificar cuánto consume cada uno con `/context`:

```bash
Memory files: 500 tokens
├ CLAUDE.md (proyecto): 164 tokens
└ CLAUDE.md (usuario): 336 tokens
```

> ⚠️ El `CLAUDE.md` global es el más costoso porque se carga en absolutamente todos tus proyectos. Mantenlo conciso y con solo lo que realmente necesitas en todos lados. Todo lo específico de un proyecto va en el `CLAUDE.md` del proyecto.



# 5. /plan — Activar el modo plan de la sesión actual

El modo plan le dice a Claude que **investigue y proponga cambios sin ejecutarlos**. Claude puede leer archivos, explorar el proyecto y hacer preguntas, pero no toca tu código hasta que tú lo apruebes.

## 5.1 ¿Cuándo usarlo?

| Situación | ¿Usar modo plan? |
| --- | --- |
| Explorar ideas y debatir opciones en proyectos pequeños | ❌ Mejor el modo normal — más conversacional |
| Feature que toca muchos archivos | ✅ Sí — ver el plan antes de aprobar |
| Refactor grande o riesgoso | ✅ Sí — revisar exactamente qué va a cambiar |
| Explorar una codebase desconocida antes de cambiar algo | ✅ Sí — Claude solo lee, no modifica |

💡 `/plan` no es solo un comando — es uno de los **modos de permiso** de Claude Code. Al activarlo cambias el modo de la sesión completa. Claude puede leer archivos y explorar el proyecto pero no toca tu código hasta que tú lo apruebes. Puedes ciclar entre modos con `Shift + Tab`:

```bash
default → acceptEdits → plan → auto
```

## 5.2 Cómo activarlo

```bash
# Dentro de Claude Code con el comando
/plan

# Al iniciar la sesión desde la terminal
claude --permission-mode plan
```

Cuando está activo verás en el pie de pantalla:

`⏸ plan mode on (shift+tab to cycle)`

---



## 5.3 Cómo funciona

Al darle una tarea en modo plan, Claude:

- **Lee** los archivos relevantes
- **Explora** la estructura del proyecto
- **Genera un plan** con esta estructura:

```bash
Plan: [nombre del plan]

Context
→ Qué existe actualmente y qué se quiere lograr

Approach
→ La estrategia técnica elegida y por qué

Changes
→ Exactamente qué archivos va a tocar y cómo

Notes
→ Decisiones técnicas que tomó y por qué

Verification
→ Cómo verificar que los cambios funcionaron
```

- **Espera tu aprobación** antes de tocar cualquier archivo

---



## 5.4 Las 4 opciones al recibir un plan

```bash
Claude has written up a plan and is ready to execute. Would you like to proceed?

❯ 1. Yes, auto-accept edits
  2. Yes, manually approve edits
  3. No, refine with Ultraplan on Claude Code on the web
  4. Tell Claude what to change
```

| Opción | Qué hace | Cuándo usarla |
| --- | --- | --- |
| `1. Yes, auto-accept edits` | Ejecuta el plan aprobando todos los cambios automáticamente | Cuando confías en el plan completo |
| `2. Yes, manually approve edits` | Ejecuta pero pide confirmación en cada cambio individual | Cuando quieres supervisar paso a paso |
| `3. No, refine with Ultraplan` | Abre claude.ai para refinar el plan visualmente — **requiere git** | Para planes complejos que necesitan más iteración |
| `4. Tell Claude what to change` | Claude descarta el plan, te hace preguntas y genera uno nuevo | ✅ Cuando el plan no es lo que necesitas |

> 💡 La opción 4 es iterativa — puedes seguir refinando el plan tantas veces como necesites hasta que sea exactamente lo que quieres.

---



## 5.5 Los planes se guardan en disco

Cada vez que inicias un `/plan` con una tarea nueva se crea un archivo con nombre aleatorio:

```bash
/Users/tu_usuario/.claude/plans/crystalline-whistling-hamster.md
/Users/tu_usuario/.claude/plans/vectorized-puzzling-wirth.md
```

> 💡 Si usas la opción 4 para refinar, el mismo archivo se actualiza. Solo se crea un archivo nuevo cuando inicias un plan completamente diferente.

---



## 5.6 Ejemplo real

```bash
❯ /plan
⎿  Enabled plan mode

❯ agrega una función dividir al script.sh

⏺ Updated plan

Plan: Add dividir function to script.sh

Context
The script.sh contains arithmetic utility functions (sumar, restar,
multiplicar). The user wants to add a dividir function.

Changes
File: /Users/angelgarciachanga/test-claude/script.sh
1. Add dividir() function after multiplicar()
2. Add a sample call at the bottom: dividir 10 2

Notes
- Uses the same $(( )) arithmetic expansion pattern
- Integer division, consistent with the rest del script
- No division-by-zero guard — existing functions have no error handling

Verification
Run bash script.sh and confirm output includes 5 (from dividir 10 2)
```

---

## 5.7 Salir del modo plan

```bash
# Con atajo de teclado
Shift + Tab  # cicla al siguiente modo

# O desde la terminal al iniciar sin el flag
claude  # sin --permission-mode plan
```



# 6.  /task — Gestionar tareas en segundo plano

📌 **Pendiente — Bloque Agentes:** Este comando gestiona tareas que
se ejecutan en segundo plano, generalmente creadas por agentes paralelos.
Lo documentamos en detalle cuando veamos agentes.

