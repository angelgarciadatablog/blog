# 🔐 Qué hacer cuando `gcloud` pierde credenciales aunque hayas ejecutado `gcloud init`

## 🧠 Contexto

Puede ocurrir que anteriormente hayas ejecutado:

```bash
gcloud init
```

Y todo haya funcionado correctamente (login, selección de proyecto, configuración activa).

Sin embargo, en otro momento puedes ver:

```bash
gcloud auth list
```

Salida:

```plain text
Nocredentialedaccounts.
```

Esto puede generar confusión porque el proyecto aún aparece configurado al ejecutar:

```bash
gcloud config list
```

---

## 🎯 Por qué ocurre esto

Es importante entender que:

> La configuración del proyecto y la autenticación son cosas distintas.

`gcloud` guarda información en dos niveles:

### 1️⃣ Configuración (Project, región, etc.)

Se guarda en:

```plain text
~/.config/gcloud/configurations/
```

Esto incluye:

- Proyecto activo

- Configuración por defecto

Esta información puede seguir existiendo aunque no haya sesión activa.

---

### 2️⃣ Credenciales (token de autenticación)

Se guardan en:

```plain text
~/.config/gcloud/credentials.db
```

Si el token:

- Expira

- Se borra

- Se invalida

- Cambias de máquina

- Reinstalas SDK

Entonces perderás autenticación aunque el proyecto siga configurado.

---

## 🧠 Punto clave

Estar logueado en la consola web de Google Cloud

≠

Estar autenticado en el SDK local (`gcloud`).

Son sesiones distintas.

---

## ✅ Cómo verificar si realmente estás autenticado

Ejecutar:

```bash
gcloud auth list
```

Si ves:

```plain text
Nocredentialedaccounts.
```

Entonces necesitas volver a autenticarte.

---

## 🔄 Cómo recuperar credenciales

Simplemente ejecutar:

```bash
gcloud auth login
```

Esto:

1️⃣ Abre el navegador

2️⃣ Permite iniciar sesión con tu cuenta Google

3️⃣ Genera un nuevo token local

4️⃣ Habilita el SDK nuevamente

Luego verificar:

```bash
gcloud auth list
```

Debe aparecer tu cuenta con un `*` indicando que es la activa.

---

## 🧠 Consideraciones importantes

- La autenticación es local a cada máquina.

- Si cambias de computadora, debes autenticar nuevamente.

- Si reinstalas el SDK, debes autenticar nuevamente.

- La pérdida de credenciales no afecta tus proyectos en la nube.

---

## 🎓 Modelo mental correcto

```plain text
CuentaGoogle(identidad)
        ↓
gcloudSDK(token local)
        ↓
Proyecto activo
        ↓
Recursos Cloud
```

Si falta el token local, el SDK no puede operar.