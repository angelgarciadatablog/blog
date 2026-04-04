# **5 — Símbolos especiales**

Dentro de Claude Code hay 4 símbolos que activan comportamientos especiales:

| Símbolo | Cómo se usa | Qué hace |
| --- | --- | --- |
| `!` | `! ls -la` | Ejecuta un comando bash directamente desde Claude Code sin pedirle a Claude que lo haga |
| `@` | `@src/index.js` | Referencia un archivo del proyecto para que Claude lo lea y use como contexto |
| `&` | `& claude "tarea"` | Ejecuta una tarea en segundo plano mientras sigues trabajando |
| `/btw` | `/btw ¿qué es un hook?` | Hace una pregunta rápida sin interrumpir la conversación principal |

## 5.1 Modo bash (!)

```bash
# En lugar de pedirle a Claude que liste los archivos
# puedes ejecutarlo tú directamente
! ls -la
! git status
```

💡 Útil cuando quieres ejecutar algo rápido sin que Claude intervenga. Recuerda que `permissions.deny` bloquea a Claude, no a ti — con `!` puedes leer cualquier archivo aunque Claude no pueda.

## 5.2 Referenciar archivos (@)

```bash
# Pedirle a Claude que revise un archivo específico
revisa @src/index.js y dime si hay mejoras

# Referenciar varios archivos
compara @src/v1.js con @src/v2.js
```

💡 Claude lee el archivo completo y lo agrega al contexto de la conversación. Respeta el `.gitignore` si tienes activado `Respect .gitignore in file picker` en `/config`.

## 5.3 Background (&)

```bash
# Ejecutar una tarea larga en segundo plano
& claude "revisa todos los archivos del proyecto y genera un reporte"
```

💡 Útil para tareas largas. Puedes seguir trabajando mientras Claude procesa en segundo plano. Los resultados aparecen cuando termina.

## 5.4 Pregunta lateral (/btw)

```bash
# Pregunta rápida sin perder el hilo principal
/btw ¿qué diferencia hay entre == y === en JavaScript?
```

💡 Claude responde la pregunta y luego vuelve al contexto de la conversación principal como si no hubiera pasado nada.



# 6 — Comandos esenciales del día a día

| Comando | Qué hace |
| --- | --- |
| `/help` | Muestra todos los comandos disponibles y atajos |
| `/clear` | borra el historial de la conversación actual en memoria |
| `/compact` | Limpia el historial pero guarda un resumen en contexto |
| `/status` | Muestra versión, modelo, cuenta, conectividad y estado de herramientas |
| `/model` | Cambia el modelo de Claude para esta sesión |
| `/copy` | Copia la última respuesta de Claude al portapapeles |
| `/diff` | Muestra cambios no commiteados y diffs por turno |
| `/exit` | Sale de Claude Code |
| `/config` | Abre el panel de configuración |
| `/doctor` | Diagnostica y verifica tu instalación de Claude Code |
| `/init` | Inicializa o actualiza el archivo CLAUDE.md del proyecto |

## 6.1 /compact — Limpiar el historial

```bash
# Compact con instrucciones específicas de resumen
/compact enfócate en los cambios de la API que hicimos
```

# 7 — Comandos de sesión

| Comando | Qué hace |
| --- | --- |
| `/resume` | Historial de conversaciones (Permite retomar una conversación anterior) |
| `/rename` | Renombra la conversación actual |
| `/branch` | Crea una rama de la conversación en este punto |
| `/rewind` | Restaura el código y/o conversación a un punto anterior |
| `/export` | Exporta la conversación actual a un archivo o portapapeles |
| `/desktop` | Continúa la sesión actual en Claude Desktop |
| `/teleport` | Retoma una sesión de Claude Code desde claude.ai |

## 7.1 /resume — Historial de conversaciones

- Te permite ver todas las conversaciones anteriores (sesiones) y retomar
- Se restaura el historial completo de la conversación que seleccionaste

```bash
/resume
```

- **Sin git (tu caso actual):**

Las sesiones se guardan por directorio exacto. Si iniciaste Claude en /test-claude, el /resume solo mostrará sesiones de ese directorio. Si lo iniciaste en /test-claude/subcarpeta, solo verás las de ahí. Son independientes.

- **Con git:**

El directorio raíz del repo es la referencia. Sin importar si iniciaste Claude desde /mi-repo, /mi-repo/src o /mi-repo/src/components, todas esas sesiones se agrupan bajo el mismo proyecto porque comparten el mismo .git. El /resume las mostraría todas juntas.



## 7.2 /rename — Renombrar conversación

Nombra la sesión actual para identificarla fácilmente. 

El nombre aparece en la barra del prompt y puedes reanudar esa sesión después con /resume.

- /rename mi-sesion — asigna ese nombre manualmente
- /rename (sin args) — genera un nombre automático basado en la conversación

```bash
# Sin argumento → genera un nombre automático basado en el contexto
/rename

# Con argumento → tú eliges el nombre
/rename mi-nombre-personalizado
```



## 7.3 /branch — Crear una rama de la conversación

Crea una bifurcación de la conversación actual en ese punto. **No requiere git.**

Imagina que vas por el punto A de una conversación y quieres explorar dos enfoques diferentes sin perder ninguno:

```bash
Conversación principal
         │
         A ──── /branch ────► Rama B (enfoque 1)                                                                                                                                 
                          └──► Rama C (enfoque 2)
```

Cada rama mantiene su propio historial independiente desde ese punto. Luego puedes volver a cualquiera con /resume.

### **Casos de uso típicos:**

- Probar dos soluciones distintas a un problema
- Experimentar sin "arruinar" la conversación principal
- Retomar un punto anterior con un enfoque diferente





## 7.4 /Rewind — Restaura el código y/o conversación a un punto anterior

Deshace los últimos mensajes de la conversación. Es como un **Ctrl+Z** pero para tu conversación con Claude. Si la respuesta que te dio no te gustó o tomó un camino incorrecto, puedes retroceder al punto anterior y volver a intentarlo.

**Diferencia con /branch:**

- /rewind — retrocedes y **reemplazas** lo que pasó
- /branch — retrocedes pero **conservas** ambos caminos





## 7.5 /Export — Exporta la conversación actual a un archivo o portapapeles

Exporta la conversación actual como texto plano para que puedas guardarla o documentarla. Útil para documentar conversaciones importantes o guardar el historial fuera de Claude Code.  

- /export — abre un diálogo para copiar al portapapeles o guardar en archivo
- /export mi-archivo.txt — guarda directamente en ese archivo



## 7.6 /Desktop — Continúa la sesión actual en Claude Desktop

Transfiere la sesión actual de Claude Code CLI a la aplicación **Claude Desktop**, manteniendo el contexto e historial de la conversación.

- Requiere tener instalada la app **Claude Desktop**. 



## 7.6 /Teleport — Retoma una sesión de Claude Code desde claude.ai

Las sesiones que /teleport puede detectar se generan de **3 maneras específicas**:

**1. claude.ai/code (web)**

- Entras a claude.ai/code desde el navegador
- Claude corre en servidores de Anthropic, clona tu repo de GitHub y ejecuta tareas en la nube

**2. Desde tu terminal con --remote**

- claude --remote "arregla el bug de autenticación"
-  Crea una sesión remota en la nube desde tu propia terminal

**3. GitHub Actions / Slack**

- Tareas automatizadas disparadas por comentarios en PRs, issues, o workflows de CI/CD

