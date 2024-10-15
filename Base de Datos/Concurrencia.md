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


