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

Opcion uno: agarro la mas grande posible 