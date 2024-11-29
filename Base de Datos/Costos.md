---
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
Estes no tiene por que ser el de la clave, de hecho es probable que no convenga. Si yo tengo partidos de futbol y la clave es equipos + fecha quizas me conviene hacer clustering por jugadores porque voy a estar buscsando mucho mas los goles de x jugador que cosas de cada partido.
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

Si hay una disyunción de condiciones, es más complicado aprovechar índices $σ Ai=v1 ∨ Aj=v2 (R)$ 
Si no tenemos un índice por alguno de los atributos, hay que hacer File Scan 
Si tenemos índices por ambos, podríamos acceder a los dos índices y a los datos devueltos por cada uno de ellos (unión entre los resultados de ambos)


#### Distribución no uniforme de los valores

Cuando los valores no tienen una distribución uniforme, la estimación de la fórmula vista no es buena 
$Cost(σ Ai=v (R)) = Height(I(A,R)) + ⌈n(R) / V(A,R)⌉$
Si estoy buscando clientes por país, quizás el 95 % de los clientes son de Argentina y el 0.1% de un país remoto

La fórmula debería adaptarse ya que los costos son muy distintos ○ Probablemente no convenga Index Scan para Argentina

Para esto el SGBD mantiene histogramas con la frecuencia de los valores que tiene cada columna. A veces no todos, sino los N más frecuentes. Esto esutil para valores discretos y con repeticiones

![[Pasted image 20241116111350.png]]
Para Brasil, se accederan a 1,000 bloques ya que el histograma nos dice que mil filas son de brasil $Cost(σ país='Brasil' (Clientes)) = 3 + 1000 = 1003$ 
Para Argentina conviene $File Scan Cost(σ país='Argentina' (Clientes)) = 10,000$ 
Para tonga, se usa la fórmula quitando los valores conocidos $Cost(σ Ai=v (R)) = 3 + ⌈ 1,000 / 47 ⌉ = 3 + 22 = 25$


#### Estimacion de al cardinalidad
Se estima cuantas fiilas fueron devueltas por el operador. Si no se tiene el histograma se estiam la cardinalidad segun la variabilidad $n(σ Ai=v (R)) = ⌈n(R) / V(A,R)⌉$

Si se tiene histograma y se conoce el valor, se lo utiliza 
Si se tiene histograma pero no se conoce el valor, se estima según la variabilidad
En vez de n(R) se usa n(R) menos las frecuencias conocidas 
A la variabilidad V(A,R) se le resta la cantidad de frecuencias conocidas

Tambien se pueden querer saber la cantidad de bloques devueltos por el operador 
$B(σ Ai=v (R)) = ⌈n(σ Ai=v (R)) / F(R)⌉$

>[!example] F(Clientes): 100,000 / 10,000 = 10 (Entran 10 filas por bloque)  Para Brasil y Argentina se usa el histograma para la cardinalidad n(σ país='Brasil' (Clientes)) = 1,000 (usa 100 bloques) n(σ país='Argentina' (Clientes)) = 95,000 (usa 9,500 bloques) Para tonga, se estima quitando los valores conocidos n(σ país='Tonga' (Clientes)) = ⌈ (100,000 - 99,000) / (50 - 3) ⌉ n(σ país='Tonga' (Clientes)) = ⌈ 1,000 / 47 ⌉ = 22 (usa 3 bloques)



## Proyeccion 
Es importante saber si hay que eliminar o no duplicados. Si la consulta no tiene DISTINCT o si se proyecta por una superclave, no es necesario eliminar duplicados. Costo $Cost(πx(R)) = B(R)$. Y salen tantas filas comoi habia n(πX(R)) = n(R)

Si no hay que eliminar duplicados, hay que manteneros en memoria para saber si devolverlos o no. Si B(πx(R)) > memoria disponible, el costo deja de ser B(R). Si cambia la cantidad de filas devueltas n(πA1(R)) = V(A1,R) o n(πA1,A2(R)) = V(A1,R) * V(A2,R) si no hay correlación entre los atributos.


