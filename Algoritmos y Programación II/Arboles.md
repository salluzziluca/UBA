# Arbol
Coleccion de nodos conectados con multiples nodos. El nodo principal es llamado r (raiz) y los subarboles T1, T2, T3, cada uno de ellos con su raiz conectada mediante un vertice al nodo raiz.
![[Pasted image 20220426182647.png]]

Un nodo no puede tener dos padres. 
Los nodos se dividen por niveles (1ero, 2do, 3ero, etc)
![[Pasted image 20220426183242.png]]

Un nodo puede tener padre y puede tener hijos. El nodo raiz no tiene padres. Los nodos hoja no tienen hijos. En este grafico hay 7 nodos hoja.
Las hojas nos ayudan a ver cuando llegamos al final de una rama

## Arbol binario
> Es un arbol en el que cada padre tiene dos hijos como maximo. 

## Preorden (preorder)
Sirve para hacer una copia fiel del arbol
>Primero se visita el nodo actual, luego el subarbol izq, luego el derecho.
![[Pasted image 20220426190605.png]]
	recorrido A-B-D-H-I-E-C-F-G-J
	![[Pasted image 20220426192343.png]]

## Inorder
Arbol ordenado de menor a mayor
>Primero se visita el subarbol izquierdo, luego el nodo actual, luego el subarbol derecho
>![[Pasted image 20220426192143.png]]
>Recorrido: H-D-I-B-E-A-F-C-J-G

## Postorder
Nos da el borrado de un arbol. Borra de las hojas para atras. 
Primero se visita el subarbol izquierdo, luego el subarbol derecho, luego el nodo actual


## Arboles de busqueda binario

![[Pasted image 20220426194116.png]]

### Busqueda 
 Comparamos el buscado con la raiz, si es igual, listo. Si es menor que la raiz, vamos a la izquierda, si es mayor, vamos al subarbol derecho. Asi hasta encontrar (o no), el arbol
### Inserccion
![[Pasted image 20220426195452.png]]
Comparo el numero a insertar con la raiz. Si es menor que la raiz, vamos a la izquierda, si es mayor, vamos al subarbol derecho. Repetimos hasta encontrar un elemento igual al que queremos insertar o llegar al fin de un subarbol. 
Al llegar al final, creamos un nuevo nodo


==EL TP NO ES EXACTAMENTE IGUAL; PERO BUENO==
![[Pasted image 20220503205215.png]]
![[Pasted image 20220503205613.png]]