

```bash
#Verificar si esta instalado GIT en el ordenador

git --version
```

git version 2.39.5 (Apple Git-154)





```bash
#Revisar los archivos de la carpeta actual
ls 

#Entrar a la carpeta de documentos
cd documents

#Crear una carpeta llamada "repositorios" dentro de documentos
mkdir repositorios


```



```bash
#Entrar a la carpeta repositorios
cd repositorios

#Revisar si los archivos ocultos dentro de una carpeta para ver si es un repositorio
ls -a
```





```bash
# Inciar un control de versiones con git
git init
```

Initialized empty Git repository in /Users/datablog/Documents/repositorios/.git/





```bash
#Renombra la rama actual (la que acabas de crear) como main
git branch -m main
```







Opcional: Crear una carpeta si el repositorio está vacío

```bash
#Crear una archivo readme de tipo .md
touch README.md

#Revisa que se haya creado
ls
```

*Hasta el momento tenemos un directorio creado en local con un archivo readme.md dentro. A la vez se ha iniciado el control de versiones por lo que podemos utilizar comandos git para versionar los cambios que se hagan dentro del directorio.

