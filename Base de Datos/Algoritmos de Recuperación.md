---
dg-publish: true
---
En los 3 se asumen que los solapamientos son recuperables y que evitan rollbacks en cascada (ver [[Recuperabilidad]])

## Algoritmo UNDO (inmmediate update) 
>[!quote] Antes de que una modificación sobre un ítem X ← v_new por parte de una [[transacción]] no commiteada sea guardada en disco (flushed), se debe salvaguardar en el log en disco el último valor commiteado vold de ese ítem.


1. Cuando al transaccion T_i modifica el item X reemplazando su valor v_old por v, se escribe (WRITE, T_i, X, v_old) en log. Luego se hace flush al log del disco
2. El registro (WRITE, Ti , X, vold ) debe ser escrito en el log en disco (flushed) antes de escribir (flush) el nuevo valor de X en disco (WAL).
3. Todo ítem modificado debe ser guardado en disco antes de hacer commit.
4. Cuando Ti hace commit, se escribe (COMMIT, Ti) en el log y se hace flush del log a disco (FLC).

Los tres primeros puntos aseguran que todas las modificaciones realizadas sean escritas a disco antes de que la [[transacción]] termine. 
De esta forma, una vez cumplimentado el paso 4, ya nunca será necesario hacer REDO. Si la [[transacción]] [[Fallas|falla]] antes ó durante el punto 4, será deshecha (UNDO) al reiniciar. 
Se considera que la [[transacción]] commiteó cuando el registro (COMMIT, Ti) queda escrito en el log, en disco


### Reinicio
Cuando el sistema se reinicia 

1. Se recorre el log de adelante hacia atrás, y por cada [[transacción]] de la que no se encuentra el COMMIT se aplica cada uno de los WRITE para restaurar el valor anterior a la misma en disco. 
2.  Luego, por cada [[transacción]] de la que no se encontró el COMMIT se escribe (ABORT, T) en el log y se hace flush del log a disco.

El reinicio es idempotente. Si se ejecuta varias veces (hay una [[Fallas|falla]] en el reinicio) no pasa nada

![[Pasted image 20241022195555.png]]

