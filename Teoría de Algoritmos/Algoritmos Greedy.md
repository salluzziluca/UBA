---
aliases:
  - algoritmo greedy
  - greedy
  - Greedy
  - Algoritmo Greedy
  - algoritmos greedy
---
> Hago lo que mas me conviene AHORA, no pienso en el futuro, solo en el presente

**Aplicamos una regla sencilla que nos permita obtener el óptimo local a mi estado actual.**. Aplicamos esa regla iterativamente buscando que nos lleve al optimo general

Es deontologista

El tema es que nos puede llevar a maximos locales 
[[Recorridos Grafos#Algoritmo de Prim|prim]], [[Recorridos Grafos#Agoritmo de kruskal|kruskal]] y [[Recorridos Grafos#Dijkstra|dijkstra]] son greedys


- No siempre dan el resultado optimo
- Demostrar que dan el optimo es dificil 
- Son intuitivos y faciles de entender
- suelen ser rapidos
- pueden ser buenas aproximaciones para problemas complejos
- suelen ser faciles de codear


## Problema de Scheduling 
Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin. Quiero utilizar el aula para dar la mayor cantidad de charlas. 

La facultad tiene una sola aula y quiero dar la mayor cantidad de clases posibles
