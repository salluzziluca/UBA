---
dg-publish: true
---
# Recorridos [[Grafos]]
### En profundidad: DFS (Depth First Search)
En este caso se van a visitar los nodos hijos primero, avanzando hasta que no se pueda continuar. Luego se “vuelve” hasta un hijo donde se tenían más caminos, y se vuelve a realizar la misma lógica.

### En anchura: BFS (Breath First Search)
Se encara el recorrido del [[Grafos|grafo]] en anchura, es decir, primero visita nodos hermanos/vecinos antes de visitar nodos hijos. Para su implementación se utiliza una cola


## Dijkstra
Algoritmo dijkstra 1. 
Se elige el vértice V sobre el cual se quiera aplicar el algoritmo 
2. Se crean dos lista de nodos, una lista de nodos Visitados y otra listas de nodos NO Visitados, que contiene a todos los nodos del [[Grafos|grafo]].
3. Se crea una tabla con 3 columnas, Vértice, Distancia mínima V y el nodo anterior por el cual se llegó. 
4. Se toma el vértice V como vértice inicial y se calcula su distancia a sí mismo, que es 0. 
5. Se actualiza la tabla, en la cual todas las distancias de los demás vértices a V se marcan como infinito. 
6. Se visita el vértice NO VISITADO con menor distancia conocida desde el primer vértice V, que es el vértice con el que comenzamos ya que la distancia a ese es 0 y las demás infinito. 
7. Se calcula la distancia entre los vértices sumando los pesos de cada uno con la distancia de V. 
8. Si la distancia calculada de los vértices conocidos es menor a la que está en la tabla se actualiza y también los vértices desde donde se llegó.
9. Se pasa el vértice V a la lista de Vértices visitados. 
10. Se continua con el vértice no visitado con menor distancia desde ese. 
Y así sucesivamente...
![[Pasted image 20220614210430.png]]
![[Pasted image 20220614210441.png]]
De esta forma obtenemos la forma mas liviana de llegar a cada nodo. Se usa un [[Heap]]
## Orden topológico
Buscar aristas con cero aristas adyacentes y recorrelo, asi obtenemos nuevos ![[Pasted image 20220621203109.png]]

## Algoritmo de Prim
Crea un spanning tree. Una aproximacion general de los caminos mas cortos entre todos los nodos.

Queremos pasar de un [[Grafos|grafo]] pesado a un arbol con el minimo trabajo para la mayoria de los recorridos.
Partiendo desde un nodo, buscamos la arista con menor peso (mas chica) y vamos agregando al arbol nodos nuevos siempre yendo al nodo que este en la direccion de la arista mas chica posible.
Basicamente: agarro la mas corta y agrego. Buscamos la arista mas corta desde cualquier nodo, no el ultimo que agregamos
![[Pasted image 20220621204526.png]]

Fijandonos siempre de no hacer un ciclo
![[Pasted image 20220621204550.png]]

FInalmente

![[Pasted image 20220621204627.png]]
![[Pasted image 20220621204635.png]]

## Agoritmo de kruskal
tenes n [[Grafos]]
armas una lista de aristas de menor a mayor
ir arista por arista. concatenando los [[Grafos]] que esa arista mira
![[Pasted image 20250204131512.png]]


Recorriendo la lista a ver si las diferentes aristas unen dos [[Grafos]] distintos. Si lo hacen, los uno.

![[Pasted image 20250204131524.png]]
no h

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

