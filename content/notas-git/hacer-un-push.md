

```bash
#revisar el repositorio donde se hará el push
git remote -v

# origin  https://github.com/usuario/mi-repositorio.git (fetch - traer)
# origin  https://github.com/usuario/mi-repositorio.git (push - subir)
```





```bash
#revisar los cambios realizados en el repositorio local
git status
```



```bash
#Agrega todos los archivos que han sido modificados al staging área
git add .

#Agrega solo uno de los archivos modificados al staging área
git add data/sections.json
```





```bash
#Confirmar los cambios realizados
git status

#Esto lista solo los archivos que están en staging, 
#sin mostrar los que están modificados pero no agregados
git diff --cached --name-only
```





```bash
#Configurar el usuario que hará el commit en este repositorio
git config user.name "Angel García"
git config user.email "angelgarciachanga@gmail.com"

#Configurar el usuario que hará el commit en este repositorio 
#(recomendado si siempre usarás el mismo correo en tu PC)
git config --global user.name "Angel García"
git config --global user.email "TU_CORREO_DE_GITHUB"


git config --list
```



```bash
#Esto mueve los cambios del staging al repository (commit histórico).
git commit -m "Actualizar secciones en sections.json"
```



```bash
#Muestra los últimos 5 commits incluyendo el que acabamos de realizar
git log --oneline -5

#Muestra todos los commit, para salir hay que presionar q
git log
```



```bash
#Finalmente, para subir los cambios al repositorio remoto:
#origin → es el nombre del repositorio remoto (GitHub).
#main → es la rama en la que estás trabajando.
git push origin main
```





---



# Qué pasa si haces `git push` sin estar logeado en GitHub

Cuando ejecutas:

```
git push
```

Git intenta conectarse al repositorio remoto definido en `origin`.

Si no existe una sesión válida, GitHub inicia un proceso de autenticación.

Lo que ocurra depende del **método de conexión** del repositorio.

---

# CAMINO 1 — Repositorio configurado con HTTPS

Repositorio remoto:

```
https://github.com/usuario/repositorio.git
```

---

## 🔄 Flujo completo

1️⃣ Ejecutas:

```
git push
```

2️⃣ Git intenta conectarse a GitHub.

3️⃣ GitHub detecta que NO hay credenciales guardadas.

4️⃣ Ocurre una de estas acciones:

### 👉 Caso moderno (lo normal hoy)

Se abre automáticamente el navegador:

```
Authorize Git Credential Manager
```

Te pide:

- iniciar sesión en GitHub
- aprobar acceso desde esa computadora.

---

### 👉 Caso alternativo

Git pide en terminal:

```
Username:
Password or token:
```

(la contraseña real ya no funciona, solo token).

---

5️⃣ Después de aprobar:

- GitHub genera un **Personal Access Token**
- macOS lo guarda en el llavero (Keychain)
- el push continúa automáticamente.

---

## Resultado

- quedas autenticado
- futuros `git push` no pedirán login.

---

## Si cancelas el login

Obtendrás algo como:

```
remote: Permission denied
fatal: Authentication failed
```

---

# ✅ CAMINO 2 — Repositorio configurado con SSH

Repositorio remoto:

```
git@github.com:usuario/repositorio.git
```

---

## 🔄 Flujo completo

1️⃣ Ejecutas:

```
git push
```

2️⃣ Git intenta autenticarse usando tu llave SSH local.

---

### Caso A — No existe llave SSH

Error típico:

```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

GitHub está diciendo:

> No reconozco esta computadora.

---

### Caso B — Existe llave pero no está registrada en GitHub

Mismo error:

```
Permission denied (publickey)
```

Porque GitHub no tiene tu clave pública.

---

### Caso C — Primera conexión correcta

GitHub puede preguntar:

```
Are you sure you want to continue connecting?
```

Respondes:

```
yes
```

Y queda registrada la conexión.

---

## Resultado

Una vez configurado SSH:

- nunca vuelves a logearte
- no hay navegador
- autenticación automática.

---

# Diferencia conceptual clave

| Situación | HTTPS | SSH |
| --- | --- | --- |
| No autenticado | abre login web | error inmediato |
| Primera configuración | automática | manual |
| Credencial guardada | Keychain | archivo SSH |
| Uso diario | fácil | profesional |

---

# 🔎 Algo importante 

El login ocurre **solo cuando Git necesita permiso**, no cuando clonas ni cuando ves remotes.

Git puede existir perfectamente sin autenticación hasta el momento del push.

---

GitHub valida:

```
QUIÉN hace el push → autenticación (HTTPS/SSH)
QUIÉN escribió el commit → email del commit
```

Son dos identidades distintas.