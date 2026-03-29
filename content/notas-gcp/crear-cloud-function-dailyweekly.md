

Cloud Functions crea internamente un servicio en Cloud Run.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/de23cfd5-a657-441d-a610-2ceb9f2391fa/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=43aee931b3a0aa8c495420fe776d16430b669d931541c1028416fe18ee6d332e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)







![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/cddff7db-ad1b-4e98-91b0-d0474d4cae39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=230517cd0a52fba6a1581aaa496c4bf621755107a77a3339f39d858e772178d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*Es importante que el nombre refleje claramente su propósito.

*Correcto para BigQuery US.





![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/e786d6eb-f134-4d71-b687-3a0703535446/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=1795a161b8b43e5517c89e32a5da976d6111d63ba630fec7e61694671c1c2947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 1️⃣ Autenticación

Ahora mismo no veo cuál opción marcaste, pero debe estar seleccionada:

```plain text
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

```plain text
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



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/71f72679-2be2-4f3d-99cc-45c78eff6704/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=ebd9a6aa2bf995181eb1a26e42d0a55b523bfa6735f4a0418bf6fa75e4ad2b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*Agregar la service account





![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/c5165902-8511-4b37-8a78-a06e7beb11af/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=819e00b520e2b821640758e6f0dc7d15759954714a840ef494193bbee09ede6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*Agregar las variables de entorno del repo (.env)





![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/e3f359f8-777d-4c6a-9cb7-1be5505669f4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=747a2c3bf3e7604e44fab5eb58a50fdcee942635e8398bd46ec8318bd930eb5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*En algunos casos, con una funición más compleja tendría que asignar más memoria



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/492efc04-19db-4c00-a861-064042b14e21/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR37MBO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T061059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZrs1jfFjp%2BrtfBrqdKz2M2ylt5lS5FJGLL7%2FIcYHRFQIgFAbpwZ0IuO3Q%2Bu16rue9VCsqJALfuarF%2FNQoNupFAM4q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPcrvfcaQ%2FUPiOFQ4CrcAxmJukWAyjLJegaHlFP%2BW1TFSDGgaflhquEQw7ydni1amvvoX%2Bu0Z0DKC9B%2Fv5YstAFpdSFZNwb95wZG2peF8lfhc9w06hVMD%2BOAIkqQDJbwLGyIB3rVK0lvUCuQMpYKngtkr%2FGR9T7DGNP9h3PwrmISx8N4nrtSUmiRMzVjOCktCdZPh%2BnGX2F5xhLZrMe8JbZu6Y14Q2IEReQWUQrZtA9tDB1XLugzPY2lnlXEYE7v7%2Bc5d5qhLkAAT5nMuzGsY2yr2sVVCYNKi7SQu%2FfUSrzj3MqwSnWNphJwtrUA7BEXsJxKmDq6EZpH%2FcI1QUwavFQ1rjREV3keIsvjMw9q9Woz4HFU0gvhjYPexY5q9e1biOPbQit3P1egjQfrgEmNrzGLDeqj8DSyWKLlSkDefUPelN9w75sxcjbckcO0IZHV9kA5ShLlA8a2PePmrTKEErZ6qtMCq0almhbpkFpzY82cSHOgAxpxP8IrsaDcGVG9oIVP%2FajOfVYq3TdKms%2B4gtWgXqTNu5%2BrxMwllO%2Bc4Y6AARuY1FdLtcZbgcwAMPCpl7G%2BJMbWAGx5jeJ%2BS4uA8n1KBsigKrWQ6hiqX%2BohPcRad7z4mWAAkpoz6Gqv7uq%2FS3cDXGU8p6buxzN2MI7Hos4GOqUBb12inKEcpI%2BmIwb1h0vaiHhP%2B7ATdF11%2Fu2B0Ux9Cx4nfr8vrXS0r4ZeoC%2F9T7orACbJ9z%2BZTjvCmYXUig4B9%2BpmBZJOSRqMfi1VN5Wf4GBR59NLmEwmLvD5uEt0CaxwysCRCWcQUflFV5nGi%2BKwbdrdZmYH%2B5d124u660rWqhPsBmNtBI0WWu6tu4PGBSb80yNcAbF6MEPrg7c952dc95f3Itxv&X-Amz-Signature=2f980b7f6b20bfeb2136fd8ddb01fb36eca0cf0886e7523b28116a374f8d7a9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

```plain text
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