

> Resumen

Tenemos un repo tanto en local como en github

1. En local hacemos un cambio en el archivo .html (agregamos un video)
1. En remoto (github) también hacemos un cambio en el archivo .html (agregamos una playlist)
1. Al momento de querer hacer `git push` no vamos a poder porque hay cambios en github remoto (playlist) que no lo tiene identificado el local.
1. Entonces debemos traer los cambios de remoto al local, o en otras palabras actualizar el repo local con los cambios que se tiene en remoto (github)
1. El comando que realiza eso es `git pull`, sin embargo, si solo colocamos `git pull`, se creará un commit más que hace referencia a que dos cambios se unieron: uno local (video) y remoto github (playlist). Ese commit de más puede causar confusión cuando se revise el historial de commits. En este contexto, dicho commit puede considerarse innecesario (no siempre), ya que el merge no aporta información clara sobre los cambios realizados, sino solo sobre la sincronización entre local y remoto.
1. Sin embargo, si utilizamos `git pull --rebase`, no se creará ese commit con el merge, solo se justarán ambos commits (el del video y el de la playlist) uno encima de otro, de manera que ambos al final Git toma los commits remotos y luego reaplica los commits locales encima, manteniendo sus mensajes originales y dejando un historial lineal.
1. En caso de que los cambios entren en conflicto (por ejemplo, en local agregamos un video y en remoto se eliminó ese mismo video), tanto `git pull` como `git pull --rebase` **detectarán el conflicto**, se detendrán y Git pedirá que el usuario lo resuelva manualmente eligiendo qué cambio prevalece o combinándolos.



> Explicación detallada

![](img/2e6477bcd0eb803b8b18d527aafd1316.webp)



![](img/2e6477bcd0eb805bb3f3c08a14f854e8.webp)



![](img/2e6477bcd0eb80619e75c855a4d883d1.webp)





> Si ha conflicto entre cambios sale lo siguiente:

![](img/2e6477bcd0eb8029bab9edd04c5e64b5.webp)



![](img/2e6477bcd0eb8004ac5bff5d8af41b14.webp)

![](img/2e6477bcd0eb80ff88c1d2185c670294.webp)







Elegir qué cambio prevalecerá:

![](img/2e6477bcd0eb80e48485f82a3214ba21.webp)

![](img/2e6477bcd0eb80c89f1cd4bffa42b58e.webp)

![](img/2e6477bcd0eb80fd8482fde3c2816bcb.webp)





![](img/2e6477bcd0eb809396d0cb72ab8233f5.webp)





---

![](img/2e6477bcd0eb80d3b367cc7cac7d3346.webp)