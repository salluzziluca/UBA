# Tabla Hash o Hash Map
Una estructura que contiene valores. Estos valores se pueden hallar mediante claves.

![[Pasted image 20220531183348.png]]

Al ingresarle una clave para buscar nos devuelve un numero asociado, esto lo hace mediante una 

## Función hash
Esta funcion transforma claves en números asociados
![[Pasted image 20220531183553.png]]
En la imagen de arriba, tenemos una colisión, son dos claves que hasheadas dan al mismo valor

## Tipos de has
### Hash abierto
- Los elementos se guardan afuera de la estructura (por eso es abierto)
- Tipo de direccionamiento cerrado (siempre que tengamos una colision, la clave va a terminar en el valor al que colisiona, si F hashea como 0, aunque colisione, siempre va a ir a 0)
- Su complejidad en el peor caso (todo colisiona al mismo numero porque tenemos una funcion hash horrible) es O(n)
![[Pasted image 20220531190252.png]]
### Hash Cerrado
- Los elementos se guardan adentro de la estructura
- Tipo de direccionamiento abierto. Por ende, el tamaño de la tabla >= nro de claves
- Para resolver colisiones buscamos nuevas posiciones para el valor
#### Tipos de metodos de busqueda
![[Pasted image 20220531193829.png]]

#### Rehash
![[Pasted image 20220531193740.png]]
Cuando el fctor de carga es mayor a un numero elegido por nosotros, rehasheamos, aumentando la capacidad del hash