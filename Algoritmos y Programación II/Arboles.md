# Arbol
Coleccion de nodos conectados con multiples nodos. El nodo principal es llamado r (raiz) y los subarboles T1, T2, T3, cada uno de ellos con su raiz conectada mediante un vertice al nodo raiz.
![[Pasted image 20220426182647.png]]

Un nodo no puede tener dos padres. 
Los nodos se dividen por niveles (1ero, 2do, 3ero, etc)
![[Pasted image 20220426183242.png]]

Un nodo puede tener padre y puede tener hijos. El nodo raiz no tiene padres. Los nodos hoja no tienen hijos. En este grafico hay 7 nodos hoja.
Las hojas nos ayudan a ver cuando llegamos al final de una rama

## Arbol binario

## Preorden (preorder)
>Primero se visita el nodo actual, luego el subarbol izq, luego el derecho.
![[Pasted image 20220426190605.png]]
	recorrido A-B-D-H-I-E-C-F-G-J

## Inorder
>Primero se visita el subarbol izquierdo, luego el nodo actual, luego el subarbol derecho