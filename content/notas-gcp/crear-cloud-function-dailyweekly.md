

Cloud Functions crea internamente un servicio en Cloud Run.

![](img/30a477bcd0eb803493acc0ca17395fa3.webp)







![](img/30a477bcd0eb80ddb5f0d6d73ff355bf.webp)

*Es importante que el nombre refleje claramente su propósito.

*Correcto para BigQuery US.





![](img/30a477bcd0eb807c94c1eb38c6af8ffd.webp)



# 1️⃣ Autenticación

Ahora mismo no veo cuál opción marcaste, pero debe estar seleccionada:

```
Necesita autenticación
```

❌ No selecciones "Permite el acceso público".

Porque:

- Esta función será invocada por Cloud Scheduler.
- No debe estar expuesta públicamente.
- Es backend interno de pipeline.

👉 Marca **Necesita autenticación**.

---

# 🟢 2️⃣ Facturación

“Basada en solicitudes” está perfecto ✔

Eso significa:

- Solo pagas cuando se ejecuta.
- Ideal para pipelines batch.

Déjalo así.

---

# 🟢 3️⃣ Escalamiento

"Ajuste de escala automático" ✔ correcto.

Número mínimo de instancias = 0 ✔

Eso permite que:

- Se apague cuando no se use.
- Ahorres costo.

No necesitas tocar máximo por ahora.

---

# 🔴 4️⃣ Ingress (Muy importante)

Ahora tienes seleccionado:

```
Todos
```

Eso permite acceso desde Internet.

Para tu caso profesional, mejor opción:

👉 Selecciona **Interno**

¿Por qué?

Porque:

- Solo Cloud Scheduler (dentro del proyecto) la llamará.
- No necesitas acceso público.
- Es más seguro.



![](img/30a477bcd0eb80a7959edaf9efb1185e.webp)

*Agregar la service account





![](img/30a477bcd0eb803b8b5cf92d78e2c766.webp)

*Agregar las variables de entorno del repo (.env)





![](img/30a477bcd0eb80e4a3a7f950872c58eb.webp)

*En algunos casos, con una funición más compleja tendría que asignar más memoria



![](img/30f477bcd0eb80beb523cd357c51231f.webp)

*300 segundo es suficiente para este caso, pero según la complejidad de la función, puede aumentar (540s)



# 🟢 3️⃣ Memoria y CPU

512 MB ✔

1 CPU ✔

Perfecto para tu carga actual.



# 🟢 4️⃣ Redes

No toques nada.

No necesitas VPC.

Déjalo como está.



# 🟢 5️⃣ Seguridad

Encriptación administrada por Google ✔

Correcto.





# 🧱 1️⃣ Nombre del contenedor

Ves algo como:

```
Nombredel contenedor: placeholder-1
```

Eso es interno de Cloud Run.

En Cloud Functions Gen2:

- Google construye automáticamente el contenedor
- Tú no gestionas imagen Docker
- Tú no defines ENTRYPOINT
- Tú no defines CMD

❌ No debes cambiarlo.

Déjalo exactamente como está.





# 💾 2️⃣ Volúmenes

No necesitas volúmenes.

Los volúmenes se usan cuando:

- Montas secretos como archivos
- Conectas discos
- Haces almacenamiento temporal persistente

Tu pipeline:

- Extrae API
- Transforma
- Carga BigQuery

No necesita almacenamiento persistente en disco.

❌ No agregues volúmenes.







> Copiar el contiendo de las carpetas del repo

![](img/30f477bcd0eb80fabd68ed16107764ce.webp)



![](img/30f477bcd0eb806f9902dafa58c57c62.webp)