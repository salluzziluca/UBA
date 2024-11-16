---
Dia: 2024-11-16
dg-publish: true
---
Son algoritmos diseñados para correr en tiempo polinomial, encuentran una solucion que grantiza estar cerca del optimo. Esto es demostrable (podemos demostrar que encontramos solucion cerca del optimo).
Esto es debido a que hay problemas muy dificiles en los que el tiempo polinomial es probablemente inconseguible


## Problema de Balanceo de Carga 
Dadas m Máquinas y un conjunto n de trabajos, donde cada trabajo j toma un tiempo tj, se desea asignar el trabajo en las Máquinas de forma balanceada.
Dada una asignación A(i) para la Máquina i, su tiempo de trabajo es


Y queremos encontrar la asignación que minimice el máx valor de Ti, que también representa el tiempo que se tardará en finalizar todos los trabajos
El Problema de Balanceo de Carga es NP-difícil
### greedy
ordenando los trabajos de mayor a menor y dandole cada trabajo al que menos tiempo asignado tenga funciona hasta ahi 
Si m >= n, Greedy es siempre óptimo
Si n > m, para estos trabajos en orden, los primeros m+1 trabajos cuestan lo mismo o más que el trabajo m+1. Cualquier solución óptima debe asignar dos de esos trabajos a la misma máquina (demostrable por palomas y nidos)

cota de solucion optima ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeJojid2iyqx4FwYUhMuhf8KMq6KvbrpbCgEA_euYHI0yQdhWL5gF7Y9LQV1ytQyFa4uv5QwPwBD7bkh09I6GUVRPMVKNKJWLZsk5KClnRk2mAuDWTiDZFlcrsa1QdQa3LVdUso-CpA4RIoBklKLc4eHjtqrl0=s2048?key=mdz1rszErP6Jo6syDALanw)