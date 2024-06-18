Que es un deadlock? describa por lo menos 3 casos. 
Por deadlock nos referimos al momento en el que la ejecución de uno o mas programas concurrentes se ve detenida por la incapacidad de adquirir el lock del contexto actual.
Esto se puede dar por la necesidad de recursos compartidos: 
El thread1 necesita un recurso del thread2 y este a su vez necesita otro recurso del thread1 para avanzar. Esto hace que ambos se queden trabados y la ejecución se detenga
Por la espera de un recurso externo: un thread en particular se queda lockeado mientras espera un recurso exterior (vease por ejemplo un json enviado por una API) y como nunca lo recibe nunca suelta el lock