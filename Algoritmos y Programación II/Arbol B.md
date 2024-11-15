---
dg-publish: true
---
# Arbol B
Es un tipo de [[Arboles|arbol n-ario]]. Que se caracteriza por expandirse a lo ancho en vez de a lo largo.
k = claves
m = cantidad maxima de descendientes = k +1
⌊k/2⌋ = cantidad minima de claves
⌈m/2⌉ = cantidad minima de descendientes
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
Cuando borramos elementos, tenemos que verificar que el nodo no tenga un underflow, es decir, que tenga menos claves que la mínima (⌊k/2⌋).

![[Pasted image 20220523152923.png]] 
Al borrar el 19, vamos a tener en ese nodo solo una clave, por lo que hay que redistribuir:
Para esto podemos usar dos convenciones:
- subo clave más chica del hermano derecho y bajo el padre que separa ambos
- subo clave mas grande del hermano izquierdo y bajo el padre que separa ambos
En este ejemplo usaremos la primera

![[Pasted image 20220523153001.png]]


Si ahora queremos borrar el 20
![[Pasted image 20220523153209.png]]
No podemos redistribuir porque nos quedaria el nodo hermano derecho tambien con cantidad de claves menor a la minima. Tenemos entonces que concatenar.
"Uno al nodo afectado con algún hermano y el padre que separa ambos"
![[Pasted image 20220523153310.png]]

[[machete_arbol_b.pdf]]


## Arbol B+

Los árboles B+ tienen ciertas reglas de actualización que les dan propiedades buenas para ser usados como índices
Salvo el nodo raíz, todos los nodos se encuentran con al menos un 50% de ocupación
Todos los nodos hoja tienen la misma altura
Operaciones de ABM intentan reorganizar lo menos posible los nodos del árbol