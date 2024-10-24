Un problema es [[NP (nondetherministic polynomial)|NP]] completo sii:
Es 
Todo problema [[NP (nondetherministic polynomial)|NP]] se puede reducir a ese. Es decir: Si yo tengo otro problema [[NP (nondetherministic polynomial)|NP]] $y$ y mi problema [[NP (nondetherministic polynomial)|NP]] $x$: $y\leq_{p}x$
son lo mas dificil de lo mas dificil

##### Consecuencias: 
Si X es un problema [[NP (nondetherministic polynomial)|NP]]-Completo, solo puedo resolverse en tiempo polinomial sii [[P]] = [[NP (nondetherministic polynomial)|NP]] 
Si al menos un problema [[NP (nondetherministic polynomial)|NP]]-Completo puede resolverse en tiempo polinomial, entonces todos pueden y [[P]]=[[NP (nondetherministic polynomial)|NP]]



### Problemas [[NP (nondetherministic polynomial)|NP]] completos
#### Teorema de Cook & Levin: Circuit Satisfiability 

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfGOJvAdFpiIYGKUngmron3TZdQALAKQaXdp8Hz-stiCtOcvdq55hsOrtg4xaORV_OjeM91iIjd_7nfgZCRD_2bjGrb5UPhxJ7iK-wUU1i6jtFwvRVzhvKugbTTP6FWEbiEzuKwWdvscf495q6VrzSh8SJh99L3=s2048?key=ddV7CqlIamrZHzGhNajamQ)

Ese es un problema [[NP (nondetherministic polynomial)|NP]] completo.

Si logramos reducir un [[NP (nondetherministic polynomial)|NP]] completo a otro problema X->X es [[NP (nondetherministic polynomial)|NP]]-completo (por transitividad)
Si puedo reducir circuit satisfability a 3-SAT transformando el problema a SAT con 3 terminos y luego pasando a SAT

![[Pasted image 20241024105452.png]]

como vimos en [[Reducciones]] $3-SAT \leq_{p} Independet \ set \leq_{p} vertex \ cover$ por lo que independent set y vertex cover tambien son NP completos 


### Ej1: Reducir "si un numero es multiplo de otro" a "ver si un elemento está en una lista"
Tenemos una lista con todos los multiplos de ese numero y nos fijamos si el numero en cuestion se encuenta en la lista


### Ej2: reduciendo independent set a k-clique
1. Obtenemos el grafo complemento ->Aristas que no estan en G 
2. Definimos que hay un independent set de al menos K vertices sii hay un clique de al menos K vertices en el grafo complemento
Como es un si y solo si y independent set es NP-Completo, K-clicke es NP-Completo


## Estrategias para reducir en general 
- Reduccion por equivalencia simple (independent set y vertex cover o lo de arriba con clique)
- Reduccion de caso especial a caso general(N reinas a independent set)
- Reduccion por encodeo de caracteristicas


### Ej3 Problema del viajante 
lo ponemos dirigido y sin cumplir la desigualdad triangular.
Existe un camino de costo/distancia con maximo D?

como podemos reducir [[Grafos Hamiltonianos]] a el problema del viajante?
a las aristas que no existe le agrego peso 2 (para que no vaya por ahi) y a las que existen peso 1. 
Existe un ciclo hamiltoniano en el original sii existe un camino TSP en el nuevo grafo de a lo sumo (y exactamente) n = cantidad de vertices. No puede ser menos que n. Si es mayor que N, uso una arista de peso 2-> uso una arista que no existe en el orginal

### Reduciendo 3-SAT a Ciclo hamiltoniano 

Por que a 3SAT? porque es siempre una buena idea cuando no se nos ocurre a que mas reducir, ya que es bastante simple 

Dado un problema 3-ST cualquiera (variables, clausulas) como definimos si es astisfacible por tener una caja resolverda de [[hai]]