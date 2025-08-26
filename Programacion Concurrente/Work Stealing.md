---
Dia: 2025-08-26
dg-publish: true
---
Algoritmo usado para hacer scheduling de tareas entre threads. Worker threads inactivos roban trabajo a threads ocupados, para realizar balanceo de carga.

Cada thread tiene un Deque (double end queue). Donde almacela las tareas listas para ejecutar. Cuando un thread termina de hacer 