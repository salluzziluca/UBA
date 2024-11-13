---
Dia: 2024-11-11
dg-publish: true
---
## MongoDB

1. Para tweets que tengan 1000 o m´as rewteets (‘retweet count’) y hayan depu´es de las 12 del mediod´ıa, obtener los ids, texto y cantidad de favoritos para los 5 con m´as favoritos (‘favorite count’). Utilice una ´unica consulta b´asica con find(, ).sort({}).limit()
```js
db.tweets.find({
  $and: [
    { "retweet_count": { $gte: 1000 } },
    { $expr: { $gte: [{ $hour: { $toDate: "$created_at" } }, 12] } }
  ]
}, {
  _id: 1,
  full_text: 1,
  favorite_count: 1
})
.sort({ "favorite_count": -1 })
.limit(5)
```


1. Por cada hashtag y hora del d´ıa (00, 01, 02, ...) obtener el total de favoritos conseguidos por tweets que contengan la palabra “futbol” en el texto. Se debe indicar si se ignoraron o no los tweets que no tienen hashtags (justificar). Se debe utilizar el pipeline de agregaci´on.
En mi caso no tome los tuits que no tienen hashtags, pensando justamente en que se quiere analizar los diferentes hashtags por hora, ya que esto permite evaluar trafico de redes de las diferntes subtematicas dentro del ambito del futbol (partidos en particular, equipos, etc). Si agruparamos todos los hashtags nulos en una categoria, estos no nos brindarian informacion util
```js

  [
    {$match: {
        $and: [
          { full_text: {$regex: RegExp('futbol', 'i') } }
        ]
      }},
    {$unwind: {
        path: '$entities.hashtags',
        preserveNullAndEmptyArrays: false
      }},
    {$group: {
        _id: { hashtag: '$entities.hashtags.text',
          	hour: { $hour: '$created_at' }},
        totalFavorites: { $sum: '$favorite_count' }
      }},
    {$project: {
        hashtag: '$_id.hashtag',
        hour: '$_id.hour',
        totalFavorites: 1
      }}]
```

3.
- match: filtra aquellos tuits en idioma portugues y provenientes de brasil
- group agrupa los tuis por id de la conversacion. Si el tuit no es una respuesta (por lo que no tiene in reply to status id str, se usa el id del tuit propio). Dentro de cada grupo se guarda el id, el contenido del tuit, el user y la fecha de creacion. Almacena tambien el avg retweets del grupo.
- Projec
- 
## Neo4j
1. Muestre los familiares de Billy Moore que no han tenido participaci´on en ning´un crimen.
```cypher
match (bm:Person {name: "Billy", surname: "Moore"})-[:FAMILY_REL]-(p:Person) where not (p)--(:Crime) return p
```

1. Muestre la (o las) persona(s) que ha(n) realizado mas de 7 comunicaciones telef´onicas.
```cypher
Match(p:Person)-[:HAS_PHONE]-(f:Phone)-[:CALLED|CALLER]-(pc:PhoneCall)

  

WITH p, COUNT(pc) AS llamadas_realizadas

WHERE llamadas_realizadas > 7

RETURN p, llamadas_realizadas
```
