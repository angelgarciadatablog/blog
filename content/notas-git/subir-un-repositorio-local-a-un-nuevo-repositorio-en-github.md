

```bash
##revisar los cambios que se han hecho en el repositorio local
git status

#Guardar los cambios
git add .

#Revisar lo que se va a guardar en el historial
git status

#Realizar el primer commit para guardar en el historial
git commit -m "este es un primero commit que se guardará según los cambios hechos"

#"cuando se crea un primer commit, se creará automáticamente una rama llamada main". 
#Pero hasta que no haya ese primer commit, la rama no existe de verdad
#Para verificar que se creo la rama ejecutar el siguiente comando
git branch
```





Conectar el repositorio local con un repositorio remoto ya credo en github

```bash
#conectar al repositorio remoto
git remote add origin https://github.com/angelgarciadatablog/angel-notebooks.git

#verificar la conexión
git remote -v

#hacer el push de lo que está en local hacia lo remoto
git push origin main
```

*Esa ruta se utiliza siempre y cuando estes autenticado vía https





Si es primera vez que te harás un push te pedirá identificarte:

Esta identificación solo se añade al usuario actual del ordenador

```bash
# Configurar nombre (usa tu nombre real o de GitHub)
git config --global user.name "Angel García"

# Configurar email (usa el mismo email de tu cuenta GitHub)
git config --global user.email "tu-email@gmail.com"

# Verificar que se guardó
git config --global user.name
git config --global user.email
```





El primer push pedirá autenticación con la cuenta de GitHub

```bash
#hacer el push de lo que está en local hacia lo remoto
git push origin main
```



![](img/2a8477bcd0eb8091b12cf2d96a0dc992.webp)



![](img/2a8477bcd0eb80dbaf92d0956fa45b61.webp)