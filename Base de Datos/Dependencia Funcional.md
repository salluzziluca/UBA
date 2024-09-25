
Dado una Relacion R(A), una depenedncia funcional X->Y con X, Y \in A es una restriccion sobre las posibles tuplas de R que implica que dos tuplas con igual valor del conjunto de atributos X deben también tener igual valor del conjunto de atributos Y.
$$∀s, t ∈ R : s[X] = t[X] → s[Y] = t[Y]$$La dependencia funcional X → Y implica que hay una relación funcional entre los valores de X y los de Y dentro de la base de datos
Cuando Y ⊂ X decimos que X → Y es trivial.

Ej Padron-> Apellido Alumno
Si hay el mismo pardon, va a estar el mismo apellido
Padron-> Nombre Alumno 
Codigo-> Nombre Materia
Padron, Codigo-> Nota aprobabacion

Las dependencias se definien a partir de la semantica. No podemos inferir viendo solo los datos. Tengo que saber que representan



Puedo unir. Por ejemplo: Padron-> Apelldio, Nombre

Clausura: Todo el conjunto de atributos al que puedo llegar con el conjunto inicial que tengo


## Dependencia Funcional Parcial 
Una dependencia funcional X → Y es parcial cuando existe un subconjunto propio $A ⊂ X, A \neq X$ para el cual $A → Y$
Es decir. Si yo tengo A, B -> L. Puedo llegar a L sin usar solamente A, B 

## Dependencia funcional completa 
Una dependencia funcional X → Y es completa si y sólo si no es parcial.


## Dependencia transitivas
Cuando algo depende de algo que no es la clave
![[Pasted image 20240924210707.png]]
![[Pasted image 20240924210714.png]]
En el ejemplo, nombre_producto tiene dependencia transitiva en la clave primaria porque {nro_factura, nro_item} → cod_producto y cod_producto → nombre_producto.