La cantidad de bloques puede ser menor ya que la fila ocupa menos.
![[Pasted image 20241116112516.png]]


### Sort Externo

Cuando el resultado no entra en memoria y hay que elimiar duplicados, con leer la tabla no alcanza. La ultima fila puede producir un valor que ya se envio en la primera fila
Para resolver este problema, podemos primero ordenar la tabla por el atributo de proyección con un Sort externo 
Esta operación tiene un costo mayor
En la última etapa, al leerse en forma ordenada los datos, se devuelve el primero de cada uno de ellos


 de memoria disponibles 
1. Primera etapa: #### Etapas 
Tenemos M bloquesGeneramos particiones ordenadas de M-1 bloques en memoria (Sort interno) 
	1. 1 bloque de memoria lo usamos para acumular la salida 
2.  Segunda etapa: Recorremos M-1 particiones ordenadas a la vez, y generamos una única partición con los datos ordenados de esas particiones (Merge)

####  Costo 
La cantidad total de etapas está dada por logM-1(B(R)) 
- Hasta 3 bloques: Solo primera etapa (sort interno)
- De 3 a 9 bloques: Primera etapa y 1 pasada de merge 
- 10 a 27 bloques: Primera etapa y 2 pasadas de merge  Siempre se escribe y lee B(R) salvo en la última etapa que sólo se lee 
- Definimos un costo de ordenamiento basado en M bloques de memoria: $Cost(OrdM(R)) = 2 * B(R) * ⌈logM-1(B(R))⌉ - B(R)$



Para resolver la proyección con sort externo, salvo la primera lectura, no se trabaja con toda la fila ○ Se trabaja con las columnas proyectadas ○ Tienen un B(πX(R)) < B(R) 
Adaptamos la fórmula trabajando con el B(πX(R)) ○ Sumamos B(R) y restamos B(πX(R)) para compensar $Cost(B(πX(R))) = 2*B(πX(R)) * ⌈logM-1(B(πX(R)))⌉ - 2*B(πX(R)) + B(R)$


## Costos de Operadores de Conjunto

Para los tres casos, se debe trabajar con ambas tablas ordenadas 
- Si no entran en memoria y hay que ordenarlas, usar un sort externo 
- Al costo de ordenamiento se le suma grabar a disco la tabla ordenada 
- Luego se leen ambas tablas en orden y se procesan las fila
$Cost(R ∪|∩|- S) = Cost(OrdM(R)) + Cost(OrdM(S)) + 2 * (B(R) + B(S))$

#### Union 
Se recorren ordenadas las filas r y s de R y S
Se deben devolver todas las filas 
- Si r = s se devuelve una sola de ellas y se avanza sobre ambas tablas hasta que cambien 
- Si son distintas, se devuelve la menor de ellas y se avanza en su tabla hasta que cambie 
- Cuando se llega al final de una tabla, se devuelve todo lo que queda en la otra, sin duplicados
#### Interseccion 
Se recorren ordenadas las filas r y s de R y S 
Se deben devolver las filas que están en ambas 
- Si r = s se devuelve una sola de ellas y se avanza sobre ambas tablas hasta que cambien 
- Si son distintas, se avanza la tabla de la que tiene el menor valor hasta que cambie, sin devolver nada 
- Cuando se llega al final de una tabla, se termina el algoritmo

#### Resta 
Se recorren ordenadas las filas r y s de R y S 
Se deben devolver las filas que están sólo en r 
- Si r = s se avanza sobre ambas tablas hasta que cambien de valor, sin devolver nada 
- Si r > s se avanza la tabla S hasta que cambie de valor 
- Si r < s se devuelve r y se avanza R hasta que cambie de valor 
- Si termina R, se finaliza el algoritmo 
- Si termina S, se devuelven todos los r restantes, sin repetidos, y se termina el algoritmo
### Cardinalidad y bloques

