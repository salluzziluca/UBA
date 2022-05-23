	# AVL
Es un tipo de [[Arboles#Arbol binario|arbol binario]] autobalanceado, pensado para que no se degenere a lista y siempre la busqueda sea O(log(n)).

![[Pasted image 20220503183147.png]]

![[machete_rotaciones.jpg]]
## Factor de balanceo
Es un atributo que se le agrega a cada nodo, representa la diferencia de alturas entre su subarbol derecho y su subarbol izquierdo. Puede ser -1 0 1 (arbol izquierda mas largo, iguales, arbol derecha mas largo). 

Si esta desbalanceado, hay que hacer una rotacion 
### Rotación a derecha 
![[Pasted image 20220503183402.png]]

Pero si el 13 ya tiene dos hijos...
![[Pasted image 20220503183612.png]]

### Rotación izquierda
![[Pasted image 20220503184752.png]]

### Rotación izquierda + rotación derecha
![[Pasted image 20220523132627.png]]