# 📘 ¿Qué hace realmente `git log`?

```bash
git log
```

`git log` muestra:

👉 **la historia de commits del repositorio**.

Pero no es solo una lista…

es literalmente el recorrido del historial que Git usa internamente.

---

## Cómo piensa Git el proyecto

Git no guarda versiones como carpetas numeradas.

Guarda una cadena de commits conectados:

```
A ← B ← C ← D (HEAD)
```

Cada commit sabe:

- quién lo creó
- cuándo
- qué cambió
- cuál fue el commit anterior.

`git log` simplemente recorre esa cadena hacia atrás.

---

## Lo que viste cuando ejecutaste `git log`

Algo así:

```
commit 54ec3e0...
Author: Angel Garcia
Date: ...

    mensaje del commit
```

Cada bloque representa:

📸 una “foto” completa del proyecto en ese momento.

---

#  Qué información muestra un commit

Por defecto `git log` enseña:

| Campo | Qué significa |
| --- | --- |
| commit | identificador único (hash) |
| Author | quién escribió el cambio |
| Date | cuándo se creó |
| mensaje | explicación del cambio |

Ese hash es importante:

👉 si cambia el autor o email, cambia el hash

(eso fue justo lo que hicimos al limpiar).

---

# Por qué se abre una pantalla especial

Porque el historial puede ser enorme.

Git usa un visor (`less`) para poder:

- desplazarte
- buscar
- navegar sin llenar la terminal.

---

# Versiones MUY útiles de `git log`

Estas las usan casi todos los developers:

---

## 1️⃣ Log compacto (el favorito)

```
git log --oneline
```

Ejemplo:

```
54ec3e0 WIP antes de limpieza
1d37280 introduccion a vectores
6236774 estructura inicial
```

Mucho más legible.

---

## 2️⃣ Ver el árbol visual ( importante)

```
git log --graph--oneline--decorate--all
```

Muestra algo como:

```
* 54ec3e0 (HEAD -> main)
* 1d37280
* 6236774
```

Aquí ves ramas y merges visualmente.

---

## 3️⃣ Ver quién cambió qué

```
git log -p
```

Muestra exactamente las líneas modificadas.

---

# Insight importante (nivel intermedio)

`git log` no mira archivos.

Mira **el grafo de commits**.

Git es básicamente un grafo dirigido de commits.



`git log` abre un programa llamado **pager** (normalmente `less`) para poder desplazarte.

Para salir simplemente:

```
q
```

👉 Presiona la tecla **q** (de *quit*).

---

## Atajos útiles mientras estés dentro (por si te sirve para tu documentación)

- `q` → salir
- `↑ ↓` → mover línea por línea
- `space` → bajar una página
- `b` → subir una página
- `/texto` → buscar dentro del log
- `n` → siguiente resultado de búsqueda