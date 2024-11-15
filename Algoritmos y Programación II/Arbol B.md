---
dg-publish: true
---
# Arbol B
Es un tipo de [[Arboles|arbol n-ario]]. Que se caracteriza por expandirse a lo ancho en vez de a lo largo.
k = claves
m = cantidad maxima de descendientes = k +1
⌊k/2⌋ = cantidad minima de claves
⌈m/2⌉ = cantidad minima de descendientes
 ## Caracterísiticas de arbol B
 - Poca profundidad
 - Acceso poco costoso
 - Claves ordenadas
 - Siempre insertamos en nodos hoja

## Insercion
Primero se busca llenar el nodo actual, una vez que este tiene todas sus claves llenas, al intentar insertar otro no vamos a poder (overflow), vamos a tener que partir en dos el nodo y subdividir.
![[Pasted image 20220523145314.png]]
Si queremos insertar el 8 aca, se puede, movemos todo a la derecha y lo ponemos primero
![[Pasted image 20220523145350.png]]
Si queremos insertar el 2 aca, ya no podemos, no hay mas espacio. Entonces el 20 sube y las otras dos partes del nodo bajan

![[Pasted image 20220523145439.png]]

![[Pasted image 20220523145522.png]]

Si ahora queremos insertar el 19, de vuelta no podemos. Por lo que, igual que la vez anterior, sube el 12 y las otras dos partes del nodo bajan.

![[Pasted image 20220523145617.png]]

## Eliminación
Cuando borramos elementos, tenemos que verificar que el nodo no tenga un underflow, es decir, que tenga menos claves que la mínima (⌊k/2⌋).

![[Pasted image 20220523152923.png]] 
Al borrar el 19, vamos a tener en ese nodo solo una clave, por lo que hay que redistribuir:
Para esto podemos usar dos convenciones:
- subo clave más chica del hermano derecho y bajo el padre que separa ambos
- subo clave mas grande del hermano izquierdo y bajo el padre que separa ambos
En este ejemplo usaremos la primera

![[Pasted image 20220523153001.png]]


Si ahora queremos borrar el 20
![[Pasted image 20220523153209.png]]
No podemos redistribuir porque nos quedaria el nodo hermano derecho tambien con cantidad de claves menor a la minima. Tenemos entonces que concatenar.
"Uno al nodo afectado con algún hermano y el padre que separa ambos"
![[Pasted image 20220523153310.png]]

[[machete_arbol_b.pdf]]


## Árbol B+

El Árbol B+ es una variación del Árbol B con algunas diferencias clave en la estructura y organización de los nodos. Estos árboles están diseñados para optimizar las operaciones de búsqueda y almacenamiento secuencial.

### Características del Árbol B+

- **Todas las claves se encuentran en los nodos hoja**: En los Árboles B+, los nodos internos solo contienen claves para guiar la búsqueda, mientras que todas las claves reales se almacenan en los nodos hoja.
- **Listas enlazadas entre hojas**: Los nodos hoja están conectados entre sí mediante punteros para facilitar recorridos secuenciales eficientes.
- **Acceso más rápido a los datos**: Debido a la separación entre los nodos internos y los nodos hoja, las operaciones de búsqueda en un Árbol B+ son más rápidas en comparación con un Árbol B tradicional.
- **Espacio más eficiente**: Al separar la función de búsqueda (nodos internos) de los datos (nodos hoja), se aprovecha mejor el espacio de almacenamiento.

### Estructura de los nodos

- **Nodos internos**: Contienen solo claves y punteros a otros nodos internos o nodos hoja. No almacenan datos.
- **Nodos hoja**: Contienen todas las claves y los punteros necesarios para recorrer el árbol secuencialmente.

### Inserción en un Árbol B+

1. **Buscar la posición adecuada**: Se sigue el mismo procedimiento que en el Árbol B para encontrar el nodo hoja adecuado.
2. **Insertar la clave**: Si hay espacio en el nodo hoja, se inserta directamente. Si no hay espacio, ocurre un _overflow_, y el nodo se divide.
3. **Propagar la división**: Si un nodo hoja se divide, la clave media sube al nodo interno padre, y se crean dos nodos hoja. Si el nodo interno se llena, la división se propaga hacia arriba.

### Eliminación en un Árbol B+

1. **Eliminar la clave del nodo hoja**: Se verifica si el nodo cumple con la cantidad mínima de claves después de la eliminación.
2. **Redistribuir o combinar nodos**: Si el nodo tiene menos claves que la mínima, se redistribuyen las claves desde los nodos hermanos o se combinan nodos. La clave correspondiente en el nodo interno se ajusta.
3. **Mantenimiento del puntero**: Las conexiones entre los nodos hoja deben mantenerse para que el recorrido secuencial sea consistente.

### Ventajas del Árbol B+

- **Búsqueda secuencial rápida**: Gracias a las conexiones entre nodos hoja, es muy eficiente realizar un recorrido en orden.
- **Menor profundidad**: Como todos los datos están en los nodos hoja y estos pueden contener más claves, el árbol tiende a ser menos profundo.
- **Acceso directo a los datos**: Las claves reales están en los nodos hoja, lo que simplifica las operaciones de búsqueda y acceso a datos.