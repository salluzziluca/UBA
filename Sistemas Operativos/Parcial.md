Que es un deadlock? describa por lo menos 3 casos. 
Por deadlock nos referimos al momento en el que la ejecución de uno o mas programas concurrentes se ve detenida por la incapacidad de adquirir el lock del contexto actual.
Esto se puede dar por la necesidad de recursos compartidos: 
El thread1 necesita un recurso del thread2 y este a su vez necesita otro recurso del thread1 para avanzar. Esto hace que ambos se queden trabados y la ejecución se detenga
Por la espera de un recurso externo: un thread en particular se queda lockeado mientras espera un recurso exterior (vease por ejemplo un json enviado por una API) y como nunca lo recibe nunca suelta el lock


Un inodo tiene sus permisos, su numero de hard links, el UID (id dueño) y GID (id grupo dueño), size, fecha de creacion y modificacion y punteros a datos. 12 punteros. 9 a datos directos, el 10 a datablocks, el 11 a datablocks de datablocks, el 12 a datablocks de datab,ocks de datablocks



Componentes de un VFS

Inodos: estos contienen toda la informacion necesaria sobre un archivo/directorio. Tienen la cantidad de hardlinks, su tamaño, sus fechas de modificacion y creacion, sus permisos, el UID y el GID y los punteros a datos. 
Data block, los inodos apuntan a bloques de datos donde está guardada la informacion, estos pueden apuntar directamente a la info o a otro bloques de datos en caso de necesitarse mas espacio. 
Bitmap de inodos, sirve para saber cuales inodos estan libres y cuales no, el bitmap tiene un bit por inodo y este va a estar en 0 o 1 segun si esta libre u ocupados
Bitmap 


Diferencias entre thread y procesos.
Cad proceso puede tener uno o mas threads. EL proceso tiene code, data y heap, y cada thread tiene registros, program counter y stack. puede haber mas de un hilo por proceso.  **Los hilos de un mismo proceso también comparten descriptores de archivos,el contexto del filesystem y manejo de señales.**

Dentro del kernel, sin embargo, no existe distincion alguna. Para ambos se utiliza clone() (con distintos flags). De hecho fork)( y phtread_:create son wrappers de clone()



Memoria: variacion de estrucutara del address space respecto a mem fisica en base & bound, tabla de regs y paginacion. 
Explique con Diagramas

Base and bound hace referencia a dos registros homonimos que marcaban el inicio y el fin de la memoria ocupada. Cuando se necesitaba alocar mas memoria, se desplazaba el bound lo necesario hacia adelante