

Lista los usuarios que hicieron commits dentro del repo

```bash
git log --format="%an | %ae" | sort -u
```



# Qué hace este comando

Se compone de tres partes:

---

## 1️⃣ `git log`

Recorre TODO el historial de commits.

---

## 2️⃣ `-format="%an | %ae"`

Le dices a Git:

> “Muéstrame solo el autor y el email”.

Significa:

Ejemplo de salida cruda:

```plain text
Angel Garcia | angelgarciadatablog@gmail.com
Angel Garcia | angelgarciadatablog@gmail.com
Angel García | noreply@github.com
Angel Garcia | angelgarciadatablog@gmail.com
```

---

## 3️⃣ `sort -u`

Esto ya es Linux/macOS, no Git.

Hace dos cosas:

- ordena

- elimina duplicados (`u` = unique)

Resultado final:

👉 lista única de identidades que han firmado commits.

---

# 🧠 Por qué es tan usado

Porque responde rápido preguntas como:

- ¿Quién ha contribuido al repo?

- ¿Hay emails personales filtrados?

- ¿Hay identidades duplicadas?

- ¿Tengo firmas inconsistentes?

Exactamente lo que estás haciendo ahora.

---

# Variantes muy usadas (nivel práctico)

## Ver autores + cantidad de commits

```plain text
git shortlog-sne
```

Ejemplo:

```plain text
15  Angel Garcia <angelgarciadatablog@gmail.com>
3   Angel García <noreply@github.com>
```

👉 Este sí es casi el **estándar clásico**.

---

## Solo nombres únicos

```plain text
git log--format="%an" |sort-u
```

---

## Solo correos únicos

```plain text
git log--format="%ae" |sort-u
```