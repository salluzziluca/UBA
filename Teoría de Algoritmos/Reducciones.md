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


## Satisficibilidad (SAT)
yo tengo clausulas, una composicion de ORs 
$$C_{1}= x_{1}\lor x_{2} \lor x_{3} or x_{4} \lor\dots \lor x_{n}$$
y despues tengo $$S= C_{1} \land C_{2} \land C_{3} \land\dots \land$ C_{k}$$
Luego, busco que S sea true. Este problema es lo **suficientemente general** como para poder resolver un monton de cosas

### 3SAT 
Las clausulas C tiene solo 3 variables. SAT y 3 SAT son equivalente


- Cláusulas con 2 términos (w, y): reemplazar por (y ⋁ w ⋁ z) y ($y ⋁ w ⋁ \bar{z}$)
- Cláusulas con 1 término (y): Reemplazamos esa cláusula por (y ⋁ z1 ⋁ z2) y demás variantes (4) (con los negados)
- Cláusulas con 3 términos: nada que hacer
- Cláusulas con más de 3: 
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcIscgB7v6DRF_YPtudOpKNCIHe8eJBx3iqsCpVlT_wluzTyrucayVQ4B7KjQGWnLF7krxGvSQU2EO0wFjmuJ2J4M0lBZtGzdOYepYfdQEQWiPKHHmPpWQaRek0tShQR_5oMHiSTIV8VjIP4fLrRbIpNmBPtDrT=s2048?key=CZi-J0L0AHjEjsxwcKVr9g)



## 3-SAT $\leq_{p}$ Independent set
1. Ponemos nodos = terminos (para cada termino ponemos un nodo, teniendo en cuenta los negados $3*k$ nodos)
2. Creamos triangulos por cada clausula 
3. ponemos aritas en posibles conflictos 
4. se puede demostrar que G tiene un set independiente de tamaño K sii el 3-SAT es satisfacible

pero no podrian dos variables estar en 1 dentro de la misma clausula? sip

pero no estamos buscando resolver el problema, solo saber si se puede resolver

##### Si hay 3-sat, hay independent set
Si es satisfacible, al menos 1 nodo de cada triangulo es True/1. Agarramos un vertice de cada triangulo tal que valga Trye/1 -> ese set es independiente (no puede generar conflictos)

##### Si hay independent set, hay 3 sat 
por cada X, si esta en el set, vca1, sei esta el complemento va el 0. Si no hay ninguno ponemos alguno en 0 y otro en 1 (no pueden estar ambos). Como es un independent set de tamaño k, necesariamente hay al menos un 1 por cada triangulo, se cumple 3 sat

La notación ≤p es transitiva. 
3-SAT ≤p Independent Set
Independent Set ≤p Vertex Cover
No necesitamos demostrar que 3-SAT ≤p Vertex Cover. 


## Problemas vs Algoritmos vs Chequeos 
Un probuela puede tener diferentes soluciones (algoritmos)-> tomamos lo mas eficiente 
Dado un problema un algoritmo nos da una solucion 
Dado un probleama y una solucion, deberiamos tener un validador

Tenemos un certificador eficiente si un validador es correcto y se ejecuta en tiempo polinomial


## Clases de complejidad
![[P]]



#### Estan los siguientes problemas en NP?
- [x] Busqueda de un arreglo maxiimo
- [x] determinar si un grafo es bipartito 
- [x] problema de scheduling
- [x] puntos mas cercanos en un plano 
- [x] fuljo en una red
- [x] problema de al mochilas 
- [x] n reinas
- [x] independent set
- [x] vertex cover
- [x] 3-SAT

## $P \subseteq NP?$
SI

## $NP \subseteq P?$
NO SE SABE 
basicamente hay que demostrar si *chananananan*

# $$P = NP$$

![[Pasted image 20241023140653.png]]
Buscamos ver si esa diferencia entre P y NP realmente existe
Los problemas que estan en el borde son los mas dificiles, los NP completos. Todos los problemas se peuden reducir a NP completos

Entonces si yo encuentro una buena solucion (polinomica) para 3SAT (que es NP completo) puede reducir todos los problemas a 3SAT




## [[Dominating Set]] es NP?
Es un problema de elección de subconjuntos. 
### Por vertex cover
Voy a reducir vertex cover a dominating set (digo que vertex cover es tan dificil como dominating set)

Tenemos nuestro grafo original G, y vamos a construir otro grafo. Este nuevo grafo va a tener los mismos vértices que el original.
Aparte, tenemos un vértice por cada arista del grafo original. Unimos los vértices adicionales con los vértices que originalmente unían (como poner un vértice en el medio). 
Ahora resulta que si el grafo original tiene un vertex cover de tamaño K, entonces esos mismos vértices forman un dominant set en el nuevo grafo → si hay un dominant set de tamaño k, hay un vertex cover de tamaño k →  pudimos reducir VC a DS → DS es NP Completo.

![[Pasted image 20241027210819.png]]

Si hay vertex cover de al menos k vertices hay dominating set de al menos k vertices

### Por 3 sat
Partimos de tener n variables y m cláusulas. Creamos un grafo de 3n + m nodos: Tenemos un nodo por cada variable (xi), por cada complemento, y uno extra (ui), y uno por cada cláusula. 

Formamos triángulos entre el vértice de xi, su complemento y su extra → El extra sólo se une a variable o complemento → uno de los dos debe quedar seleccionado (si es ui, es que puede ser cualquiera). 


Tenemos n triángulos donde un vértice (extra) sólo se une a 2 de estos → al menos uno de esos 3 debe quedar seleccionado (similar a 3-SAT <=pIndependent Set), pero no puede haber más de 1 por triángulo porque podemos seleccionar hasta n, sino es imposible dominar las variables extra. 

Luego, para que los vértices de claúsulas queden dominados, alguna de sus variables deben quedar en el conjunto → si hay Dominating Set, esta asignación permite que todas las cláusulas del 3-SAT sean satisfechas. 


Ningun triangulo de la clausula puede estar en dominating set

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeT9I8dcAuTAQdNEec0ae6gph3J6PFTLRMaS2uSAOIVqHzHQ7kuNZYuk05pJNQID05BF7Bi0lq8jYZEWjAZwKWIRX6LAezw696_3haDBXV6JpHUAo2INM6mcoZRdVvVjC9hiUFPSrUQdyyWgMdBWnUsm8AwHCw=s2048?key=dOksPkXbGgnHIZbYEi2SXw)**

Si hay un domianting set necesariamente los vertices de las clausulas estan dominados y la clausula existe una forma de ponerla en true (eso en cada clausula, por ende la salida sera true)

Ej: x1 not x2 y x3. Me uno a x1, no x2 y x3. Si o si alguno de esos 3 vertices tiene que estar en el dominating set. Si yo le pongo true a ese toda la clausula seria true. 

yo llamo a dominating set con un grafo formado de esta forma 

**esta asignación permite que todas las cláusulas del 3-SAT sean satisfecha**