
### Restricciones de dominio
> Dado UN [[Base de Datos/Atributos|atributo]] A de una relacion R el valor del atribuo en una [[tupla]] T debe pertenecer al dominio Dom(A)

Se permiten nulls

Los [[Base de Datos/Atributos|atributos]] tienen que ser atomicos
### Restricciones de unicidad 

No pueden existir dos tuplas distintas que coincidan en los valores de todos sus [[Base de Datos/Atributos|atributos]].
Cuando un un subconjunto de [[Base de Datos/Atributos|atributos]] alcanza para identificar una [[tupla]] es una [[Superclave (SK)]]

Las [[Superclave (SK)|superclaves]] son minimales las llamamos [[[[Claves Candidatas]]|[[claves candidat]]as]]. 
De entre todas las [[Claves Candidatas]] elegimos la [[clave primaria]]


### Restriciones de integradad de [[Entidades|entidad]] 
La [[clave primaria]] de una relacon no puede tomar el valor nulo.


### Restriccion de integridad referencial
Cuando un conjunto de [[Base de Datos/Atributos|atributos]] [[Claves foráneas (FK)|FK]] de una relación R hace referencia a la [[clave primaria]] de otra relación S, entonces para toda [[tupla]] de R debe existir una [[tupla]] de S cuya [[clave primaria]] sea igual al valor de [[Claves foráneas (FK)|FK]], a menos que todos los [[Base de Datos/Atributos|atributos]] de [[Claves foráneas (FK)|FK]] sean nulos.
Ejemplo: Si una [[tupla]] en Actuaciones hace referencia “Star Wars III”, entonces debe existir “Star Wars III” en la relación Películas.

Clave foranea ([[Claves foráneas (FK)|foreing key]], [[Claves foráneas (FK)|FK]]) se denomina a un [[Base de Datos/Atributos|atributo]] de una relacion R que hace referencia a la calve primaria de otra relacion S. Se suelen <u>subrayar con guiones</u> 
## EJ
peliculas(nombre, año, director, oscars)
Si suponemos que no puede haber dos peliculas con el mismo nombre. nombre es clave candidata. Es unica por lo que es [[clave primaria]]
Si se pueden repetir nombre no tengo [[Claves Candidatas]]. Asi que creo el ID.
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
![[Pasted image 20240828162501.png]]