### Checkpoint 
El procedimiento de [[Checkpoints#Checkpoints inactivos|checkpoint inactivo]] se llevaria a cabo de esta forma: 
dejo de acpetar nuevas [[Transacción|transacciones]] 
espero a que todas hagan commit 
escribo CKPT en el log y vuelco a disco

En cambio, para el [[Checkpoints#Checkpoints activos|checkpoint activo]]:
1. Escribo un registro BEGIN CKPT, T_act([[Transacción|transacciones]] activas)
2. Espero a que todas las activas hagan su commit (pero sin dejar de recibir nuevas [[Transacción|transacciones]])
3. Escribir END CKPT en log y volcarlo a disco

En la recuperación hay nuevamente dos situaciones: Que encontremos primero un registro (END CKPT).En ese caso, deberemos retroceder hasta el (BEGIN , Tx ) más antiguo del listado que figure en el (BEGIN CKPT). Deshago los writes y Escribo (ABORT, Ty ) para aquellas que no hayan commiteado.
bdQue encontremos primero un registro (BEGIN CKPT).Si el checkpoint llego sólo hasta este punto no nos sirve. Deberemos volver hacia atrás, pero sólo hasta el inicio de la más antigua del listado
## REDO (deferred update)

>[!quote] Antes de realizar el commit, todo nuevo valor v asignado por la [[transacción]] debe ser salvaguardado en el log, en disco.

¿Ésto me obliga a guardar el ítem modificado en disco antes de commitear la [[transacción]] que lo modificó? 
No, sólo el registro de log! De hecho, en el algoritmo REDO el ítem es actualizado en disco luego de commitear la [[transacción]].

El algoritmo debe commitear sin guardar en disco los items modificados. 
Ante una [[Fallas|falla]] posterior al commit, sera necesario hacer un REDO de todos los valores que la tranasccion habia asiEn la recuperación es posible que debamos retroceder
hasta el inicio de la transacción más antigua en el listado
de transacciones, para deshacerla en caso de que no
haya commiteado.ganado a los items 
Esto implica recorrer todo el log de atras para adelanteaplicando cada uno de los write 


### reinicio 
1. Se analiza cuales [[Transacción|transacciones]] commitaron 
2. Se reocrre el log de atras para adelante volviendo a aplicar el wirte de las [[Transacción|transacciones]] que ya commitearon , para asegurar que quede actualizado el valor de cada ítem.
3. Luego, por cada [[transacción]] de la que no se encontró el COMMIT se escribe (ABORT, T) en el log y se hace flush del log a disco.

### Checkpoint 
Utilizando [[Checkpoints#Checkpoints activos|active checkpoint]]:
Escribir un registro BEGIN CKPT, Tactivas con el listado de todas las [[Transacción|transacciones]] activas y vuelvo el log a disco 
Hago el volcado a diisco de todos los items que hayan sido modificados por [[Transacción|transacciones]] que ya commitearon 
Escribo END CKPT en el log y lo vuelco a disco 


Que encontremos primero un registro (END CKPT).En ese caso, deberemos retroceder hasta el (BEGIN , Tx ) más antiguo del listado que figure en el (BEGIN CKPT) para rehacer todas las transacciones que commitearon. Escribir (ABORT, Ty ) para aquellas que no hayan commiteado. 

Que encontremos primero un registro (BEGIN CKPT).Si el checkpoint llego sólo hasta este punto no nos sirve, y entonces deberemos ir a buscar un checkpoint anterior en el l

## Algoritmo UNDO/REDO 
Buscamos evitar que una transaccion que se grabo a disco no haya commiteado y que una transaccion que ya commiteo no haya sido grabada a disco 

En el algoritmo UNDO/REDO es necesario cumplir con ambas reglas a la vez. El procedimiento es el siguiente:
1. Cuando una [[transacción]] Ti modifica el item X remplazando un valor vold por v, se escribe (WRITE, Ti , X, vold , v) en el log. 
2. El registro (WRITE, Ti , X, vold , v) debe ser escrito en el log en disco (flushed) antes de escribir (flush) el nuevo valor de X en disco. 
3. Cuando Ti hace commit, se escribe (COMMIT, Ti) en el log y se hace flush del log a disco. 
4. Los ítems modificados pueden ser guardados en disco antes o después de hacer commit

### Reinicio 
1. Se recorre el log de adelante hacia atrás, y por cada [[transacción]] de la que no se encuentra el COMMIT se aplica cada uno de los WRITE para restaurar el valor anterior a la misma en disco. 
2. Luego se recorre de atrás hacia adelante volviendo a aplicar cada uno de los WRITE de las [[Transacción|transacciones]] que commitearon, para asegurar que quede asignado el nuevo valor de cada ítem. 
3. Finalmente, por cada [[transacción]] de la que no se encontró el COMMIT se escribe (ABORT, T) en el log y se hace flush del log a disco.

![[Pasted image 20241022204043.png]]

En este caso tiene que deshacer todos los cambios de T1 (porque no se deberia haber guardado en disco) y asegurarse que todo lo de T2 esta guardado.
![[Pasted image 20241022204327.png]]


### Checkpoint 
1. Escribir un registro (BEGIN CKPT, tact) con el listado de todas las [[Transacción|transacciones]] activas hasta el momento y volcar el log a disco. 
2. Hacer el volcado a disco de todos los ítems que hayan sido modificados antes del (BEGIN CKPT). 
3. Escribir (END CKPT) en el log y volcarlo a disco


En la recuperación es posible que debamos retroceder hasta el inicio de la [[transacción]] más antigua en el listado de [[Transacción|transacciones]], para deshacerla en caso de que no haya commiteado, o para rehacer sus operaciones posteriores al BEGIN CKPT, en caso de que haya commiteado.





## Ejemplos 

### Undo/Redob
![[Pasted image 20241023204308.png]]

Miro de abajo hacia arriba y pongo los valores viejos de t1 (el que no commiteo) 
Voy de arriba hacia abajo y guardo los valores de T2 (que si commiteo) para asegurarme que esten 
Aborto todos los que no hayan commiteado

### checkpoint activo en redo 
![[Pasted image 20241023210057.png]]

Es necesario rehacer las [[Transacción|transacciones]] 2, 3 y 5 (que son las que commitearon) desde la línea 03. Entonces, asignamos B = 5, D = 8, E = 5, F = 7, H = 20. Finalmente agregamos (ABORT, T4) al log


### checkpoint activo en undo/redo



![[Pasted image 20241023211552.png]]


| T1     | T2     | T3    |
| ------ | ------ | ----- |
| L1(X)  |        |       |
| RT1(X) |        |       |
| L1(Y)  |        |       |
| RT1(Y) |        |       |
| WT1(X) |        |       |
| CT1    |        |       |
| U1(X)  |        |       |
| U1(Y)  |        |       |
|        | L2(Y)  |       |
|        | RT2(Y) |       |
| RT3(Z) | L2(Z)  |       |
|        | RT2(Z) |       |
|        | WT2(Z) |       |
|        | C      |       |
| L3(X)  |        | L3(Z) |
|        |        |       |
| U2(Z)  |        |       |
| RT3(X) |        |       |
| U3(Z)  |        |       |
| U3(X)  |        |       |
