Es una técnica de diseño en la que:
1. dividimos el problema en subproblemas
2. Resolvemos cada subproblema recursivamente (porque conviene)
3. Combinamos la soluciones a cada subproblema

## Ejemplos de algoritmos
1. [[Busqueda#Binaria|Busqueda binaria]]
2. [[Sorting#Mergesort|mergesort]] y [[Sorting#Quick Sort|quicksort]]
3. Otros algoritmos de dificultad similar 
4. [[Arboles]] (incluyendo [[Heap|heaps]])

### ejemplo con mergesort 
```python
def mergesort(arr):
	if len(arr) <=1:
		return arr
	medio = len(arr)/2
	izq = mergesort(arr[:medio])
	der = mergesort (arr[medio:])
	return intercalar_ordenado(izq, der)
```
Utilizando el ![[Complejidad de Algoritmos#Teorema maestro|teorema maestro]]
Obtenemos para el mergesort: $T(n)=2T (\frac{n}{2}) +O(n))$. Esto, con mucha matematica de por medio, nos da que la [[Complejidad de Algoritmos|complejidad algoritmica]] del mergesort es $O(n\ log(n))$.

En casos particulares podriamos necesitar usar el [[Teorema Maestro general]]


## Problema 1:  multiplicacion de números muy grandes
- Escribimos la mutiplicacion como si estuvieramos laburando en base 2 ([[1.3 Binario|binario]]), y separamos la primera y 