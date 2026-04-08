**Git** → es la herramienta base de control de versiones. Solo necesita tu nombre y email para firmar commits. No sabe nada de GitHub específicamente.

**GitHub CLI (gh)** → es una herramienta para interactuar con **GitHub como plataforma** desde la terminal. Necesita login real con tu cuenta de GitHub.

| Acción | Git | GitHub CLI |
| --- | --- | --- |
| Hacer commits | ✅ | ❌ |
| Push/pull a repos | ✅ | ❌ |
| Crear un repo en GitHub | ❌ | ✅ |
| Abrir un Pull Request | ❌ | ✅ |
| Ver issues | ❌ | ✅ |
| Hacer fork | ❌ | ✅ |
|   |   |   |

## **¿Cómo autentica Git en Mac?**

| Método | Mac | Windows | Linux | ¿Profesional? |
| --- | --- | --- | --- | --- |
| **SSH** | ✅ | ✅ | ✅ | ✅ Estándar |
| **Keychain (OAuth)** | ✅ | ❌ | ❌ | ⚠️ Personal |
| **PAT (token manual)** | ✅ | ✅ | ✅ | ⚠️ Puntual |

Git usa el **macOS Keychain** para guardar credenciales de forma independiente a `gh`. Puedes verificarlo con:

```bash
git credential-osxkeychain get
```

Esto devuelve tu ID de usuario de GitHub y un **Personal Access Token (PAT)** guardado. Por eso puedes hacer push sin tener sesión activa en `gh` — son dos sistemas separados.





## **¿Cómo logearte con gh?**

```bash
gh auth login
```

Es el comando central de autenticación de gh. Sirve para:

- **Agregar cuentas de GitHub** — cada vez que lo ejecutas puedes autenticar una cuenta nueva, gh las guarda todas en (`~/.config/gh/hosts.yml` )
- **Cambiar el protocolo** — durante el proceso te pregunta si quieres usar HTTPS o SSH, actualizando la sesión existente
- **Reconectar o renovar** — si un token expiró o quieres actualizar la configuración de una cuenta ya guardada

## **¿Cómo está configurado tu gh ahora mismo?**

```bash
gh auth status
```

Muestra todas las cuentas guardadas en gh, tanto la activa como las inactivas, con su protocolo y estado.

Tu resultado mostró:

- Protocolo: `https`
- Token guardado en: `keyring` (el almacén de credenciales de Windows)

## **HTTPS vs SSH:**

|   | HTTPS | SSH |
| --- | --- | --- |
| **Cómo funciona** | Token de acceso | Par de llaves (pública/privada) |
| **Autenticación** | Token guardado en keyring | Llave privada en tu equipo |
| **Seguridad** | Buena | Mejor |
| **Uso profesional** | Común | Más estándar en entornos pro |
| **Múltiples cuentas** | Complicado | Más manejable |



## **Los problemas reales con una sola cuenta en gh:**

**Escenario 1 — Clonar un repo de otra cuenta:**

```bash
gh repo clone otra-cuenta/su-repo
```

✅ Funciona si el repo es público
❌ Falla si el repo es privado — gh usará `angel-reechai` y no tendrá acceso



**Escenario 2 — Push a un repo de otra cuenta:**

```bash
git push
```

⚠️ Git intentará autenticarse con las credenciales guardadas — si no coinciden con el dueño del repo, te dará error de permisos



# **Otras formas de manejar múltiples cuentas en gh:**

gh desde la versión 2.x soporta múltiples cuentas. Puedes agregar una segunda cuenta así:

```bash
gh auth login --hostname github.com
```

Y cambiar entre ellas con:

```bash
gh auth switch
```



**El flujo real con 2 cuentas:**

```bash
# Primera vez (solo una vez por cuenta)
gh auth login  # logueas cuenta trabajo → se guarda
gh auth login  # logueas cuenta personal → se guarda

# Del día a día (instantáneo, sin login)
gh auth switch  # alterna entre las dos cuentas guardadas
```

---

**Pero hay una forma aún más cómoda:**

Con SSH configurado correctamente, **ni siquiera necesitas hacer****`gh auth switch`****manualmente** — cada repo usa la cuenta correcta automáticamente según la llave SSH configurada.