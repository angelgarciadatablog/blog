Git no tiene un "login" como tal, pero guarda tu identidad para firmar los commits. Ejecuta:

```bash
git config --global user.name
git config --global user.email
```

Esto nos dice con qué nombre y correo están firmados tus commits en este usuario. Pega el resultado y vemos si corresponde a tu cuenta de trabajo.



### **Una cosa importante sobre Git:**

Esta configuración es `--global`, lo que significa que aplica a todos los repositorios en este usuario. Si en algún proyecto específico necesitas usar otra cuenta (por ejemplo tu cuenta personal), se puede sobrescribir a nivel de repositorio con:

```bash
git config --local user.email "tu@otroemail.com"
```

*Se hace **una sola vez** dentro de la carpeta del repositorio, y a partir de ese momento todos los commits de ese repo usarán esa identidad.

```bash
# 1. Entras a la carpeta del repo
cd C:\Users\Lenovo\proyectos\mi-repo-personal

# 2. Configuras la identidad local (solo una vez)
git config --local user.email "tu@personal.com"
git config --local user.name "Tu Nombre"

# 3. A partir de aquí todos tus commits usan esa cuenta
git commit -m "mi commit"
```
```


El `--local` **no afecta commits pasados** — solo aplica a los commits futuros.
**Los commits pasados no se tocan** — quedan firmados con la identidad que tenían cuando se hicieron. Es simplemente la forma en que funciona Git, los commits son inmutables.


**¿Se puede cambiar la identidad de commits pasados?**

Técnicamente sí, con `git rebase` o `git filter-branch`, pero es una operación avanzada y riesgosa — especialmente si ya subiste esos commits a GitHub. No se recomienda salvo que sea realmente necesario.