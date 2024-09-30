 Nos da un metodo preciso con contados pasos para obtener las raices, pero eso está pensando para algebra de precision infinita en donde no nos importa el error de redondeo. Incluso puede pasar que el error de redondeo en sistemas mal condicionados sea tan grande que nos arruine 

### Sistemas equivalentes
Dos sistemas equivalentes cuando comparten al solucion. Puedo aplicar tranasformaciones a un sistema de ecuaciones que me devuelva uno siempre equivalente 

### Matrices triangulares
Transformar un sistema para convertirno en una matriz triangular superior U. 
Pasamos de Ax=b a Ux= y. Es mucho mas facil sacar la solucion en Ux= y que en Ax=b

![[Pasted image 20240930095151.png]]

tengo entonces esta matriz:
![[Pasted image 20240930100154.png]]
Quiero hacer cero las demas filas. Llevo a cabo este proceso
![[Pasted image 20240930100219.png]]
Ahi se ve que a todas las filas las divido por a11. Ese es el pivote

#### Pivotear: 
Intercambiar filas para tener pivote no nulo. 


## Factorizacion LU
![[Pasted image 20240930102423.png]]
## Errores en SEL directos 
![[Pasted image 20240930103854.png]]


## Wilkinson 
![[Pasted image 20240930104445.png]]


## Refinamiento Iterativo