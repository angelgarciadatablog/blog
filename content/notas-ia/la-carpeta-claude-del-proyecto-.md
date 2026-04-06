# ¿Qué es y cuándo se crea?

La carpeta `.claude/` dentro de tu proyecto es el **centro de configuración local** de Claude Code para ese proyecto específico. A diferencia de `/Users/tu_usuario/.claude/` que es global para tu usuario, esta carpeta solo aplica cuando ejecutas `claude` en ese directorio.

⚠️ No se crea automáticamente al ejecutar `claude` — se genera bajo demanda cuando la necesitas o cuando cambias alguna configuración desde `/config`.

## Estructura completa

| Archivo/Carpeta | Qué es | ¿Se commitea? |
| --- | --- | --- |
| `CLAUDE.md` | Instrucciones para Claude (alternativa al de la raíz) | ✅ Sí |
| `settings.json` | Configuración compartida del equipo | ✅ Sí |
| `settings.local.json` | Preferencias personales del proyecto | ❌ No |
| `commands/` | Comandos personalizados invocables con `/nombre` | ✅ Sí |
| `skills/` | Comandos personalizados avanzados (recomendado) | ✅ Sí |
| `agents/` | Subagentes del proyecto | ✅ Sí |
| `rules/` | Reglas por tipo de archivo o directorio | ✅ Sí |
| `.mcp.json` | Servidores MCP del proyecto | ✅ Sí |
| `agent-memory/` | Memoria persistente de subagentes | ✅ Sí |
| `output-styles/` | Estilos de respuesta personalizados | ✅ Sí |
| `worktrees/` | Worktrees de git aislados | ❌ No |

💡 Esta es la estructura base. Dependiendo de configuraciones más avanzadas como hooks, plugins y automatizaciones, pueden aparecer archivos y carpetas adicionales.

```bash
/Users/tu_usuario/mi_proyecto/.claude/
├── settings.json          ← configuración del equipo (se commitea)
├── settings.local.json    ← preferencias personales (NO se commitea)
├── CLAUDE.md              ← alternativa al CLAUDE.md de la raíz
├── commands/              ← comandos personalizados simples (legacy)
│   └── mi-comando.md
├── skills/                ← comandos personalizados avanzados (recomendado)
│   └── mi-skill/
│       └── SKILL.md
├── agents/                ← subagentes del proyecto
│   └── mi-agente.md
├── rules/                 ← reglas por tipo de archivo
│   └── frontend.md
├── .mcp.json              ← servidores MCP del proyecto
├── worktrees/             ← worktrees de git aislados
├── agent-memory/          ← memoria persistente de subagentes
└── output-styles/         ← estilos de respuesta personalizados
```



Según la documentación oficial hay dos ubicaciones válidas para el `CLAUDE.md` del proyecto:

```bash
/Users/tu_usuario/mi_proyecto/CLAUDE.md        ← opción 1 (más común)
/Users/tu_usuario/mi_proyecto/.claude/CLAUDE.md ← opción 2 (alternativa)
```

Ambas funcionan igual — Claude las reconoce y carga. La diferencia es solo organizacional:

- En la raíz → más visible, más fácil de encontrar
- Dentro de `.claude/` → más ordenado si prefieres tener todo lo de Claude en un solo luga

💡 Si existen ambas, Claude las carga y concatena igual que con los otros niveles.

