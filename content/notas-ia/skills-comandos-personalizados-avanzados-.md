# 1. ¿Qué es una skill?

Una skill es la evolución de un `command/`. Se define con un archivo `SKILL.md` y puede hacer todo lo que hace un command, más capacidades avanzadas como correr en subagentes aislados, activarse automáticamente y controlar qué herramientas usa Claude.

---

# 2. commands/ vs skills/

|   | `commands/` | `skills/` |
| --- | --- | --- |
| Formato | Archivo `.md` simple | Carpeta con `SKILL.md` y archivos de soporte |
| Frontmatter YAML | ❌ No | ✅ Sí |
| Subagentes | ❌ No | ✅ Sí |
| Activación automática | ❌ No | ✅ Sí — Claude la usa cuando detecta que aplica |
| Control de herramientas | ❌ No | ✅ Sí |
| Archivos de soporte | ❌ No | ✅ Scripts, referencias, assets |
| Estado | Legacy | ✅ Recomendado |

💡 Si tu comando es simple y no necesita estas capacidades, `commands/` es perfectamente válido. Usa `skills/` cuando necesitas más potencia.

---

# 3. Dónde pueden vivir

| Ubicación | Alcance |
| --- | --- |
| `/Users/tu_usuario/.claude/skills/` | Todos tus proyectos |
| `/Users/tu_usuario/mi_proyecto/.claude/skills/` | Solo este proyecto |

---

# 4. Estructura de una skill

La estructura mínima es una carpeta con un `SKILL.md`:

**Un skill = una carpeta**, no un archivo. Aunque solo tenga un `SKILL.md` dentro:

```markdown
.claude/skills/
└── documentar/          ← esto es la skill (la carpeta)
    └── SKILL.md         ← el archivo principal dentro
```

Esto es diferente a `commands/` donde el archivo ES el comando:

```markdown
.claude/commands/
└── revisar.md           ← esto es el command (el archivo directamente)
```

Una skill más compleja puede incluir archivos de soporte:

```bash
.claude/skills/
└── documentar/
    ├── SKILL.md           ← instrucciones principales (obligatorio)
    ├── agents/            ← subagentes especializados
    ├── scripts/           ← scripts que Claude puede ejecutar
    ├── references/        ← documentación de referencia
    └── assets/            ← archivos de soporte
```

💡 No necesitas todas las carpetas — empieza solo con `SKILL.md` y agrega lo que necesites.

---

# 5. Anatomía del `SKILL.md`

Tiene dos partes: **frontmatter YAML** y **las instrucciones**:

```markdown
---
name: documentar
description: Genera un README.md detallado y profesional para el proyecto actual,
leyendo el código fuente real. Úsalo siempre que el usuario pida documentar el
proyecto, generar un README, o describir cómo funciona el proyecto.
---

# Skill: documentar

Tu tarea es generar un `README.md` detallado y preciso para el proyecto actual,
basándote en el código real que encuentres.

## Proceso

### 1. Explorar el proyecto
Antes de escribir nada, explora el repositorio...

### 2. Escribir el README
- Usa Markdown bien formateado
- Los ejemplos deben ser reales y funcionales
```



---

# 6. El frontmatter YAML

| Campo | Obligatorio | Qué hace |
| --- | --- | --- |
| `name` | No | Nombre del comando. Si se omite usa el nombre de la carpeta |
| `description` | ✅ Recomendado | Cuándo y cómo usar la skill. Claude lo usa para activarla automáticamente |
| `disable-model-invocation` | No | `true` → solo tú puedes invocarla, Claude no la activa sola |
| `user-invocable` | No | `false` → solo Claude puede invocarla, no aparece en el menú `/` |
| `allowed-tools` | No | Herramientas que Claude puede usar sin pedir permiso cuando la skill está activa |
| `context` | No | `fork` → corre en un subagente aislado |
| `agent` | No | Qué subagente usar cuando `context: fork` |
| `effort` | No | Nivel de esfuerzo: `low`, `medium`, `high`, `max` |

---

# 7. Activación automática vs manual

A diferencia de `commands/`, las skills pueden activarse solas basándose en su `description`:

```markdown
Tú escribes:   "necesito un README para este proyecto"
Claude detecta: la skill "documentar" aplica aquí
Claude la carga y la ejecuta automáticamente
```

Para controlar esto:

```markdown
# Solo tú la invocas — Claude no la activa sola
disable-model-invocation: true

# Solo Claude la activa — no aparece en el menú /
user-invocable: false
```

