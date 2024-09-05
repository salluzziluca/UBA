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
Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin fijo, no las puedo mover. Quiero utilizar el aula para dar la mayor cantidad de charlas. 

La facultad tiene una sola aula y quiero dar la mayor cantidad de clases posibles

Agarro el primero mas corto y lo comparo con los que los siguientes. Los que se me superponen los descarto, agarro el mas corto que no se me superponga. Hago lo mismo desde este evento

```python 
def scheduling(horarios):
	horarios_ordenados = ordenar_por_horario_fin(horarios)
	charlas = []
	for horario in horarios_ordenados:
		if len(charlas) == 0 or not hay_interseccion(charlas[-1], horario):
			charlas.append(horario)
	return charlas

def hay_intersection(anterior, nueva):
    return anterior[FIN] > nueva[INICIO]:
```

## Árboles Huffman
Plantea una forma de comprimir texto en base a la frecuencia de caracteres en el mismo. 
Utiliza dos [[heap#Heap minimal|heap minimales]]  de forma auxiliar para ir generando el árbol de códigos. Los que aparecen mas que sean mas faciles (igual que en morse)

Ej: paralelepipiedo

| letra | frecuencia |
| ----- | ---------- |
| p     | 3          |
| A     | 2          |
| R     | 1          |
| L     | 2          |
| E     | 3          |
| I     | 1          |
| D     | 1          |
| O     | 1          |
|       |            |
Encolo en un primero heap minimal. Cuando desencolo me devuelve los valores de menor a mayor

Desencolamos dos elementos y creamos un arbol con t1 y t2, el cual va a tener el valor de la suma de las frecuencias de ambos. 
Ej Si tengo O y R, ambas de 1 de frec, su arbol me va a quedar ![[Pasted image 20240902141537.png]]
Ese arbol lo reencolo. 

Por ultimo codifico.
![[Pasted image 20240902141625.png]]
```python 
def huffman(texto):
	frecuencias = calcular_frecuencias(texto)
	q = heap_crear()
	for caracter in frecuencia:
		q.encolar( Hoja(caracter, frecuencia) )
	while q.cantidad() > 1:
		t1 = q.desencolar()
		t2 = q.desencolar()
		q.encolar( Arbol(t1, t2, t1.frecuencia + t2.frecuencia) )
	return codificar(q.desencolar())


```


## Problema del cambio
Quiero dar vuelto usando la menor cantidad de monedas

Opcion uno: agarro la mas grande posible sin pasarme. Calculo lo que me falta y repito lo mismo

Mejora: me quedo con el modulo, por cada moneda chequeo una sola vez. Divido el total por la moneda. Es decir, si tengo 37 en vez de hacer 10 chequeo 10 chequeo 10 chequeo le resto directo 3 de 10

Esto es O(tipos_monedas)

No es perfecto. Si tengo un sistema monetasrio 1 5 6 9 voy a terminar con 9 1 1 cuando lo mas eficiente seria 5 + 6. Esto es por la localidad

## Problemas de compras con inflación

Tengo una lista de productos. Tengo inflacion todos los dias. Como hago para comprar lo mas posible gastando la menor guita. Puedo compar un solo producto por dia.

Agarramos el mas caro primero jijo ESTO SI QUE ES ARGENTINAAAAA


## Problema de la carga de combustible

Un cambion viaja de una ciuidad a otra deteneidnose a cargar nafta cuando necesita. E Tanque permite viajar K kilometros

Las estaciones estan distribuidoas siendo d_i distancia desde i-1 hasta i 

donde me conviene cargar poara detenerme la menor cantidad de veces

Conviene siempre la estacion mas lejana en la que te alcance al nafta


## Problema de la mochila
Tengo elementos con peso y con valor. Quiero meter la mayor cantidad de elementos con el mayor valor posible para maximizar la ganancia. Puedo ordenarlos por peso, ordenarlos por valor u ordenarlos por valor/peso. Ambas tienen contraejemplos.

Lo mejor es calcular por valor/peso y por mayor valor

### Problema de la mochila II
En vez de guardar los elementos enteros, puedo guardar partes (me estoy robando tortas de una pasteleria). ACa nos conviene quizas meter todo entero y despues cuando ya no nos queda tanto lugar y metiendo de a partes

## Problema de Scheduling II
Tengo tareas con duracion y deadline, pero puede hacerse en cualquier momento siempre que sea antes del deadline
Buscamos minimizar la latencia con las que las tareas se ejecutan, es decir, cuanto despues de su deadline terminan L= f-d


Podemos ordenar por duracion de tarea(t_i): nos comemos el deadline!!
Si  yo tengo $[(1, 100), (10,10)]$ siendo el primero valor duracion y el segundo deadline nos conviene agarrar la segunda porque termina antes y la estamos pateando  

Ordenando por los que les queda poco para llegar al deadline 
 $[(1, 2), (10,10)]$. Vamos a elegir la 10,10 cuando la otra era mas urgente

Ordenamos por deadline: Es optimo!!
Decimos que un schedule tiene una inmversion si tenemos dos elementos $s_{1} \ y \ s_j$ tal que $i<j \ pero \ deadline_i >deadline_j$ (en criollo, un elemento con deadline posterior viene antes que uno con deadline anterior)

Invertir no puede aumentar la latencia

Para no tener inversiones solo pueden variar la posicion de teareas que tengan mismo deadline y sean consecutivas. La ultima de estas va a tener mayor latencia

Si tengo una schedule sin inversiones, quiere decir que tengo latencia maxima. Pero pueden o no ser optimos segun cuantas tareas terminen al mismo tiempo (de esto no se encarga la inversion)

![[Pasted image 20240905131547.png]]



Al menos existe un schedule sin inversiones optimo