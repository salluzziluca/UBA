## Control con locks
Es pesimista, bloqueo por si llega a pasar algo.

Utiliza locks para bloquear los recursos, Los loscks son insertados por le SGBD como instrucciones especiales en medio de la transaccion 

Una vez insertados, las transacciones compiten entre ellas por su ejecución

Es ṕosible pero no trivial garantizar la serializabilidad

ver [[Taller de Programación/Concurrencia|Concurrencia]]
## Control por timestamp 
[[Enfoque de Control de Concurrencia Optimista]]
## Control por snapshots
[[Enfoque de Control de Concurrencia Optimista]]