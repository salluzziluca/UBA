### Restricciones de unicidad 
No puee haber dos tuplas con los miosmo valres

### Restricciones de dominio
> Dado UN [[Base de Datos/Atributos|atributo]] A de una relacion R el valor del atribuo en una [[tupla]] T debe pertenecer al dominio Dom(A)

Se permiten nulls

Los [[Base de Datos/Atributos|atributos]] tienen que ser atomicos

No pueden existir dos tuplas distintas que coincidan en los valores de todos sus [[Base de Datos/Atributos|atributos]].
Cuando un un subconjunto de [[Base de Datos/Atributos|atributos]] alcanza para identificar una [[tupla]] es una [[Superclave (SK)]]

Las [[Superclave (SK)|superclaves]] son minimales las llamamos [[[[Claves Candidatas]]|[[claves candidat]]as]]. 
De entre todas las [[claves candidatas]] elegimos la [[clave primaria]]

#### Ej
Ejemplo Películas(nombre_película, año, nombre_director, cant_oscars) 
Si suponemos que no puede haber dos películas con el mismo nombre “nombre_película” es clave candidata. Es la única. 
La designaremos como clave primaria. Lo representamos como: Películas(<ins>nombre_película<, año, nombre_director, cant_oscars). {nombre_película, cant_oscars} es superclave, pero no es clave candidata porque no es minimal. Si admitimos que existen películas distintas con el mismo nombre Deberíamos crear un atributo “id” que nos permita identificar a cada película. El esquema de relación sería ahora: Películas(id, nombre_película, año, nombre_director, cant_oscars) “id” será la clave primaria. Mariano Beiró | Dpto. de Computación - Facultad de Ingenierí
### Restriciones de integradad de [[Entidades|entidad]] 
La [[clave primaria]] de una relacon no puede tomar el valor nulo.


### Restrccion de integridad referencial
Si tengo tabla de peliculas actores y actuaciones no puedo poner en actuaciones poner una pelicula que no existe. Cuando estoy referencando una taba los valores tienen que estar dentro de la tabla que se esta referenciando

Clave foranea (foreing key, FK) se denomina a un [[Base de Datos/Atributos|atributo]] de una relacion R que hace referencia a la calve primaria de otra relacion S. Se suelen subrayar con guiones
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
