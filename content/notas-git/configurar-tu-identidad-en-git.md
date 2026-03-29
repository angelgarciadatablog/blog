Hay dos identidades distintas:

# 1) Identidad del commit (Git local)

Define:

- nombre visible

- correo grabado para siempre

# Nivel global

El `--global` significa "global para todos los repositorios de MI usuario del sistema", no "global para todo el ordenador". Cada usuario del SO tiene su propio archivo `.gitconfig`.

```bash
# Configurar nombre (usa tu nombre real o de GitHub)
git config --global user.name "Angel García"

# Configurar email (usa el mismo email de tu cuenta GitHub)
git config --global user.email "tu-email@gmail.com"

# Verificar que se guardó
git config --global user.name
git config --global user.email

```

# Nivel local

Se crea cuando haces algo como:

```bash
git config user.name "Algo"
git config user.email "algo@email.com"
```

👉 Solo afecta ese repositorio.



# Nivel fallback del sistema

Si no existe nada:

👉 usa usuario + hostname del computador.

(Eso puede exponer nombre de usuario u correo del ordenador)





```plain text
git var GIT_AUTHOR_IDENT
```

Eso mostrará exactamente **cómo Git se identifica AHORA MISMO** si hicieras un commit.



---



# 2) Identidad de subida (GitHub)

Define:

- permisos

- acceso al repo

- quién puede push

Esto usa:

- HTTPS + token

- o SSH key

(NO tiene relación directa con el author del commit).



# 🔐 Cómo GitHub sabe quién está haciendo `git push`

Cuando haces:

```plain text
git push
```

GitHub necesita autenticarte.

Hoy existen **dos formas principales**:

1️⃣ HTTPS + Token (la más común al inicio)

2️⃣ SSH Key (la más profesional y cómoda a largo plazo)

---

# 1. HTTPS + Personal Access Token (PAT)

## Idea simple

Antes se usaba contraseña.

Ahora GitHub dice:

> “No uses tu password, usa una llave especial (token).”

Ese token es como:

👉 una contraseña larga creada solo para Git.

---

## Cómo funciona internamente

Cuando haces push:

```plain text
Tu Mac → GitHub
GitHub: ¿quién eres?
Mac: aquí está mi token guardado
GitHub: OK, eres esta cuenta
```

---

## Dónde se guarda en Mac

Gracias a esto que vimos antes:

```plain text
credential.helper=osxkeychain
```

Tu token queda guardado en:

👉 **Llavero de macOS (Keychain Access)**

Por eso normalmente solo te pide login una vez.

---

## Cómo se configura (flujo normal)

La mayoría ya lo hizo sin darse cuenta:

1. Clonas un repo usando URL HTTPS:

```plain text
https://github.com/usuario/repo.git
```

1. Haces `git push`

1. GitHub abre login en navegador

1. Apruebas acceso

1. macOS guarda el token automáticamente

Y listo.

No vuelves a verlo.

---

## Ventajas

- Fácil

- Automático

- Ideal para empezar

## Desventajas

- Depende del llavero

- A veces pide login otra vez

- Menos usado en setups avanzados

---

# 2. SSH Key (la forma profesional)

## Idea simple

En vez de contraseña:

👉 tu computadora tiene una **llave privada**.

GitHub tiene la **llave pública**.

Cuando te conectas:

```plain text
GitHub: demuestra que eres tú
Mac: firma con su llave privada
GitHub: coincide → acceso permitido
```

Nunca envías contraseña.

---

## Qué se crea realmente

En tu Mac aparecen dos archivos:

```plain text
~/.ssh/id_ed25519        ← privada (NUNCA compartir)
~/.ssh/id_ed25519.pub    ← pública (se sube a GitHub)
```

---

## Cómo se configura (resumen claro)

### 1️⃣ Crear la llave

```plain text
ssh-keygen-t ed25519-C"angelgarciadatablog@gmail.com"
```

(presionas Enter varias veces)

---