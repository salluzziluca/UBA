## Control con locks
Es pesimista, bloqueo por si llega a pasar algo.

Utiliza locks para bloquear los recursos, Los loscks son insertados por le [[Sistemas de Gestion de Bases de Datos|SGBD]] como instrucciones especiales en medio de la transaccion 

Una vez insertados, las transacciones compiten entre ellas por su ejecución

Es ṕosible pero no trivial garantizar la serializabilidad

ver [[Sistemas Operativos/Concurrencia#Locks|locks]]

LoS [[Sistemas de Gestion de Bases de Datos|SGBD]] implementan dos tipos de locks: 
-  De escritura (exclusivos)
- De lectura (no exclusivos)
Solo con locks no alcanza. Se utiliza el protocolo de lock de dos fases.
1. Fase de adquisicion 
2. Fase de liberacion 

Si necesito A y B puedo adquirir A, hacer lo que tengo que hacer, Adquiri B, liberar A al toque y al final liberar B.

Con esot garantizamos que haya seriabilizad
Puedo tener [[Parcial#Deadlock|deadlock]] o un livelock

#### Deteccion de deadlocks

Analizar el [[Grafos|grafo]] de alocación de recursos: un [[Grafos|grafo]] dirigido que posee a las transacciones y los recursos como nodos, y en el cual se coloca un arco de una [[transacción]] a un recurso cada vez que una [[transacción]] espera por un recurso, y un arco de un recurso a una [[transacción]] cada vez que la [[transacción]] posee el lock de dicho recurso. Cuando se detecta un ciclo en este [[Grafos|grafo]], se aborta (rollback) una de las transacciones involucradas. El concepto es muy similar al del [[Grafos|grafo]] de precedencias para un solapamiento.

Definir un timeout para la adquisición del Lock(X), después del cual se aborta la [[transacción]].


#### Prevencion de deadlock 
Que cada [[transacción]] adquiera todos los locks que necesita antes de comenzar su primera instrucción, y en forma simultánea. (Lock(X1, X2, ...Xn)). 2 Definir un [[ordenamiento]] de los recursos, y obligar a que luego todas las transacciones respeten dicho [[ordenamiento]] en la adquisición de locks. 3 Métodos basados en timestamps.

#### Starvation
ver [[Scheduling#Starvation]]. 
## Control por timestamp 
[[Enfoque de Control de Concurrencia Optimista]]
Cada vez que empieza una transaccion le asigno un timestamp. Y se guarda siempre en cada item modificado quien y cuando lo modifico

Se permite la ocurrencia de conflictos, pero siempre que las transacciones de cada conflicto aparezcan de acuerdo al orden serial equivalente: (WTi (X), RTj (X)) → TS(Ti) < TS(Tj)

Cada item tiene un readTS y un writeTS. Este devuelve el timestamp de la transaccion mas joven que leyo/escribio el item.

Si una transaciion quier leer o escribir se fija en los readTS y writeTS. Si fue escrito o leido por alguien con un timestamp mayor al suyo, ABORTA (read too late o write too late)
## Control por snapshots

Cada transaccion ve una spanshot de la la [[Bases de Datos|base de datos]] correspondiente al instante e su inicio. 
Permite un mayot solapamiento pero requiere mas [[memoria]] y, cuando hay conflictos, obliga a deshacer una de ellas. La que commiteo prinmero gana
[[Enfoque de Control de Concurrencia Optimista]]