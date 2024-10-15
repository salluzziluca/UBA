ejecutra rmuktiples trsnacciones en forma simltanea. 
La idea es aprovechar al maximo la capacidad de computo( si dos querys usan dos 6 datos distintos, deberiamos poder ejecutandolas concurrentemente

Serializar no es una opcion. Serializar = ir en serie. No empezar una hasta no terminar la otra. Esto no es bueno porque una lenta tapa una rapida
Mientras una transacción espera que el SO escriba una página en disco, otra transacción podría realizar una operación en memoria

Los recursos compartidos son los datos, ahi esta el problema


Utilizaremos concurrencia solapada


![[Pasted image 20241015191657.png]]

El resultado difiere no seugn cual empieza primera, sino que parte de cada instruccion se ejecuta en que orden.


## Modelo de datos
Consideraremos que nuestra bdd esta formada por ==items== 
Un item uede representar: valor de atributo en fila determinada, una fila de una tala, un bloque de disco, una tabla

las instrucciones atomicas basicas son leerItem y escribirItem

>[!note] El tamaño de ítem escogido se conoce como granularidad, y afecta sustancialmente al control de concurrencia

>[!important]  No nos importan las lecturas y escrituras per se, solo el hecho de escribir y leer. No QUE leen y QUE escriben

>[!important] Leer y escribir no es efectivamente leer y escribir EN DISCO, puede estar todo en un buffer, hay que tener en cuenta los permisos que efecitvamente tiene el SGBD



Una transaccion es una unidad logica de trabajo en la SGBD
Es una secuencia ordenada de instrucciones que deben ser ejecutadas en su totalidad o bien no ser ejecutadas, al margen de la interferencia con otras transacciones simultáneas.


La ejecucion de una transaccion debera cumplir con las propiuedades ACID
Atomicidad
Consistnecia: cad ejecucion debe oreservar la consistencia de datos
aIslamiento: cuando ejecuto varias trsnacciones concrrentemente. Deberia obtener el mismo resultado que si ejecuto primero una y despues la otra. La ejecucion concurrente debe ser equivalente a ALGUNA ejecucion serial

Durabilidad: Una vez que el SGBD infoma que la trsnaccion se completo, esta se debe persistir. No puede el SGBD decir: esto termino!! y que no quede guardada

Se disponen de mecanismos de recuperacion para deshacer rehacer transacciones en caso de fallas (todo o nada)

begin: indica el comienzo de la trsnacciones
commit: indica que esta ha temrinado exitosamente 
abort: indica que se produzco error o falla y que todos los efectos deben ser dehechos (rollback)

## Anomalias 
### Lectura sucia (dirty read)
Se llama lectura sucia cuando una transaccion T2 lee un item que fue modificado por otra transaccion 
Si luego t1 se deshace, la lectura que hizo t2 no es valoida

![[Pasted image 20241015193602.png]]

### Lost update 

Cuando una trsa