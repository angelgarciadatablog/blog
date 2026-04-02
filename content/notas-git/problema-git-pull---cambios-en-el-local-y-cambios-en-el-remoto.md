

> 

### Inicio

Situación inicial (ambos, remoto y local empiezan igual):



> 

### Divergencia (cada uno escribe diferente):

Tú en tu laptop:

```bash
commit A → commit B (Agregas Capítulo 2: "El héroe sale...")
```



Tu colaborador en GitHub:

```bash
commit A → commit C (Agrega Capítulo 3: "El villano aparece...")
```





> Opción 1: Manual



```bash
# 1. Descarga cambios SIN combinar, 
# estos cambios no son visible en el local, sino que están en local, pero guardados en la memoria de git
git fetch origin main

# 2. Revisa qué cambió / para revisarlo a detalle se puede usar: git show origin/main:archivo
git log origin/main

# 3. Ve las diferencias / presiona q para salir de esta vista
git diff main origin/main

# 4. Si te gusta, combina
#Aquí recien aparecen los archivos nuevos del remoto en el local
#Sino se agrega el comentario -m se abrirá el edito Vim para agregar comentarios
git merge origin/main -m "Merge: agregar CNAME y actualizar index"

# 5. Si no te gusta, no hagas nada
# (tus archivos locales no se tocaron)
```







> Opción 2: Automática



```bash
# Configura: "usa merge"
git config pull.rebase false
# Ejecuta: fetch + merge
git pull origin main
```

***Detalles importantes:**Sobre `git config pull.rebase false`:

-Solo necesitas ejecutarlo **UNA VEZ**

-Queda guardado en tu configuración

-Después solo usas `git pull origin main`





> Resultado en ambos casos

```bash
```
**Resultado:**
```
        commit A (base común)
        /      \
commit B        commit C
(Cap. 2)        (Cap. 3)
        \      /
      commit D (MERGE)
      
Libro final tiene:
- Capítulo 1 (original)
- Capítulo 2 (tuyo)
- Capítulo 3 (del colaborador)
```