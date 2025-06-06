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


## [[Vertex Cover]]: Reduccion 

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

Ya vimos que si asumimos P!=NP, todos los algoritmos NP-Completos son equivalentes a la hora de obtener una solucion optima en tiempo polinomial. 
No es asi a la hora de obtener soluciones aproximadas. En el caso de Set Cover la aproximacion que vimos fue probada de estar muy cerca a la mejor posible y en el de vertex cover es la mejor que se conoce, pero aun asi esto esta muy lejos de los pedidos que nos pueden llegar a como por ejemplo "quiero que el error sea de menos del 10%".


Vamos a intentar usar PD para hacer aproximaciones arbitrariamente buenas

#### Mochila 
NP-Dificil

Tenemos una mochila con capacidad W. Cada elemento tiene peso y valor. Queremos maximizar el valor sin pasarnos de W. 

Se agrega un parametro de aproximacion $\varepsilon$, esta va a ser nuestra medida de precision. La solucion deberia entregar elementos que no superen W y una suma de valores como mucho $1+\varepsilon$ de distancia al optimo. 

El algoritmo corre polinomia,mente par aun valor dijo de $\varepsilon$, pero muestra un crecimiento exponencial a medida se disminuye ε

El nivel de Aproximación alcanzable es más potente
El algoritmo corre polinomialmente para un valor fijo de ε
El problema es que, a medida que se achica el factor ε, el tiempo de ejecución crece en medidas exponenciales
Al momento en que definimos un valor de ε que haga que la solución sea la óptima garantizada, el algoritmo deja de ser polinomial


Por PD la mochila se resuelve en O(nW), con una dependencia pseudo polinomial sobre W.

Con un W y peso chicos, es rapido aunque los valores sean muy grandes. Por lo que si lo doy vuelta, deberia ser rapido coon valores chicos y W y Peso grandes.

**Podemos aprovechar los algoritmos que son Pseudo-Polinomiales sobre los valores de los parámetros para diseñadores Esquemas de Aproximación**

$O(n2. v∗), \ con \ v∗ = max_{i}\ v_{i}$
Si todos los elementos valen 0. Es lo mas facil del mundo.
Si todos los valores son enteros pequeños, tenemos un algoritmo polinomial.
Si los valores son grandes, no hace falta usar esos, se los puede dividir por algun valor y hacer que sean mas pequeños, redondandolos

Queremos redondear todos los valores para acercarse un múltiplo de b
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUccNDI0a0ID38KdJwdwnsgq-xm0dhTmXrj00ab22puJRDKB4VpmofCL76jvlb-U4AH3Yw5EBxSzYzrU28G-H9H9cVtoZASSrQ1LbnoMMynoweKNMnNAALGDSAszngB3qyERMlLScCCT1naAj5mlUWcp6cb6zmg=s2048?key=vSCnIklsR08rHzZ-vlAHQQ)**
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUd_lMmtoyEUB8Z9MX1y_3oxKVnie9vKXtoBWuvH5meZJpngmTz2MF3cGC7BxD-UR34u2_AKbZbRMa8FleNKtX7cIJmzAon1RZhfTSUTl2LdpGyS8vrd95X5INA8wzorhxLSpl1ecLl8iuWSXjF__YtP_kFry_PV=s2048?key=vSCnIklsR08rHzZ-vlAHQQ)**

La aproximacion esta a una distancia no mayor que b. 
Todos son multiplos de b, se pueden didividir por b. 

Encontrar una solucion optima para los valores reescalados al dividir por B es una solucion equivalente al problema con los valores aproximados.

los elementos con peso mayor a W los omitimos. Asumimos que $\varepsilon^{-1}$ es entero
$$b = ε/(2n) * max \ v_{i}$$
Resolvemos el problema con todos los valores reescalados (divididos) por b. La solución aproximada al problema original es el conjunto de elementos encontrados por esta solución (que es óptima) del problema redondeado
El algoritmo se asegura siempre de dar un conjunto de elementos con suma de pesos menores a W
El algoritmo es polinomial para un valor fijo de ε

