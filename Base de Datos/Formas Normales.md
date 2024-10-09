
Busca:
- Preservar la informacion 
- Eliminar la redundancia (si los datos aparecen una sola vez y despues se referencian, cuando tengo que cambiar el valor hago una sola modificacion)
- Evitar las anomalias de ABM

2FN: si de la derecha hay un atributo no primo, de la izquierda hay una superclave completa u otro atributo no primo

3FN: a la izquierda tiene que haber una superclave completa o de la derecha tiene que haber un atributo primo

FNBC: a la izquierda tiene que haber una superclave completa
## Primera Forma Normal (1FN)
>Decimos que un esquema de [[Bases de Datos|base de datos]] relacional está en primera forma normal (1FN) cuando los dominios de todos sus [[Base de Datos/Atributos|atributos]] sólo permiten valores atómicos (es decir, indivisibles) y monovaluados

![[Pasted image 20240924192916.png]]este ejemplo no cumple
Podríamos tener tabla con n tupas nombre, mail o varias columnas, una por mail

## Segunda Forma Normal (2FN)
Decimos que una relación está en segunda forma normal (2FN) cuando todos sus [[Atributo Primo de una Relacion|atributos no primos]] tienen [[Dependencia Funcional#Dependencia funcional completa|dependencia funcional completa]] de las [[claves candidatas]]


## Tercera Forma Normal (3FN)

Decimos que una relacion esta en tercera forma normal cuando no esiten [[Dependencia Funcional#Dependencia transitivas|dependencias transitivas]] CK->Y de [[Atributo Primo de una Relacion|atributos no primos]] con CK clave candidata


## Forma Normal Boyce-Codd
>Una relación está en forma normal Boyce-Codd (FNBC) cuando no existen dependencias transitivas CK → Y, con CK clave candidata. Es decir, eliminamos la posibilidad de tener dependencias transitivas X → Y en las que Y es un [[Atributo Primo de una Relacion|atributo primo]]. Esto seria como agarrar la 3FN y sumarle la condicion de que Y sea primo tmb. Es decir, ahora se cumple para Y primo e Y no primo.
Dicho de otra forma, una relación está en FNBC cuando para **toda** dependencia funcional no [[Dependencia Funcional Trivial|trivial]] X → Y, X es [[Superclave (SK)|superclave]].

![[Pasted image 20240924211541.png]]

##  Algoritmos para buscar [[claves candidatas]]
1. Busco [[Base de Datos/Atributos|atributos]] independientes-> estan en todas las [[Claves Candidatas]]
2. Busco [[Base de Datos/Atributos|atributos]] que solo aparecen en lado izq -> estan en todas las [[claves candidatas]] 
3. Busco [[Base de Datos/Atributos|atributos]] que esten solo de lados derechos -> no estan en ninguna clave candidata
4. Los que aparecen tanto en izq como en derecho, no tenemos infomracion