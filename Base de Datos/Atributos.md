---
aliases:
  - atributo
---

Cada [[Entidades|entidad]] tendra ==valores particulares== para cada uno de los atributos del tipo de [[Entidades|entidad]] al que corresponde.

Ej: Tipo de [[Dato]] `Pais(nombre, población, superifice)`. [[Entidades|Entidad]]: `(Argentina, 40.117.096, 2.780.400km^2`

## Dominio de un atributo
El dominio de un atributyo es el conunto de valores que el mismo puede tomar.

Ej: 
Para la [[Entidades|entidad]] País: 
- El atributo nombre es una cadena de caracteres (string). 
- El atributo población es un número entero positivo. 
- El atributo superficie es un número real positivo.
En ciertos casos se le puede asignar el valor nulo o NULL al atributo.

## Atributos complejos 
![[Pasted image 20240820195650.png]]
## Atributos almacenados vs derivados
Depende de dos atributos almacenados
![[Pasted image 20240820200224.png]]
## Atributos multivaluados vs Monovaluados
Cuando una instancia puede tener mas de un valor para un mismo atributo es multivaluado 
![[Pasted image 20240820200114.png]]