---

# 8. Cómo crear una skill manualmente

```markdown
# 1. Crear la carpeta en el proyecto
mkdir -p /Users/tu_usuario/mi_proyecto/.claude/skills/mi-skill

# 2. Crear el SKILL.md
cat > /Users/tu_usuario/mi_proyecto/.claude/skills/mi-skill/SKILL.md << 'EOF'
---
name: mi-skill
description: Descripción de cuándo y cómo usar esta skill
---

Instrucciones para Claude aquí...
EOF
```

⚠️ Después de crear una skill nueva necesitas **reiniciar Claude Code** para que la detecte. Sal con `/exit` y vuelve a entrar.

---

# 9. Cómo crear una skill con `skill-creator`

La forma más fácil es usar la skill oficial de Anthropic que guía el proceso:

```markdown
/skill-creator
```

Claude te hace preguntas sobre qué quieres que haga la skill, genera el `SKILL.md` y lo guarda en el directorio correcto.

**Ejemplo real** — creamos la skill `documentar` en `test-claude`:

```markdown
/skill-creator

→ "quiero crear una skill llamada documentar que genere 
   documentación del código del proyecto"

→ Claude pregunta: ¿qué tipo de documentación? ¿formato? ¿dónde guardar?

→ Genera automáticamente el SKILL.md con instrucciones detalladas

→ /documentar  ← ya disponible para usar
```

💡 La forma más recomendada de crear una skill es con `/skill-creator` — Claude te guía con preguntas, genera el `SKILL.md` bien estructurado y lo guarda en el directorio correcto automáticamente.

---



# 10. Pasar argumentos

Igual que en `commands/`, puedes usar `$ARGUMENTS`, `$0`, `$1`:

```markdown
---
name: explicar-funcion
description: Explica en detalle una función del proyecto
---
```

```markdown
/explicar-funcion saludar script.sh
```

---

# 11. Ver skills disponibles

```markdown
/skills
```

Muestra las skills separadas por nivel:

```markdown
Skills
4 skills

Project skills (/Users/tu_usuario/test-claude/.claude/skills, .claude/commands)
documentar · ~89 description tokens
dato-curioso · ~15 description tokens
revisar · ~12 description tokens

User skills (/Users/tu_usuario/.claude/skills)
datablog-design-v1 · ~69 description tokens
skill-creator · ~83 description tokens
```





# 12. Cómo consume tokens una skill

Cuando inicias una sesión, Claude no carga el contenido completo de cada skill — solo carga su **description** del frontmatter. El contenido completo del `SKILL.md` se carga solo cuando la skill se invoca.

Puedes verlo con `/context`:

```markdown
Skills · /skills

Project
└ documentar: 110 tokens    ← solo la description
└ dato-curioso: 15 tokens   ← description muy corta
└ revisar: 12 tokens        ← description muy corta

User
└ skill-creator: 83 tokens
└ datablog-design-v1: 69 tokens
```

Esto tiene dos implicaciones importantes:

|   | Description (siempre en contexto) | SKILL.md completo (bajo demanda) |
| --- | --- | --- |
| **Cuándo se carga** | Al inicio de cada sesión | Solo cuando se invoca la skill |
| **Para qué sirve** | Claude decide si la skill aplica | Claude ejecuta las instrucciones |
| **Costo en tokens** | Fijo — pocos tokens | Variable — puede ser grande |

⚠️ Por eso la `description` es crítica — es lo único que Claude lee para decidir si usar la skill automáticamente. Una description vaga hace que Claude no la active cuando debería.

💡 Mantén las descriptions concisas pero específicas. La documentación oficial recomienda máximo 250 caracteres — descriptions más largas se truncan en el listado de skills.



# 13.  Archivos de soporte de una skill

Una skill puede tener más que solo el `SKILL.md`. Las siguientes carpetas las documentaremos cuando tengamos más contexto de agentes:

| Carpeta | Para qué sirve | Dónde se documenta |
| --- | --- | --- |
| `agents/` | Subagentes especializados que la skill puede invocar | Bloque — Agentes |
| `scripts/` | Scripts que Claude ejecuta antes de procesar | Bloque — Agentes |
| `references/` | Documentación de referencia que Claude carga cuando necesita | Bloque — Agentes |
| `assets/` | Archivos de soporte como templates, HTML, imágenes | Bloque — Agentes |

