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