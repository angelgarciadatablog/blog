La carpeta `commands/` te permite crear comandos personalizados invocables con `/nombre` dentro de Claude Code. Cada archivo `.md` se convierte en un comando.

```bash
.claude/commands/
├── revisar.md       → se invoca con /revisar
└── dato-curioso.md  → se invoca con /dato-curioso
```

---



# 1. Cómo crear un comando

```bash
# Crear la carpeta
mkdir -p /Users/tu_usuario/mi_proyecto/.claude/commands

# Crear el comando - archivo revisar.md
cat > .claude/commands/revisar.md << 'EOF'
Revisa el código de este proyecto y dime:
1. Qué hace cada archivo
2. Si hay algo que mejorar
3. Si hay bugs evidentes
EOF
```

Luego dentro de Claude Code:

```bash
/revisar
```

Claude ejecuta exactamente lo que dice el archivo `.md`.

---

# 2. Pasar argumentos

**`$ARGUMENTS`****— recibe todo como un bloque de texto:**

```bash
Explica detalladamente este concepto en español, con un ejemplo práctico: $ARGUMENTS
```

```bash
/explicar recursividad y sus casos de uso
```

Claude recibe todo el texto después del comando como un solo string.

---



# **3. $0, $1, $2 — argumentos por posición:**

```bash
Di hola a $0 y cuéntale un dato curioso sobre $1
```

```bash
/dato-curioso Angel programación
```

Claude recibe:

- `$0` → `Angel`
- `$1` → `programación`

**Resultado real probado:**

```bash
Hola Angel! 👋

Aquí va tu dato curioso sobre programación:

El primer "bug" de computadora real fue un insecto de verdad. En 1947,
la ingeniera Grace Hopper encontró una polilla atrapada en los relés de
la computadora Harvard Mark II...
```

---

# 4. ¿Qué es `$ARGUMENTS` vs `$0`, `$1`?

|   | `$ARGUMENTS` | `$0`, `$1`, `$2` |
| --- | --- | --- |
| Qué recibe | Todo el texto después del comando | Cada palabra por separado |
| Cuándo usarlo | Cuando el input es una frase o texto libre | Cuando necesitas parámetros específicos y ordenados |
| Ejemplo | `/explicar qué es la recursividad` | `/dato-curioso Angel programación` |

---

# 5. Eliminar un comando

```bash
rm /Users/tu_usuario/mi_proyecto/.claude/commands/nombre-del-comando.md
```

---

💡 El nombre del archivo define el comando. Usa nombres descriptivos de la acción: `revisar`, `dato-curioso`, `generar-tests` — no nombres de los parámetros.

⚠️ `commands/` es la forma **legacy** — sigue funcionando y no va a desaparecer, pero `skills/` es la versión más avanzada y recomendada para casos complejos. Si tu comando es simple, `commands/` es perfectamente válido.