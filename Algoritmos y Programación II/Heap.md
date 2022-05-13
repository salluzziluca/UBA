# Heap binario
Es un tipo de [[Arboles#Arbol binario|arbol binario]]
Tiene una relacion de tipo vertical. Los menores arribas y mayores abajo o viceversa
Es un arbol casi completo: Si sobran lugares, es porque todos menos el ultimo nivel estan completos, el ultimo tiene que estar lleno de izquierda a derecha, pueden faltar cualquier cantidad de elementos y tambien puede estar completo. 

## Heap maximal
![[Pasted image 20220510182114.png]]

## Heap minimal
![[Pasted image 20220510182145.png]]

## Primitivas
### Insertar
Siempre se inserta por el final por la derecha abajo. Una vez que se inserta, el nodo que flote mas va a tender a subir y a dejar a los demas abajo-
![[Pasted image 20220510184707.png]]
![[Pasted image 20220510184725.png]]

### Quitar
Se quita siempre por arriba. Luego empiezan a flotar los demas elementos. 
![[Pasted image 20220510184743.png]]
![[Pasted image 20220510184754.png]]