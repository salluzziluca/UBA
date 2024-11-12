---
aliases:
  - grafo
dg-publish: true
---

Es un par odenado $G=(V,E)$ donde V es el conjunto de vértices y E el conjunto de aristas
Dicho de otra forma, son vertices que se conectan mediante distintas aristas
Un vertice puede volver sobre si mismo (lazo), siempre y cuando esto tenga un costo o una penalizacion
![[Pasted image 20220614182834.png]]

## Tipos de grafos
![[Pasted image 20220621185749.png]]
![[Pasted image 20220621185947.png]]
![[Pasted image 20220621190901.png]]
### Grafo no dirigido
Todas sus aristas son bidireccionales, se pueden recorrer en cualquiera de las dos direcciones
Puedo ir de A a B y de B a A 
![[Pasted image 20220614184322.png]]

### Grafo dirigido
Al menos una de sus aristas es unidireccional. (puede haber aristas bidireccionales)
![[Pasted image 20220614184330.png]]
#### Handshaking Lemma
En todo grafo no dirigido, la cantidad de vertices con un grado impar, es par.

$Todos\ los\ grados = 2*aristas$
$grados_{pares} + grados_{impares} = 2 *aristas$. 2.aristas es par y  grados pares es sumatoria de cosas pares, entoces grados impares es par
### Grafo con peso
Todas sus aristas poseen un valor que implica un costo a la hora de tener que transitar de un vértice a otro

### Clasificación
podemos tener 
- Grafos dirigidos con peso
- Grafos dirigidos sin peso
- Grafos no dirigidos con peso
- Grafos no dirigidos sin peso

### Grafo simple
Es aquel que no posee aristas múltiples ni lazos. Es decir, para un par de vértices hay una sola arista.
![[Pasted image 20220614185043.png]]

### Grafo denso
Un grafo es denso cuando su numero de aristas esta muy cerca del valor maximo de aristas que puede tener
$$D = \frac {2 |E|}{|V| (|V|-1)}$$
Siendo E la cantidad de aritas y V la cantidad de vertices¿
Si D tiende a 0 tenemos un grado disperso (siendo 0 un grafo con cero aristas)
![[Pasted image 20220614185847.png]]


Si D tiende a 1 tenemos un grafo denso
![[Pasted image 20220614185833.png]]

### Grafo cíclico
Es un grafo en el que se pueden recorrer las aristas adyacentes empezando y terminando en el mismo lugar
![[Pasted image 20220614190442.png]]
derecha cíclico izquierda acíclico.

### Grafo bipartito 
Un grafo es bipartito si todos los ciclos son de longitud par
grafo bipartito <-> no tiene ciclos impares. Todos los nodos se pueden agrupan en dos grupos y no se conectan internamente entre grupos
![[Pasted image 20240823144255.png]]
### ![[Grafos Eulerianos]]

### ![[Grafos Hamiltonianos]]

### ![[Grafos Regulares]]

## Camino
Un recorrido a través de un grafo, CUALQUIERA. Pasando por sus vertices de toque

### Camino Simple 
Un camino, pero que pasa a lo sumo una vez por cada vértice

## Componente Conexa
Conjunto de vértices donde existe un camino de un vértice a otro (únicamente para  [[Grafos#Grafo no dirigido|grafos no dirigidos]]).

## Grado de entrada
Cantidad de aristas que entran al vértice (solo en [[Grafos#Grafo dirigido|grafos dirigidos]])

## Grado de salida 
Cantidad de aristas que salen del vértice(solo en [[Grafos#Grafo dirigido|grafos dirigidos]])

## Grado de vertice
En [[Grafos#Grafo no dirigido| grafos no dirigidos]] la cantidad de aristas que salen y entran al vertice (son las mismas).

## Utilización "default"
Son utiles para hacer mapas. En este caso, queremos pasar por la mayor cantidad de paradas desde el punto A al punto B
![[Pasted image 20220614183846.png]]

## Primitivas
##### Crear
##### Insertar
inserta un vertice
##### Insertar arista
##### Borrar
Borra un vértice
##### Borrar arista
##### Destruir

## Representaciones
### Matriz de adyacencia
![[Pasted image 20220614193225.png]]Para que sea simple todos los valores tienen que estar entre 0 y 1 menos la diagonal que tiene que ser siempre 0
En un [[Grafos#Grafo dirigido| grafo dirigido]] la matriz registra solo el vértice de inicio y el vértice final.
![[Pasted image 20220614193400.png]]
Si el grafo tiene [[Grafos#Grafo con peso| peso]] la matriz registra eso
![[Pasted image 20220614193516.png]]

### Lista de adyacencia 
Cada vertice contiene una lista simplemente enlazada
![[Pasted image 20220614194257.png]]

Con [[Grafos#Grafo dirigido| grafo dirigido]] respetamos las direcciones
![[Pasted image 20220614194514.png]]
Y si es un [[Grafos#Grafo con peso|grafo con peso]] guardamos el peso como un valor más
![[Pasted image 20220614194559.png]]
### Matriz de incidencia
Para esto necesitamos identificar las aristas
Si el grafo a representar es dirigido: se le asigna -1 al vértice de salida y 1 al vértice de entrada Esta matriz es Z , donde m es la cantidad de aristas y n es la cantidad de vértices. mxn 
Por cada arista identificamos que nodos inciden con él y lo marcamos en un grafo no dirigido con 1. 
Si el grafo fuera dirigido y con peso, en vez de utilizar el número 1 se utiliza el número del peso de cada arista.

![[Pasted image 20220614200158.png]]


Con [[Grafos#Grafo dirigido| grafo dirigido]] respetamos las direcciones
![[Pasted image 20220614200222.png]]

Y si es un  [[Grafos#Grafo dirigido| grafo dirigido]]  y un [[Grafos#Grafo con peso|grafo con peso]] guardamos combinamos ambas cosas
![[Pasted image 20220614200331.png]]

![ gRecorridos Grafos]]



## Puntos de articulación 
Vertices que si los saco aumento la cantidad de componentes conexas 