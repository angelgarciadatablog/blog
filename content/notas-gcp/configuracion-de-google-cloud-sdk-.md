# 1. Verificar si ya hay sesión activa:

Antes de autenticarse, siempre verificar si ya existe una sesión:

```bash
gcloud auth list
```

Tres escenarios posibles:

1. **Ves tu cuenta con****`*`** — ya estás autenticado y activo, no necesitas hacer nada más.
   ```bash
   ACTIVE  ACCOUNT
   *       tu@gmail.com
   ```
1. **Ves tu cuenta pero sin****`*`** — las credenciales existen pero la cuenta no está activa. Solo actívala:
   ```bash
   gcloud config set account tu@gmail.com
   ```
1. **Lista vacía** — no hay ninguna sesión guardada. Procede al siguiente paso.



# 2. Autenticarse

Hay dos comandos (más uno aparte) para autenticarse y es importante entender cuándo usar cada uno.

1. **`gcloud init`** — autentica *y* configura. Hace tres cosas en secuencia: abre el navegador para iniciar sesión, luego te pregunta qué proyecto quieres usar, y finalmente configura región y zona por defecto. Úsalo cuando es la primera vez o cuando quieres reconfigurar todo desde cero.* (logear y configurar)*
   ```bash
   gcloud init
   ```
   Cuando corres `gcloud init` por primera vez, el flujo en la terminal es este:
   1- Se abre el navegador para iniciar sesión con tu cuenta de Google.
   2- Al completar el login, el navegador muestra una página de confirmación
   3- De vuelta en la terminal, aparece la lista de proyectos disponibles para elegir:
   ```bash
   You are signed in as: [tu@gmail.com].

   Pick cloud project to use:
    [1] proyecto-uno
    [2] proyecto-dos
    [3] Enter a project ID
    [4] Create a new project
   Please enter numeric choice or text value (must exactly match list item):
   ```
   Elegir un proyecto es obligatorio — `gcloud init` no termina hasta que seleccionas uno o creas uno nuevo.
   Lo que `gcloud init` guarda en tu máquina:Token de autenticación, Proyecto activo, Configuración del CLI.
   Todo se guarda en `~/.config/gcloud/configurations` y **no depende de que la terminal esté abierta**. Si cierras la terminal y la vuelves a abrir, sigues autenticado, el proyecto sigue configurado y `gcloud` y `bq` siguen funcionando exactamente igual.



1. **`gcloud auth login`** — solo autentica. No toca ninguna configuración existente. Úsalo cuando ya tienes todo configurado y solo necesitas agregar o refrescar una cuenta. *(Logear)*
   ```bash
   gcloud auth login
   ```
   *También guarda el token, pero en otra subcarpeta **`~/.config/gcloud/credentials.db`** y persiste entre sesiones de terminal.*



1. **`gcloud auth application-default login`** — este es un tercer tipo de autenticación distinto a los anteriores. Las credenciales que genera no son para el CLI, sino para las **librerías cliente** — por ejemplo cuando tu aplicación en Python usa `google-cloud-bigquery` o `google-cloud-storage`. Si solo usas la terminal con `gcloud` o `bq`, no lo necesitas.
   ```bash
   gcloud auth application-default login
   ```

# 3. Múltiples cuentas

El SDK permite tener varias cuentas autenticadas simultáneamente en la misma máquina. Cada vez que corres `gcloud auth login` con una cuenta diferente, se agrega a la lista sin reemplazar las anteriores.

```bash
gcloud auth list
```
```
ACTIVE  ACCOUNT
*       trabajo@empresa.com
        personal@gmail.com
        cliente@otrodominio.com
```

Para cambiar la cuenta activa:

```bash
gcloud config set account personal@gmail.com
```

Para revocar (cerrar sesión) de una cuenta específica:

```bash
gcloud auth revoke personal@gmail.com
```



# 4. Configuraciones y perfiles

