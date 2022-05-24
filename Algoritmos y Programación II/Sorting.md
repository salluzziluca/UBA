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
## Merge sort
Divide en dos 
va hacia la izquierda
Va hacia la derecha
mergea (ordenando)
![[Pasted image 20220524145516.png]]
![[Pasted image 20220524145524.png]]
![[Pasted image 20220524145536.png]]

## Quick Sort
1. Inicializo el pivote y su posición
2. Itero reubicando los mayores al pivote
3. Ubico al pivote en su posicion
4. Me llamo recursivamente a izquierda y luego a derecha
Pongo un pivote al final y una posicion pivote al inicio
![[Pasted image 20220517192919.png]]
Voy comparando el pivote con el punto pivote. Si es mayor (o menor, segun querramos), hago un swap. sabiendo que voy a necesitar una posicion extra para ese elemento cuando el vector se ordene.
![[Pasted image 20220517193051.png]]
Cada vez que encontramos un valor que cumple con la condición, lo swapeamos
![[Pasted image 20220517193240.png]]
![[Pasted image 20220517193224.png]]
 De esta forma, vamos a adelantar la posicion pivote, nos quedara un vector ordenado con mayores y menores al pivote 
 ![[Pasted image 20220517193539.png]]

asi, hacemos lo mismo con todas las sub-partes del vector
![[Pasted image 20220517193654.png]]
Siempre el pivote es el ultimo elemento y la posicion pivote el primero.
![[Pasted image 20220517193620.png]]

### Caracteristicas de quick sort
- Complejidad algorítmica
	O(n)
- Complejidad computacional
	n+k