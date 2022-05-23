# Arbol B
Es un tipo de [[Arboles|arbol n-ario]]. Que se caracteriza por expandirse a lo ancho en vez de a lo largo.
k = claves
m = cantidad maxima de descendientes = k +1
⌊k/2⌋ = cantidad minima de claves
⌈m/2⌉ = cantidad máxima de claves
 ## Caracterísiticas de arbol B
 - Poca profundidad
 - Acceso poco costoso
 - Claves ordenadas
 - Siempre insertamos en nodos hoja

## Insercion
Primero se busca llenar el nodo actual, una vez que este tiene todas sus claves llenas, al intentar insertar otro no vamos a poder (overflow), vamos a tener que partir en dos el nodo y subdividir.
![[Pasted image 20220523145314.png]]
Si queremos insertar el 8 aca, se puede, movemos todo a la derecha y lo ponemos primero
![[Pasted image 20220523145350.png]]
Si queremos insertar el 2 aca, ya no podemos, no hay mas espacio. Entonces el 20 sube y las otras dos partes del nodo bajan

![[Pasted image 20220523145439.png]]

![[Pasted image 20220523145522.png]]

Si ahora queremos insertar el 19, de vuelta no podemos. Por lo que, igual que la vez anterior, sube el 12 y las otras dos partes del nodo bajan.

![[Pasted image 20220523145617.png]]

## Eliminación