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

#### Primitivas
##### Agregar
Para agregar, hasheamos la clave y asignamos el valor a esa posición. Si tenemos una colision agregamos un elemento a la lista correspondiente a esa posicion

##### Buscar
Hasheamos la clave e iteramos en la lista de ese valor. Vemos si encontramos o no el elemento
##### Quitar
Es decir, cada vez que quitamos, iteramos dentro de la lista del valor asignado, ahi quitamos igual que en lista

### Hash Cerrado
- Los elementos se guardan adentro de la estructura
- Tipo de direccionamiento abierto. Por ende, el tamaño de la tabla >= nro de claves
- Para resolver colisiones buscamos nuevas posiciones para el valor
#### Tipos de metodos de busqueda
![[Pasted image 20220531193829.png]]

#### Rehash
![[Pasted image 20220531193740.png]]
Cuando el fctor de carga es mayor a un numero elegido por nosotros, rehasheamos, aumentando la capacidad del hash


#### Primitivas
##### Agregar
Para agregar, hasheamos la clave y asignamos el valor a esa posición. Si tenemos una colision:

En hash cerrado, usamos uno de los [[Tabla Hash o Hash Map#Tipos de metodos de busqueda|tipos de metodos de busqueda]] para encontrarle una nueva posición.


##### Buscar
Hasheamos la clave y vemos si efectivamente existe o no el elemento. Iteramos hasta encontrarlo o hasta llegar a un espacio vacio.
##### Quitar
Cada vez que quitamos tenemos que asegurarnos de que todos los elementos que colisionan (que tienen el mismo valor hasheado) esten pegados. Es decir, cada vez que quitamos, iteramos hasta encontrar un elemento que se pueda reorganizar (un colisionado) o hasta encontrar un espacio vacio



abierto:
complejidades igual que lista. Porque el peor caso es que se degenere

Cerrado: crear y destruir O(1)
insertar O(n) recorrer todo
quitar O(n) recorrer todo
obtener O(n) recorrer todo
cantidad O(n)