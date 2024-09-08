# Sorting
Son algoritmos para ordenar un conjunto de datos.

![[Pasted image 20220517184034.png]]
Caracteristicas
- Complejidad algoritmica
- Complejidad espacial
	Cuanta "memoria" necesita
- Inplace
	Si ordena los elemento en el lugar
- Estabilidad
	Es estable si preserva el orden relativo de los elementos
- Comparatividad
	Es comparativo cuando se comparan elementos entre si
- Adaptatividad
	Es adaptativo cuando se adapta al comun de datos
## Ordenamiento por Fuerza Bruta
Pruebo todas las combinaciones posibles. Primero lo agarro como está, si no queda ordenado permuto y el primero y el segundo. Si no funciona permuto el primero con el 3ro, si no esta premuto el 2do con el 3ro, y asi. Complejidad FACTORIAL
## Mergesort
Divide en dos 
va hacia la izquierda
Va hacia la derecha
mergea (ordenando)
![[Pasted image 20220524145516.png]]
![[Pasted image 20220524145524.png]]
![[Pasted image 20220524145536.png]]

### Complejidad algorítmica de mergesort
$$\LARGE O(n.log(n))$$
## Quicksort
1. Inicializo el pivote y su posición
2. Itero reubicando los mayores al pivote
3. Ubico al pivote en su posicion
4. Me llamo recursivamente a izquierda y luego a derecha
Pongo un pivote al final y una posicion pivote al inicio
![[Pasted image 20220517192919.png]]
Voy comparando el pivote con el punto pivote. Si es mayor (o menor, segun querramos), hago un swap. sabiendo que voy a necesitar una posicion extra para ese elemento cuando el vector se ordene.
![[Pasted image 20220517193051.png]]
Cada vez que encontramos un valor que cumple con la condición, lo swapeamos y adelantamos uno la posicion de pivote. Es decir, siempre detras de la posicion de pivote han de quedar numeros que cumplan con la condición.
![[Pasted image 20220517193240.png]]
![[Pasted image 20220517193224.png]]
 finalmente swapeamos la posicion pivote con el pivote y nos quedan de un lado valores que cumplen la condicion y del otro valores que no
 ![[Pasted image 20220517193539.png]]

asi, hacemos lo mismo con todas las sub-partes del vector
![[Pasted image 20220517193654.png]]
Siempre el pivote es el ultimo elemento y la posicion pivote el primero.
![[Pasted image 20220517193620.png]]

### Caracteristicas de quick sort
- Complejidad algorítmica
mejor caso $O(n.log(n))$
	O(n^2)
- Complejidad computacional
	n+k


## Counting sort
Creamos un Array de 0 a 9
Inicializamos todas las posiciones en 0
Itero incrementando según la posición
![[Pasted image 20220524153944.png]]
![[Pasted image 20220524154006.png]]
Al actual le sumo el anterior
![[Pasted image 20220524154039.png]]
Creamos un array en donde ordenar

finalmente 

![[Pasted image 20220524154254.png]]

## Complejidad algorítmica de counting sort 
$$\LARGE O(n)$$