# 1. Formas de utilizar Claude

| Forma | Para qué sirve |
| --- | --- |
| **claude.ai** | Chat en el navegador, uso diario, exploración |
| **API** | Integrar Claude en tus apps y scripts |
| **Claude Code** | Trabajar con Claude directo en tu terminal y proyectos |

# 2. ¿Qué es Claude Code?

Claude Code es el CLI oficial de Anthropic. Te permite trabajar con Claude **directamente desde tu terminal**, dentro de tus proyectos reales. No es solo un chat — Claude puede leer tus archivos, escribir código, ejecutar comandos y entender el contexto de tu proyecto completo.

| Plan | Precio | Claude Code | Para quién |
| --- | --- | --- | --- |
| **Free** | Gratis | ❌ No incluido | Explorar claude.ai |
| **Pro** | ~$20/mes | ✅ Incluido | Uso intensivo, devs |
| **Max** | ~$100/mes | ✅ Incluido | Uso muy intensivo |

⚠️ **Importante:** El plan gratuito **no incluye acceso a Claude Code**. Necesitas mínimo el plan Pro para usarlo.



# 3. ¿Ya tienes Claude Code?

```bash
claude --version
```

| Resultado | Qué significa |
| --- | --- |
| Muestra una versión (ej: `2.1.81`) | ✅ Ya lo tienes, continúa al 3.3 |
| `command not found` | ❌ Hay que instalarlo |

# 4. Instalar Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Este comando siempre instala la versión más reciente. No hay versión hardcodeada.

Respuesta:

```bash
Setting up Claude Code...

✔ Claude Code successfully installed!        
                                                                         
  Version: 2.1.91
                                                                            
  Location: ~/.local/bin/claude


  Next: Run claude --help to get started

⚠ Setup notes:
  • Native installation exists but ~/.local/bin is not in your PATH. Run:

  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc


✅ Installation complete!
```

Una vez instalado, Claude Code se guarda en:

```bash
~/.local/bin/claude
```

> 💡 A diferencia de n8n u otras herramientas de Node.js, Claude Code es **autónomo** — no comparte ni depende de la versión de Node.js que tengas en nvm.



### ⚠️ Advertencia post-instalación: PATH no configurado

Es posible que al terminar la instalación veas este mensaje:

```bash
~/.local/bin is not in your PATH
```

Esto significa que aunque Claude Code está instalado, tu terminal aún no sabe dónde encontrarlo. Para resolverlo ejecuta:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

> 💡 Este comando hace dos cosas: agrega `~/.local/bin` a tu PATH de forma permanente en `~/.zshrc`, y recarga la configuración para que tome efecto inmediatamente sin tener que cerrar la terminal.

Luego verifica que quedó bien:

```bash
claude --version
```

---



## 4.1 ¿Claude Code instala Node.js en mi sistema?

No. Claude Code es un ejecutable autónomo con su propio runtime interno. Ese runtime **no queda disponible** para el sistema ni para otras herramientas.

```bash
Claude Code → runtime interno propio → solo lo usa él
n8n         → necesita Node.js de nvm → son completamente independientes
```

> ⚠️ Si necesitas Node.js para otras herramientas como n8n, debes instalarlo por separado con nvm. La instalación de Claude Code no te lo proporciona.

---

## 4.2 ¿Qué pasa si hay varios usuarios en la misma Mac?

Claude Code se instala en el directorio home de cada usuario. Cada usuario debe instalarlo de forma independiente:

```bash
Tu Mac
├── Usuario 1 (angel)
│   └── ~/.local/bin/claude  ✅ tiene Claude Code
│
└── Usuario 2
    └── ~/.local/bin/        ❌ no existe, debe instalarlo por su cuenta
```

> 💡 Misma lógica que nvm — cada usuario tiene su propio entorno aislado.

## 4.3 Si en algún momento necesitas desinstalarlo:

```bash
# Eliminar el binario de claude
rm -f ~/.local/bin/claude

# Eliminar claude (archivos de versión)
rm -rf ~/.local/share/claude

# Eliminar configuración y historial (opcional) de claude
rm -rf ~/.claude
rm ~/.claude.json
```

> ⚠️ El último bloque elimina toda tu configuración, herramientas permitidas, servidores MCP y historial de sesiones. Omítelo si solo quieres reinstalar.



## 4.4 ¿Cuánto espacio ocupa Claude Code?

```bash
# Ver cuánto pesa el binario
du -sh ~/.local/bin/claude

# Ver cuánto pesa el runtime
du -sh ~/.local/share/claude

# Ver cuánto pesa la configuración
du -sh ~/.claude
```

| Ruta | Peso aprox. | Qué contiene |
| --- | --- | --- |
| `~/.local/bin/claude` | 0B | Symlink (acceso directo al binario real) |
| `~/.local/share/claude` | ~544MB | Binario real + runtime interno |
| `~/.claude` | ~68MB inicial | Configuración, historial, caché |

> 💡 `~/.local/bin/claude` pesa 0B porque no es el archivo real sino un **symlink** que apunta a `~/.local/share/claude`. El peso real está en los 544MB.

### ¿Crece con el uso?

Sí, principalmente `~/.claude` aumenta a medida que usas Claude Code:

| Qué agregas | Dónde crece |
| --- | --- |
| Skills | `~/.claude` |
| Configuración de agentes | `~/.claude` |
| Servidores MCP | `~/.claude` |
| Historial de sesiones | `~/.claude` |
| Actualizaciones de Claude Code | `~/.local/share/claude` |

### En una Mac con varios usuarios:

```bash
Usuario 1 → ~/.local/share/claude ≈ 544MB
           → ~/.claude            ≈ crece según uso

Usuario 2 → ~/.local/share/claude ≈ 544MB
           → ~/.claude            ≈ crece según uso

Total base ≈ ~1GB solo en binarios
```



