Uso las [[Redes de Flujo]] como si fueran una tecnica de disenioo



## Para [[Grafos#Grafo bipartito|grafos bipartitos]]
![[Pasted image 20241018135627.png]]
Y le ponemos a cada vertice peso 1, de esa forma se puede usar una sola vez cada vertice


## Disjoint paths
**Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos).**
![[Pasted image 20241018135834.png]]


Un camino podria ser 0 1 2 6 5 7 y otro 0 2 3 6 7


# Circulacion con demandas
Supongamos que tenemos varias "fuentes" con un suministro, y "sumideros" con una demanda. Ahora cada nodo tiene una demanda (positiva, negativa o 0). 

Nuevas condiciones: 
1. Condición de capacidad: 0 <= f(e) <= Ce
2. Condición de demanda: fin(v) - fout(v) = dv

## EJ: biblioteca 
Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. 



1. Creamos super fuente y super sumidero.
2. Para los sumideros, agregamos una arista de t a t* con capacidad = demanda. 
3. Para las fuentes, agregamos una arista de s* a s con capacidad = suministro.


![[Pasted image 20241018142506.png]]


## Cotas minimas
Ahora para cada arista, además de tener una capacidad tenemos una cota inferior que debe cumplirse, y cada nodo puede tener una demanda. 

Nuevas condiciones:
Condición de capacidad: Le <= f(e) <= Ce
Condición de demanda: fin(v) - fout(v) = dv

Lo que hacemos entonces es definir un flujo que cumpla las capacidades (incluyendo cotas)

Y creamos un grafo nuevo con capacidad = C_v - consumido (excepto que la demanda se cumpla, en cuyo caso no ponemos ni el vertice y ni las artias)

![[Pasted image 20241018201047.png]]

En este caso yo tengo 8 y 5 de capacidad. Me piden que de minima pase 3 por lo que creo un grafo con capacidad = C_v (8 y 5) -3



### Ej: aviones
Podemos decir que podemos usar un avión para un segmento/vuelo i y luego para otro j si: 
1. El destino de i y el origen de j son el mismo. 
2. Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente. 
Decimos que el vuelo j es alcanzable desde el vuelo i si es posible usar el avión del vuelo i y después para el vuelo j. 
Problema: ¿Podemos cumplir con los m vuelos usando a lo sumo k aviones?

![[Pasted image 20241018203451.png]]**1. Nuestras unidades de flujo son literalmente los aviones.
    
1. Ponemos las aristas de los vuelos que queremos si o si cumplir con cota mínima y capacidad = 1 (para forzar que se usen). 
    
2. Si otro vuelo es alcanzable por las reglas anteriores, ponemos otra arista de capacidad 1. 
    
3. Ponemos una fuente con aristas de capacidad 1 a los orígenes. 
    
4. Ponemos un sumidero con aristas de capacidad 1 desde los destinos.
    
5. Se une fuente y sumidero con capacidad K
    
6. La fuente tiene demanda -K y el sumidero K.**


## Project selection