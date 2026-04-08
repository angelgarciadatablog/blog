**¿Qué es Google Cloud SDK?**

Es un conjunto de herramientas CLI para interactuar con los servicios de Google Cloud desde la terminal. El comando principal es `gcloud`.



**¿Por qué necesita login?**

Porque Google Cloud es un servicio de pago — cada acción (crear servidores, subir archivos, consultar bases de datos) está asociada a una cuenta y a un proyecto de facturación.



**Los comandos principales:**

| Comando | Para qué sirve |
| --- | --- |
| `gcloud` | Gestionar infraestructura (VMs, redes, etc.) |
| `gsutil` | Gestionar almacenamiento (buckets) |
| `bq` | Gestionar BigQuery |

## **Primera revisión:**

**¿Qué vamos a revisar?**

1. Qué cuenta está activa
1. A qué proyecto está conectado
1. Si corresponde a tu cuenta de trabajo

---

Ejecuta esto:

```bash
gcloud auth list
```

**Ahora verifiquemos a qué proyecto está apuntando:**

```bash
gcloud config list
```



## **Una cosa importante sobre gcloud:**

A diferencia de gh, gcloud maneja el concepto de **configuraciones** — puedes tener múltiples configuraciones con diferentes cuentas y proyectos, y cambiar entre ellas:

```bash
# Ver todas las configuraciones
gcloud config configurations list

# Cambiar de configuración
gcloud config configurations activate nombre-configuracion
```

Útil cuando trabajas con múltiples proyectos o cuentas de Google Cloud.



## **¿Cómo funciona gcloud con múltiples cuentas?**

gcloud usa el concepto de **configuraciones** — cada una guarda:

- Una cuenta de Google
- Un proyecto activo
- Región y zona por defecto (opcional)

**La relación cuenta → proyecto:**

`Cuenta 1: angelg@reechai.com
    └── Proyecto: proyecto-datos1

Cuenta 2: angel@otraempresa.com
    └── Proyecto: proyecto-empresa-2

Cuenta 3: angel@tercera.com
    └── Proyecto: proyecto-3`

Cada configuración apunta a una cuenta + proyecto específico.



**Lo que esto significa:**

- Si tienes **3 cuentas diferentes** → necesitas 3 configuraciones
- Si tienes **1 cuenta con 3 proyectos** → necesitas 3 configuraciones
- Si tienes **1 cuenta, 1 proyecto, 3 datasets** → necesitas solo 1 configuración, los datasets se acceden directamente con `bq`



**El concepto clave:**

> La configuración de gcloud solo define **desde dónde trabajas** (proyecto activo). Los permisos de acceso a otros proyectos los gestiona **IAM de Google Cloud** a nivel de cuenta.





## Agregar una nueva cuenta



## Paso 1. Revisar configuración actual

```bash
# Ver configuraciones existentes
gcloud config configurations list

# Ver configuración activa
gcloud config list

# Ver cuentas autenticadas
gcloud auth list
```
```



## Paso 2. Agregar una nueva configuración cuenta-proyecto

```bash
gcloud config configurations create angel-angelgarciadatablog
```

*Aquí angel-angelgarciadatablog es el nombre de la configuración, en donde sería bueno tener de manera descriptiva el usuario de google y el proyecto



 Ahora autenticamos la cuenta:

```bash
gcloud auth login
```

![](img/32c477bcd0eb8084a65add3797e4b8e3.webp)

*tiene que ser la cuenta de google de la cuenta de google cloud

## Paso 3. Ahora establece el proyecto:

```bash
gcloud config set project angelgarciadatablog
```

*en este caso estamos estableciendo como configuración el proyecto ya creado en google cloud llamado angelgarciadatablog



Verifiquemos que quedó bien:

```bash
# Ver configuración activa
gcloud config list

# Ver configuraciones existentes
gcloud config configurations list
```



 Para agregar nuevos proyectos que están en la misma cuenta de google: Repite desde el paso 2

```bash
gcloud config configurations create angel-angelgarciadatablog
```

```bash
gcloud config set account cuenta-google@gmail.com
gcloud config set project nombre-proyecto
```







## Eliminar una configuración cuenta-proyecto

```bash
# Ver configuraciones existentes
gcloud config configurations list

# Primero activamos otra configuración para que no haya conflicto
gcloud config configurations activate nombre-otra-configuracion

# La eliminamos
gcloud config configurations delete nombre-configuracion
```