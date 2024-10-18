Podemos modelar con grafos flujos de materiales (ej: cloacas, informacion en redes)

El grafo es diriigido 
Tiene una unica fuente y un unico sumidero 
Cad vertice intermedio simplemente traslada lo que le pasan, no produce ni consume. Ccada arista tiene un peso que refleja su capacidad de transporte
![[Pasted image 20241017153009.png]]


-  No se aceptan bucles
- No puede hacer ciclos de dos vertices (aristas antiparalelas)
- Solo puede haber una fuente
- Solo puede haber un sumidero

Para eliminar aristas antiparalelas: ![[Pasted image 20241017153236.png]]


Para tener solo una fuente:
![[Pasted image 20241017153402.png]]


para tener solo un sumidero: 
![[Pasted image 20241017153432.png]]



## Red residual 
Grafo con los mismo vertices, pero tiene como aristas: 
1. Las mismas del original, al que aún les quede capacidad por utilizar. El peso es esa capacidad restante. Si yo tenia 12 de capacidad pero solo use 10, me quedan 2 de residual
2. La arista opuesta, con peso la capacidad utilizada. 
3. Si alguno de los anteriores es 0, no hay arista.
En el peor de los casos el grafo residual tiene el doble de aristas
**Un grafo residual es una red de flujo, salvo por las aristas antiparalelas.**

![[flujo residual]]
### augmentin path 
Si encontramos un camino de la fuente s al sumidero t en el grafo residual, entonces encontramos un camino por qel que podemos aumentar el flujo.  
Buscamos aumentar el flujo total, pero puede reducirse el que pasa por una arista en particular. 


## algoritmo de ford-fulkerson 
```python 
def flujo(grafo, s, t):
	inicializamos el flujo por toda arista a 0
	Mientras haya un camino en la red residual:
		aumentamos el flujo acorde al camino

```

Dependiendo de cómo se haga esto, puede no converger el algoritmo!
Busca encontrar el flujo maximo, no el camino mas corto
![[Pasted image 20241018122745.png]]
![[Pasted image 20241018122729.png]]
ahi vemos que como el flujo de 0 a 1 es 11 y el de 1 a 3 es 12, el primero capea al 2do


![[Pasted image 20241018124408.png]]

A ver, antes de 3 a 5 estabamos usando 11 y teniamos de residual (nos sobraba) 8. Pero como de 4 a 3 llega un flujo de 7, usa 7 de los 8 residuales de 3 a 5 y terminamos usando 18 con 1 residual


![[Pasted image 20241018124530.png]]

Finalmente, podemos u