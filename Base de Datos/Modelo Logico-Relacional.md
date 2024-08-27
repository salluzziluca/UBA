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
### Restricciones de unicidad 
No puee haber dos tuplas con los miosmo valres

### Restricciones de dominio
> Dado UN atributo A de una relacion R el valor del atribuo en una tupla T debe pertenecer al dominio Dom(A)

Se permiten nulls

Los atributos tienen que ser atomicos

No pueden exstiri dos tuplas distintas que coincidan en los valores de tosos sus atributos 
Cuando un un subconjunto de atributos alcanza para identificar una tupla es una superclave

Las superclaves son minimales las llamamos claves candidatas. 
De entre todas las claves candidatas elegimos la clave primaria

### Restriciones de integradad de entidad 
La clave primara de una relacon no puede tomar el valor nulo.


### Restrccion de integridad referencial
Si tengo tabla de peliculas actores y actuaciones no puedo poner en actuaciones poner una pelicula que no existe. Cuando estoy referencando una taba los valores tienen que estar dentro de la tabla que se esta referenciando

Clave foranea (foreing key, FK) se denomina a un atributo de una relacion R que hace referencia a la calve primaria de otra relacion S. Se suelen subrayar con guiones
## EJ
peliculas(nombre, año, director, oscars)
Si suponemos que no puede haber dos peliculas con el mismo nombre. nombre es clave candidata. Es unica por lo que es clave primaria
Si se pueden repetir nombre no tengo claves candidatas. Asi que creo el ID.
Ahora seria peliculas(id, nombre, año, id , director, oscars)

## Claves subrrogadas(ID)
En la materia no se busca que usemos tato ID, sino mas las claves naturales (para que aprendamos bien).
LO bueno de usar claves subrrogadas es que si te cambian como funciona tu clave natural te chupa un webo

Ver UUID (universal unique ID)

## Ej2
ActoresPeliculas(peli, año, direector, oscars,actor)
la clave seria actor,pelicula.
No es un buen modelo porque sigue siendo redundante

## Mutiples de relaciones
Es mejor almacenar esquemas de relacion a uno solo esquema enorme
==ver diapo 18==



## Operaciones 

Los operaciones del modelo relacionas se especifican a traves del algebra relacional o el calculo relacional

### Consulta 
### Actualizacion

#### Insercion
tengo que validar las 4 reglas
#### Eliminaciont
tengo que validad la integridad referencial
Si borro un actor y estaba en varias pelis quedan todas esas con un actor no valido 

Se puede resolver usando cascada ( borro todas sus apariciones)
O de forma restrictiva (primero borrame la actuacion y despues te dejo borrar el actor)
Pongo en null los atributos referenciales a actor


#### Modificacion 
Tengo que revisar dominio (que este bien e dato)
Tengo que revisar unicidad tambien si cambio algun valor de la clave primaria
idem con entidad
integridad referencial tambien. Si modifico un valor referenciado tengo que fijarme que no se rompan sus referencias. PUedo hacer cascada


## Transac
