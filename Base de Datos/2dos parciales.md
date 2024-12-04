---
Dia: 2024-12-04
dg-publish: true
---
![[Pasted image 20241204102357.png]]
a) Costo de file scan = 400,000 bloques Costo index scan = 2 + 66,667 + 2 + 2500 = 69,171 bloques b) 200,000 filas de argentina 7,500 filas de uzbekistan La seleccion devuelve: 207,500 filas

![[Pasted image 20241204102446.png]]![[Pasted image 20241204102457.png]]



![[Pasted image 20241204102523.png]]
```json 
db.collection.aggregate([
	{
	$match: {
		"categoria": "Informatica"
		}
	},
	{
	$unwind: "$autores"
	},
	{
	$group: {
	_id: "$autores",
	"cantidad": {
	$sum: 1
			},
	"promedio_puntaje": {
	$avg: "$puntaje"
			}
		}
	},
	{
	$match: {
	"cantidad": {
	$gte: 10
			}
		}
	},
	{
	$project: {
	"autor": "$_id",
	"cantidad": 1,
	"promedio_puntaje": 1,
	_id: 0
		}
	}
])
```



![[Pasted image 20241204102806.png]]
```cypher 
MATCH (t1:Usuario)-[p1:PUNTUA]->(pub:Publicacion)<-[p2:PUNTUA]-(t2:Usuario)
WHERE t1.username < t2.username AND p1.puntaje >= 8 AND p2.puntaje >= 8
AND NOT EXISTS {
MATCH (t1)-[p3:PUNTUA]->(:Publicacion)<-[p4:PUNTUA]-(t2)
WHERE ( p3.puntaje >= 8 AND p4.puntaje <= 7 ) OR ( p3.puntaje <= 7 AND p4.puntaje >=8 )
}
WITH t1, t2 , COUNT(pub) AS cantidad
WHERE cantidad >= 5
RETURN t1, t2, cantidad
```


![[Pasted image 20241204102851.png]]
5) b) Es serializable porque no tiene ciclos. Un solapamiento serial equivalente seria T1 -> T2 -> T3 c) T2 y T3 leen cosas escritas por T1 Como T1 commitea antes que T2 y que T3, es recuperable El write de Y de T3 no lo lee ninguna transaccion activa con lo que es recuperable

![[Pasted image 20241204102911.png]]
a) Hasta el inicio de la transaccion mas antigua entre T1 y T3, es decir, hasta la linea 1 b) En A grabamos 10, en B 40, en C 17 y en B 30 Queda en A 10, en B 30, en C 17




---- 

(Procesamiento de consultas) Como recordará de exámenes previos, los siguientes esquemas
de relación almacenan información sobre las multas de tránsito de la Ciudad de Buenos Aires:
![[Pasted image 20241204105113.png]]
Tenga en cuenta que el infractor que cometió una multa con un vehículo no es necesariamente
la misma persona registrada como propietaria de ese vehículo.
Esta base de datos registra distintos tipos de multa, que van desde el tipo 1 (menos severa)
al tipo 4 (muy severa). Entre las multas de tipo 4 se incluyen infracciones como “ingresar al
Paseo del Bajo en contramano” o “cruzar semáforo en rojo sonando una sirena falsa”, que
determinan el quite de la licencia de por vida al propietario del vehículo.
Por lo tanto, cuando una persona se presenta para renovar su licencia de conducir, además de
chequear que la persona no haya cometido ella misma infracciones, se chequea que jamás se
haya cometido una infracción de tipo 4 con ninguno de los vehículos que son de su propiedad.
De lo contrario, la licencia es denegada. La siguiente consulta, en particular, es realizada cuando Marlon Siniestra (DNI 18.324.715) se presenta a renovar su licencia en las oficinas de
la Dirección de Tránsito:
```SQL
SELECT ∗
FROM Propietario p INNER JOIN Multa m USING ( matricula )
WHERE p.DNI = 18324715 AND m.tipo = 4 ;
```
Se pide:
a) Sugiera dos índices que puedan utilizarse para ejecutar más eficientemente esta consulta.
Luego dibuje un plan de ejecución que haga uso de estos dos índices para la consulta.
Específicamente, dibuje el árbol del plan de consulta y anote sobre el mismo los métodos
de acceso o algoritmos que se utilizarán en cada paso.
b) Estime el costo del plan de ejecución que armó en el punto anterior, en términos de
cantidad de accesos a bloques de disco.
Para el ejercicio considere que los índices son de tipo árbol y tienen altura 4. Además,
considere para sus cálculos la siguiente información de catálogo:
![[Pasted image 20241204104742.png]]

