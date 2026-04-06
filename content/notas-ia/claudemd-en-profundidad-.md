# **1. ¿Qué es y para qué sirve?**

`CLAUDE.md` es un archivo markdown que le da a Claude **instrucciones persistentes** sobre tu proyecto. Una vez que existe, se carga automáticamente al inicio de cada sesión — Claude lo lee antes de que escribas tu primer mensaje.

⚠️ `CLAUDE.md` **no se crea automáticamente** al ejecutar `claude`. Tienes que crearlo tú — manualmente o con `/init`. Una vez que existe, Claude lo carga en cada sesión sin que tengas que hacer nada.

Es la diferencia entre tener que explicarle a Claude el contexto de tu proyecto en cada sesión, o que ya lo sepa desde el inicio.



# 2. Dónde puede vivir

El `CLAUDE.md` más común es el que vive en la raíz de tu proyecto:

```bash
/Users/tu_usuario/mi_proyecto/CLAUDE.md  ← el principal
```

Este es el que usarás en el día a día. Se commitea a git y aplica a todos los que trabajen en el proyecto.

## 2.1 Los otros niveles — opcionales

Existen otros niveles para casos más específicos:

| Nivel | Ubicación | Cuándo usarlo |
| --- | --- | --- |
| **Personal del proyecto** | `/Users/tu_usuario/mi_proyecto/CLAUDE.local.md` | Preferencias tuyas que no quieres commitear |
| **Global personal** | `/Users/tu_usuario/.claude/CLAUDE.md` | Preferencias que aplican en todos tus proyectos |
| **Organización** | `/Library/Application Support/ClaudeCode/CLAUDE.md` | Solo empresas con IT centralizado |

```bash
#Personal del proyecto
/Users/tu_usuario/mi_proyecto/
├── CLAUDE.md              ← instrucciones del proyecto (se commitea)
├── CLAUDE.local.md        ← instrucciones personales (NO se commitea)
└── .claude/               ← configuración del proyecto
    ├── settings.json
    ├── settings.local.json
    ├── skills/
    ├── agents/
    └── commands/
```

```bash
#Global personal
/Users/tu_usuario/
└── .claude/
    ├── CLAUDE.md              ← instrucciones globales (aplica a todos tus proyectos)
    ├── settings.json          ← configuración global
    ├── skills/                ← skills globales
    ├── agents/                ← agentes globales
    ├── plans/                 ← planes guardados
    ├── projects/              ← sesiones por proyecto
    └── keybindings.json       ← atajos de teclado
```



## 2.2 Cómo los carga Claude

Claude recorre el árbol de directorios hacia arriba desde donde ejecutas `claude` y carga todos los `CLAUDE.md` que encuentra. No se sobreescriben — **se concatenan**:

```bash
cd /Users/tu_usuario/proyecto-A
claude
```

```bash
Claude carga en orden:
1. ~/.claude/CLAUDE.md          ← global personal
2. ~/proyecto-A/CLAUDE.md       ← del proyecto
3. ~/proyecto-A/CLAUDE.local.md ← personal del proyecto (si existe)
```

💡 Los archivos de subdirectorios no se cargan al inicio — solo cuando Claude lee archivos en esos subdirectorios.





# 3. Cómo escribirlo bien

Estructura recomendada:

```bash
# CLAUDE.md

## Overview
Breve descripción del proyecto y su propósito.

## Stack
- Node.js + Express
- PostgreSQL con Prisma ORM
- Jest para tests

## Comandos importantes
- `npm run dev` → inicia el servidor
- `npm test` → corre los tests
- `npm run migrate` → corre las migraciones

## Convenciones de código
- Usa async/await, nunca callbacks
- Nombres de variables en inglés
- Comentarios en español

## Lo que NO debes tocar
- El archivo `.env`
- La carpeta `/legacy`
```



## 3.1 Buenas prácticas

**Sé específico, no vago:**

```bash
❌ "Formatea el código correctamente"
✅ "Usa 2 espacios de indentación"

❌ "Testea tus cambios"
✅ "Ejecuta `npm test` antes de commitear"
```

**Usa headers y bullets:**
Claude escanea la estructura igual que un humano — las secciones organizadas son más fáciles de seguir que párrafos densos.

**Sin contradicciones:**
Si dos reglas se contradicen, Claude puede elegir una arbitrariamente. Revisa periódicamente que no haya instrucciones conflictivas.



# 4. Límites y tokens

El `CLAUDE.md` se carga en el contexto al inicio de cada sesión y consume tokens:

| Recomendación | Por qué |
| --- | --- |
| Máximo 200 líneas por archivo | Archivos más largos consumen más contexto y reducen la adherencia |
| Si crece mucho, divide en archivos con `@` | Mantén el principal enfocado |
| Solo lo esencial que Claude no puede inferir | No documentes lo obvio |

⚠️ El `CLAUDE.md` global (`/Users/tu_usuario/.claude/CLAUDE.md`) es el más costoso porque se carga en **todos tus proyectos**. Mantenlo especialmente conciso.

---



# 5. Generarlo y actualizarlo con `/init`

```bash
# Dentro de Claude Code
/init
```

| Escenario | Qué hace `/init` |
| --- | --- |
| Proyecto vacío | No genera nada — necesita código para analizar |
| Primera vez con código | Genera `CLAUDE.md` desde cero analizando el proyecto |
| `CLAUDE.md` existe y está actualizado | Confirma que está bien |
| `CLAUDE.md` existe pero el código cambió | Muestra diff y propone solo los cambios necesarios |

## 5.1 Flujo recomendado

```bash
1. Haces cambios en tu código
2. /init → Claude detecta cambios y propone actualizar CLAUDE.md
3. Confirmas los cambios
4. Opcionalmente: "actualiza el README basándote en el CLAUDE.md"
```

---

# 6. Importar otros archivos con `@`

Cuando tu `CLAUDE.md` crece demasiado, puedes dividirlo en archivos y referenciarlos:

```bash
# CLAUDE.md

Ver @README para el overview del proyecto.
Ver @package.json para los comandos disponibles.

## Instrucciones adicionales
- Flujo de git: @docs/git-instructions.md
- Convenciones de API: @docs/api-conventions.md
```

Los archivos importados se cargan en el contexto al inicio de la sesión junto con el `CLAUDE.md` que los referencia.

💡 Las rutas relativas se resuelven desde el archivo que contiene el `@`, no desde el directorio de trabajo.

---



# 7.  CLAUDE.local.md — versión personal no commitable

Es el equivalente personal del `CLAUDE.md` del proyecto. Se carga junto al `CLAUDE.md` pero **no se commitea a git**.

```bash
# Crear en la raíz del proyecto
touch CLAUDE.local.md

# Agregar al .gitignore
echo "CLAUDE.local.md" >> .gitignore
```

Úsalo para:

- URLs locales de desarrollo (`http://localhost:3000`)
- Credenciales de sandbox personales
- Preferencias que no aplican a todo el equipo
- Notas de debugging que solo te sirven a ti

```bash
# CLAUDE.local.md

## Mi entorno local
- API local: http://localhost:8080
- Usuario de prueba: test@example.com
- DB local: postgresql://localhost/mi_proyecto_dev
```

