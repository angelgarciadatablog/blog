Dentro de Claude Code hay 4 símbolos que activan comportamientos especiales:

| Símbolo | Cómo se usa | Qué hace |
| --- | --- | --- |
| `!` | `! ls -la` | Ejecuta un comando bash directamente desde Claude Code sin pedirle a Claude que lo haga |
| `@` | `@src/index.js` | Referencia un archivo del proyecto para que Claude lo lea y use como contexto |
| `&` | `& claude "tarea"` | Ejecuta una tarea en segundo plano mientras sigues trabajando |
| `/btw` | `/btw ¿qué es un hook?` | Hace una pregunta rápida sin interrumpir la conversación principal |

# 1. Modo bash (!)

```bash
# En lugar de pedirle a Claude que liste los archivos
# puedes ejecutarlo tú directamente
! ls -la
! git status
```

💡 Útil cuando quieres ejecutar algo rápido sin que Claude intervenga. Recuerda que `permissions.deny` bloquea a Claude, no a ti — con `!` puedes leer cualquier archivo aunque Claude no pueda.

# 2. Referenciar archivos (@)

```bash
# Pedirle a Claude que revise un archivo específico
revisa @src/index.js y dime si hay mejoras

# Referenciar varios archivos
compara @src/v1.js con @src/v2.js
```

💡 Claude lee el archivo completo y lo agrega al contexto de la conversación. Respeta el `.gitignore` si tienes activado `Respect .gitignore in file picker` en `/config`.



# 3. Background (&)

```bash
# Enviar una tarea para que se ejecute en segundo plano
& revisa todos los archivos del proyecto y genera un reporte
```

> 📌 **Pendiente de verificar:** En pruebas básicas `&` se comportó igual que una pregunta normal. Su comportamiento real en segundo plano se verá con más claridad en el **Bloque Agentes**, donde tiene más contexto de uso.



# 4. Pregunta lateral (/btw)

```bash
# Pregunta rápida sin perder el hilo principal
/btw ¿qué diferencia hay entre == y === en JavaScript?
```

💡 Claude responde la pregunta y luego vuelve al contexto de la conversación principal como si no hubiera pasado nada.



