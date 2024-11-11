Un problema es [[NP (nondetherministic polynomial)|NP]] completo sii:
Es 
Todo problema [[NP (nondetherministic polynomial)|NP]] se puede reducir a ese. Es decir: Si yo tengo otro problema [[NP (nondetherministic polynomial)|NP]] $y$ y mi problema [[NP (nondetherministic polynomial)|NP]] $x$: $y\leq_{p}x$
son lo mas dificil de lo mas dificil

##### Consecuencias: 
Si X es un problema [[NP (nondetherministic polynomial)|NP]]-Completo, solo puedo resolverse en tiempo polinomial sii [[Teoría de Algoritmos/P]] = [[NP (nondetherministic polynomial)|NP]] 
Si al menos un problema [[NP (nondetherministic polynomial)|NP]]-Completo puede resolverse en tiempo polinomial, entonces todos pueden y [[Teoría de Algoritmos/P]]=[[NP (nondetherministic polynomial)|NP]]



### Problemas [[NP (nondetherministic polynomial)|NP]] completos
#### Teorema de Cook & Levin: Circuit Satisfiability 

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfGOJvAdFpiIYGKUngmron3TZdQALAKQaXdp8Hz-stiCtOcvdq55hsOrtg4xaORV_OjeM91iIjd_7nfgZCRD_2bjGrb5UPhxJ7iK-wUU1i6jtFwvRVzhvKugbTTP6FWEbiEzuKwWdvscf495q6VrzSh8SJh99L3=s2048?key=ddV7CqlIamrZHzGhNajamQ)

Ese es un problema [[NP (nondetherministic polynomial)|NP]] completo.

Si logramos reducir un [[NP (nondetherministic polynomial)|NP]] completo a otro problema X->X es [[NP (nondetherministic polynomial)|NP]]-completo (por transitividad)
Si puedo reducir circuit satisfability a 3-SAT transformando el problema a SAT con 3 terminos y luego pasando a SAT

![[Pasted image 20241024105452.png]]

como vimos en [[Reducciones]] $3-SAT \leq_{p} Independet \ set \leq_{p} vertex \ cover$ por lo que independent set y [[Vertex Cover]] tambien son [[NP (nondetherministic polynomial)|NP]] completos 


### Ej1: Reducir "si un numero es multiplo de otro" a "ver si un elemento está en una [[Lista]]"
Tenemos una [[Lista]] con todos los multiplos de ese numero y nos fijamos si el numero en cuestion se encuenta en la [[Lista]]


### Ej2: reduciendo independent set a k-[[clique]]
1. Obtenemos el [[Grafos|grafo]] complemento ->Aristas que no estan en G 
2. Definimos que hay un independent set de al menos K vertices sii hay un [[clique]] de al menos K vertices en el [[Grafos|grafo]] complemento
Como es un si y solo si y independent set es [[NP (nondetherministic polynomial)|NP]]-Completo, K-clicke es [[NP (nondetherministic polynomial)|NP]]-Completo


## Estrategias para reducir en general 
- Reduccion por equivalencia simple (independent set y [[Vertex Cover]] o lo de arriba con [[clique]])
- Reduccion de caso especial a caso general(N reinas a independent set)
- Reduccion por encodeo de caracteristicas


### Ej3 Problema del viajante 
lo ponemos dirigido y sin cumplir la desigualdad triangular.
Existe un camino de costo/distancia con maximo D?

como podemos reducir Ciclo hamiltoniano a el problema del viajante?
a las aristas que no existe le agrego peso 2 (para que no vaya por ahi) y a las que existen peso 1. 
Existe un ciclo hamiltoniano en el original sii existe un camino TSP en el nuevo [[Grafos|grafo]] de a lo sumo (y exactamente) n = cantidad de vertices. No puede ser menos que n. Si es mayor que N, uso una arista de peso 2-> uso una arista que no existe en el orginal

### Reduciendo 3-SAT a Ciclo hamiltoniano 

Por que a 3SAT? porque es siempre una buena idea cuando no se nos ocurre a que mas reducir, ya que es bastante simple 

Dado un problema 3-ST cualquiera (variables, clausulas) como definimos si es astisfacible por tener una caja resolvedora de [[Grafos Hamiltonianos|caminos hamiltonianos]]

