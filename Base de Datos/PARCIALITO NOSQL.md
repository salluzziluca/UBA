---
Dia: 2024-11-11
---
## MongoDB

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



```js
[
  {
    $match: {
      full_text: /futbol/i // Filtra tweets que contengan "futbol" (case-insensitive)
    }
  },
  {
    $project: {
      // Extraemos la hora del día del campo created_at y transformamos los hashtags a un array
      hour: {
        $hour: {
          $toDate: "$created_at"
        }
      },
      hashtags: {
        $ifNull: [
          {
            $split: ["$full_text", "#"]
          },
          []
        ]
      },
      favorite_count: 1
    }
  },
  {
    $unwind: {
      path: "$hashtags",
      preserveNullAndEmptyArrays: true // Conserva tweets sin hashtags como array vacío
    }
  },
  {
    $match: {
      // Filtra hashtags vacíos, para no contar los tweets sin hashtags
      hashtags: {
        $ne: ""
      }
    }
  },
  {
    $group: {
      _id: {
        hashtag: "$hashtags",
        hour: "$hour"
      },
      // Agrupa por hashtag y hora
      total_favorites: {
        $sum: "$favorite_count"
      }
    }
  },
  {
    $sort: {
      "_id.hour": 1,
      "_id.hashtag": 1
    } // Ordena por hora y hashtag
  }
]
```
1. Muestre los familiares de Billy Moore que no han tenido participaci´on en ning´un crimen.
```cypher
match (bm:Person {name: "Billy", surname: "Moore"})-[:KNOWS]-(p:Person) where not (p)--(:Crime) return p
```

1. Muestre la (o las) persona(s) que ha(n) realizado mas de 7 comunicaciones telef´onicas.
```cypher
Match(p:Person)-[:HAS_PHONE]-(f:Phone)-[:CALLED|CALLER]-(pc:PhoneCall)

  

WITH p, COUNT(pc) AS llamadas_realizadas

WHERE llamadas_realizadas > 7

RETURN p, llamadas_realizadas
```
