## Fuerza bruta
Tenemos un problema combinatorio-> tenemos que probar todas las combinaciones/soluciones/permutaciones

ordenamiento por fuerza bruta: ![[Sorting#Ordenamiento por Fuerza Bruta]]
## Regla Básica de Backtracking
> Cuando sabemos que una combinación parcial que ya construimos no va a llevar al resultado válido, **podamos** y volvemos para atrás


1) Si ya encontre una solucion, la devuelvo y termino.
2) Avanzo si puedo
3) Pruebo si la solución parcial es válida
	1) Si no lo es, retrocedo y vuelvo a 
	2) Si lo es, llamo recursivamente y vuelvo a 1)
4) Si llegue hasta aca, ya probe con todo y no encontre una solucion
(no válido para todos los casos, pero el esquema suele ser similar)


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

es O(2^n)



## Ej3: [[Grafos Hamiltonianos|Caminos Hamiltonianos]]
Tengo un grafo y busco ssu camino hamiltoniano


![[Pasted image 20240908204402.png]]
Voy usando un [[Recorridos Grafos#En profundidad DFS (Depth First Search)|DFS]], desmarcando los visitados cuando no hay una solucion por este camino, para poder visitarlo de vuelta desde otra rama.
Arranco en el 0 voy al 5, voy al 3, voy al 2, no llego a nada, vuelvo para atras, 
0 5 3 5 7 6, me falta el 2, vuelvo al 3, no tengo opciones, del 5 voy al 6
0 1 5 6 7 4 3 2 

```python 
def camino_hamiltoniano_dfs(grafo, v, visitados, camino):
    visitados.add(v)
    camino.append(v)
    if len(visitados) == len(grafo):
        return True
    for w in grafo.adyacentes(v):
        if w not in visitados: # Esta es en sí nuestra poda
            if camino_hamiltoniano_dfs(grafo, w, visitados, camino):
                return True
    visitados.remove(v)     # Permitiendo volver a venir a este vértice
    camino.pop()            # por otro camino
    return False
```


## EJ4 coloreo de grafos
Dado un grafo de k colores diferentes, es posible pintar los vertices de tal forma que ningun par de vertices adyacentes tenga el mismo color?
![[Pasted image 20240908205357.png]

1. Si todos los países están coloreados, devuelvo True 
2. Pruebo colorear con un color el siguiente país
3. Verifico si la solución parcial es válido
	1. Si no lo es, retrocedo y vuelvo a 2) a probar con otro color 
	2. Si lo es, llamo recursivamente y vuelvo a 1) → Si no encontramos solución, volvemos a 2) a probar con otro color  
4. Si llego hasta aca, ya probe con todo y no encontre una solucion


## Ej5 Sudoku
![[Pasted image 20240912103540.png]]
Si llenara todo de unos, despues todo de dos, despues todo de 3... ...despues todo de unos menos una casilla a la que le pongo un 2, despues todo de unos menos una casilla a la que le pongo un 3... Seria **fuerza bruta**


Para hacerlo con **backtracking** agarro un cuadrado y me fijo si por fila, columna y cuadrante puedo poner un 1. Luego voy a otro casillero y chequeo por las mismas 3 variables, pero teniendo el cuenta el numero anterior. Es muuuy ineficiente porque tengo que podar varias veces.

Puedo pensarlo con grafos
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUc5JM4I4822Il0z7PQkQc0GBFBDjfAGJ4DYicbTCxl43ISQI46Uq3DA4dbTymO9xSK8UV4CdECqpkPUtYpBNPk5et4pp8KoKeID9Zq4-UBJ7e3l0a19P-0ZnMXrgEgAZ2kLehSdB_s581IRjUHBviZ060yBRJM5=s2048?key=gKqW96ITNxjx2HmFvGD60A)**
Y para resolverlo hago COLOREO CON 9 COLORES LESFUKINGOOO