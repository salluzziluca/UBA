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
Puedo tener deadlocks o 
## Control por timestamp 
[[Enfoque de Control de Concurrencia Optimista]]
## Control por snapshots
[[Enfoque de Control de Concurrencia Optimista]]