Las configuraciones son independientes de las sesiones. Una configuración es simplemente un archivo con propiedades guardadas — cuenta, proyecto, región — que puedes activar con un solo comando. No son sesiones, no autentican ni desautentican nada.
Son útiles cuando trabajas con múltiples proyectos o clientes regularmente y no quieres cambiar propiedades una por una cada vez.


Crear y configurar un perfil:

```bash
#Crear la configuración con un alias "trabajo"
gcloud config configurations create trabajo

#Asignar una cuenta de gmail para esa configuración 
gcloud config set account trabajo@empresa.com

#Asignar un proyecto de google cloud a la que esa cuenta tiene acceso
gcloud config set project proyecto-empresa

#Asignar una región (opcional)
gcloud config set compute/region us-central1
```

Ver todas las configuraciones existentes:

```bash
gcloud config configurations list
```

Cambiar entre configuraciones:

```bash
#Activa la configuración con alias trabajo
gcloud config configurations activate trabajo

#Activa la configuración con alias cliente-a
gcloud config configurations activate cliente-a
```



# 5. Ver y modificar valores de la configuración activa

Una vez dentro de una configuración, puedes consultar y modificar sus propiedades individuales (account, project, region, etc) sin tener que recrearla. 

— Ver toda la configuración activa (account, project, region, etc):

```bash
gcloud config list
```

— Ver una propiedad específica:

```bash
gcloud config get project
gcloud config get account
gcloud config get compute/region
```

*Útil cuando solo necesitas confirmar un valor puntual o capturarlo dentro de un script, sin procesar el output completo de **`gcloud config list`**.*



— Modificar una propiedad específica dentro de una configuración:

```bash
gcloud config set project OTRO-PROYECTO-ID
gcloud config set account otra@gmail.com
gcloud config set compute/region us-east1
```

*Estos cambios aplican solo a la configuración activa en ese momento. Si cambias a otra configuración con **`gcloud config configurations activate`**,** cada una conserva sus propios valores independientemente.*



—Elimina la propiedad de la configuración activa:

```bash
gcloud config unset project
gcloud config unset account
gcloud config unset compute/region
```

*Elimina la propiedad de la configuración activa. A partir de ese momento esa propiedad queda sin valor — si algún comando la requiere, habrá que especificarla explícitamente en cada llamada o volver a definirla con **`gcloud config set`**.*



— Renombrar una configuración:

```bash
gcloud config configurations rename nombre-viejo nombre-nuevo
```

El alias es lo único que no se modifica con `gcloud config set` — todo lo demás sí.



**Nota:** para cambiar entre proyectos lo ideal es tener una configuración por cada combinación cuenta-proyecto y cambiar entre ellas con 

```bash
gcloud config configurations activate alias-proyecto
```



# 6. Configuraciones huérfanas y limpieza

Dado que las configuraciones y las sesiones son independientes, revocar una cuenta no borra las configuraciones que la usaban — quedan apuntando a credenciales que ya no existen.

Si tienes esto:

```bash
config-1  →  cuenta-a@gmail.com  ← revocada
config-2  →  cuenta-a@gmail.com  ← revocada
config-3  →  cuenta-b@gmail.com  ← activa
```

Las configuraciones huérfanas seguirán listándose y parecerán normales, pero cualquier comando que requiera autenticación fallará al usarlas.

**Importante:** si la configuración activa en ese momento es la huérfana, el SDK se vuelve inestable porque cada comando intenta leer credenciales que no existen. Lo primero en ese caso es activar una configuración sana (con login en la cuenta de gmail):

```bash
gcloud config configurations activate config-3
```

Luego puedes limpiar las huérfanas de dos formas:


Borrarlas:

```bash
gcloud config configurations delete config-1
gcloud config configurations delete config-2
```



O reasignarlas a una cuenta que sí tiene sesión activa:

```bash
#Activas una configuración 
gcloud config configurations activate config-1

#Le agregas una cuenta de gmail en la cual tienes el login
gcloud config set account cuenta-b@gmail.com

```



> Pregunta: ¿Qué pasaría si estoy dentro de una configuración (cuenta-proyecto) la cual tiene acceso a una vista de bigquery que hace un llamado a una tabla dentro de otro proyecto?

