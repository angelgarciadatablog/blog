# 1. Iniciar autenticación

Claude Code usa tu cuenta de Anthropic. No necesitas configurar nada manualmente — el proceso es automático vía navegador.



# 2. Primera vez que ejecutas `claude`

```bash
# Navega primero a tu proyecto
cd ~/proyectos/mi-proyecto

# Ejecuta claude
claude
```

Lo que ocurre en orden:

1. Claude Code detecta que no hay sesión activa
1. Se abre tu navegador automáticamente
1. Inicias sesión con tu cuenta de Anthropic
1. Autorizas el acceso
1. El navegador te confirma que puedes cerrar la pestaña
1. Tu terminal muestra la confirmación de seguridad del workspace:

---

Respuesta:

```bash
Accessing workspace:
/Users/tu_usuario/proyectos/mi-proyecto

Quick safety check: Is this a project you created or one you trust?
Claude Code'll be able to read, edit, and execute files here.

❯ 1. Yes, I trust this folder
  2. No, exit
```

Confirmas con `1` y Claude Code queda listo para usar

> ⚠️ La autenticación con Anthropic solo ocurre **una vez**. Queda guardada en `~/.claude` y no te la pedirá de nuevo aunque cierres la terminal o reinicies la Mac.

---



# 3. ¿Desde qué directorio ejecutar `claude` la primera vez?

> ⚠️ **Importante:** En Mac, cuando abres la terminal por defecto te posiciona en tu directorio de usuario `/Users/tu_usuario`. Si ejecutas `claude` desde ahí, le estás dando acceso a **todo lo que hay en tu usuario** — documentos, descargas, proyectos, configuraciones, todo.

**La buena práctica es navegar primero a tu proyecto:**

```bash
# ❌ Evitar — le das acceso a todo tu usuario
cd ~
claude

# ✅ Correcto — navegas primero a tu proyecto específico
cd ~/proyectos/mi-proyecto
claude
```

---

# 4. Las siguientes veces que ejecutas `claude`

La autenticación ya está guardada. Lo único que ocurre es la confirmación del workspace si es un directorio nuevo:

**En un directorio ya confiado → entra directo:**

```bash
cd ~/proyectos/mi-proyecto
claude
# Entra directamente sin preguntas
```

**En un directorio nuevo → te pregunta si confías:**

```bash
cd ~/proyectos/nuevo-proyecto
claude
# Muestra la confirmación de seguridad del workspace
```

> 💡 La confirmación de seguridad aparece **una vez por directorio**. Una vez que confirmas, Claude Code recuerda ese directorio.

---



# 5. La pantalla de inicio de Claude Code

Una vez autenticado y dentro de un directorio, verás esta pantalla:

```bash
╭─── Claude Code v2.1.81 ──────────────────────────────────────────╮
│                                        │ Tips for getting started │
│         Welcome back Angel!            │ Run /init to create a    │
│                                        │ CLAUDE.md file           │
│   Sonnet 4.6 · Claude Pro ·            │                          │
│   tu@gmail.com's Organization          │ Recent activity          │
│   /Users/tu_usuario                    │ ...                      │
╰──────────────────────────────────────────────────────────────────╯
❯
```

Lo que muestra:

| Elemento | Qué significa |
| --- | --- |
| `Welcome back` | Ya estás autenticado |
| `Sonnet 4.6 · Claude Pro` | Modelo y plan activos |
| `tu@gmail.com's Organization` | Cuenta vinculada |
| `/Users/tu_usuario` | Directorio donde está operando |
| `Recent activity` | Últimas sesiones, puedes retomarlas con `/resume` |

---

## ⚠️ Advertencia de directorio home

Si ejecutaste `claude` desde tu directorio home verás este aviso:

`Note: You have launched claude in your home directory. For the best experience...`

> ⚠️ Claude Code mismo te está advirtiendo que no es la mejor práctica. Sal con `/exit` y vuelve a entrar desde tu proyecto específico.

---

> ⚠️ Para Claude Code, proyecto = ruta exacta. Siempre entra desde la raíz de tu proyecto, no desde un subdirectorio. De lo contrario se crearán sesiones separadas aunque sea el mismo proyecto.



## Salir de Claude Code

```bash
# Opción 1 — comando
/exit

# Opción 2 — atajo de teclado
Ctrl + C
```



# 6. Conceptos clave antes de continuar

Antes de usar Claude Code en el día a día, hay tres conceptos que conviene tener claros:

| Concepto | Qué es | Dónde vive |
| --- | --- | --- |
| **Sesión** | El historial de una conversación con Claude en un directorio específico (queda en local) | `~/.claude/projects/` en tu Mac |
| **CLAUDE.md** | Archivo de instrucciones persistentes para Claude en un proyecto | En la raíz de tu proyecto, junto a tu código. A diferencia de las sesiones, puedes commitearlo a git y compartirlo con tu equipo. |
| **Auto memory** | Notas que Claude escribe solo sobre tus preferencias y patrones (queda en local) | `~/.claude/projects/<proyecto>/memory/` |

Los tres son independientes entre sí:

- Puedes tener sesiones sin tener `CLAUDE.md`
- Puedes tener `CLAUDE.md` sin sesiones previas
- El auto memory se genera solo con el uso

💡 Cada uno de estos conceptos tiene su propio bloque en esta documentación. Por ahora basta con saber que existen y para qué sirven.



**CLAUDE.md** → SÍ está en tu proyecto:

```bash
~/proyectos/mi-proyecto/
├── CLAUDE.md        ← aquí, junto a tu código
├── src/
└── package.json
```

> 💡 `/init` es un comando que genera automáticamente un archivo `CLAUDE.md` en tu proyecto — el archivo donde le das instrucciones persistentes a Claude. Lo veremos en detalle en el bloque dedicado a CLAUDE.md.

**Sesiones** → NO están en tu proyecto, están en `~/.claude`:

```bash
~/.claude/projects/
└── Users-angel-proyectos-mi-proyecto/  ← carpeta que representa tu proyecto
    └── [historial de conversaciones]
```

---

O sea Claude crea una carpeta en `~/.claude/projects/` que representa a tu proyecto, pero el historial de conversaciones vive ahí, no dentro de tu proyecto real.

> ⚠️ **Las sesiones crecen con el tiempo.** Cada conversación que tengas con Claude Code se guarda localmente. En el largo plazo esto puede ocupar espacio considerable en tu Mac. Revisa periódicamente cuánto ocupan:



# 7. Verificar que estás autenticado

```bash
claude doctor
```

Busca esta línea en el output:

`✓ Logged in as: tu@email.com`

---



# 8. Cerrar sesión

```bash
claude logout
```

> 💡 Útil si necesitas cambiar de cuenta o si alguien más va a usar Claude Code en el mismo usuario de Mac.

