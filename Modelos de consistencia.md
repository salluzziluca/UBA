En el estudio de la replicacion en la base de datos tirvuidoas se iutolizas dintnso modelos de consistnecias 

Uno de los modelos mas fuertes es el de consistencia secuencial.

Cuando yo actualizo un [[dato]], hasta que no se envia a todos los [[Nodo|nodos]] que tiene ese [[dato]], no digo que está ok


## Consistencia Secuencial 

>[!info] Se dice que una base de datos distribuida tiene consistencia secuencial cuando “el resultado de cualquier ejecución concurrente de los procesos es equivalente al de alguna ejecución secuencial en que las instrucciones de los procesos se ejecutan una después de otra

![[Pasted image 20241029202451.png]]

Por lo tanto esto tiene consistencia secuencial 

![[Pasted image 20241029202647.png]]

En este caso P1 esta leyendo un valor de a desactualizado 


## Consistencia Casual


Se busca capturar eventos que esten casualmente relacionados 
 Si el evento b fue influenciado por un evento a, la causalidad requieren que todos vean a antes que b.
Dos eventos no relacionados son concurrentes