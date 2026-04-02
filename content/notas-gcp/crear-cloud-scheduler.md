![](img/30f477bcd0eb809eaaa4e127146237c3.webp)

*De preferencia que la región coincida con la de la cloud funtion



![](img/30f477bcd0eb809bb522e52bd467c8bb.webp)

*Aquí se coloca la URL que generó la cloud funtion, usualmente esa URL no debería compartirse, en caso no tenga seguridad, pero en este caso si la tiene:





![](img/30f477bcd0eb8091a846c9940a842166.webp)

*Cero reintentos en este caso porque la función carga datos a big query y no queremos que tenga la posibilidad de cargar duplicados

*El plaso de intento es de 600s porque la cloud funtion tienen una duración de 540 segundos

*Como los reintentos son cero, todo lo que tenga que ver con retirada y duplicaciones no se aplica para este caso (se deja por defecto igual no afectará)