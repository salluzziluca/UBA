## Fuerza bruta
Tenemos un problema combinatorio-> tenemos que probar todas las combinaciones/soluciones/permutaciones

ordenamiento por fuerza bruta: ![[Sorting#Ordenamiento por Fuerza Bruta]]
## Regla Básica de Backtracking
> Cuando sabemos que una combinación parcial que ya construimos no va a llevar al resultado válido, **podamos** y volvemos para atrás

### Ordenamiento con Backtracking
Cuando veo que el actual es menor que el anterior, vuelto para atrás, se que por esa rama no va a poder ser.

### [[Grafos]] con Backtracking 
Las opciones son dos, ir moviendonos sin un recorrido o hacerlo con un [[Recorridos Grafos#En profundidad DFS (Depth First Search)|DFS]], desmarcando los visitados cuando no hay una solucion por este camino, para poder visitarlo de vuelta desde otra rama.


## Ej1: Reinas

Tablero de NxN, ubicar a N reinas de de manera tal de que ninunga pueda comerse a ninguna
![[Pasted image 20240908195134.png]]
Esto ya no es solucion, no importa lo que yo haga esto no va a ser valido. Entonces ya pruebo otra variacion

![[Pasted image 20240908195228.png]]
Esto funciona asi que sigo

![[Pasted image 20240908195238.png]]
sigoo

Esto no me termina de servir porque no puedo meter en ningun lugar la 4ta reina


![[Pasted image 20240908195337.png]]

vuelvo al inicio

al final arrancar desde el 0,0 tampoco funciona

podemos ir por columnas 
![[Pasted image 20240908195449.png]]


## Ej2: Independent Set 
QUiero guardar en un grafo K elementos. Debo elegir K vertgices en los cuales guardar cada uno. PERO no quiero  que haya dos elementos adyacentes. Es decir, que una arista los una. Quiero una lista de vertices que no tengan aristas entre ellos
![[Pasted image 20240908201731.png]]
En este grafo los vertices 0, 2, 4 y 6 no tienen aristas entre ellos

```python 
def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w: continue
            if grafo.hay_arista(v, w):
                return False
    return True
    
def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n:
        return es_compatible(grafo, puestos)
    if v_actual == len(grafo):
        return False

    if not es_compatible(grafo, puestos):
        return False

    # Mis opciones son poner acá, o no
    puestos.add(vertices[v_actual])
    if _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)
```
