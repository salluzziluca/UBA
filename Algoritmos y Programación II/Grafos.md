Es un par odenado $G=(V,E)$ donde V es el conjunto de vértices y E el conjunto de aristas
Dicho de otra forma, son vertices que se conectan mediante distintas aristas
Un vertice puede volver sobre si mismo (lazo), siempre y cuando esto tenga un costo o una penalizacion
![[Pasted image 20220614182834.png]]

## Tipos de grafos

### Grafo no dirigido
Todas sus aristas son bidireccionales, se pueden recorrer en cualquiera de las dos direcciones
Puedo ir de A a B y de B a A 
![[Pasted image 20220614184322.png]]

### Grafo dirigido
Al menos una de sus aristas es unidireccional. (puede haber aristas bidireccionales)
![[Pasted image 20220614184330.png]]


### Grafo con peso
Todas sus aristas poseen un valor que implica un costo a la hora de tener que transitar de un vertice a otro

### Clasificacion
podemos tener 
- Grafos dirigidos con peso
- Grafos dirigidos sin peso
- Grafos no dirigidos con peso
- Grafos no dirigidos sin peso

### Grafo simple
Es aquel que no posee aristas multiples ni lazos
![[Pasted image 20220614185043.png]]
## Utilización "default"
Son utiles para hacer mapas. En este caso, queremos pasar por la mayor cantidad de paradas desde el punto A al punto B
![[Pasted image 20220614183846.png]]