Indices: DNI en propietarios y matricula en multa
![[consulta]]
Seleccion: Index scan con DNI como indice de clustering 
$Cost(σ Ai=v (R)) = Height(I(A,R)) + ⌈B(R) / V(A,R)⌉$
4+⌈100.000/300.000⌉ = 4+1=5

su cardinalidad seria n/variabiilidad = 600.000/300.000= 2
y su B = n/F(r)=  600.000/6=100.000
F(r) = n/B = 6

costo junta: loop con unico indice
Cost(R⨝S) = B(R) + n(R) * ( Height(I(A,S)) + ⌈B(S) / V(A,S)⌉ )
B(R) no me interesa por pipeline y n(R) = 2 
$2*(4+⌈30.000/100.000⌉ )=2*(4+1)=2*5=10$
luego la ultima seleccion no tiene costo. 
Costo total = 5+10=15

Luego 
$mín(⌈B(R)/V(A,R)⌉ ; ⌈B(S)/V(A,S)⌉) \leq M - 2$
B(vehiculos)/Variabilidad = 200.000/600.000 = 1/3. B(multas)/variabilidad = 30.000/100.000=1/3 todo joya

(Procesamiento de consultas) Para las mismas tablas del ejercicio anterior y la misma información de catálogo, se quiere calcular cuántas multas se han cometido con cada marca de vehículo. Asumiendo que no se cuenta con ningún tipo de índice y que se dispone de M=20.000 bloques de memoria, se arma el siguiente plan de ejecución en el que la junta se realiza por el método de hash GRACE:
![[Pasted image 20241204111658.png]]

Se pide:
a) Indique qué cantidad k de particiones intentaría generar para que la junta hash GRACE sea factible de ser realizada, justificando su respuesta. Estime qué tamaño promedio –en términos de cantidad de bloques– tendrían las particiones en ese caso.
b) Indique cuál es el/los atributo/s a los que habrá que aplicar la función de hash en cada tabla, a efecto de construir las particiones
c) Estime cuál sería el costo de realizar la junta planteada, en términos de cantidad de accesos a bloques de disco. Considere que el agrupamiento posterior se realiza en pipeline utilizando un diccionario en memoria, y por lo tanto no incurre en costos de acceso a disco.

N<=M-1
por lo que N= 20.000-1 -> 19.999 
Luego min(B(R)/N, B(S)/N)<= M-2-> 30.000/N <= M-2
ambas entran porque 30.000/19.999 <= M-2 y 200.000/19.999 <=M-2

b) los atributos a hashear sean matriculas en la tabla de vehiculos y matriculas en la tabla de multas

$3*B(Multa) +3*B(vehiculos)= 3*30.000+3*200.000$



## Mongo 
(MongoDB) El Club de Cinéfilos quiere armar un ranking de actores que permita a sus
miembros saber quiénes son los 100 actores a los que más vale la pena seguir. Para ello,
cuentan con una base de datos de películas en MongoDB, que indica el puntaje en IMDB
de cada película junto con el listado de actores de la película, tal como ejemplifica el
siguiente documento:
```json
{
	"_id" : 10910355903998401931 ,
	" nombre_pelicula " : " Interstellar " ,
	" genero_principal " : " CienciaFicción" ,
	"puntaje_IMDB" : 8. 7 ,
	" actores " : [ 'Matthew McConaughey ' , ' Jessica Chastain' , 'Anne Hathaway ' ,
	' Mackenzie Foy ' , ' Timothée Chalamet ' , 'Matt Damon' , ' Michael Caine ' ]
}
```
Mientras discutían qué métrica utilizar para rankear a los actores, algunos sugerían usar el puntaje promedio en IMDB de sus películas como un valor representativo. Otros encambio consideraban que se debía tomar el mejor puntaje de entre todas las películas
en las que el actor participó, ya que si un actor participó en una película muy buena, entonces valía la pena seguirlo aún cuando su promedio fuera malo.
Finalmente, se decidió por una estrategia híbrida en que se ordenará a los actores por su puntaje promedio en todas sus películas, pero se exluirá luego a aquellos actores cuya mejor película no tenga un puntaje mayor o igual a 8.0.
1) Escriba una consulta en MongoDB que devuelva el listado de los 100 mejores actores ordenados por este criterio, indicando para cada actor su nombre y apellido, su puntaje promedio, y la máxima puntuación obtenida por sus pelícuas.
2) Explique si la consulta anterior puede ser ejecutada con la colección shardeada por el atributo $\_id$. En caso afirmativo, explique brevemente cómo podría realizarse el cálculo anterior en forma distribuida entre los shards y los servidores de agregación. En caso negativo, explique cuál debería ser el/los atributo/s de sharding, y cómo se realizaría el cálculo en forma distribuída en ese caso.

