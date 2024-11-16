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

Una de nuestras Máquinas en T tuvo más carga que cualquier otra, ¿cómo?
Habrá habido un último trabajo tj en ser colocado en esa máquina
Ese trabajo debe tener índice mayor o igual a m+1, porque los primeros m trabajos se asignan a máquinas distintas, entonces
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUf-xXIpOnVUVOakN7E_lEcaLLA6tCpY0oHA0pNJ_O0BvLoJAtMMo6FraQXaOjp108_jFUUrN5XV-jMJu1rQUUOF8BndONuEUX63bNb4D9NZeCWsCcxe_hMhVYRkhGMDjSJPf-02NScVCYHJrpNnMGnRgDUfdkxu=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcF7xThz3s-sTgYUwuRoZfc4SxuYDVZQvvrTDihAI7o9OTHi2CqBHUC6ZZbC5NnrJ1lVCzTqCsX448OSI3y2Ln53g2bp0zQEK-bqXrqPzhRiMoPL1TaLBpRuKjvpXHyZ7Z86fE5kz7QPt9Ulngz56dtF1quXBH8=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdFRGoB5Glv5tVG5PYGiqUAevAeDqtXCC2w-Cje_3f98XWSPEQtMm90ELhqBl85-x_kWguzRCyAYu_LyNnjVqY4OoHvldR-d0ciy_VtOG59Vw9iQUslMi1P95AyDCZHXwGXcK0k5XwdHX7fuV3ARg394MSkb0o=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcZb2pIPW5efkKyKHsi1DkVGG8BCYve8_6SET6dT0JwBP9YEJluafYTxwNLfoQQeP8pMZdDv4o0KPFv1jtBscr3DFPV3PWArNEwkWvXFnddlXECbXbYlgggW_f2LKH9I4HpGARiAm7lzAIy9pYQe4nFF-6XTObM=s2048?key=mdz1rszErP6Jo6syDALanw)**


## Vertex Cover: Rduccion 

Busco convertir la entrada de vertex cover a la entrada de ser cover. 
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcOt8Eir5zkiX9WYGzxmEycJQdffmb_6XvXBIHBnGB8m5TWOPDUkjXIOpecxjNdzNTa3R65xmRaOZoePqVAKKICzGfC0ICK2JocydlVfe8IA7ktfeShRfr2Te-pd8zY98iIwQ36auihZvl7L5j5T-p5D2VkQAu8=s2048?key=mdz1rszErP6Jo6syDALanw)**
Para cada Vértice se define el subconjunto del Vértice como todas las aristas que inciden al Vértice. Queremos encontrar una cobertura de E, todas las aristas.

Set Cover encuentra la forma de cubrir todos los elementos. Los Subsets de aristas encontrados son los vértices a utilizar

Esta aproximación nos da una solución como mucho H(d) veces el óptimo para el Problema de Vertex Cover
