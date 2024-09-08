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