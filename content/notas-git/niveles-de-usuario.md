## **Los 3 niveles de configuración en Git**

### **1.****`-global`****(Recomendado para empezar)**

```bash
git config --global user.name "Angel García"
git config --global user.email "angel@ejemplo.com"
```

✅ **Se aplica a:** TODOS los repositorios en tu computadora

✅ **Cuándo usar:** Cuando siempre usas el mismo nombre/email (tu cuenta personal)

✅ **Se guarda en:** `~/.gitconfig` (tu carpeta de usuario)

### **2.****`-local`****(Por proyecto)**

```bash
git config --local user.name "Angel García - Empresa X"
git config --local user.email "angel@empresa.com"
```

✅ **Se aplica a:** Solo el repositorio actual

✅ **Cuándo usar:** Cuando quieres usar diferentes credenciales por proyecto

✅ **Se guarda en:** `.git/config` (dentro de tu proyecto)

⚠️ **Nota:** Debes estar dentro de un repositorio Git

### **3.****`-system`****(Raro)**

```bash
git config --system user.name "Nombre"
```

✅ **Se aplica a:** Todos los usuarios de la computadora

✅ **Cuándo usar:** Computadoras compartidas (raro)

⚠️ Requiere permisos de administrador





## **Prioridad (si hay conflicto)**

**Local** > **Global** > **System**

Si configuras algo en `--local`, ignora lo de `--global`

## **Caso de uso práctico**

**Escenario común:**



```bash
# Global: Tu email personal (por defecto)
git config --global user.name "Angel García"
git config --global user.email "angel.personal@gmail.com"

# Local: Email del trabajo (solo en proyectos de trabajo)
cd proyecto-trabajo/
git config --local user.email "angel.garcia@empresa.com"
```

**Resultado:**

- Proyectos personales → usan `angel.personal@gmail.com`
- Proyecto trabajo → usa `angel.garcia@empresa.com`





