---
dg-publish: true
---
Si nos encontramos ante una [[Fallas|falla]] del tipo 1 o 2, cuando el sistema se reinica, la [[Bases de Datos|base de datos]] tiene que ser llevado al estado inmediato anterior al comienzo de la transaccion. Para eso necesitamos tener informacion en el log acerca de los cambios que la transaccion fue realizando. 

Para cada instruccion: 
 X → Buffer en [[memoria]] → Disco
![[Pasted image 20241022194646.png]]
![[Pasted image 20241022194635.png]]


## Regla WAL (write ahead log)

Antes de guardar un item modificado en el disco, se de escribir el regstro de log correspondiente en el disco. 

## Regla FLC 
Antes de realizaar el commit el log debe ser volcado a disco


![[Algoritmos de Recuperación]]
[[Teorema CAP]]