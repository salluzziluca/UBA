---
Dia: 2024-11-12
dg-publish: true
---
Viva moreno carajo, hay que hacer costos 

![[Pasted image 20241115185216.png]]

1. Parser y Translator
	Rechazar consulta inválida
2. Optimizador
	Conversión a expresión de A.R.
	Expresión equivalente de A.R.
	Estrategia para cada operador
3. Evaluación del plan de ejecución
	Devolver el resultado en base a los datos


Mediante heurísticas la expresión se convierte en una expresión equivalente, obteniéndose un plan de consulta ● En base a datos sobre los datos de la base (metadatos) que se encuentran en el catálogo, se elige cómo resolver cada operador de álgebra relacional, obteniéndose el plan de ejecución


### Tipos de costos 

- Costo de acceso a disco (lectura o escritura)
- Costo de procesamiento 
- Costo de uso de memoria
- Costo de uso de redes
En este tipo de otpimizaciones ya no corren por parte del usuario. Sin internas de la bdd y es dificil tener ingerencia en ellos

## Reglas de equivalencia 

Buscamos consultas equivalentes y nos fijamos cual es mas optima 

![[Pasted image 20241115185750.png]]
![[Pasted image 20241115185836.png]]
Hacer una junta es equivalente a realizar el producto
cartesiano entre las tablas y luego revisar la condición de junta
con una selección
$σc( R X S ) = R ⨝c S$


Distribución de la selección en la junta $σc( R ∗ S ) = σcR( R ) ∗ σcS( S )$ 
Si la condición c puede escribirse como $cR∧cS$ donde $cR$ y $cS$ involucran atributos sólo de R y S respectivamente

Distribución de la proyección en la junta $πX( R ∗ S ) = πXR( R ) ∗ πXS( S )$ 
Si todos los atributos de junta están contenidos en X, se construyen XR y XS como conjuntos que tienen los atributos de X que están en R o S respectivamente


## Heuristicas de Optimizacion 

>[!important] 
>Reglas generales
>Realizar las selecciones lo antes posible
>Reemplazar productos cartesianos por juntas cuando se pueda 
>Proyectar para descartar atributos no utilizados lo antes posible 
>Priorizar selección antes que proyección ○ Tener cuidado si el árbol no queda left deep (evaluar pipelining) 
>Realizar las juntas más restrictivas primero
>Dos consultas equivalentes pueden tener costos distintos


![[Pasted image 20241115190354.png]]
Determinar todos los árboles equivalentes según las reglas vistas es muy costosos 
Se utilizan heurísticas para agilizar el proceso ○ El objetivo general es reducir el tamaño de relaciones intermedias  
Para aprovechar pipelining se prefieren árboles “left deep” en el que los hijos derechos siempre son accesos a tablas
![[Pasted image 20241115190438.png]]

Una vez elegido el árbol de consulta a utilizar, se debe elegir de qué modo resolver cada operador algebraico

Existen distintos algoritmos para cada operador cuyo costo
depende de muchos factores
- Cantidad de datos
- Tamaño de datos
- Existencia de índices
- Memoria disponible
Se estima el costo (lo cual tiene que ser mucho menos costoso que ejecutar la consulta)

Para esto, tiene información sobre los datos de las tablas 
Guarda estos metadatos en el catálogo}
PostgreSQL usa la tabla pg_statistics y su vista pg_stats

### Catálogo
- n(R) : cantidad de filas de la tabla R
- B(R) : cantidad de bloques que ocupa la tabla R
- F(R) : (factor de bloque) cantidad de filas por bloque en la tabla R. Se puede calcular como n(R) / B(R)
- V(A, R) : (variabilidad de A en R) cantidad de distintos valores que tiene el atributo A en la tabla R
- También información sobre índices
- Height(I(A,R)) : Altura del índice, para índices de tipo árbol


Mantener el catalogo actualizado puede ser costoso.
Los motores suelen hacerlo con cierta periodicidad, o cuando están ociosos, o cuando el usuario lo indique explícitamente


