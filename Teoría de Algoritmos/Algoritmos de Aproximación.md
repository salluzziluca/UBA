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
El Problema de Balanceo de Carga es [[NP (nondetherministic polynomial)|NP]]-difícil
### [[Algoritmos Greedy|greedy]]
ordenando los trabajos de mayor a menor y dandole cada trabajo al que menos tiempo asignado tenga funciona hasta ahi 
Si m >= n, [[Algoritmos Greedy|Greedy]] es siempre óptimo
Si n > m, para estos trabajos en orden, los primeros m+1 trabajos cuestan lo mismo o más que el trabajo m+1. Cualquier solución óptima debe asignar dos de esos trabajos a la misma máquina (demostrable por palomas y nidos)

cota de solucion optima ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeJojid2iyqx4FwYUhMuhf8KMq6KvbrpbCgEA_euYHI0yQdhWL5gF7Y9LQV1ytQyFa4uv5QwPwBD7bkh09I6GUVRPMVKNKJWLZsk5KClnRk2mAuDWTiDZFlcrsa1QdQa3LVdUso-CpA4RIoBklKLc4eHjtqrl0=s2048?key=mdz1rszErP6Jo6syDALanw)

Una de nuestras Máquinas en T tuvo más carga que cualquier otra, ¿cómo?
Habrá habido un último trabajo tj en ser colocado en esa máquina
Ese trabajo debe tener índice mayor o igual a m+1, porque los primeros m trabajos se asignan a máquinas distintas, entonces
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUf-xXIpOnVUVOakN7E_lEcaLLA6tCpY0oHA0pNJ_O0BvLoJAtMMo6FraQXaOjp108_jFUUrN5XV-jMJu1rQUUOF8BndONuEUX63bNb4D9NZeCWsCcxe_hMhVYRkhGMDjSJPf-02NScVCYHJrpNnMGnRgDUfdkxu=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcF7xThz3s-sTgYUwuRoZfc4SxuYDVZQvvrTDihAI7o9OTHi2CqBHUC6ZZbC5NnrJ1lVCzTqCsX448OSI3y2Ln53g2bp0zQEK-bqXrqPzhRiMoPL1TaLBpRuKjvpXHyZ7Z86fE5kz7QPt9Ulngz56dtF1quXBH8=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdFRGoB5Glv5tVG5PYGiqUAevAeDqtXCC2w-Cje_3f98XWSPEQtMm90ELhqBl85-x_kWguzRCyAYu_LyNnjVqY4OoHvldR-d0ciy_VtOG59Vw9iQUslMi1P95AyDCZHXwGXcK0k5XwdHX7fuV3ARg394MSkb0o=s2048?key=mdz1rszErP6Jo6syDALanw)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcZb2pIPW5efkKyKHsi1DkVGG8BCYve8_6SET6dT0JwBP9YEJluafYTxwNLfoQQeP8pMZdDv4o0KPFv1jtBscr3DFPV3PWArNEwkWvXFnddlXECbXbYlgggW_f2LKH9I4HpGARiAm7lzAIy9pYQe4nFF-6XTObM=s2048?key=mdz1rszErP6Jo6syDALanw)**


## [[Vertex Cover]]: Rduccion 

Busco convertir la entrada de [[vertex cover]] a la entrada de ser cover. 
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcOt8Eir5zkiX9WYGzxmEycJQdffmb_6XvXBIHBnGB8m5TWOPDUkjXIOpecxjNdzNTa3R65xmRaOZoePqVAKKICzGfC0ICK2JocydlVfe8IA7ktfeShRfr2Te-pd8zY98iIwQ36auihZvl7L5j5T-p5D2VkQAu8=s2048?key=mdz1rszErP6Jo6syDALanw)**
Para cada Vértice se define el subconjunto del Vértice como todas las aristas que inciden al Vértice. Queremos encontrar una cobertura de E, todas las aristas.

Set Cover encuentra la forma de cubrir todos los elementos. Los Subsets de aristas encontrados son los vértices a utilizar

Esta aproximación nos da una solución como mucho H(d) veces el óptimo para el Problema de [[Vertex Cover]]

### Independent set

