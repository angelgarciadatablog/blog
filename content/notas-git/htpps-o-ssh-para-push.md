

# HTTPS vs SSH en Git

## ¿Qué son?

Dos protocolos para autenticarte con GitHub al hacer push/pull/clone.

---

## Comprobar cuál estás usando

**En un repo concreto:**

```python
git remote -v
```

- Si empieza por `https://` → HTTPS

- Si empieza por `git@` → SSH

**Verificar si SSH está configurado con GitHub:**

```python
ssh -T git@github.com
# OK:    Hi usuario! You've successfully authenticated...
# Error: Permission denied (publickey)
```

**Ver tus claves SSH locales:**

```python
ls ~/.ssh
# Si existe id_ed25519 o id_rsa → tienes una key generada
# Si está vacío o no existe → no tienes SSH configurado
```

---

## Configurar HTTPS

Es el más simple. Solo necesitas un **Personal Access Token** (PAT) en lugar de contraseña.

**1. Generar el token:**
GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token → scope `repo`

**2. Usarlo:**
La primera vez que haces push te pide usuario y contraseña. En contraseña pegas el token.

**3. Guardarlo para no repetirlo:**

```python
git config --global credential.helper osxkeychain
```

macOS lo guarda en el llavero automáticamente.

---

## Configurar SSH

**1. Generar la key:**

```python
ssh-keygen -t ed25519 -C "tu@email.com"
# Presiona Enter x3 (ruta por defecto, sin passphrase)
```

**2. Copiar la clave pública:**

```python
cat ~/.ssh/id_ed25519.pub
```

**3. Añadirla a GitHub:**
GitHub → Settings → SSH and GPG keys → New SSH key → pegar

**4. Verificar:**

```python
ssh -T git@github.com
# Hi usuario! You've successfully authenticated...
```

---

## Cambiar el protocolo de un repo existente

```python
# De SSH a HTTPS
git remote set-url origin https://github.com/usuario/repo.git

# De HTTPS a SSH
git remote set-url origin git@github.com:usuario/repo.git
```

---

## ¿Cuál usar?

**HTTPS** si:

- Trabajas en múltiples máquinas o entornos temporales

- No quieres configuración extra

- Es tu situación actual — todos tus repos lo usan

**SSH** si:

- Trabajas siempre desde las mismas máquinas

- Quieres evitar tokens y credenciales

- Tienes varios repos y prefieres no gestionar tokens

