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


## Arbol B+

El Árbol B+ es una variación del Árbol B, que se caracteriza por una estructura optimizada para búsquedas y almacenamiento secuencial.

### Características del árbol B+

- Todas las claves se encuentran en los nodos hoja.
- Los nodos internos solo contienen claves para guiar la búsqueda, sin datos.
- Los nodos hoja están enlazados mediante punteros para facilitar recorridos secuenciales.
- Acceso a los datos más rápido y eficiente.
- Las claves en los nodos hoja se mantienen ordenadas y conectadas.

### Inserción

1. **Buscar la posición adecuada**: Se sigue el mismo procedimiento de un árbol B para encontrar el nodo hoja adecuado.
2. **Insertar la clave**: Si el nodo hoja tiene espacio, se inserta directamente. Si no, ocurre un _overflow_ y el nodo se divide.
3. **Propagar la división**: La clave media sube al nodo interno padre y se crean dos nodos hoja.

### Eliminación

1. **Eliminar la clave del nodo hoja**: Verificar que el nodo mantenga al menos la cantidad mínima de claves.
2. **Redistribuir o combinar nodos**: Si el nodo queda con menos claves de las permitidas, se redistribuyen las claves con nodos hermanos o se combinan.
3. **Mantenimiento del puntero**: Asegurar que los punteros entre nodos hoja se actualicen correctamente para mantener el recorrido secuencial.

### Ventajas del árbol B+

- **Búsqueda secuencial rápida** gracias al enlace entre nodos hoja.
- **Menor profundidad** y acceso más eficiente, ya que los datos se mantienen en los nodos hoja.
- **Acceso directo a los datos**, lo que simplifica las operaciones de búsqueda y recorrido.

El árbol B+ es ampliamente utilizado en sistemas de bases de datos y sistemas de archivos debido a su eficiencia en operaciones de lectura y recorridos secuenciales.