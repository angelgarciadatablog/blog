| Comando | Qué hace |
| --- | --- |
| `/resume` | Historial de conversaciones (Permite retomar una conversación anterior) |
| `/rename` | Renombra la conversación actual |
| `/branch` | Crea una rama de la conversación en este punto |
| `/rewind` | Restaura el código y/o conversación a un punto anterior |
| `/export` | Exporta la conversación actual a un archivo o portapapeles |
| `/desktop` | Continúa la sesión actual en Claude Desktop |
| `/teleport` | Retoma una sesión de Claude Code desde claude.ai |

# 1— /resume — Historial de conversaciones

- Te permite ver todas las conversaciones anteriores (sesiones) y retomar
- Se restaura el historial completo de la conversación que seleccionaste

```bash
/resume
```

- **Sin git (tu caso actual):**

Las sesiones se guardan por directorio exacto. Si iniciaste Claude en /test-claude, el /resume solo mostrará sesiones de ese directorio. Si lo iniciaste en /test-claude/subcarpeta, solo verás las de ahí. Son independientes.

- **Con git:**

El directorio raíz del repo es la referencia. Sin importar si iniciaste Claude desde /mi-repo, /mi-repo/src o /mi-repo/src/components, todas esas sesiones se agrupan bajo el mismo proyecto porque comparten el mismo .git. El /resume las mostraría todas juntas.



# 2— /rename — Renombrar conversación

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



# 3— /branch — Crear una rama de la conversación

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





# 4— /Rewind — Restaura el código y/o conversación a un punto anterior

Deshace los últimos mensajes de la conversación. Es como un **Ctrl+Z** pero para tu conversación con Claude. Si la respuesta que te dio no te gustó o tomó un camino incorrecto, puedes retroceder al punto anterior y volver a intentarlo.

**Diferencia con /branch:**

- /rewind — retrocedes y **reemplazas** lo que pasó
- /branch — retrocedes pero **conservas** ambos caminos





# 5— /Export — Exporta la conversación actual a un archivo o portapapeles

Exporta la conversación actual como texto plano para que puedas guardarla o documentarla. Útil para documentar conversaciones importantes o guardar el historial fuera de Claude Code.  

- /export — abre un diálogo para copiar al portapapeles o guardar en archivo
- /export mi-archivo.txt — guarda directamente en ese archivo



# 6— /Desktop — Continúa la sesión actual en Claude Desktop

Transfiere la sesión actual de Claude Code CLI a la aplicación **Claude Desktop**, manteniendo el contexto e historial de la conversación.

- Requiere tener instalada la app **Claude Desktop**. 



# 7— /Teleport — Retoma una sesión de Claude Code desde claude.ai

Las sesiones que /teleport puede detectar se generan de **3 maneras específicas**:

**1. claude.ai/code (web)**

- Entras a claude.ai/code desde el navegador
- Claude corre en servidores de Anthropic, clona tu repo de GitHub y ejecuta tareas en la nube

**2. Desde tu terminal con --remote**

- claude --remote "arregla el bug de autenticación"
-  Crea una sesión remota en la nube desde tu propia terminal

**3. GitHub Actions / Slack**

- Tareas automatizadas disparadas por comentarios en PRs, issues, o workflows de CI/CD