## Diseño lógico 
Paso intermedio entre el modelo conceptual y el interno
![[Pasted image 20240828111814.png]]

## Definición de Modelo Relacional
Creado en 1970 por Codd.
Es una formalización matemática basada en el concepto de relación

### Dominio
> Conjuntos de valores homogéneos

Ej: D1={Barcelona, Sevilla, Buenos Aires}
D2={Argentina, españa, chile}

### [[1.1 Conjuntos#Producto Cartesiano|Producto Cartesiano]]
AxB se define como el conjunto de pares que cumplen a in A y b in B
D1xD2= Bcn arg, bcn españa, bcn chile, sevilla ar, sevilla españa.....

### Relacion
es un subconjunto de un producto cartesiano
Subconjuntos interesantes de nuestro ej: R={Bcn, españa}{sevilla españa}{BsAs Argentina}

Un nombre de relación junto con una lista de [[Base de Datos/Atributos|atributos]] asociados se denomina esquema de relación 
R(A1, A2, A3)
ej; Peliculas(nombre_pelicula, año, nombre_director)

Cada uno de los [[Base de Datos/Atributos|atributos]] de un esquema de la relacion está asociado a un dominio particular. nombre_pelicula->dom(nombre_pelicula) = string 
año dom(año)=$N⁺$


Una relacion con un esquema de relacion R(A1, A2, ..., An) estando los [[Base de Datos/Atributos|atributos]] A_i asociados a los dominios $D_i = dom(A_i)$ es un subjconjunto del producto cartsianod D1xD2x...xDn. $Películas ⊂ dom(nombre\_pelicula) × dom(año ) × dom(nombre\_director) × dom(cant\_oscars)$
Y se debe cumplir que cada uno de los [[Base de Datos/Atributos|atributos]] Ai pertenezca a su dominio.

Películas = {(Kill Bill, 2003, Quentin Tarantino, 0), (Django Unchained, 2012, Quentin Tarantino, 2), (Star Wars III, 2005, George Lucas, 0), (El Cisne Negro, 2010, Darren Aronofsky, 1)}
Un elemento de una relacion se denomina *[[tupla]]*
etonces la [[tupla]]  Películas(Kill Bill, 2003, Quentin Tarantino, 3)seria falso porque no esta dentro del dominio

El valor tomado por un [[Base de Datos/Atributos|atributo]] A en una [[tupla]] es t[A]
la *cardinalidad* en una relacion R es la cantidad de tuplas que posee
La simbolizaremos n(R). 
Ejemplo: n(Películas) = 4
## Representacion
### Tablas
Una forma útil de representar una relación es a través de una tabla en la que las columnas representan los [[Base de Datos/Atributos|atributos]] y las filas representan las tuplas.
![[Pasted image 20240828112655.png]]

### Archivos
Otra nomenclatura comúnmente utilizada –y más vinculada al nivel físico– habla de archivos en lugar de tablas, registros en lugar de filas, y campos en lugar de columnas.
![[Restricciones del modelo Logico Relacional]]


![[Operaciones del Modelo Lógico-Relacional]]