```json 
[
	{$unwind: "$actores"},
	{$group:{
		_id="$actores",
		promedio: {$avg: "$puntaje_IMDB"},
		mejor_pelicula: {$max: "$puntaje_IMDB"}
	}},
	{$match:{
		"mejor_pelicula":{
		$gte:8}
		}
	},
	{$sort:{
		"promedio": -1
		}
	},
	{$limit:100}	
		
]
```

Si, shardear por id siempre es una opcion, no siempre la mejor, pero es ir a lo seguro. Se podrian hashear los diferentes IDs y agruparlos en shards segun lo que devuelva esa funcion de hashing. dE esa forma quedarian distribuidas las diferentes peliculas de manera bastante equitativa. El unico tema es que al calcular el promedio por actor, esto se hara por shard, por l que el numero variará mucho entre shards. LA solucion es que devuelvea la suma de las  peliculas y la cantidad de peliculas de ese shard para el actor


## neo
b) (Neo4j) La Facultad de Ingeniería quiere implementar un sistema de búsqueda de empleo en el que los estudiantes puedan cargar las asignaturas que cursaron y las empresas
puedan cargar los conocimientos que requieren en cada búsqueda. El objetivo del sistema
es recomendar a los estudiantes ofertas de empleo para las cuales estén potencialmente
calificados, a partir de la información que se almacenará en una base de datos en Neo4j
con los siguientes nodos y aristas:
```cypher
1 ( est:Estudiante {nombre : 'Guillermina' , apellido : ' Fabbri ' ,
2 username : ' laguille9  ' , padrón : 109329 } )
3 ( asign : Asignatura {nombre : ' Base de Datos ' , codigo : '7515 ' } )
4 ( conoc : Conocimiento {nombre : 'BASES DE DATOS NOSQL' } )
5 ( conoc2 : Conocimiento {nombre : 'POSTGRESQL' } )
6 ( busq : Busqueda {nombre_empresa : ' El Sauce S .R. L . ' ,
7 fecha : '2023−10−27 ' , contacto : ' rrhh@elsauce.com.ar ' } )
8 . . .
9 ( est )−[ :APROBO]−>(asign)
10 ( asign )−[ :OFRECE]−>(conoc )
11 ( busq )−[ :DESEA]−>(conoc )
```
Así, cuando un estudiante se encuentre buscando empleo, el sistema le rankeará las
búsquedas disponibles mostrando primero aquellas para las cuales el estudiante se encuentra mejor preparado, en el sentido de que cumpla con poseer la mayor cantidad de
conocimientos que la misma exije.
Escriba una consulta en Neo4j que, dado un estudiante específico de padrón p liste las búsquedas ordenadas con dicho criterio, indicando los datos de la búsqueda y la cantidad de conocimientos deseados por la misma que el alumno posee.

```cypher
MATCH (est: Estudiante {padron = p})->[:APROBO]->(asing: Asignatura)->[:OFRECE]->(con: Conocimiento)<-[:DESEA]-(busq: Busqueda)
RETURN busq count(distinct conoci)
Order BY count(distinct conoci) DESC
```


## Concurrencia 


a) (Concurrencia) Dado el siguiente solapamiento de transacciones: `bT1 ; bT2 ; bT3 ; WT3 (Y); WT3 (X); WT1 (Y); cT3 ; RT2 (Y); RT2 (X); cT2 ; WT1 (X); cT1 1)` Dibuje el grafo de precedencias del solapamiento. 2) Indique si el solapamiento es serializable. Justifique su respuesta. 3) Indique si el solapamiento es recuperable. Justifique su respuesta
![[Excalidraw/Concurrencia|Concurrencia]]