Si encuentro un [[Vertex Cover]], es cierto que el complemento (todos los vértices que no utilizo) es un Independent Set. Ajustando todos los pesos a 1, por lo tanto:

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdgt1brThw0HiIfw47bAUfv28vOxfgf5i3gtJuF6JtVAfydNBFY2TRYLQJJbnRNld3imdV6awPiqz6Tmw6Wo_agpUx5PU1se2axTv9ibl4TEndW8cPk8l8AdYnQOZp1V3L0y9fs-54np4pdQpvm4yxeSLuM9RhW=s2048?key=mdz1rszErP6Jo6syDALanw)**

Nos gustaría aprovechar la solución de [[Vertex Cover]] para resolver Independent Set
Imaginemos un [[Grafos|Grafo]] que tiene la misma cantidad, |V|/2 vértices que pertenecen al [[Vertex Cover]], y |V|/2 vértices que forman el máximo Independent Set
Sucede que dado el margen de error de la aproximación de [[Vertex Cover]], perfectamente podría ocurrir que el [[Vertex Cover]] obtenido sea todos los vértices V

Lo que nos dejaría con una aproximación del máximo Independent Set de… Set Vacío

### Pricing Method

El Pricing Method como metodología utiliza esta perspectiva económica de precios para llegar a la solución por Aproximación. Veamosla para [[Vertex Cover]]

Si las aristas son agentes de esta economía, debe haber algún tipo de idea que establezca qué precios son acordes (fairness) y están dispuestas a pagar, y qué precios serían excesivos (unfair)

En este caso, los precio son acordes si, para cada vértice i, las aristas adyacentes a ese vértice no tienen que pagar más que el costo de ese vértice: 

La Metodología además nos provee una forma de medir qué tan buena es la Aproximación. Para cualquier solución S*, veamos si podemos ajustar la suma de los pesos utilizados:

![[Pasted image 20241116163932.png]]Si unvertice cuesta 10 no puede ser que todas las aritas para llegar ahi sumen mas que ese precio

![[Pasted image 20241116164315.png]]

Cuales solucion que uno puede plantear suma como maximo el valor del precio de las aristas

asignar todos los precios en 0 
- Mientras haya una arista uniendo dos vértices que no estén “pagos” 
- seleccionar esa arista 
- incrementar el precio de esa arista dentro de un precio acorde, no excesivo 
- La solución S será el set de todos los vértices “pagos"

![[Pasted image 20241116164943.png]]No parece justo (“fair”) que una arista pague por ambos de sus vértices. Pero esta “unfairness” es acotada, como mucho a cada arista se le cobra dos veces.


Esto nos permite poder ajustar los vértices y dejarlos pagos sin incurrir en costos de las aristas por encima de una cota, y en consecuencia, acotará también qué tan lejos está la solución de una solución óptima

![[Pasted image 20241116165342.png]]


### [[Programación Lineal]]

Podemos decir que cada xi vale 1 si pertenece al [[Vertex Cover]], 0 si no
Esto no es [[Programación Lineal]]. Esto es Programación Entera
Se trata de un problema similar, donde las variables solamente pueden tomar valores enteros
Y resulta que para este problema, no hemos encontrado soluciones en tiempo polinomial. Lo cual es razonable, ya que acabamos de hacer una reducción
![[Pasted image 20241116170052.png]]


Relajo y lso valores pueden estar entre 0 y 1 en vez de ser 0 o 1

![[Pasted image 20241116171007.png]]
Esta metodología siempre encuentra un valor de la función objetivo mejor o igual a la solución óptima de [[Vertex Cover]]


![[Pasted image 20241116171729.png]]


## Scheduling, aproximacion 

El problema de elegir el más corto: quizás hay otros dos más largos que van mejor ¿Habrá una peor situación?
Cada intervalo seleccionado por ser más corto, puede bloquear otros de la solución óptima. ¿Cuántos?
1. Demostrar: un intervalo de la solución A choca como máximo con dos intervalos de la óptima O (contradicción)
2. Cada intervalo en O puede estar también en A, o choca con un intervalo en A
Contemos todos los intervalos de O según su relación con A.

![[Pasted image 20241116172205.png]]


## Metodologia 4: Programacion dinamica y rendondeos