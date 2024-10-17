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
1. Las mismas del original, al que aún les quede capacidad por utilizar. El peso es esa capacidad restante
2. La arista opuesta, con peso la capacidad utilizada. 
3. Si alguno de los anteriores es 0, no hay arista.
En el peor de los casos el grafo residual tiene el doble de aristas
**Un grafo residual es una red de flujo, salvo por las aristas antiparalelas.**


