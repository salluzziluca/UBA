
### Restricciones de dominio
> Dado UN [[Base de Datos/Atributos|atributo]] A de una relacion R el valor del atribuo en una [[tupla]] T debe pertenecer al dominio Dom(A)

Se permiten nulls

Los [[Base de Datos/Atributos|atributos]] tienen que ser atomicos
### Restricciones de unicidad 

No pueden existir dos tuplas distintas que coincidan en los valores de todos sus [[Base de Datos/Atributos|atributos]].
Cuando un un subconjunto de [[Base de Datos/Atributos|atributos]] alcanza para identificar una [[tupla]] es una [[Superclave (SK)]]

Las [[Superclave (SK)|superclaves]] son minimales las llamamos [[[[Claves Candidatas]]|[[claves candidat]]as]]. 
De entre todas las [[claves candidatas]] elegimos la [[clave primaria]]


### Restriciones de integradad de [[Entidades|entidad]] 
La [[clave primaria]] de una relacon no puede tomar el valor nulo.


### Restriccion de integridad referencial
Cuando un conjunto de [[Base de Datos/Atributos|atributos]] [[Claves foraneas (FK)|FK]] de una relación R hace referencia a la [[clave primaria]] de otra relación S, entonces para toda [[tupla]] de R debe existir una [[tupla]] de S cuya [[clave primaria]] sea igual al valor de [[Claves foraneas (FK)|FK]], a menos que todos los [[Base de Datos/Atributos|atributos]] de [[Claves foraneas (FK)|FK]] sean nulos.
Ejemplo: Si una [[tupla]] en Actuaciones hace referencia “Star Wars III”, entonces debe existir “Star Wars III” en la relación Películas.

Clave foranea ([[Claves foraneas (FK)|foreing key]], [[Claves foraneas (FK)|FK]]) se denomina a un [[Base de Datos/Atributos|atributo]] de una relacion R que hace referencia a la calve primaria de otra relacion S. Se suelen <u>subrayar con guiones</u> 
## EJ
peliculas(nombre, año, director, oscars)
Si suponemos que no puede haber dos peliculas con el mismo nombre. nombre es clave candidata. Es unica por lo que es [[clave primaria]]
Si se pueden repetir nombre no tengo [[claves candidatas]]. Asi que creo el ID.
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
Pongo en null los [[Base de Datos/Atributos|atributos]] referenciales a actor


#### Modificacion 
Tengo que revisar dominio (que este bien e [[dato]])
Tengo que revisar unicidad tambien si cambio algun valor de la [[clave primaria]]
idem con [[Entidades|entidad]]
integridad referencial tambien. Si modifico un valor referenciado tengo que fijarme que no se rompan sus referencias. PUedo hacer cascada


## Transacción
Serie de operaciones que o bien se hacen enteras o no se hacen.(ej: transaccion)
Yo defino esta serie de operaciones como transaccion
