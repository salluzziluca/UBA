> EL usuario puede acceder al kernel, pero se busca limitar siempre la ejecución directa.
> 

Cada vez que el procesador pasa de modo kernel a modo usuario, el kernel antes de irse pone un timer. Despues de ese tiempo el kernel se despierta

IOPL: Dos bits que I/O Privilege Level