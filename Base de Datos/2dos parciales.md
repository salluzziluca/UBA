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