No es serializable porque hay un ciclo T2 lee un dato qeu despues T1 escribe y T1 escribe un dato que despues t2 lee.

No es recuperable porque T1 escribe en Y y luego T2 lee, mas t1 commitea despues de T2


## recuperacion 
![[Pasted image 20241204121701.png]]


En la recuperación hay nuevamente dos situaciones: Que encontremos primero un registro (END CKPT).En ese caso, deberemos retroceder hasta el (BEGIN , Tx ) más antiguo del listado que figure en el (BEGIN CKPT). Deshago los writes y Escribo (ABORT, Ty ) para aquellas que no hayan commiteado.
bdQue encontremos primero un registro (BEGIN CKPT).Si el checkpoint llego sólo hasta este punto no nos sirve. Deberemos volver hacia atrás, pero sólo hasta el inicio de la más antigua del listado

Encontramos el end en la 11 y subimos hasta encontrar su begin ckpt en la 06. El checkpoint es sobre T2, por lo que retrocedo hasta el begin de T2. A partir de ahi (linea 2) deshago y hago abort de todo lo que no haya commiteado (t3 y t4). 
A = 8, b =8, c = 9 y aborto T3 yt4

---

(Procesamiento de consultas) Gustavo trabaja en la Dirección de Tránsito del municipio de Tandil. Cada vez que un conductor se acerca para renovar su licencia de conducir, Gustavo debe verificar que el mismo no posea ninguna multa de tránsito pendiente de pago. Para consultar el estado de deuda del conductor, Gustavo accede a una base de datos relacional con las siguientes dos tablas:
![[Pasted image 20241204135216.png]]

La base de datos también dispone de un índice secundario por DNI_propietario y de un índice de clustering por pagada, ambos sobre la tabla Multas. Cuando Clemenciano Taqui llega para renovar su licencia (nro. 740523), Gustavo ejecuta la siguiente consulta en la base de datos:

```SQL 
SELECT ∗
FROM licencias INNER JOIN multas ON DNI_conductor=DN I_p ropietario
WHERE nro_licencia =740523
AND pagada IS FALSE ;
```

Se pide: 
a) Proponga un plan de ejecución eficiente para esta consulta. Para ello dibuje un plan de consulta y anote sobre el mismo los métodos de acceso o algoritmos que se utilizarán en cada paso.

![[Drawing 2024-12-04 13.57.12.excalidraw]]



b) Estime el costo del plan de ejecución que armó en el punto anterior, en términos de cantidad de accesos a bloques de disco. 
Para el ejercicio considere que los índices son de tipo árbol y tienen altura 4. Además, considere para sus cálculos la siguiente información de catálogo:

![[Pasted image 20241204135306.png]]

costo file scan licencias = B(Licencias) = 5.000

por pipeline sale una sola licencia, la 740523, por lo que n()=1 

luego para el loop con unico indice secundario sin clustering (DNI PROPIETARIO)

$Cost(R⨝S) = B(R) + n(R) * ( Height(I(A,S)) + ⌈n(S) / V(A,S)⌉ )$ 

$1*(H+\left( \frac{n(multas)}{V(DNI\_PROP,MULTAS)} \right)$
= 1(4+60.000/15.000)=4+4=8

luego la proxima seleccion por pipelining no tiene costo



El Instituto Nacional de Coordinación Agrícola se ocupa de brindar asistencia a los productores rurales, contando con un extenso equipo de asesores asignados a las distintas provincias del país. Su base de datos cuenta con los siguientes esquemas de relación con datos sobre los asesores y los productores rurales:
![[Pasted image 20241204141448.png]]

Se quiere construir una tabla para poner en contacto a los asesores con los productores de las provincias que les fueron asignadas, a través de la siguiente operación de junta:
$Asesores ▷◁_{prov\_asignada=prov\_origen}  Productores$
Estime la cardinalidad del resultado de esta junta en términos de cantidad de tuplas y en términos de cantidad de bloques, utilizando el siguiente histograma de frecuencias extraído de la información de catálogo que muestra la frecuencia de las 5 provincias principales de cada tabla. Considere además que V (prov_asignada, Asesores) = V (prov_origen, P roductores) = 23 y que el factor de bloque de ambas tablas es de 10.

![[Pasted image 20241204141545.png]]