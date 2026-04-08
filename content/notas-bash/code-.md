## 1️⃣ Activa el entorno virtual (desde la raíz del proyecto)

Asegúrate de estar en:

```bash
youtube-data-pipeline
```

Luego ejecuta:

```bash
source venv/bin/activate
```

---

## 2️⃣ Verifica que quedó activo (esto es clave)

Deberías ver **dos señales**:

### a) El prompt

```
(venv)angelgarciachanga@MacBook-Air-de-Angel youtube-data-pipeline %
```

### b) El Python correcto

Ejecuta:

```bash
which python
```

Resultado esperado:

```
.../youtube-data-pipeline/venv/bin/python
```

---

## 3️⃣ NO abras VS Code todavía

Primero quiero que:

- el venv esté activo
- la shell esté “limpia”
- VS Code herede ese contexto

---

## 4️⃣ Cuando confirmes esto…

Con eso, **recién ahí** abrimos VS Code con:

```bash
code .
```





### 🔴 — NO está en el PATH (tu caso actual)

No devuelve nada o muestra:

```
code not found
```

👉 Esto confirma que **no está registrado en el PATH**.

---

## 🔎 Forma 2 (comprobación adicional)

También puedes probar:

```bash
code --version
```

Si dice:

```
zsh:command not found: code
```

👉 Confirmado al 100%.

---

## 🧠 Qué significa “no estar en el PATH”

- VS Code **sí está instalado**
- macOS **no sabe** que `code` es un comando
- la terminal no lo puede ejecutar

Esto es totalmente normal en macOS.

---

## ✅ Forma correcta de solucionarlo (recomendada)

La opción **más segura y estándar** es esta (desde VS Code):

1. Abre **Visual Studio Code**
1. `Cmd + Shift + P`
1. Escribe:
   ```
   Shell Command: Install'code'commandin PATH
   ```
1. Enter
1. Cierra VS Code
1. Cierra la terminal
1. Abre una terminal nueva

Luego prueba:

```bash
which code
```

Ahora **sí debería devolver una ruta**.