### Indices
Se puede indexar los datos de una tabla por una o más expresiones
El índice, generalmente implementado como un [[Algoritmos y Programación II/Arbol B#Arbol B+|Arbol B+]], guardará para cada posible valor de las expresiones, en qué bloque o bloques hay filas con ese valor
Esto agiliza la búsqueda por esas expresiones
- También búsquedas por rangos
- En índices por varias expresiones, sólo agiliza en búsquedas que las usan en el orden definido
Si yo quiero buscar desde Roman hasta Ruben, puedo hacerlo tambien facil

#### Clustering 
Algunos motores tienen la opción de hacer índices de clustering, en los cuales los datos físicamente están ordenados por la clave del índice
- Esto permite reducir el costo de acceso
- Si un valor del índice está en 5 filas y entran 10 filas por bloque, esas 5 filas casi seguro estarán en un único bloque si el índice es de clustering
- Si no es de clustering, probablemente estarán en 5 bloques distintos
Mantener este tipo de indices es costoso ya que se reestructura el indicine y el archivo con lso datos ante ABMs
Solo se puede hacer un indice de clustering por tabla 
tambien agiliza consultas por rangos 

## Costos de Operadores 
Analizamos el costo de resolver cada operador por separado 
No consideramos el costo de almacenar el resultado final ya que estos pueden ser intermedio sy no almacenarse, solo estimaremos los bloques. 
Luego veremos como combinar el costo de varios operadores

El costo lo mediremos en bloques de disco accedidos ya sea en Read or Write 
Las bases de datos mantienen cache de datos ya accedidos en memoria para ahorrarse lecturas
El costo real puede diferir del estimado. No es 100% acertado, igual sirve para elegir el metodo que deberia ser mas optimo 

### Seleccion
#### File Scan
La forma más sencilla de resolver una selección es recorrer bloque a bloque todos los datos de la tabla y evaluar fila a fila si se cumple o no la condición
El costo es Cost(σc(R)) = B(R)

#### Index Scan
Cuando la condición es de la siguiente forma σ Ai=v (R) y hay un índice por la columna Ai, puede convenir utilizar un índice para resolver la consulta (Index Scan)


Costo de acceder al índice por la clave de búsqueda v 
Costo de encontrar los N bloques que, según el índice indica, contienen filas con Ai = v

sin clustering: $Cost(σ Ai=v (R)) = Height(I(A,R)) + ⌈n(R) / V(A,R)⌉$

Si es de clusteriing, las filas van a estar en bloques contiguos: 
$Cost(σ Ai=v (R)) = Height(I(A,R)) + ⌈n(R) / (V(A,R) * F(R))⌉$ Equivalente a: $Cost(σ Ai=v (R)) = Height(I(A,R)) + ⌈B(R) / V(A,R)⌉$


Si la condición no es por igualdad, puede extenderse la fórmula anterior pero en general el costo es mayor, salvo rangos acotados $σ Ai>=v1 ∧ Ai<=v2 (R)$


#### Conjunto de condiciones 
Si hay una conjunción de condiciones, igualmente puede aprovecharse un índice por alguna de las columnas $σ Ai=v1 ∧ Aj=v2 (R)$
Se usa el índice por el atributo indexado (asumamos A1) ○ Se accede a las filas con Ai = v1 y se revisa previo a devolverlas que también cumplan que Aj = v2

También se podría haber aprovechado un índice compuesto que comience con Ai y Aj 
Si hay dos índices distintos por cada atributo, se usan ambos y se accede a los bloques devueltos por ambos

#### Disyuncion de condiciones 

Si hay una disyunción de condiciones, es más complicado aprovechar índices σ Ai=v1 ∨ Aj=v2 (R) 
Si no tenemos un índice por alguno de los atributos, hay que hacer File Scan  Si tenemos índices por ambos, podríamos acceder a los dos índices y a los datos devueltos por cada uno de ellos (unión entre los resultados de ambos)