Demostracion: tu vieja 


### CAMINO hamiltoniano es [[NP (nondetherministic polynomial)|NP]]-Completo?

Reducimos ciclo hamiltoniano a camino hamiltoniano 
1. Agarro un v3etice al azar y lo reemplazo por v' y v''. Todas las aristas salientes de v ahora salen de v', todas las entrantes entran a v'' 
2. Existe cilco hamiltopniano en el ogiginal si existe camino hamiltoniano en el nuevo (este necesariamente empieza en v' y termina en v'')

### Ejercicioo tranqui: Algoritmo para ver si a + b = c

Está en [[NP (nondetherministic polynomial)|NP]]? si
Esta en [[Teoría de Algoritmos/P]]? Si
Como podemos reducir este problema al problema del viajante?QUEEEEEE
obvio que se puede ajkdas

### Coloreo de grafos
Cuando k=2 -> problema de grafo bipartito 
cuando k=3-> ya nos fuimos a NP completo??
Como es dificil de comparar [[coloreo]] a otro problema, vamos a 3-SAT (reducimos 3SAT a colreo de 3 colores)


1. Creamos un nodo por cada variable xi y un nodo por su complemento
2. Unimos los vértices de variables con sus complementos
3. Creamos 3 nodos especiales: True, False y Base. (para los 3 colores)
4. Unimos a cada variable y complemento con Base, para formar triángulos
5. Unimos True y False con Base para formar otro triángulo. 
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdCw4Kc3Bwm5TUyuQX6eCd2FJvToeBzuU5rkigEe0GAb6CmRc2nrFxIBMWpT71KSvfBsze6-iillj_iAb26kC5XvJI-EqEwBknhT1M8vjWPJB-GOoZ-zxqmPvB6E8TxcFySNbJMYByr7NlDl0mJ59RlJ9xkv2g=s2048?key=ddV7CqlIamrZHzGhNajamQ)
Supongamos que tenemos la expresión $x1 ⋁ \bar{  x_{2}} ⋁ x3$
Al menos 1 debe ser True → Al menos 1 debe tener el color de True.

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdXxII12DZk-lJaPs7TTGD1519yBMh96jYBSCDcp9Hx3DqFsxmrQrH7KIbgtaocLadko1dJzWnjNvRv7NoLcwOBUwKTcb4yCR_zWUtLdnAUxx1w7beJUc3NkUHTw0v26xLhFBstyyENxFUEBtsbKgzJgN2_IbvX=s2048?key=ddV7CqlIamrZHzGhNajamQ)**



### Reducimos 3-[[coloreo]] a k-[[coloreo]]

Agregamos k-3 nodos que se unen entre sí y a todos los vértices originales; 
El grafo resultante es k-coloreable si el original grafo es 3-coloreable.
→ Para todo K > 3 también es NP-Completo

### Bipartito a coloreo 

pinto con dos colores y listo

### Subser sum 
Por programación dinámica: O(nW) → pseudopolinomial → No depende del tamaño de la entrada sino de los valores (y termina siendo exponencial). Salvo que W = Polinomio(n). 

¿Es NP?
podemos reducir otro problema (3-dimensional-matching) a este → es NP-Completo. 


### Scheduling 
Problema más general: No tenemos sólo deadlines y duración, sino también release times (momento en el cual la tarea comienza a estar disponible)
Bueno… este problema es NP-Completo. 

Reducimos SubsetSum a este: 
1. Definimos a S como la suma de todos los elementos. Creamos las tareas: la tarea i tiene duración wi, release de 0 y deadline S+1 (entonces se los puede ordenar a todos). 
2. Creamos una n-ésima+1 tarea con release time W y deadline W+1, de duración 1. 
3. Si el problema de scheduling puede resolverse, es únicamente porque se pudieron poner cosas que sumen W justo antes de esta tarea, y luego todas las demás. Además no puede haber tiempo al pedo porque todo suma S, y teníamos S+1 de tiempo total, con 1 ya consumido por esta tarea. 

**Reducir desde el caso particular donde empecemos con un SubsetSum con W = Polinomio(n) no implica nada → Este caso no es NP-Completo.**