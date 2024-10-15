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
Un item uede representar: atributo