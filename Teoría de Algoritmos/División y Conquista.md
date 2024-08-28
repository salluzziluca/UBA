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

```

## Problema 2: obtener extremo de un poligono
Tiene que ser convexo.Para que no tenga maximos locales y poder descartar partes. Para todo segmento L el poligono tiene que ser monotionico. Que lo corte mas de 2 veces. Equivalente a los angulos anterioes <= 180 grad 

![[Pasted image 20240827122108.png]]
En este caso busco el punto mas alto con respecto al eje y. Agarro dos vertices y los comparo. Si A crece y C crece y ademas C está mas alto que A(caso del dibujo, entonces) el punto mas alto va a estar entre c y b 

Reorganizo los puntos
![[Pasted image 20240828094615.png]]
Ahora A esta bajando y C está bajando. Con C por debajo de A, entonces el punto mas alto esta entre A y C


### Algoritmo

Empezamos con A y B = 0, C = n/2

Si tenemos 2 vertices, comparamos a mano 
aplicamos logica de partir. 
Nos quedamos con una mitad y comparo de vuelta, simil [[Busqueda#Binaria|busqueda binaria]]. O(logn)


## Problema 3: Busco puntos mas cercanos en 2 dim
Dado n puntos en un plano, buscar la pareja que se encuentre más cercana. 
Si comparo todo es O(n^2)

En una dimension-> ordenamos (O(n logn)) y despues comparamos cad elemento con sus adyacentes (O(n))

En 2 dim se complica, pero podemos usar nociones de [[Sorting#Mergesort|mergesort]]. Buscamos la pareja mas cercana mas cercana del lado izq y otra del lado derecho y en tiempo lineal buscamos los mas cercanos
1. Pongo un x de corte y obtengo las dos mitades Q y R
2. obtengo Q_x Q_y R_x R_y 
3. llamo recursivamente a las dos mitades y me devuelve el mejor candidato
4. Ya se al distancia menor, agarro los puntes que esten a esa distancia "d" de la x de corte y comparo los 15 siguientes que se encuentren en esos puntos. 
$$T(n)=2T\left( \frac{n}{2} \right)+O_{(n)}$$

### algoritmo
```python
def closest_pairs_rec(px, py):
	if len(px) <= 3: return el mínimo de comparar cada punto
	#Construir Qx, Qy, Rx, Ry (O(n))
	q0, q1 = closest_pairs_rec(Qx, Qy)
r0, r1 = closest_pairs_rec(Rx, Ry)
d = min(dist(q0, q1), dist(r0, r1))
x* = máxima coordenada x de Qx
S = puntos de P que están a distancia <= d de la recta x = x*
Construir Sy (O(n))
por cada punto s de Sy computar distancia contra los siguientes 15 puntos
	quedarse con s y s' que minimizan esa distancia
	if dist(s, s') < d: return s, s'
	elif dist(q0, q1) < dist(r0, r1): return q0, q1
	else: return r0, r1

```

## Problema 4: Mutiplicacion de matrices
El algoritmo sencillo es O(n^3)
Si divido las matrices en n/2xn/2 terminamos con 8 llamados recursivos e igual nos da O(n^{2,8})
### Algoritmo de Strassen
En vez de 8 llamados recursivos hacemos 7
$$T(n)= 7\left( T\left( \frac{n}{2} \right) \right)+O(1)\to T(n)=O(n^{\log_{2}7}) \approx O(n^{2,8})$$

## Problema 5: FTT- Transformada rapida de Fourier

Tenemos dos vectores A y B y queremos obtener la covolucion entre ambos

Se puede llegar de O(n^2) a O(n logn)

## Problema 6: Conteo de inversiones 
Tengo un conjunto de b elementos '2 rreglos/listas ordenados por diferentes criterios (A y B)
Quiero dar una semejanza endre dichas listas