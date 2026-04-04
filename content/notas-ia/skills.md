

Los skills son archivos `.md` que pueden guardarse localmente o globalmente, funcionan en **Claude Code, claude.ai y API**, y pueden invocarse explícitamente o activarse automáticamente.

## Defininición:

- Son archivos `.md` (con YAML frontmatter + instrucciones)
- Se pueden guardar en `.claude/` en tu carpeta de usuario



### **Ubicaciones posibles** (no solo una):

- `~/.claude/skills/nombre/` → Global (todos los proyectos)
- `.claude/skills/nombre/` → Local del repo (solo ese proyecto)
- Skills empresariales (compartidos en organización)





### **SÍ funcionan en el navegador** (claude.ai):

Según la documentación oficial, los skills **sí funcionan en claude.ai** si:

- Tienes plan Pro, Max, Team o Enterprise
- Tienes "code execution" habilitado
- Los subes como archivos ZIP en **Settings → Features → Custom Skills**



### **También funcionan en la API**:

Los skills funcionan en:

- Claude Code (CLI)
- Claude.ai (navegador) - subiéndolos manualmente
- Claude API - usando el parámetro `container` con `skills`





## Importante entender al momento de actualizar un skill:

| Claude Code (local) | claude.ai (navegador) |
| --- | --- |
| Lee automáticamente de `~/.claude/skills/` | Necesitas subir ZIP manualmente |
| Se actualiza si editas el archivo | Es una copia separada, hay que re-subir si cambias |
| `/comando` funciona | No hay comandos `/`, solo invocación natural |