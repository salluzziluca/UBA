# Recorridos Grafos

## Orden topológico
Buscar aristas con cero aristas adyacentes y recorrelo, asi obtenemos nuevos ![[Pasted image 20220621203109.png]]

## Algoritmo de Prim
Queremos pasar de un grafo pesado a un arbol con el minimo trabajo para la mayoria de los recorridos.
Partiendo desde un nodo, buscamos la arista con menor peso (mas chica) y vamos agregando al arbol nodos nuevos siempre yendo al nodo que este en la direccion de la arista mas chica posible.
Basicamente: agarro la mas corta y agrego. Buscamos la arista mas corta desde cualquier nodo, no el ultimo que agregamos
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

![[Pasted image 20220628190016.png]]
Aca tengo 13 grafos que no estan contectados. 
LA lista de aristas seria [1, 1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7 ,8, 9, 10, 11, etc]
Recorriendo la lista a ver si las diferentes aristas unen dos grafos distintos. Si lo hacen, los uno.
Empezaria uniendo 1 con 2, despues 9 con 10, 7 con 3 y asi...


## Floyd-Warshall
ENcuentra el camino minimo entre todos los pares. Es como aplicar [[Grafos#Dijkstra|Dijkstra]] a cada uno de los nodos
![[Pasted image 20220628193905.png]]

Para eso vamos a elegir un V_0. Comparamos los recorridos directos de un nodo a otro con el recorrido pasando por el V_0
![[Pasted image 20220628194151.png]]
![[Pasted image 20220628194207.png]]
Como ir de 4 a 2 es infinito ( no se puede llegar directamente) y ir de 4 a 1 a 2 es 10, reemplazamos el inf por el 10
![[Pasted image 20220628194219.png]]

Luego hacemos lo mismo cambiando de V_0
![[Pasted image 20220628194240.png]]
![[Pasted image 20220628194301.png]]

Volvemos cambiar de V_0
![[Pasted image 20220628194353.png]]
Y una ultima vez
![[Pasted image 20220628194402.png]]

