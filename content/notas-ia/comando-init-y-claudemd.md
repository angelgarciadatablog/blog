

---

# **Documentación: Comando /init y CLAUDE.md**

## **¿Qué es CLAUDE.md?**

CLAUDE.md es un archivo de documentación que Claude lee automáticamente al iniciar una sesión. Le dice a Claude:

- Qué es tu proyecto
- Qué tecnologías usas
- Qué reglas seguir
- Convenciones del equipo

**Analogía:** Es como un manual de instrucciones del proyecto para Claude.





## **Comando /init**

### **¿Qué hace?**

Crea automáticamente un archivo CLAUDE.md analizando tu proyecto.

### **¿Cuándo usarlo?**

- **Primera vez** que usas Claude Code en un proyecto
- Cuando quieres que Claude entienda el contexto del proyecto





### **Cómo usarlo:**

```bash
cd ~/mi-proyecto
claude
/init
```

### **Resultado:**

Claude genera un archivo `CLAUDE.md` con:

- Descripción del proyecto
- Stack tecnológico detectado
- Estructura de carpetas
- Comandos útiles
- Convenciones sugeridas





### **✅ Cuándo actualizar CLAUDE.md:**

- Cambias de stack tecnológico
- Agregas/quitas librerías importantes
- Cambias convenciones de código
- Cambias estructura del proyecto
- Nuevos miembros se unen al equipo





## **Cómo actualizar CLAUDE.md**



### **Opción 1: Volver a ejecutar /init (NO recomendado)**

```
/init
```

**Por qué NO usarla:**

- ❌ Sobrescribe TODO el archivo
- ❌ Pierdes personalizaciones manuales
- ❌ Pierdes reglas de negocio específicas
- ⚠️ Solo útil si quieres empezar desde cero





### **Opción 2: Actualización específica (Para cambios pequeños)**

Dentro de Claude Code:

```
"Actualiza CLAUDE.md: ahora usamos React 18 en lugar de 17"
```

**Cuándo usarla:**

- ✅ Cambio muy específico que conoces bien
- ✅ Quieres control total sobre qué se actualiza

**Riesgo:**

- ⚠️ Puedes olvidar mencionar otros cambios relacionados





## **Opción 3: Detección automática (RECOMENDADO)** ⭐

```
"Analiza el proyecto actual, compáralo con CLAUDE.md,
y actualízalo con todos los cambios que encuentres.
Mantén las reglas de negocio y convenciones existentes."
```

**Por qué es la mejor:**

- ✅ Claude detecta TODOS los cambios automáticamente
- ✅ No olvidas nada
- ✅ Mantiene contenido personalizado
- ✅ No sobrescribe reglas de negocio

**Prompt completo recomendado:**

```
"Actualiza CLAUDE.md basándote en el estado actual del proyecto:

1. Analiza package.json y detecta cambios en dependencias
2. Revisa archivos de configuración (vite.config, tsconfig, etc)
3. Verifica la estructura de carpetas actual
4. Compara con el CLAUDE.md existente
5. Actualiza las secciones técnicas (Stack, Configuración)
6. MANTÉN intactas las secciones de:
   - Reglas de negocio
   - Convenciones personalizadas
   - Notas del equipo
7. Agrega una sección de changelog al final"
```





### **Opción 5: Crear un skill personalizado (Automatización completa)** 🎯

Puedes crear tu propio comando `/actualizar-claude` que ejecute el proceso automáticamente.

**Crear el skill:**

```bash
mkdir -p ~/.claude/skills/actualizar-claude
nano ~/.claude/skills/actualizar-claude/SKILL.md
```



**Contenido del SKILL.md:**

```markdown
actualizar-claude
description: Actualiza CLAUDE.md detectando cambios en el proyecto automáticamente--Actualiza CLAUDE.md basándote en el estado actual del proyecto:
1. Analiza package.json y detecta cambios en dependencias
2. Revisa archivos de configuración (vite.config, tsconfig, webpack.config, etc)
3. Verifica la estructura de carpetas actual
4. Compara con el CLAUDE.md existente
5. Actualiza las secciones técnicas:
  Stack tecnológico
  Configuración del proyecto
  Estructura de carpetas
6. MANTÉN intactas las secciones de:
  Reglas de negocio
  Convenciones personalizadas del equipo
  Notas importantes
  Decisiones de arquitectura
7. Agrega una sección "Última actualización" con la fecha de hoy
8. Lista los cambios detectados en formato de changelog
Sé exhaustivo en la detección de cambios pero conservador al mantener documentación existente.
```



**Usar el skill:**

```markdown
# Dentro de Claude Code:
/actualizar-claude
```

 ✅ Claude ejecuta todo el proceso automáticamente
✅ Detecta cambios
✅ Actualiza CLAUDE.md
✅ Mantiene reglas de negocio



**Ventajas:**

- ✅ Un solo comando ejecuta todo el proceso
- ✅ Consistente en todos tus proyectos
- ✅ Reutilizable (skill personal global)
- ✅ No tienes que recordar el prompt largo

**Ubicación:**

- Skill personal: `~/.claude/skills/` (funciona en TODOS los proyectos)
- Skill de proyecto: `.claude/skills/` (solo ese proyecto)

