En los 3 se asumen que los solapamientos son recuperables y que evitan rollbacks en cascada (ver [[Recuperabilidad]])

## Algoritmo UNDO (inmmediate update) 
>[!quote] Antes de que una modificación sobre un ítem X ← v_new por parte de una transacción no commiteada sea guardada en disco (flushed), se debe salvaguardar en el log en disco el último valor commiteado vold de ese ítem.


1. Cuando al transaccion T_i modifica el item X reemplazando su valor v_old por v, se escribe (WRITE, T_i, X, v_old) en log. Luego se hace flush al log del disco
2. El registro (WRITE, Ti , X, vold ) debe ser escrito en el log en disco (flushed) antes de escribir (flush) el nuevo valor de X en disco (WAL).
3. Todo ítem modificado debe ser guardado en disco antes de hacer commit.
4. Cuando Ti hace commit, se escribe (COMMIT, Ti) en el log y se hace flush del log a disco (FLC).

Los tres primeros puntos aseguran que todas las modificaciones realizadas sean escritas a disco antes de que la transacción termine. 
De esta forma, una vez cumplimentado el paso 4, ya nunca será necesario hacer REDO. Si la transacción [[Fallas|falla]] antes ó durante el punto 4, será deshecha (UNDO) al reiniciar. 
Se considera que la transacción commiteó cuando el registro (COMMIT, Ti) queda escrito en el log, en disco


### Reinicio
Cuando el sistema se reinicia 

1. Se recorre el log de adelante hacia atrás, y por cada [[transacción]] de la que no se encuentra el COMMIT se aplica cada uno de los WRITE para restaurar el valor anterior a la misma en disco. 
2.  Luego, por cada [[transacción]] de la que no se encontró el COMMIT se escribe (ABORT, T) en el log y se hace flush del log a disco.

El reinicio es idempotente. Si se ejecuta varias veces (hay una [[Fallas|falla]] en el reinicio) no pasa nada

![[Pasted image 20241022195555.png]]

## REDO (deferred update)

>[!quote] Antes de realizar el commit, todo nuevo valor v asignado por la transacción debe ser salvaguardado en el log, en disco.

¿Ésto me obliga a guardar el ítem modificado en disco antes de commitear la transacción que lo modificó? 
No, sólo el registro de log! De hecho, en el algoritmo REDO el ítem es actualizado en disco luego de commitear la transacción.

El algoritmo debe commitear sin guardar en disco los items modificados. 
Ante una falla posterior al commit, sera necesario hacer un REDO de todos los valores que la tranasccion habia asiganado a los items 
Esto implica recorrer todo el log de atras para adelanteaplicando cada uno de los write 


### reinicio 
1. Se analiza cuales transacciones commitaron 
2. Se reocrre el log de atras para adelante volviendo a aplicar el wirte de las transacciones que ya commitearon , para asegurar que quede actualizado el valor de cada ítem.
3. Luego, por cada transacción de la que no se encontró el COMMIT se escribe (ABORT, T) en el log y se hace flush del log a disco.


## Algoritmo UNDO/REDO 
Buscamos evitar que una transaccion que se grabo a disco no haya commiteado 