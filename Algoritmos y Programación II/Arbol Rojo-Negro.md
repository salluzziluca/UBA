---
dg-publish: true
---
# Arbol Rojo-Negro
Es un [[Arboles#Arbol binario|arbol binario]] en cuyos nodos, ademas de almacenar su elemento y sus hijos, se almacena su color, para tenerlo balanceado de una forma mas eficiente

## Reglas
- La raiz siempre tiene que ser negra
- Los nodos rojos siempre tienen hijos negros
- Las hojas siempre son negras y no almacenan datos (nos referimos a los punteros a nulls)
- todos los caminos desde un nodo hacia las hojas pasan por la misma cantidad de nodos negros. A esa cantidad de nodos se la llama altura negra.
![[Arbol Rojo Negro]]
Altura negra de este arbol: 2

## Inserción $O(log(n))$ 
Se insertan siempre nodos rojos y luego se rebalancea.
![[Pasted image 20220523142008.png]]

---
![[Pasted image 20220523142239.png]]

[[machete_arbol_rojo_negro.pdf]]