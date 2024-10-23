A veces pasa que uno ve un problema y dice: ah, este es igual a este otro 

o que veo un problema y como uno sabe resolver uno mas dificil intenta volcar el mas facil al mas dificil


Una reduccion es una herramienta para comprarar dificultad entre problemas. 

>[!quote] El problema X es al menos tan dificil de resolver como el problema Y

Redujimos Y a X
Asumimos que tenemos una caja negra que resuelve X y vamos a probar que por tener esa caja ya podemos resolver Y.

Si una instancia arbitraria de Y puede ser ser resuelta con una cantidad de pasos polinomicos y una cantidad de llamads polinomicas a la caja que resuelve X decimos que Y es reducible polinomialmente a X 
$$Y \leq_{p}X$$

En criollo: Resolver Y se reduce a reoslver X y hacer cosas para que coincida


Como X es al menos tan dificil como Y, si X se peude resolvr en tiempo polinomial, entonces Y tambien se puede resolver en tiempo polinomico

## Ejemplos de reducciones
### EJ1: ordenar vs encontrar el maximo 
Ordenar es al menos tan dificil como encontrar el maximo en un arreglo. Redujimos encontrar el maximo a ordenar

Ademas, sabemosq ue hay un algoritmo polinomial para ordenar-> encontrar un maximo tambien es polinomial

### Ej2: Bipartite Matching 
Ejercicio de redfes de flujo. Efectivamente s ehizo una reduccion, se busco llevarlo a redes de flujo y listo, resuelto. 

### Ej3: independen set y N-reinas
conviene reducir N-Reinas a Independent Set o Independent Set a N-Reinas?


### Ej4: Subset Sum y problema de la mochila

### Ej5: Busquedas I 
Podemos reducir el problema de "buscar un elemento en un arreglo ordenado" a "buscar un elemento en un arreglo(desordenado)"
De un ordenado a un desordenado si (seria peor) pero no al reves
#### Busquedas II 
Podemore reducir polinomialmente la busqueda del maximo de un arreglo a la busqueda de un elemento en un arreglo?
POLINOMILAMENTE No se puede. Porque, de vuelta, no es poilonomial 

### Ej6: 
Tenemos una caja que eleva al cuadrado 
Podemos reducir $a*b$ al problema de elevar al cuadrado 
recordemos que $$(a+b)^2= \frac{(a+b)^2 -a^2-b^2}{2}$$


---


A partir de ahora vamos a plantear los problemas de una forma más booleana. Por ejemplo, en Independent Set el problema original es encontrar el set independiente más grande, pero vamos a plantear si existe un set de (al menos) tamaño k. 
Notar: con esto resolveeríamos el problema más general, y podemos usar búsqueda binaria para buscar el máximo k. 

## Problema 1: Independent set vs vertex cover
![[Pasted image 20241023131055.png]]

Sabemos que no podemos resolver ambos en tiempo polinomial, pero,, y su dificultad relativa?

S es un set independiente de G sii V - S es vertex cover de G

Reducimos IS<= vertex cover si teenmos una caja negra que ressuelve sdi un grago tiene un VC de tamaño K. Para ver si tiene un IS de tamaño X le consultamos a lla caja negra si el mismo grafo tiene un VC de tamaño k= n-X


**Como IS ≤p VC y VC ≤p IS, son igual de difíciles.**

Entonces si puedo resolver a uno en tiempo polinomial puedo resolver el otro en tiempo polinomial


## Satisficibilidad
yo tengo clausulas, una composicion de ORs 
$$C_{1}= x_{1}\lor x_{2} \lor x_{3} or x_{4} \lor\dots \lor x_{n}$$
y despues tengo $$C_{1} \land C_{2} \land C_{3} \land\dots \land$ C_{k}$
