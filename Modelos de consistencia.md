En el estudio de la replicacion en la base de datos distribuidos se utilizan distintos modelos de consistencia 

Uno de los modelos mas fuertes es el de consistencia secuencial.



## Consistencia Secuencial 

>[!info] Se dice que una base de datos distribuida tiene consistencia secuencial cuando “el resultado de cualquier ejecución concurrente de los procesos es equivalente al de alguna ejecución secuencial en que las instrucciones de los procesos se ejecutan una después de otra
Cuando yo actualizo un [[dato]], hasta que no se envia a todos los [[Nodo|nodos]] que tiene ese [[dato]], no digo que está ok

![[Pasted image 20241029202451.png]]

Por lo tanto esto tiene consistencia secuencial 

![[Pasted image 20241029202647.png]]

En este caso P1 esta leyendo un valor de a desactualizado 


## Consistencia Casual


Se busca capturar eventos que esten casualmente relacionados 
Si el evento b fue influenciado por un evento a, la causalidad requieren que todos vean a antes que b.
Dos eventos no relacionados son concurrentes.

![[Pasted image 20241029204326.png]]

Aca no hay escrituras causales. Son todas concurrentes.

inicial a= 5, b= 7
![[Pasted image 20241029204837.png]]

Aca p2 lee 20, por lo que tiene que ir primero p1. El problema es que p2 si o si escribe b=3, pero p3 quiere leer b=3 y a=5. Esta ejecucion no tiene consistencia casual.



## consistencia eventual 
>[!info] si en el sistema no se producen modificaciones (escrituras) por un tiempo suficientemente grande, entonces eventualmente todos los procesos verán los mismos valores

Esto es debido a que en la mayoría de sistemas reales son pocos los procesos que realizan modificaciones mientras que la mayoria lee

El tema es que tenemos varios estados de una misma BDD, hasta que se llega a propagar todo.

Es por esto que se definen dos parámetros 
Quorum de escritura: 
Recién digo que la estructura esta okay cuando W-1 nodos del listado de preferencia registraron la escriturara 

Quorum de lectura: Te devuelve el dato luego de que R nodos distintos (incluido el mismo) confirman la lectura
![[Pasted image 20241029210023.png]]


Para mantener sincronizadas las réplicas, Dynamo utiliza una estructura llamada Merkle tree que consiste en un árbol en que cada nodo no-hoja es un hash criptográfico de los valores de sus hijos.