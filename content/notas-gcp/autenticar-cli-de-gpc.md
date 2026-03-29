

> gcloud init

Esto va a:

1️⃣ Abrir el navegador
2️⃣ Pedirte login con tu cuenta personal
3️⃣ Mostrar lista de proyectos
4️⃣ Guardar la configuración local

**Solo se hace una vez al principio para autenticarte con una cuenta y elegir un proyecto**



Al final se abrirá está página:

https://docs.cloud.google.com/sdk/auth_success?hl=es-419

# 🧠 Qué estamos haciendo realmente

Hasta ahora solo instalamos herramientas.

Con `gcloud init`:

- Se crea un perfil local

- Se guarda un token de autenticación

- Se define el proyecto activo

- Se habilita conexión real a la nube

Es como hacer `git config` pero para Google Cloud.





## Elije un proyecto.

necesariamente tienes que elegir un proyecto.

```bash
You are signed in as: [tucorreodegoogle@gmail.com].

Pick cloud project to use:
 [1] hackspace-bootcamps-2021
 [2] prueba-423920
 [3] prueba-blogger-439506
 [4] prueba-n8n-467606
 [5] prueba2-433703
 [6] Enter a project ID
 [7] Create a new project
Please enter numeric choice or text value (must exactly match list item): 
```





# 🧠 Qué se guarda cuando usas `gcloud init`

Cuando hiciste login, se guardó en tu usuario de Windows:

- Token de autenticación

- Proyecto activo

- Configuración de CLI

Eso se guarda en una carpeta tipo: (windows)

```powershell
C:\Users\TU_USUARIO\AppData\Roaming\gcloud
```

mac

```sql
~/.config/gcloud/
```



Eso NO depende de que terminal esté abierto.

---



# 🎯 Entonces si cierras Terminal:

✔ Sigues autenticado

✔ El proyecto activo sigue configurado

✔ `gcloud` sigue instalado

✔ `bq` sigue funcionando

Cuando vuelvas a abrir PowerShell, todo sigue igual.



# 👌 Vuelves abrir la terminal y quieres verificar el usuario y proyecto:

```bash
gcloud config list
```



