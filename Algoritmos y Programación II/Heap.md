> Es la estructura por defecto de los [[Algoritmos Greedy]]
# Heap binario

Es un tipo de [[Arboles#Arbol binario|árbol binario]]
Tiene una relación de tipo vertical. Los menores arribas y mayores abajo o viceversa
Es un árbol casi completo: Si sobran lugares, es porque todos menos el ultimo nivel estan completos, el ultimo tiene que estar lleno de izquierda a derecha, pueden faltar cualquier cantidad de elementos y tambien puede estar completo. 

## Heap maximal
En este los elementos mas grandes flotan y los mas chicos se hunden
![[Pasted image 20220523184217.png]]

## Heap minimal
En este los elementos mas chicos flotan y los mas grandes se hunden.
![[Pasted image 20220523184320.png]]

## Primitivas
### Insertar
Siempre se inserta por el final por la derecha abajo. Una vez que se inserta, el nodo que flote más va a tender a subir y a dejar a los demás abajo.  A esta comparación que hace que los elementos floten se la llama sift up
![[Pasted image 20220523184718.png]]
![[Pasted image 20220523184816.png]]

### Quitar
Se quita siempre por arriba, solo se puede eliminar la raíz. Luego, buscamos el último elemento y lo ponemos en la raíz, lo dejamos hundirse (sift down) hasta volver a balancear el heap
![[Pasted image 20220523185705.png]]
![[Pasted image 20220523185310.png]]
![[Pasted image 20220523185725.png]]

## Construcción de un heap
Se realizan n operaciones log(n) por lo que aproximadamente podemos decir que
==insertar elementos en un heap vacio uno a uno tiene complejidad algorítmica $O(n*log(n)$ ==
Para construirlo vamos asignando numeros a cada uno de los elementos segun el nivel
![[Pasted image 20220523190959.png]]

Esto también nos permite saber cuál va a ser el hijo izquierdo y derecho de cada nodo. 
Nodo actual = N
Hijo izquierdo = 2N + 1
Hijo derecho = 2N + 2
Y para saber los padres
Padre = $\LARGE \lfloor \frac {n-1}{2} \rfloor$ 

Para construir entonces un heap desde un array voy cargando los elementos haciendo los sift ups correspondientes.

Esto nos permite crear un algoritmo de ordenamiento llamado heap sort el cual nos permite pasarle un vector a heap y luego ir quitando las raices para obtenerlo ordenado