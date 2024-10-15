ejecutra rmuktiples trsnacciones en forma simltanea. 
La idea es aprovechar al maximo la capacidad de computo( si dos querys usan dos 6 datos distintos, deberiamos poder ejecutandolas concurrentemente

Serializar no es una opcion. Serializar = ir en serie

Los recursos compartidos son los datos, ahi esta el problema


Utilizaremos concurrencia solapada


![[Pasted image 20241015191657.png]]

El resultado difiere no seugn cual empieza primera, sino que parte de cada instruccion se ejecuta en que orden.