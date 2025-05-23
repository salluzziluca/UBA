 Una gran herramienta pra casos donde no podes recurria a otras tecnicas de diseño como pueden ser [[División y Conquista]], [[Algoritmos Greedy]] y [[Backtracking]]

## Ej 1: Fibonacci


```python
def fib(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   return fib(n-1) + fib(n-2)
```
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcpCfCDcdNPXcizzv3wngnML3pat4eypPJj8VozEhuZjQkLPIgaFQuwGrr2SrgXgemxwLYPtqJjos2CzY2t3cz-04num6NSDSchX9p5WlGJvQV4DxPH-ylE_PfH6hIF-mrUJrZAslcHmvx-2WCFGLSOdxmNH7AD=s2048?key=KeLfOlkR0vvPVvGZperQGQ)
Esta funcion es bastante chota O(2^n) porque hace muchos recalculos. Para un fib de 5 calcula 4 veces el fib de 1.


PROGRAMACION DINAMICA ODIA LOS RECALCULOS.

Agrego arreglos y voy guardando los fibonacci y acalculados

```python 
def fib_memorioso(n):
   M_FIB = [None] * (n+1)
   return fib_rec_memorioso(n, M_FIB)

def fib_rec_memorioso(n, M_FIB):
   if n == 0:
       return 0
   if n == 1:
       return 1
   if M_FIB[n-1] == None:
       M_FIB[n-1] = fib_rec_memorioso(n-1, M_FIB)
   if M_FIB[n-2] == None:
       M_FIB[n-2] = fib_rec_memorioso(n-2, M_FIB)
   M_FIB[n] = M_FIB[n-1] + M_FIB[n-2]
   return M_FIB[n]

o, mas simple

def fib_iterativo(n):
   M_FIB = [None] * (n+1)
   M_FIB[0] = 0
   M_FIB[1] = 1
   for i in range(2, n+1):
       M_FIB[i] = M_FIB[i-1] + M_FIB[i-2]
   return M_FIB[n]
```

Ambas son O(n)!!! 

Pasa que igual no necesito todos los elementos, solo los dos anteriores

```python 
def fib_dinamico(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   anterior = 0
   actual = 1
   for i in range(1, n):
       nuevo = actual + anterior
       anterior = actual
       actual = nuevo
   return actual
```

La version anterior gastaba lineal, esta gasta constante


### Memoization o Memorización
La técnica de guardar los resultados previamente calculados se llama Memoization
En este caso nos permitió pasar de un tiempo de ejecución exponencial a uno polinomial (particularmente, proporcional al número de Fibonacci a calcular)


### Por que preferimos la version iterativa (bottom up) a la recursiva (top down)?

1. Es mas facil de entender que pasa y cuando
2. Es mucho mas facil calcular la complejidad. Es mas obvia
3. Suelen ser mas faciles de resolver de forma inductiva que recursiva 
4. Es mas facil cometer errores o pensarlo rebuscadamente en la version recursiva 
5. Nos estrectura mucho mas como pensar la solucion -> primero la ecuacion de recurrencia, edspues progrmar
6. Se pueden aplicar optimizaciones de memoria fácilmente.

