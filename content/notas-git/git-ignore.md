# 📌 Caso: Archivo `.DS_Store` subido antes de configurar `.gitignore`

## 🧠 Contexto

Durante el desarrollo del proyecto, el archivo `.DS_Store` fue subido al repositorio antes de crear el archivo `.gitignore`.

`.DS_Store` es un archivo generado automáticamente por macOS para almacenar metadatos de carpetas. No forma parte del código del proyecto y no debe versionarse.

---

## 🚨 Problema detectado

Aunque se añadió `.DS_Store` al `.gitignore`, el archivo seguía apareciendo en el repositorio.

Esto ocurre porque:

> `.gitignore` no elimina archivos que ya están siendo rastreados (tracked) por Git.

Si un archivo ya fue agregado con `git add` y confirmado con `commit`, Git lo seguirá rastreando aunque luego se agregue al `.gitignore`.



---



## 🛠️ Solución aplicada

Se eliminó el archivo del seguimiento de Git sin borrarlo del sistema local:

```bash
gitrm --cached .DS_Store
```

Luego se confirmó el cambio:

```bash
git commit -m"Remove .DS_Store from tracking"
git push
```

---

## ✅ Resultado

- El archivo desapareció del repositorio remoto.

- Se mantuvo en el entorno local.

- No volverá a subirse gracias a la regla agregada en `.gitignore`:

```plain text
.DS_Store
```



---



## 📚 Aprendizaje clave

`.gitignore` solo evita que archivos nuevos no rastreados sean añadidos al repositorio.

Para dejar de rastrear un archivo ya versionado es necesario usar:

```bash
gitrm --cached <archivo>
```