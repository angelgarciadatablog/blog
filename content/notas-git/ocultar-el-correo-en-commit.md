## PASO 3.1 — Privacidad del email en commits

Cuando haces un commit, tu email queda visible públicamente en el historial del repositorio. GitHub ofrece una solución para esto.

Ve a 👉 https://github.com/settings/emails y tienes estas opciones:

| # | Opción | Cómo se ve en commits | Pros | Contras |
| --- | --- | --- | --- | --- |
| 1 | **Email real** | `tu@email.com` | Simple, sin configuración extra | Tu email personal queda expuesto públicamente |
| 2 | **Email noreply de GitHub** | `123456+tuusuario@users.noreply.github.com` | Protege tu email real, sigue vinculando commits a tu perfil | Debes actualizar `git config` para usarlo |
| 3 | **Bloquear push con email expuesto** | — | GitHub rechaza cualquier push que exponga tu email real | Más estricto, requiere tener bien configurado el email noreply antes de poder hacer push |

> 🔒 **Recomendación profesional:** usa el **email noreply de GitHub**. Es el estándar en proyectos open source y protege tu privacidad sin perder la vinculación con tu perfil.

**Para activarlo:**

1. En github.com/settings/emails activa **"Keep my email addresses private"**
1. GitHub te mostrará tu email noreply, algo como `123456+tuusuario@users.noreply.github.com`
1. Actualiza tu configuración local de Git:

powershell

`git config --global user.email "123456+tuusuario@users.noreply.github.com"`

Verifica:

powershell

`git config --global --list`