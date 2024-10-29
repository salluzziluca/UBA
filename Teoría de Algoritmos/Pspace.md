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
3. [[Teoría de Algoritmos/P]] es PSPACE? Si, porque necesitas pedirle si o si el espacio polinomial al sistema.


### Cuantificacion (QSAT)
![[Pasted image 20241028113744.png]]
Si usáramos dos arreglos en cada paso de la recursividad: S(n) = 2 S(n-1) + [[Teoría de Algoritmos/P]](n)
Pero podemos reutilizar → S(n) = S(n-1) + [[Teoría de Algoritmos/P]](n)  <= n [[Teoría de Algoritmos/P]](n) → QSAT está en PSPACE. 


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


¿Creamos el grafo de las configuraciones?
¿Hacemos un BFS/DFS simulando el comportamiento?
No, porque no podemos cargar todos los estados en memoria (en jarras se puede porque son 24 nomas)

Como BFS y DFS mantienen un historial muy grande y no reusan espacio suficiente usamos algo similar a D&C

 **dividir el problema en dos partes, resolver una, tirar (casi) todo el trabajo intermedio y resolver la otra. **

Definimos Path(C1, C2, L) que determina si existe camino de largo a lo sumo L. 

Nuestro problema comienza con Path(C0, C*, 2n).



La versión BFS hasta podría verse como un pseudo Programación dinámica → Para obtener Path(C1, C2, L) calcula Path(C', C2, L-1) tal que C1 tenga arista a C'. 
→ BFS genera una enorme cantidad de configuraciones para sólo reducir en 1 a L. 
Ahora… ¿por qué tenemos que ir por adyacentes?


Para cada posible C' vemos si podemos llegar de C1 a C' en hasta L/2 pasos, y de C' a C2 en L/2 pasos. 
Como sólo nos importa el true/false, se descarta cualquier otra cosa. 
Entonces, se hacen hasta log2(L) = n llamados recursivos (= consumo de memoria → espacio polinomial), aparte puede depender de un polinomio de n y k. 
→**Planning está en PSPACE**

**QSAT es PSPACE-completo.**
**

QSAT <=P Competitive 3-SAT y Competitive 3-SAT <=P QSAT

**
Se puede reducir (citation needed) QSAT a CFL, por lo que CFL también es PSPACE-completo.



Un PSPACE completo, ¿Es NP-Completo?

No son NP-Completo, sino NP-difícil.


## Peor que PSPACE 
EXP/EXPTIME → Problemas que se resuelven en tiempo O(2p(n))
NEXP/NEXPTIME → Problemas que se resuelven en tiempo O(2n^O(1))
EXPSPACE → Problemas que se resuelven en espacio O(2p(n))
R → Problemas que se pueden resolver (hablamos más tarde de esto).
