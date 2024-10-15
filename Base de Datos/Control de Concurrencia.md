## Control con locks
Es pesimista, bloqueo por si llega a pasar algo.

Utiliza locks para bloquear los recursos, Los loscks son insertados por le SGBD como instrucciones especiales en medio de la transaccion 

Una vez insertados, las transacciones compiten entre ellas por su ejecución

Es ṕosible pero no trivial garantizar la serializabilidad

ver [[Sistemas Operativos/Concurrencia#Locks|locks]]

LoS SGBD implementan dos tipos de locks: 
-  De escritura (exclusivos)
- De lectura (no exclusivos)
Solo con locks no alcanza. Se utiliza el protocolo de lock de dos fases.
1. Fase de adquisicion 
2. Fase de liberacion 

Si necesito A y B puedo adquirir A, hacer lo que tengo que hacer, Adquiri B, liberar A al toque y al final liberar B.

Con esot garantizamos que haya seriabilizad
Puedo tener [[Parcial#Deadlock|deadlock]] o un livelock

#### Deteccion de deadlocks

Analizar el grafo de alocación de recursos: un grafo dirigido que posee a las transacciones y los recursos como nodos, y en el cual se coloca un arco de una transacción a un recurso cada vez que una transacción espera por un recurso, y un arco de un recurso a una transacción cada vez que la transacción posee el lock de dicho recurso. Cuando se detecta un ciclo en este grafo, se aborta (rollback) una de las transacciones involucradas. El concepto es muy similar al del grafo de precedencias para un solapamiento.

Definir un timeout para la adquisición del Lock(X), después del cual se aborta la transacción.


#### Prevencion de deadlock 
Que cada transacción adquiera todos los locks que necesita antes de comenzar su primera instrucción, y en forma simultánea. (Lock(X1, X2, ...Xn)). 2 Definir un ordenamiento de los recursos, y obligar a que luego todas las transacciones respeten dicho ordenamiento en la adquisición de locks. 3 Métodos basados en timestamps.
## Control por timestamp 
[[Enfoque de Control de Concurrencia Optimista]]
## Control por snapshots
[[Enfoque de Control de Concurrencia Optimista]]