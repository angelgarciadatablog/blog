## ✅ 1️⃣ Ver cuánto pesa cada app instalada

Abre **Terminal** y ejecuta:

```
du-sh /Applications/*
```

Esto calculará el tamaño real de cada aplicación.





## 🔎 Ahora hagamos la parte que revela la verdad

Quiero ver quién está usando más espacio REAL (cache y datos).

Ejecuta en Terminal:

```
du-sh ~/Library/Application\ Support/* |sort-hr | head-15
```