## Modelo lógico 
PPaso intermedio entre el modelo conceptual y el nterno

## Definición
Creado en 1970 por Codd.+
Es una formalizaicon matematia basada en el concepto de relacion

### Dominio
> Conjntos de valores homogeneos

Ej: D1={barcelona, sevilla, Buenos Aires}
D2={Argentina, esaña, chile}

### Producto cartesioano 
AxB se define como el conjunto de pares que cumplen a in A y b in B
D1xD2= Bcn arg, bcn españa, bcn chile, sevilla ar, sevilla españa.....

### Relacion
es un subconjunto de un producto cartesiano
Subconjuntos interesantes de nuestro ej: R={Bcn, españa}{sevilla españa}{BsAs Argentina}

Un nombre de relacion junto con una lista de atributos ascociados se denomina esquima de reacion 
R(A1, A2, A3)
ej; Peliculas(nombre pelcua, año, nombre_director)

Cada uno de los atributos de nun esquema de la relacion....


Una relacion con un quesma de relacion estando los atributos A_i asociados a los dominios D_1 = dom(A_1) es un subjconjunto del producto cartsianod D1xD2x...xDm.

Peliculas = Kill bill, 2003, Trantino 0
etonces la tupla Kill bill 2003, Trantino 3 seria falso porque no esta dentro del dominio

El valor tomado por un atributo A en una tupla es t[A]
la caridianliada en una relacion R es la cantidad de tuplas que posee

## Representacion
Una relacion es una tabla con columnas qu son atributos y filas representados tuplas

## restricciones
### Restricciones de dominio
> Dado UN atributo A de una relacion R el valor del atribuo en una tupla T debe pertenecer al dominio Dom(A)

Se permiten nulls

Los atributos tienen que ser atomicos

No pueden exstiri dos tuplas distintas que coincidan en los valores de tosos sus atributos 
Cuando un un subconjunto de atributos alcanza para identificar una tupla es una superclave

Las superclaves son minimales las llamamos claves candidatas. 
De entre todas las claves candidatas elegimos la clave primaria


## EJ
peliculas(nombre, año, director, oscars)
Si suponemos que no puede haber dos peliculas con el mismo nombre. nombre es clave candidata. Es unica por lo que es clave primaria
Si se pueden repetir nombre no tengo claves candidatas. Asi que creo el ID.
Ahora seria peliculas(id, nombre, año, id , director, oscars)

Ver UUID (universal unique ID)