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
Costo total = 2+10=12