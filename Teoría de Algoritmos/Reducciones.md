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


## EJ1: ordenar vs encontrar el maximo 
Ordenar es al menos tan dificil como encontrar el maximo en un arreglo. Redujimos encontrar el maximo a ordenar

Ademas, sabemosq ue hay un algoritmo polinomial para ordenar-> encontrar un maximo tambien es polinomial

## Ej2: Bipartite Matching 
Ejercicio de redfes de flujo. Efectivamente s ehizo una reduccion, se busco llevarlo a redes de flujo y listo, resuelto. 

## Ej3: independen set y N-reinas
conviene reducir N-Reinas a Independent Set o Independent Set a N-Reinas?


## Ej4: Subset Sum y problema de la mochila