Estimar la cardinalidad es difícil ya que no se conoce la cardinalidad de la intersección 
- En la unión, deberia restarse de n(R) + n(S) 
- En la resta debería restarse de n(R) 
El factor F(R) se mantiene, con lo que si se supiera la cardinalidad se puede calcular la cantidad de bloques


## Join 

### Loop con unico indice 

Agarro un bloque de R y lo comparo con con todos los bloques de S
Se puede usar cuando es una condicion de iugladad y una tabla (S) tiene un indice sobre los campos de la condición
Se recorre bloque a bloque la tabla R y para cada file se hace un index scan en a tabka con indice S 


EJ: se recorre la tabla alumnos y para cada alumno se hace index scan en ka tabka de notas por su valor en padron

Si hay indice en ambas tablas, hay que ver cual me conviene, ya que no se pueden usar ambos indices a la vez.
Si el indice no es de clustering:
$Cost(R⨝S) = B(R) + n(R) * ( Height(I(A,S)) + ⌈n(S) / V(A,S)⌉ )$ 
En cambio, si el índice es de clustering $Cost(R⨝S) = B(R) + n(R) * ( Height(I(A,S)) + ⌈B(S) / V(A,S)⌉ )$


### Sort Merge 


Condicion de igualdad y tablkas ordenadas por atributos de condicion. Se pueden ir procesando bloque a bloque de modo similar a los operadores de conjunto 

El unico tema es que si tenemos muchos bloques que tienen el mismo valor en la junta, puede ser un problema. Ya que nos pueden quedar afuera de memoria 

Ej: junto clientes con proveedores por proivncia. Si el join es por provincia y tenemos 1millon de clientes y un millon de proveedores por provincia tengo que tener en memoria todo. Explota
El costo vendría por leer bloque a bloque ambas tablas

l costo total entonces es: 

$Cost(R⨝S) = Cost(OrdM(R)) + Cost(OrdM(S)) + 2 * (B(R) + B(S))$

Si R o S estan ordenadas, sus costos de ordenamiento son 0 

$Cost(OrdM(R)) = 2 * B(R) * ⌈log_{M-1}(B(R))⌉ - B(R)$

### Join  - Junta Hash Grace 
Solo para condicion de igualdad.
Tengo tos tablas que no me entran en memoria. Asi que parto las tablas en particiones de modo que siempre las las particiones de la menor tabla entren en memoria + 2 bloques.

Se harian N joins con un cost B(Ri) + B(Si) de cada particion

Para armar las particiones defino una funcion de hash que me hashee el atributo en cuestion que estoy intentando igualar y me devuelva un numero entre 0 y la cantidad de particiones que quiero tener. Es decir, si yo quiero 40 particiones, el hash me va a devolver numeros entre 0 y 40.

Luego puedo junta la particion_i de R con la particion_i de S. 

>[!important] Si dos filas van a juntarse, tienen el mismo valor y por ende irán a la misma partición


Esto se me rompe si mi atributo a igualar tiene poca variabilidad o si tiene mucha variabilidad pero esta mal balanceado (hay 1millon de filas de BsAs y 10 mil del resto de provincias)



Luego levanto la primera particion de la tabla mas chica entera en memoria (ya que nos aseguramos que esto fuera psoible) y la empezamos a matchear con los bloques de su particion equivalente de la tabla mas grande

Es por esto que tenia que poder entrar una particion de la mas chica + 2 bloques (uno de datos de la otra tabla y otro para guardar datos)
 $$Cost(R⨝S) = 3 * B(R) + 3 * B(S)$$
#### Restriccion 1
N Cantidad de particiones 
M Memoria disponible 

$N \leq M-1$ 
Para guardar las particiones no puedo usar mas de M-1 bloques 

#### Restriccion 2 
Las particiones de la menor tabla deberán entrar completamente en memoria dejando 2 bloques extra para poder usar loops anidados de forma eficiente 
Segundo límite: $mín(⌈B(R)/N⌉ ; ⌈B(S)/N⌉) \leq M - 2$

