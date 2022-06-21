# Recorridos Grafos

## Orden topológico
Buscar aristas con cero aristas adyacentes y recorrelo, asi obtenemos nuevos ![[Pasted image 20220621203109.png]]

## Algoritmo de Prim
Queremos pasar de un grafo pesado a un arbol con el minimo trabajo para la mayoria de los recorridos.
Partiendo desde un nodo, buscamos vamos agregando al arbol nodos nuevos siempre yendo al nodo mas chico posible.
Basicamente: agarro la mas corta y agrego
![[Pasted image 20220621204526.png]]

Fijandonos siempre de no hacer un ciclo
![[Pasted image 20220621204550.png]]

FInalmente

![[Pasted image 20220621204627.png]]
![[Pasted image 20220621204635.png]]

## Agoritmo de kruskal
tenes n grafos
armas una lista de aristas de menor a mayor
ir arista por arista. concatenando los grafos que esa arista mira