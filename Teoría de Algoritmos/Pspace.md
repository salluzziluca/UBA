 Con [[Reducciones|NP ]] es facil probar que algo es solucion, pero no es sencillo probar que NO hay solucion
$\bar{X}$ Es un problema donde algo que tenga solucion en $X$ no la tiene en $\bar{X}$ y viceversa.
Si $X \in P \to \bar{X} \in P$

Pero... si  $X \in NP\dots¿ \bar{X} in NP?$

Como ahora en vez de "existe algun camino/seleccion/particion" es un "para todo camino/seleccion/..." y sucede que para ese caso tan general no hay solucion

## Co-NP

Si un problema pertenece a NP → es fácil demostrar cuando algo es solución. 
Si un problema pertenece a co-NP → es fácil demostrar que algo no es solución/no tiene solución ("No existe un camino de largo como mucho N", etc…). 


## Mas allá de NP 
Hay algo peor que las cosas que toman mas tiempo que exponencial


# PSPACE
Problemas que se resuelven con un algoritmo que consume una cantidad polinomial de espacio

1. Mergesort es PSPACE? Si, porque partimos en arreglos, mas o menos consumimos O(n)
2. Fibonacci es PSPACE? Si, porque lo resolvemos en O(n)
3. P es PSPACE? Si, porque necesitas pedirle si o si el espacio polinomial al sistema.


### Cuantificacion (QSAT)
![[Pasted image 20241028113744.png]]
Si usáramos dos arreglos en cada paso de la recursividad: S(n) = 2 S(n-1) + p(n)
Pero podemos reutilizar → S(n) = S(n-1) + p(n)  <= n p(n) → QSAT está en PSPACE. 


### Juegos de 2 jugadores 
1. Ajedrez 
2. Go 
3. Competitive Facility Location Problem
estan en PSPACE


### Generalizacion 
Tengo un conjunto C0 de condiciones iniciales
Tengo un conjunto C* de condiciones finales al que queremos llegar
Tengo un conjunto de operaciones/operadores O1, …, Ok, con cada Operador i con pre-requisitos Pi, una "add-list" Ai y una "delete list" Di. 
¿Es posible aplicar una secuencia de operaciones desde C0 tal que lleguemos a C*?