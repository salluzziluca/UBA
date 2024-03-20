> EL usuario puede acceder al kernel, pero se busca limitar siempre la ejecución directa.
> 

Cada vez que el procesador pasa de modo kernel a modo usuario, el kernel antes de irse pone un timer. Despues de ese tiempo el kernel se despierta

IOPL (I/O Privilege Level): son 4 bits que te muestran en que lvl de privilegio estas. 0 es kernel 3 es user. Permite saber si quien tiene en este momento acceso al procesador puede ejecutar determinadas acciones
![[Pasted image 20240320194817.png]]