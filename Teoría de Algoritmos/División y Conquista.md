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
Utilizando el ![[Teorema maestro|teorema maestro]]
Obtenemos para el mergesort: $T(n)=2T (\frac{n}{2}) +O(n))$. Esto, con mucha matematica de por medio, nos da que la [[Complejidad de Algoritmos|complejidad algoritmica]] del mergesort es $O(n\ log(n))$.

En casos particulares podriamos necesitar usar el [[Teorema Maestro general]]


## Problema 1:  multiplicacion de números muy grandes
- Escribimos la mutiplicacion como si estuvieramos laburando en base 2 ([[1.3 Binario|binario]]), y separamos la primera y la segunda mitad. Lo hacemos en binario porque es mas rapido para la compu$x = x_1 *2^\left( \frac{n}{2} \right)+x_{0}$
 Obtener la mitad 0 es hacer un & contra $2^\left( \frac{n}{2} \right)-1$. La mitad 1 es hacer n/2 shift rights
- x= abcdefgh. x_0=efgh. x_1=abcd
- entonces $y.x=(x_{1}.2^\left( \frac{n}{2} \right)+x_{0})(y_{1}.2^\left( \frac{n}{2} \right)+y_{0}))$
- $x_{1}y_{1}.2^n+(x_{1}y_{0}+x_{0}y_{1})2^\left( \frac{n}{2} \right)+x_{0}y_{0}$
- Entonces tenemos $T(n)4T\left( \frac{n}{2} \right)+O(n)\to O(n²)$. Es complicado y no mejora nada. Felicitaciones crack
Peero si en vez de tener 4 llamados recurisvimos tuvieramos 3....

```python
def mutiplicacionBigInt(x,y):
	# si largo de x e y son pequeños, devolvemos x*y. sino:
	x= x_1 2^(n/2)+x_0
	y= y_1 2(n/2)+y_0
	p = multiplicacionBigInt(x_1+x_0, y_1+y_0)
	x_0,y_0=mutiplicacionBigInt(x_0, y_0)
	x_1,y_1= mutiplicacionBigInt(x_1, y_1)
	return x_1 y_1 2^n + (p-x_1 y-1 -x_0 y_0) 2^(n/2) + x_0 y_0
