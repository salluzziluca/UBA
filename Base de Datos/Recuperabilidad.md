---
dg-publish: true
---
La serializabilidad de las [[Transacción|transacciones]] ya nos asegura la propiedad de aislamiento. 
Nos interesa ahora asegurar que una vez que una [[transacción]] commiteó, la misma no deba ser deshecha. Esto nos ayudará a implementar de una forma sencilla la propiedad de durabilidad.
Definición: Un solapamiento es recuperable si y sólo si ninguna [[transacción]] T realiza el commit hasta tanto todas las [[Transacción|transacciones]] que escribieron datos antes de que T los leyera hayan commiteado.


Un [[Sistemas de Gestion de Bases de Datos|SGBD]] no deberia jamas permtir la edecucion de un solapamiento no recuperable 


Si tengo dos [[Transacción|transacciones]] $T_{i}$ y $T_{j}$ y T_i leyo un [[dato]] de T_j, si J rollbackea, hay que ir a T_i a cambiar eso tmb (y rezar porque no haya commiteado). Esto nos puede generar una cascada de rollback


Que un solapamiento sea recuperable, no implica que no sea necesario tener que hacer rollbacks en cascada de [[Transacción|transacciones]] que aún no commitearon.

Para evitar rollbacks de cascada loq ue conviene hacer es no leer valores que todavia no fueron commiteado. SI evitamos rollbacks en cascada esa transaccion se vuelve recuperable



![[Pasted image 20241022192842.png]]


Algunos locks tambien pueden ayudar a a asegurra recuperabilidad
El protocolo [[S2PL (Strict 2 Phase Locks)|2PL estricto]] ayuda. En caso de no diferencias tipos de lock, se convierte en [[R2PL (Rigurous 2 Phase Locks)|2PL riguroso]] 