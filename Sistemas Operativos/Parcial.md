Que es un deadlock? describa por lo menos 3 casos. 
Por deadlock nos referimos al momento en el que la ejecución de uno o mas programas concurrentes se ve detenida por la incapacidad de adquirir el lock del contexto actual.
Esto se puede dar por la necesidad de recursos compartidos: 
El thread1 necesita un recurso del thread2 y este a su vez necesita otro recurso del thread1 para avanzar. Esto hace que ambos se queden trabados y la ejecución se detenga
Por la espera de un recurso externo: un thread en particular se queda lockeado mientras espera un recurso exterior (vease por ejemplo un json enviado por una API) y como nunca lo recibe nunca suelta el lock


Un inodo tiene sus permisos, su numero de hard links, el UID (id dueño) y GID (id grupo dueño), size, fecha de creacion y modificacion y punteros a datos. 12 punteros. 9 a datos directos, el 10 a datablocks, el 11 a datablocks de datablocks, el 12 a datablocks de datab,ocks de datablocks