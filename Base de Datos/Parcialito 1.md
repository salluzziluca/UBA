![[Pasted image 20240905161652.png]]


| Relación              | Clave Primaria                           | Claves Candidatas | Claves Foraneas  |
| --------------------- | ---------------------------------------- | ----------------- | ---------------- |
| H(H1, H2, F1)         | {H1}                                     | {H1}              | {F1}             |
| F(F1, F2)             | {F1}                                     | {F1}              | -                |
| A(A1)                 | {A1}                                     | {A1}              | -                |
| B(B1, A1)             | {B1, A1}                                 | {B1, A1}          | {A1}             |
| D(B1, H1)             | {B1, A1}(porque es debil y necesita a A) | {B1, A1}          | {B1, A1}         |
| E(E1, E2, E3)         | {E1, E2}                                 | {E1, E2}          |                  |
| F(F1, F2)             | {F1}                                     | {F1}              |                  |
| G(A1, E1, E2, F1, G1) | {A1, E1, E2, F1}                         | {A1, E1, E2, F1}  | {A1, E1, E2, F1} |


1. A.  Mostrar el nombre y año de filmación, de la/s película/s catalogada/s como comedia (Comedy) más vieja/s de la b
Query:
```
comedias = σ(genre)='Comedy'(movies_genres)
comedias_peliculas = π movie_id (σ genre='Comedy'(movies_genres)) ⋊ movies
τ year ASC (comedias_peliculas)

```

|movies.id|movies.name|movies.year|movies.quality|
|---|---|---|---|
|212097|'Metropolis'|1927|1|
|64833|'City Lights'|1931|1|
|163288|'It Happened One Night'|1934|1|
|216964|'Modern Times'|1936|1|
|131240|'Gone with the Wind'|1939|1|
|221130|'Mr. Smith Goes to Washington'|1939|1|
|64729|'Citizen Kane'|1941|1|
|56044|'Casablanca'|1942|1|
|91758|'Double Indemnity'|1944|1|
|163485|'It s a Wonderful Life'|1946|1|
La pelicula de categoria comedia mas vieja es Met