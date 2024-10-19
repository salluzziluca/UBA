ejecutar multiples transacciones en forma simultanea. 
La idea es aprovechar al máximo la capacidad de computo( si dos querys usan dos 6 datos distintos, deberíamos poder ejecutándolas concurrentemente

Serializar no es una opcion. Serializar = ir en serie. No empezar una hasta no terminar la otra. Esto no es bueno porque una lenta tapa una rapida
Mientras una [[transacción]] espera que el SO escriba una página en disco, otra [[transacción]] podría realizar una operación en memoria

Los recursos compartidos son los datos, ahi esta el problema


Utilizaremos concurrencia solapada


![[Pasted image 20241015191657.png]]

El resultado difiere no seugn cual empieza primera, sino que parte de cada instruccion se ejecuta en que orden.


## Modelo de datos
Consideraremos que nuestra [[Bases de Datos|bdd]] esta formada por ==items== 
Un item uede representar: valor de [[Base de Datos/Atributos|atributo]] en fila determinada, una fila de una tala, un bloque de disco, una tabla

las instrucciones atomicas basicas son leerItem y escribirItem

>[!note] El tamaño de ítem escogido se conoce como granularidad, y afecta sustancialmente al [[control de concurrencia]]

>[!important]  No nos importan las lecturas y escrituras per se, solo el hecho de escribir y leer. No QUE leen y QUE escriben

>[!important] Leer y escribir no es efectivamente leer y escribir EN DISCO, puede estar todo en un buffer, hay que tener en cuenta los permisos que efecitvamente tiene el [[Sistemas de Gestion de Bases de Datos|SGBD]]



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

Cuando una transaccion modifica un item que fue leido anteriormente por una primera transaccion que aun no termino. 


Si la primera luego modifica y escribe el item que leyó, se pierde el valor modificado por T2
Si en cambio, la T1 volviera a leer el item, se encontraria con otro valor (unrepeteale read)

![[Pasted image 20241015194125.png]]
el saldo deberia ser 500 pero termina siendo 400



### Dirty Write 
Cuando escribo algo que ya fue escrito pero no commiteado. El scheduler me saca el lock antes de commitear mi Write
![[Pasted image 20241015194428.png]]


### Anomalia del fantasma 
Busco valores qu ecumplan una condicion. Despues una T2 modifica un item y este ahora pasa a cumplir la condicion 
![[Pasted image 20241015194723.png]]


## Serializabilidad
RT (X): La transacción T lee el ítem X. 
WT (X): La transacción T escribe el ítem X. 
bT : Comienzo de la transacción T. 
cT : La transacción T realiza el commit. 
aT : Se aborta la transacción T (abort)

Un solapamiento se da cuando
bT1 ; RT1 (X); bT2 ; RT2 (X); WT2 (X); RT1 (Y); WT1 (Y); cT2 ; cT

Ahora tenemos que ver si ese solapamiento es serializable o no

para ese par de transacciones existen dos ejecuciones seriales posibles

>[!hint] Existen n! ejecuciones seriales distintas entre n transacciones 


>[!note] Decimos que un solapamiento de un conjunto de transacciones T1, T2, ..., Tn es serializable cuando la ejecución de sus instrucciones en dicho orden deja a la base de datos en un estado equivalente a aquél en que la hubiera dejado alguna ejecución serial de T1, T2, ..., Tn.


## Equivalencia 
### Equivalencia de resultados 
Cuando ambas dejan la bdd en el mismo estado 

### Equivalencia de conflictos 
Cuando ambos órdenes de ejecución poseen los mismos conflictos entre instrucciones.


TLDR un conflcto se da cuando una istruccion de una transaccion escribe un item que otra leyo, una transaccion lee un item que otra escribio, dos escriben el mismo item. Es decir, cuando dos transacciones ejecutan instrucciones sobre un mismo item y al menos una de las dos instrucciones es una escritura 

Todas dos instrucciones consecutivas que no tengan conflicto se pueden invertir 

### Equivalencia de vistas 
Cuando en cada órden de ejecución, cada lectura RTi (X) lee el valor escrito por la misma transacción j, WTj (X). Además se pide que en ambos órdenes la última modificación de cada ítem X haya sido hecha por la misma transacción.




![[Pasted image 20241015200748.png]]




## Grafo de precedencias. 
La serializacion se puede evaluadar a traves del graeo


![[Pasted image 20241015201645.png]]


EJ; 
![[Pasted image 20241015201734.png]]

![[Pasted image 20241015201752.png]]

Hay un ciclo, no es serialozable


[[Control de Concurrencia]]

## Niveles de aislamiento

![[Pasted image 20241015212531.png]]
SIEMPRE SE EVITA LA ESCRITURA SUCIA