---
Dia: 2024-11-17
dg-publish: true
---
El mundo es aleatorio!!!

Le permitiremos al algoritmo tomar deciisiones al azar independientemente de los valores de entrada. Esto es un factor completamente interno del algoritmo. 

Un algoritmo deterministico eficiente que alcula ra respuesta correcta puede verse como un caso particular de un algoritmo randomizado qeu da la respuesta correcto con alta probabilidad. 
O tambien puede verse como un algoritmo randomizaco que da siempre la respuesta correcta con una expectativa de complejidad temporal eficiente. 

Un algoritmo randomizado puede resolver un problema que quizas uno deterministico no puede. Son conceptualmente mas sencillos de entender e implementar. 

No requieren mantener estado interno o memoria del pasado. 

En sistemas distribuidos permite quebrar la simetria. 


## Problema de encontrar la media 
La mediana es el valor medio 
2 5 7 1 3. 1 2 3 5 7 la mediana seria 3. 
Ordenando es muy facil, O(n logn) para ordernar y O(1) para acceder a la posicion k. K=  (n+1)/2 si es impiar k = n/2 si es par 


## Problema de la Seleccion
Quiero encontrar el valor k de una array desordenado si estuviera ordenado
Si me piden el primero o el ultimo calculo directo max o min en On

Vamos a usar Division y Conquista 
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeYBA2Flhm_uQpKAolYV8qTHIquaT-KKjzLeoqljKO9VNMH0EgHeTOH0I2uTNUJrZSqXBwykNECSFs3Yog2W4jzgYmWhIovNfJWggIegzW4-B2w8ZgL2IQYOec8mvzntBVxqMC8-FD3j1-yg9Vqsu1fkX8mWUMP=s2048?key=iRbwHtP-n_pIwaOn1yASjg)**
Elegimos un pivote y nos fijamos si el k esta antes o despues de el. 
siempre da la solucion pero puede tardar mucho
```python 
def select(S, k):
  ai = elegir_pivot(S, k)
  for elem in S:
    Agregar elem a S- si elem<ai
    Agregar elem a S+ si elem>ai
  if |S-| == k-1: 	return ai
  if |S-| >= k: 	return select(S-, k)
  else: 			return select(S+, k-1-|S-|)
  ```
Lo raro es que es muy eficiente si elegimos como pivot la mediana, pero eso es trampa. 

En realidad, solo necesiamos un pivot bastante bien centrado.
el peor caso es tener un pivote muy mal centrado que solo nos ahorre un elemento a la vez: 
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcSajBtEAOCXulvcZHCbQkNCEWSgo8h0PeG9cRqCWvexoKmebkp4qylJEhYj6uAcReseaHF-NusCRIUFOT22r6DVJxDtKfJjz1D6pOXnBPVjVY99Yr8cPBvi549NmUmGbtRid0_pgswq994H2FaE0MyrsHn2LE=s2048?key=iRbwHtP-n_pIwaOn1yASjg)**
al final va a convenir elegir el pivote aleatoriamente

![[Pasted image 20241118152808.png]]

Esto probabilisticamente no esta tan mal ya que la mitad de los pivotes estan bien centrados


Decimos que el Algoritmo está en fase j, si la cantidad de elementos del set en consideración está entre $n(¾)^j$ y $n(¾)^{j+1}$
Para pasar de la fase j a la fase j+1, necesitamos al menos desestimar ¼ del total de elementos. Se logra para la mitad central de Pivots, con probabilidad ½.
La cantidad esperada de iteraciones para avanzar de fase es 2.
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUd2BLVJ30s8bOSxrDRJI56yo-CT-M6FCknsWdE7cbPaWCGKddSigRCgZt0Tkb4V4uZFyL51t54cwz8FDDlOkZTmmyrrUPz2bvrqVDIX2t3PGCvCpD8idzg3sRNaKh2SHffVDO5jeCYZJqmb30SVGMhUb2xE_05J=s2048?key=iRbwHtP-n_pIwaOn1yASjg)**

Gracias a la Linealiadad de la Esperanza y la sumatoria geometrica convergente: 

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfUdahWWFo7MAhtXfX5xAa8yuM0mEsn0UeEQykmM_ehi00A4OXB2Qeq1GCqKb9KoPu6hao1mH4f6wcYlbhO5LOihQ5uaV2Yh5OXQbeTxsxSuxX165rz6ZJBOBiyTXcdBt8Y6DvpbU7UyDW-YI5pdHKAZSLrqpbJ=s2048?key=iRbwHtP-n_pIwaOn1yASjg)**

Nos queda que la complejidad esperada es O(n)