#### Restriccion 3

Si la cantidad de valores distintos es menor a N, no voy a poder llenar N particiones sino V(A,R) particiones ○ Algunas particiones quedarán vacías, y las que tengan datos tendrán un tamaño mayor a B(R)/N y no entrarán en memoria 
Tercer límite: $mín(⌈B(R)/V(A,R)⌉ ; ⌈B(S)/V(A,S)⌉) \leq M - 2$


#### Ej
B(alumnos)= 100 B(Notas)=300 NM = 50

Puedo armar 10 particiones usando como funcion el resto de la division por 10 del padron.

Luego tendria 10 particiones y las iria matchenado con bloques de las particiones de la mas grande 


### Cardinalidad y Cantidad de bloques del join
Nunca vamos a devolver mas de $n(R)*n(S)$ filas

Para estimar cardinalidad debemos asumir:
Distribucion equitativa (con un histograma podemos ayudarnos a que sea mas fidedigno)
Que los valores de la tabla con menor varibilidad en los atributos de jutna estan incudisos entre los de la tabla con mayor variabilidad.

$$n(R⨝S) = n(R) * n(S) / máx(V(A,R) , V(A,S))$$

Siendo $V(A, R) :$ (variabilidad de A en R) cantidad de distintos valores que tiene el atributo A en la tabla R

Si la junta es por mas de un atributo la formula es 
$$n(R⨝S) = n(R) * n(S) / máx(V(A1,R) * V(A2,R) , V(A1,S) * V(A2,S))$$

#### Cardinalidad con histogramas

 Un histograma me puede ayudar a estimar mejor la
cardinalidad
● Si un valor de atributo aparece en ambos histogramas, las
filas de cada tabla de ese valor se juntaran entre si,
multiplicandose
● Si un valor de atributo aparece en uno solo de los
histogramas, estimar la cantidad de filas en la otra tabla y
multiplicar
● Para el resto de los atributos, utilizar la fórmula anterior

### Cantidad de bloques de join 

Para estimar el factor de bloque de una fila de $R \join S$ es el mismo al ocupado por una fila de R mas el de una fila de S. 

$$1/F(R⨝S) = 1/F(R) + 1/F(S)$$
## Pipelining 

Ahora que tenemos todos los operadores, los podes encadenar

La entrada de un operador es la salida de otro. Usamos n(operador)m B(operador) y F(operador) para los neuevos calculos 
Podemos almacenar temporalmente los resultados intermedios 

Es mejor hacer pipelining

No necesitas tener todos los bloques O1(R) para calcular O2(O1(R))
Cuando termine de procesarse O1, O2 habra procesado la salida completa de O1 

Lo bueno es que no tiene que materializarse completa la salida de O1, conviene mucho 


### Seleccion 
Una selección aplicada a la salida de un operador no agrega
costo alguno
○ Es “hacer un if” con la condición de la selección y descartar
las filas que no la cumplan
● Cada bloque que sale del operador anterior se copia en
memoria, descartando las filas que corresponda. Al llenarse
este nuevo bloque se pasa al siguiente operador
○ No hay acceso a disco, por ende no hay costo
### Proyeccion a la salida
#### Con duplicados 
Como no necesito evitar duplicados, puedo hacer pipelining sin costo extra a la salida de cualquier operador. 
Simplemente de cada fila completa recibida en el bloque, se queda con la/s columna/s proyectadas

#### Sin duplicados 
Si precisa evitar duplicados, puede ir acumulando las
proyecciones en memoria hasta ocupar el espacio disponible
○ Cuando se ocupa todo, se envía a disco ordenado
○ Se hace sort externo, pero se evita la primer lectura de B(R),
teniendo un costo menor

### Junta a la salida 
Al recibir un bloque del operador anteiror, se puede hacer junta para todas sus fulas, sin requerir los proximos bloques 
El costo es menor porque se ahorra una lectura de B(R)
![[Pasted image 20241119210237.png]]
