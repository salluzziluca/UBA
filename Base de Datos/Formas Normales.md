>Las Formas Normales son una serie de estructuras con las que un esquema de base de datos puede cumplir o no

Las formas normales clásicas son: 
- Primera forma normal (1FN) (E. Codd, 1970) 
- Segunda forma normal (2FN) (E. Codd, 1971) 
- Tercera forma normal (3FN) (E. Codd, 1971) 
- Forma normal Boyce-Codd (FNBC) (R. Boyce E. Codd, 1974) 
- Cuarta forma normal (4FN) (R. Fagin, 1977) 
- Quinta forma normal (5FN) (R. Fagin, 1979) 
  
  Cada forma normal es más fuerte que las anterior
  S está en 5FN → S está en 4FN → ... S está en 2FN → S está en 1FN.
En 1972 Codd propuso el concepto de normalizacion como el proceso a traves del cual se convierte un esquema de base da datos a uno equivalente (no pierde informacion) y que cumple con una determinada forma normal.

Busca:
- Preservar la informacion 
- Eliminar la redundancia (si los datos aparecen una sola vez y despues se referencian, cuando tengo que cambiar el valor hago una sola modificacion)
- Evitar las anomalias de ABM

## Primera Forma Normal (1FN)
>Decimos que un esquema de base de datos relacional está en primera forma normal (1FN) cuando los dominios de todos sus atributos sólo permiten valores atómicos (es decir, indivisibles) y monovaluados

![[Pasted image 20240924192916.png]]este ejemplo no cumple
Podríamos tener tabla con n tupas nombre, mail o varias columnas, una por mail

## Segunda Forma Normal (2FN)
Decimos que una relación está en segunda forma normal (2FN) cuando todos sus [[Atributo Primo de una Relacion|atributos no primos]] tienen [[Dependencia Funcional#Dependencia funcional completa|dependencia funcional completa]] de las claves candidatas


## Tercera Forma Normal (3FN)

Decimos que una relacion esta en tercera forma normal cuando no esiten [[Dependencia Funcional#Dependencia transitivas|dependencias transitivas]]CK->Y de atributos no primos con CK clave candidata


## Forma Normal Boyce-Codd
>Una relación está en forma normal Boyce-Codd (FNBC) cuando no existen dependencias transitivas CK → Y, con CK clave candidata. Es decir, eliminamos la posibilidad de tener dependencias transitivas X → Y en las que Y es un atributo primo.
Dicho de otra forma, una relación está en FNBC cuando para toda dependencia funcional no trivial X → Y, X es superclave.

![[Pasted image 20240924211541.png]]

## Dependencias Multivaluadas y 4FN