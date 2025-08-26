---
Dia: 2025-08-26
dg-publish: true
---
Algoritmo usado para hacer scheduling de tareas entre threads. Worker threads inactivos roban trabajo a threads ocupados, para realizar balanceo de carga.

Cada thread tiene un Deque (double end queue). Donde almacela las tareas listas para ejecutar. Cuando un thread termina de hacer su tarea, coloca las subtareas que se generaron a partir de haber terminado su tarea actual al final de la cola. 

Luego toma la siguiente tarea para ser ejecutada del final de la cola. 

Si su cola esta vacia, el thread no tiene mas trabajo y trata de robar tareas del inicio de la cola de otro thread (random)

Lo importante es que las tareas del final van a ser las mas chicas y las de el principio las mas grandes. 

Ej: Tengo todas tareas grandes de abrir leer y contar las lineas de 10 archivos. Agarro  y ejecuto la primera tarea (abrir leer y contar lineas de 10 archivos).  La primera subtarea va a ser hacer eso con el primer archivo. Al hacer eso con el primer archivo agrego, al final de la cola, las otras 9 subtareas de procesar 1 solo archivo.

De esa forma tendria al principio de la cola tareas grandes y al final tareas mas chicas. 

