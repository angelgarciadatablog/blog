

---

## Eliminar un commit

**Escenario:** Tienes un historial de commits y quieres eliminar el último realizado.

Primero verifica cuáles son tus dos últimos commits:

```bash
git log --oneline -2
```

```bash
//Resultado de ejemplo:

e19e6c8 (HEAD -> main) actualización de carpetas   ← quieres eliminar este
3f10683 (origin/main) optimize: compress images    ← quieres quedarte aquí
```

El resultado se muestra en el visor `less` de la terminal, y `q` es la tecla para salir.



## **¿Qué quieres hacer con los cambios de ese commit?**

**Opción A — Quieres conservar los cambios para retrabajarlos**

```bash
git reset --soft 3f10683   # apuntas al commit donde quieres quedarte, los cambios quedan en staging, listos para hacer commit directamente.
git reset --mixed 3f10683  # apuntas al commit donde quieres quedarte, los cambios quedan en tus archivos pero fuera del staging, tienes que hacer git add antes de commitear.
```

**`--mixed`****es el por defecto**

|   | Historial | Cambios en archivos |
| --- | --- | --- |
| `reset --soft / --mixed` | ❌ Borra el commit | ✅ Conserva los cambios |

**Opción B — No quieres saber nada de esos cambios**

```bash
# apuntas al commit donde quieres quedarte
git reset --hard 3f10683
```

⚠️ Siempre apuntas al commit donde **quieres quedarte**, no al que quieres eliminar. Todo lo que vino después de ese punto desaparece del historial y de tus archivos (desaparece tanto los códigos del los commits, es decir el historial, como también los cambios que se hizo en cada coomit)

|   | Historial | Cambios en archivos |
| --- | --- | --- |
| `reset --hard` | ❌ Borra el commit | ❌ Borra los cambios |



**Opción C — El commit ya está en GitHub y no quieres reescribir el historial**

```bash
# apuntas al commit que quieres deshacer
git revert e19e6c8
```

- Deshace los cambios de ese commit en tus archivos.
- El commit original permanece en el historial.
- Se crea un commit nuevo con los cambios revertidos.
- Usar cuando el commit **ya está en GitHub** y no quieres reescribir el historial.
|   | Historial | Cambios en archivos |
| --- | --- | --- |
| `revert` | ✅ Conserva el commit | ❌ Borra los cambios |





