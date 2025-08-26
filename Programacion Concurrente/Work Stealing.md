---
Dia: 2025-08-26
dg-publish: true
---
Algoritmo usado para hacer scheduling de tareas entre threads. Worker threads inactivos roban trabajo a threads ocupados, para realizar balanceo de carga.

Cada thread tiene un Deque (double end queue). Donde almacela las tareas listas para ejecutar. Cuando un thread termina de hacer su tarea, coloca las subtareas que se generaron a partir de haber terminado su tarea actual al final de la cola. 

Luego toma la siguiente tarea para ser ejecutada al final de la cola. 

Si su cola esta vacia, el thread no tiene mas trabajo y trata de robar tareas del inicio de la cola de otro thread (random)