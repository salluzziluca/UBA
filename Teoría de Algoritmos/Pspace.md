 Con [[Reducciones|NP ]] es facil probar que algo es solucion, pero no es sencillo probar que NO hay solucion
$\bar{X}$ Es un problema donde algo que tenga solucion en $X$ no la tiene en $\bar{X}$ y viceversa.
Si $X \in P \to \bar{X} \in P$

Pero... si  $X \in NP\dots¿ \bar{X} in NP?$

Como ahora en vez de "existe algun camino/seleccion/particion" es un "para todo camino/seleccion/..." y sucede que para ese caso tan general no hay solucion

## Co-NP

Si un problema pertenece a [[NP (nondetherministic polynomial)|NP]] → es fácil demostrar cuando algo es solución. 
Si un problema pertenece a co-[[NP (nondetherministic polynomial)|NP]] → es fácil demostrar que algo no es solución/no tiene solución ("No existe un camino de largo como mucho N", etc…). 


## Mas allá de [[NP (nondetherministic polynomial)|NP]] 
Hay algo peor que las cosas que toman mas tiempo que exponencial


# PSPACE
Problemas que se resuelven con un algoritmo que consume una cantidad polinomial de espacio

1. Mergesort es PSPACE? Si, porque partimos en arreglos, mas o menos consumimos O(n)
2. Fibonacci es PSPACE? Si, porque lo resolvemos en O(n)
3. [[P]] es PSPACE? Si, porque necesitas pedirle si o si el espacio polinomial al sistema.


### Cuantificacion (QSAT)
![[Pasted image 20241028113744.png]]
Si usáramos dos arreglos en cada paso de la recursividad: S(n) = 2 S(n-1) + [[p]](n)
Pero podemos reutilizar → S(n) = S(n-1) + [[p]](n)  <= n [[p]](n) → QSAT está en PSPACE. 


### Juegos de 2 jugadores 
1. Ajedrez 
2. Go 
3. Competitive Facility Location Problem
estan en PSPACE


### Generalizacion 
Tengo un conjunto C0 de condiciones iniciales
Tengo un conjunto C* de condiciones finales al que queremos llegar
Tengo un conjunto de operaciones/[[operadores]] O1, …, Ok, con cada Operador i con pre-requisitos Pi, una "add-list" Ai y una "delete list" Di. 
¿Es posible aplicar una secuencia de operaciones desde C0 tal que lleguemos a C*?}


### Juego de las jaras
![[Pasted image 20241028114943.png]]
Tengo una jarra de 5 y una de 3 y quiero llegar a 4 litros

hacemos BFS: 
(0, 0) → 
(5, 0); (0, 3) → 
(2, 3); (5, 3); (3, 0) → 
(2; 0); (3; 3) → 
(0, 2); (5, 1) → 
(5, 2); (0, 1) → 
(4, 3); (1, 0)

Vemos que conseguimos: 
(0, 0) → (5, 0) → (2, 3) → (2, 0) → (0, 2) → (5, 2) → (4, 3)
Vemos que por DFS podríamos haber conseguido también:
(0, 0) → (0, 3) → (3, 0) → (3, 3) → (5, 1) → (0, 1) → (1, 0) → (1, 3) → (4, 0)



Podemos decir que hay un grafo (dirigido) implícito de nodo = todas las 2n configuraciones posibles (todos los posibles subsets de C), con arista de C' a C'' sii existe un operador que nos lleve de C' a C''. 
En el marco de nuestro problema, … ¿Existe un camino de C0 a C*? 
En el peor de los casos tenemos que pasar por todos los estados posibles (→ O(2n))
(Si fueran de un tamaño polinomial, estaría en NP porque validarlo se hace en tiempo polinomial)

