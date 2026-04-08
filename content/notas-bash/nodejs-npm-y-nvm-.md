## 1.1 ¿Qué es Node.js?

```bash
# ¿Tienes Node.js?
node --version
```

Node.js es un **entorno de ejecución** para JavaScript. Normalmente JavaScript solo corre en el navegador, Node.js te permite correrlo también en tu computadora o servidor.

💡 Piénsalo así: así como Python tiene su intérprete para correr archivos `.py`, Node.js es el intérprete para correr archivos `.js` fuera del navegador.

Muchas herramientas modernas están construidas sobre Node.js. Por eso cuando instalas Claude Code, n8n, o docenas de otras herramientas, Node.js es un requisito. Sin embargo, ya no es necesario tener instalado Node.js para instalar claude code.

> ⚠️ **Claude Code no necesita Node.js.** Tiene su propio instalador nativo y autónomo. Node.js lo instalamos para herramientas como n8n.

## 1.2 ¿Qué es npm?

Antes de entender qué es npm, hay que entender qué es un **gestor de paquetes**: una herramienta que te permite instalar programas y librerías desde la terminal, sin tener que descargarlos manualmente desde páginas web.

En macOS (y linux) es muy común escuchar de **Homebrew**. npm funciona igual pero es exclusivo del ecosistema JavaScript.

| Gestor | Para qué sirve |
| --- | --- |
| Homebrew | Instala herramientas del sistema (Git, wget, ffmpeg, imagemagick) |
| npm | Instala paquetes dentro del ecosistema JavaScript |

npm significa **Node Package Manager** y viene incluido automáticamente cuando instalas Node.js. No necesitas instalarlo por separado.

Cada lenguaje tiene su propio gestor de paquetes:

| Lenguaje | Gestor de paquetes |
| --- | --- |
| JavaScript | `npm` |
| Python | `pip` |
| Rust | `cargo` |

> 💡 Para lenguajes como Node.js o Python **no se recomienda instalarlos con Homebrew**, sino con un gestor de versiones. Homebrew puede hacerlo y funciona, pero no te da control sobre versiones.

### npm te permite:

```bash
npm install nombre-paquete    # Instalar en tu proyecto
npm install -g nombre-paquete # Instalar de forma global en tu Mac
npm uninstall nombre-paquete  # Desinstalar
npm list                      # Ver paquetes instalados
```

---

## ¿Por qué no usar Homebrew para instalar Node.js o Python?

Homebrew instala una sola versión y punto. En proyectos reales, tarde o temprano necesitas tener varias versiones conviviendo. Por eso profesionalmente se usan **gestores de versiones**:

| Lenguaje | Gestor de versiones |
| --- | --- |
| Node.js | `nvm` |
| Python | `pyenv` |
| Ruby | `rbenv` |

> ⚠️ Homebrew **puede** instalar Node.js o Python y funciona, pero en proyectos reales se queda corto.

---

## 1.3 ¿Qué es nvm?

```bash
# ¿Tienes nvm?
nvm --version
```

El problema concreto: distintas herramientas requieren distintas versiones de Node.js:

- Una app legacy puede requerir Node.js **v14**
- n8n puede requerir Node.js **v20**

**nvm (Node Version Manager)** resuelve esto. Te permite:

- Tener **múltiples versiones** de Node.js instaladas
- **Cambiar** entre versiones con un comando
- Definir **qué versión usa cada proyecto**

---

## Instalación de nvm en Mac

```bash
# Instalar nvm
# En este caso (año 2026) utilizamos la versión 39 de nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Cerrar y reabrir la terminal, luego verificar
nvm --version
```

---

## Comandos esenciales de nvm

```bash
# Ver todas las versiones disponibles de node.js para instalar
nvm list-remote

# Instalar una versión específica
nvm install 20

# Instalar la versión más reciente estable (LTS)
nvm install --lts

# Ver qué versiones tienes instaladas
nvm list

# Cambiar a una versión específica
nvm use 20

# Ver qué versión estás usando ahora
node --version

# Definir una versión por defecto
nvm alias default 20
```



# 5. Múltiples usuarios en la misma Mac

nvm se instala **por usuario**, no de forma global en la Mac:

| Situación | Resultado |
| --- | --- |
| Usuario A instala nvm | Solo Usuario A lo tiene |
| Usuario B abre su terminal | No tiene nvm ni Node.js |
| Usuario B necesita Node.js | Debe instalarlo por su cuenta |

Esto en realidad es una **ventaja**:

- Cada usuario tiene su propio entorno aislado
- Un usuario no puede romper el entorno de otro
- Cada quien puede tener versiones distintas según sus necesidades

> ⚠️ Si en tu Mac hay varios usuarios que necesitan Node.js, cada uno debe seguir el mismo proceso de instalación de nvm de forma independiente.



## Versiones por proyecto con `.nvmrc`

```bash
# Dentro de tu proyecto, crear el archivo
echo "20" > .nvmrc

# La próxima vez que entres al proyecto
cd mi-proyecto
nvm use  # Lee el .nvmrc automáticamente y cambia a v20
```

> 💡 Esto es importante para n8n, Claude Code y cualquier herramienta que venga después — cada una puede tener su versión de Node recomendada.



## Resumen visual

```bash
Tu Mac
├── Usuario Angel
│   └── nvm
│       ├── Node v18  ← Claude Code lo usa
│       ├── Node v20  ← n8n lo usa
│       └── Node v14  ← proyecto legacy
│
└── Usuario Otro
    └── (sin nvm, debe instalarlo por su cuenta)
```



# 6. El problema de mezclar métodos

nvm **solo controla lo que él mismo instaló**. Si instalaste Node.js de otra forma, nvm no lo toca ni lo gestiona.

| Cómo instalaste Node | ¿nvm lo controla? |
| --- | --- |
| `nvm install 20` | ✅ Sí, `nvm uninstall 20` lo elimina completo |
| `brew install node` | ❌ No, nvm no sabe que existe |
| Instalador `.pkg` desde nodejs.org | ❌ No, son instalaciones independientes |

Si en algún momento instalaste Node.js con Homebrew **y** con nvm, puedes tener dos instalaciones conviviendo. Para saber cuál estás usando realmente:

```bash
which node
```

| Resultado | Qué significa |
| --- | --- |
| `~/.nvm/versions/node/...` | ✅ Estás usando el de nvm |
| `/usr/local/bin/node` | ⚠️ Estás usando el de Homebrew |
| `/usr/bin/node` | ⚠️ Estás usando el del instalador .pkg |

> ⚠️ Por eso es importante elegir **un solo método** desde el principio. Si ya tienes Node.js instalado por Homebrew o por el instalador `.pkg`, lo ideal es desinstalarlo primero antes de instalar nvm.