Nuestra solución original al problema de la mochila hace depender a los subproblemas sobre el valor de la capacidad disponible
Buscamos una versión que funcione bien para valores relativamente pequeños, independientemente de la capacidad de la mochila
Deberíamos condicionar los subproblemas no a la capacidad y los pesos, sino a los Valores

Guardamos en OPT(i, V) usando losi primeros i elementos y para al menos el valor de V, la capacidad mas baja de W que lo logra.  

El tamaño de la matriz necesaria para memorizar es: O(n2v∗). Una dimensión de la matriz con los n elementos, la otra, a lo sumo n veces el valor del máximo v*

![[Pasted image 20241117171448.png]]

Hay que fijarse que no lo hacemos por W, sino por V

```python 
def mochila(valor, peso, N, W, T=sum(valor)):
  OPT[0..N+1][0..T+1]
  for i in range(0, n+1):
    OPT[i][0] = 0
  for i in range(1, n+1):
    sum_valor = sum(valor[:i+1])
    for V in range(1, sum_valor):
      if V > sum_valor-valor[i]: 
OPT[i][V] = peso[i] + OPT[i-1][max(0, V-valor[i])]
      else:
        OPT[i][V] = min(OPT(n-1, V), 
                         peso[i] + OPT(n-1, max(0, V-valor[i])))
  return max(V donde OPT[N][V] <= W)
```


### Complejidad 
![[Pasted image 20241117172842.png]]

Ahora queremos demostrar que la solucion aproximada no se aleja $1+\varepsilon$ de la solucion posta. 


![[Pasted image 20241117174732.png]]

## Maximizar sumatoria 

Dado un un limite W y un conjuntod e valores enteros V. se busca un subconjunto de V que maximice la sumatoria de valores  sin exceder W. 

Greedy: agregar como vienen siempre y cuando no se pasen.  


### aproximacion O(n)
Iterar acumulando los valores a1, a2,..., an siempre que sean menores a W, ignorar mayores 
En un momento determinado, nuestra sumatoria excede W, en el elemento aj
En ese momento determinado, tenemos una sumatoria de elementos sin incluir aj que no excede a W, y aj tampoco excede W. La suma de ambas partes, excede W. Debe cumplirse:
o bien: la sumatoria de elementos sin incluir aj es mayor a W/2, usar como solución
o bien: aj es mayor a W/2, usar como solución
En ambos casos logramos una solución mejor que W/2, donde W es una cota del óptimo

Aplicar el algoritmo anterior
De la solución con la que me quedo (cualquiera de las dos), ahora ejecuto nuevamente con W - suma_obtenida, y sin los elementos utilizados.
Esto lo aplicamos (en el peor caso) n veces → O(n2)
Por la ley de Aquiles y la Tortuga, no llegaremos nunca al óptimo pero vamos a estar mucho más cerca (hay que analizar si no hay un caso que lo mantenga como 2-aproximación). 
Si aplicamos a que lo mejor que podemos hacer es W/2 por paso, podríamos decir que es una 2-n(2n - 1)-aproximación?


## Independent Set
Dado el siguiente grafo, donde cada nodo tiene un peso w(v), se desea maximizar la sumatoria de pesos de un Independent Set
Dar un Algoritmo Greedy para aproximar la solución al problema
Mostrar que cualquier vértice: 
- o es parte de la solución
- o tiene peso menor a un adyacente en esta solución
Analizar qué tan buena es la aproximación


**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcMiOJ2saRrVc1NPLWqTP7ZSIhh_xpEJ9khrxTZ7Umk0uiikxNV0AMK9xQP6mghiJqB6xfSLxpq2RZf0ed36Am9cX5p5fYvWzFJvJ_nsuhoA_1OcUYy_fwArghZmcpYqPRU_ige6gskM0t3qqF-JbZPQAsKgCJ5=s2048?key=vSCnIklsR08rHzZ-vlAHQQ)**