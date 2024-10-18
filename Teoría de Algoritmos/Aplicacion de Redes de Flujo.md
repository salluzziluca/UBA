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