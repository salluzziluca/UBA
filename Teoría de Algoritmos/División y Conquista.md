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
	izq = mergesort(arr[:[medio])
```