# Solucion por Programación Dinámica 
- Se basa en la idea de [[#Memoization o Memorización|Memoization]]
- Construye iterativamente las soluciones a los subproblemas hasta llegar a la solution del programable original
- Asumo todo lo anteriormente calculado para calcular el actual. De lo pequeño a lo grande
- Establecemos una lógica inductiva: "Si yo puedo asumir que ya tengo calculados todas las soluciones anteriores (casos más pequeños), ¿cómo puedo usarlos para construir la que necesito?" 


## Ej2: Scheduling por peso
Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin, y un peso asociado al valor de cada charla. Quiero utilizar el aula para maximizar la sumatoria de pesos de las charlas dadas. 

Lo que hacemos es un arreglo p(charla) que nos da cual es la primera charla que no se superpone con la actual
![[Pasted image 20240918104728.png]]
- Nos quedamos con la suposicion de que sabemos las soluciones a sub-problemas (mas pequeños). Llamemosle OPT
- La ultima charla en particular puede o no pertenecer a al solucion.
- Si no damos esa charla, entonces el problema más pequeño puede excluir esta charla
- Si damos esa charla, entonces el problema más pequeño debe excluir todas las charlas que terminen después del comienzo de esta charla
- De estas dos opciones deberíamos siempre seleccionar aquella que maximice la sumatoria de los pesos

Entonces 
![[Pasted image 20240918105613.png]]
El optimo es el maximo entre dar la charla -> su peso mas el optimo de la charla p(j) (la que se puede agenda teniendo en cuenta la actual) y no darla (buscar el opt de j-1). Es una ecuación de recurrencia!!

```python 
def sche_recursivo(inicio, fin, valor, p, j):
   if j == 0:
       return 0
   return max(valor[j] + sche_recursivo(inicio, fin, valor, p, p[j]),
              sche_recursivo(inicio, fin, valor, p, j-1))
```

Version memorioza 
```python 
def sche_memorioso(inicio, fin, valor, p, j):
   M_CHE = [None] * j
   return sche_rec_memorioso(inicio, fin, valor, p, j, M_CHE)

def sche_rec_memorioso(inicio, fin, valor, p, j, M_CHE):
   if j == 0:
       return 0
   if M_CHE[j-1] == None:
       M_CHE[n-1] = sche_rec_memorioso(inicio, fin, valor, p, j-1, M_CHE)
   if M_CHE[p[j]] == None:
       M_CHE[n-2] = sche_rec_memorioso(inicio, fin, valor, p, p[j], M_CHE)
   return max(valor[j]+M_CHE[p[j]], M_CHE[j-1])
```

Ahora si, la version dinamica

```python 
def sche_dinamico(n, p, valor):
   if n == 0:
       return 0
   M_SCHE = [0] * (n + 1)
   M_SCHE[0] = 0
   for j in range (1, n + 1):
       M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j-1])
   return M_SCHE[n]
```

Esto nos da el peso maximo en O(n). Es buenisimo pero todavia no nos sirve 


Ahora si, devuelve la solucion 
```python 
def sche_solucion(M_SCHE, valor, p, j, solucion):
   if j == 0:
       return solucion
   if valor[j]+M_SCHE[p[j]] >= M_SCHE[j-1]:
       solucion.append(j)
       return sche_solucion(M_SCHE, valor, p, p[j], solucion)
   else:
       return sche_solucion(M_SCHE, valor, p, j-1, solucion)

```


Iterativo 
```python
def sche_solucion_iterativo(M_SCHE, valor, p):
    n = len(M_SCHE)  # Número de intervalos
    solucion = []
    j = n - 1  # Empezamos desde el último intervalo

    while j > 0:
        if valor[j] + M_SCHE[p[j]] >= M_SCHE[j-1]:
            solucion.append(j)  # Incluimos el intervalo j en la solución
            j = p[j]  # Saltamos al intervalo no conflictivo más cercano
        else:
            j -= 1  # Pasamos al intervalo anterior

    solucion.reverse()  # Invertimos la solución para que esté en orden ascendente
    return solucion
```



# ABC DE LA PRORGAMCAICCSIDOID INAMICAAA
- Exploración implícita del espacio de posibles soluciones
- Descomposición del problema en subproblemas que permitan construir las soluciones de problemas más grandes
- Nos basamos en la intuición que nos da la Memorización para reconocer los sub-problemas y utilizarlos para construir la solución
- Una vez que tenemos todas las soluciones memorizadas, el problema está resuelto
- Nos ayuda evitando explorar un espacio exponencial de soluciones por fuerza bruta
- De esa manera podemos reducir la complejidad temporal de nuestro algoritmo significativamente


# DONE USAR PD


1. Hay un número polinomial de subproblemas
2. La solución al problema original puede ser construido a partir de soluciones a subproblemas
3. Hay un orden natural de los subproblemas de menor a mayor. Los subproblemas “mayores” son resueltos mediante la composición de problemas “menores”
4. La versión recursiva resuelve en formato Top-Down
5. La versión iterativa es de un formato Bottom-Up, es la que preferimos a partir de ahora al resolver ejercicios


Necesitamos:
- La forma que tienen los subproblemas
- La forma en que dichos subproblemas se componen para solucionar subproblemas más grandes

¿Cómo se encuentran?
¿En qué pensamos primero?


## Ej 3: juan el vago
Juan no quiere laburar 2 dias seguidos
![[Pasted image 20240924114152.png]]![[Pasted image 20240924114222.png]]
Es decir, o no trabaja hoy y utiliza el optimo del dia anterior. O trabaja hoy y usa el optimo de hace dos dias 
```python
def construir_elecciones(G,M):
  elecciones = []
  d = len(G)-1
  while( d >= 0 ):
    opt_ayer = G[d-1] if d>0 else 0
    opt_anteayer = G[d-2] if d>1 else 0
    valor_hoy = M[d]
    if valor_hoy + opt_anteayer >= opt_ayer:
      elecciones.insert(0, d)
      d -= 2
    else:
      d -= 1
  elecciones.reverse()
  return elecciones
```



## Ej 4: Laberinto 


## Ej 5: numpad 


## Ej 6: problema de la mochila II  
El unico tema ahora es que hay que tener mas en cuenta en el peso. Porque si yo elijo el elemento actual tengo que fijarme cual es ahora el optimo del elemento anterior CON EL PESO CAMBIADO. Es decir, con la capacidad que habia - el peso del elemento que acabo de agregar

![[Pasted image 20240925103035.png]]
Mis dos opciones son: Uso el elemento y busco el optimo de n-1 con la capacidad que tenia -el peso del elemento 
O no uso el elemento y busco el optimo de n-1 con el peso sin cambiar

```python 
	def mochila(valor, peso, N, W):
	   if N == 0:
	       return 0
	   if W < peso[N]:
	       return mochila(valor, peso, N-1, W)
	   return max(mochila(valor, peso, N-1, W),
	              valor[N] + mochila(valor, peso, N-1, W-peso[N]))
```

![[10b - Mochila - Ejemplo.pdf]]

El problema de la Mochila es un algoritmo Pseudo-Polinomial.

Eso habla de la dificultad del problema de la mochila.


## Problema del Cambio
$$C[dinero]= 1+ min(\forall moneda \leq dinero: C[dinero-moneda])$$

Pruebo con todas las monedas menores a la cantidad a la que quiero llegar y me fijo cual me da el minimo. 
```python 
def cant_monedas(sist_monetario, dinero):
   cant = [0] * (dinero + 1)
   for i in range(1, dinero + 1):
       minimo = i  # usar todas monedas de 1
       for moneda in sist_monetario:
           if moneda > i: 
           #si la moneda es mayor al dinero que estoy buscando, la salteo
               continue
           cantidad = 1 + cant[i - moneda]
           if cantidad < minimo:
               minimo = cantidad
       cant[i] = minimo
   return cant[dinero]
```


## Algoritmo de Bellman-Ford (camino mínimo)

- Inicializar todos los vértices en infinito y padres en None. El origen lo ponemos a distancia 0. 
- Iterando V veces, sobre TODAS las aristas y se busca la posibilidad de actualizar los pesos, buscando mejorar el camino mínimo. La diferencia con Dijkstra es que un camino descubierto puede mejorar gracias a las aristas negativas.
- Una vez finalizadas las V iteraciones, se verifica si aún se actualizan los pesos: en ese caso estamos ante un ciclo negativo.
- considera la existencia de aristas negativas, sabiendo que puede llegar a tener que cambiar los caminos mínimos.
- Para analizarlo de forma ordenada, plantea la forma de los sub-problemas como: encontrar el camino mínimo sabiendo que solamente podemos pasar por N vértices.
- Resuelve el problema iterativamente desde N=0 hasta $N= \#vertices$
- Ningún camino óptimo puede atravesar más de V vértices.
```python 
def camino_minimo_bf(grafo, origen):
	distancia = {}
	padre = {}
	for v in grafo:
		distancia[v] = infinito
	distancia[origen] = 0
	padre[origen] = None
	aristas = obtener_aristas(grafo)
	for i in range(len(grafo)):
		for v, w, peso in aristas:
			if distancia[v] + peso < distancia[w]:
				padre[w] = v
				distancia[w] = distancia[v] + peso
	
	for v, w, peso in aristas:
		if distancia[v] + peso < distancia[w]:
			return None # Hay un ciclo negativo (lanzar excep)
	return padre, distancia
```

## Distancia de edición
Se define que el mejor alineamiento entre dos cadenas es aquel que minimice la distancia de edicion. El criterio será: 
- Por cada par de letrsa que coinciden en alineamiento, no hay costo
- Existe la penalidad $\delta$ que refiere a no alinear las letras. Decimos que hay una brecha (gap)
- Por cada par de letras que no coinciden hay un costo $\alpha(x_{i}, y_{j})$ segun la diferencia etnre xi y yj. eg: el costo al alinear V y B puede ser bajo, por su parecido y cercania en el teclado
- El costo total del alineamiento seleccionado es la suma total de todos los costos pagados por brechas y por costo de reemplazo (cambiar letras)

eg: ocurrencia y occurrancia
oc-urr**e**ncia
occurr**a**ncia
un cambio $\alpha(e, a)$ y un una brecha $\delta$

tmbien lo puedo pensar como 
oc-urre-ncia
occurr-ancia
3 brechas


- Si el ultimo caracter de ambas cadenas coincide, no hay costo. Cuesta lo mismo alinear oro y lobo que oro y lobos
- Si el ultimo no coincide, se reemplaza usando $\alpha(x_{i}, y_j)$. Y luego se calcula el anieamiento optimo con un caracter menos de cada cadena. Ej: casa y caso, reemplazo entre o y a y despues calculo cas y cas
- Se puede introducir una brecha en alguna de las dos cadenas. Luego se calcula la solucion optima. casa y cases -> casa- con cases. Ahi alineo - con s y despues comparo entre casa y case (sin la s)
eso nos da la ecuacion de recurrencia: 
![[Pasted image 20241001125523.png]]Si son iguales no hay costo
Si el ultimo no coincide se reemplaza y se calcula el optimo entre los ultimos
brecha en cadena1 
brecha en cadena2 


## Subset sum
Tenemos un conjunto de números v1, v2, … vn, y queremos obtener un subconjunto de todos esos números cuya suma sea igual a un valor V, o bien aproximar lo mayor posible a ese valor V, sin pasarse.
Se puede adaptar al de la mochila. La capacidad es el numero al que quiero llegar y cada numero serian las cosas que puedo meter en la mochila
![[Pasted image 20241001131107.png]]

¿Podemos usar el Problema de la Mochila para resolver este ejercicio?

1. Convertir la entrada de este ejercicio en una entrada válida del Problema de la Mochila
2. Usar la solución al Problema de la Mochila
3. Verificar en base a esa solución, la solución de Subset-Sum

Si el Problema de la Mochila encuentra un valor igual a V, resuelto.

Sino, habrá encontrado el valor más cercano sin superar V.


## Tu a londres y yo a california
Manejamos un negocio que atiende clientes en Londres y en California.
Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados: Li y Ci para todo n.
Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza.
Dados los costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante n meses, sabiendo que queremos minimizar los costos de operación. Se puede empezar en cualquier ciudad.


Para un mes n, un plan que termina en Londres puede tener los siguientes costos:

- Ln + los costos operativos que hayamos tenido en meses anteriores terminando en Londres.
- Ln + los costos operativos que hayamos tenido en meses anteriores terminando en California + M.

Para un mes n, un plan que termina en California puede tener los siguientes costos:

- Cn + los costos operativos que hayamos tenido en meses anteriores terminando en California.

- Cn + los costos operativos que hayamos tenido en meses anteriores terminando en Londres + M.**


$$OPT londres [n] = L[n] + min( OPT londres [n-1], M + OPT california [n-1] )$$

  

$$OPT california [n] = C[n] + min( OPT california [n-1], M + OPT londres [n-1] )$$

