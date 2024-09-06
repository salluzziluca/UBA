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
comedias_peliculas_renombrada=ρid→movie_id ,name→name1 ,year→year1,quality→quality1(comedias_peliculas)
comedias_conjuntas = comedias_peliculas ⨯ comedias_peliculas_renombrada
comedias_conjuntas2 = σ(movies.year>movies.year1) comedias_conjuntas
comedias_no_viejas = π movies.id, movies.name, movies.year, movies.quality comedias_conjuntas2
comedias_peliculas - comedias_no_viejas
```


|           |             |             |                |
| --------- | ----------- | ----------- | -------------- |
| movies.id | movies.name | movies.year | movies.quality |
| 212097    | Metropolis  | 1927        | 1              |

La pelicula de categoria comedia mas vieja es Metrópolis

Muestre el nombre y apellido de los actores que actuaron en las mismas películas que el actor Ferdy Mayne.