---
dg-publish: true
---
1. 
![[Pasted image 20240905161652.png]]


| Relación              | Clave Primaria                           | Claves Candidatas | Claves Foraneas                      |
| --------------------- | ---------------------------------------- | ----------------- | ------------------------------------ |
| H(H1, H2, F1)         | {H1}                                     | {H1}              | {F1 ref. F}                          |
| F(F1, F2)             | {F1}                                     | {F1}              | -                                    |
| A(A1)                 | {A1}                                     | {A1}              | -                                    |
| B(B1, A1)             | {B1, A1}                                 | {B1, A1}          | {A1 ref. A}                          |
| D(B1, A1)             | {B1, A1}(porque es debil y necesita a A) | {B1, A1}          | {B1, A1}ref B, {A1} ref A            |
| E(E1, E2, E3)         | {E1, E2}                                 | {E1, E2}          |                                      |
| G(A1, E1, E2, F1, G1) | {A1, E1, E2, F1}                         | {A1, E1, E2, F1}  | {A1 ref A} {E1, E2 ref E} {F1 ref F} |


2. A.  Mostrar el nombre y año de filmación, de la/s película/s catalogada/s como comedia (Comedy) más vieja/s de la b
Query:
```
comedias = σ genre = 'Comedy' (movies_genres)
comedias_peliculas = π movies.id, movies.name, movies.year (comedias ⨝ (movies.id = movies_genres.movie_id) movies)
comedias_peliculas_renombrada=ρid→movie_id ,name→name1 ,year→year1(comedias_peliculas)
comedias_conjuntas = comedias_peliculas ⨯ comedias_peliculas_renombrada
comedias_conjuntas2 = σ(movies.year>movies.year1) comedias_conjuntas
comedias_no_viejas = π movies.id, movies.name, movies.year comedias_conjuntas2
comedias_peliculas - comedias_no_viejas
```

Resultado:

|movies.id|movies.name|movies.year|
|---|---|---|
|64833|'City Lights'|1931|

La pelicula de categoria comedia mas vieja es City Lights

2. B. Muestre el nombre y apellido de los actores que actuaron en las mismas películas que el actor Ferdy Mayne.

Query:
```

ferdy_mayne_id = πid(σ (first_name = 'Ferdy' ∧ last_name = 'Mayne') (actors))
peliculas_con_maynee = πroles.movie_id(ferdy_mayne_id ⨝ (actors.id = roles.actor_id) roles)
peliculas_con_maynee_renombrada = ρmovie_id → pelicula_id(peliculas_con_maynee)  -- Renombrar movie_id a pelicula_id
actores_de_peliculas_con_mayne = peliculas_con_maynee_renombrada ⨝ (roles.pelicula_id = roles.movie_id) roles
ids_actores_con_mayne = πroles.actor_id, roles.movie_id (actores_de_peliculas_con_mayne)

-- Contar cuántas películas tiene cada actor con Ferdy Mayne
conteo_actores = γ actor_id; count(movie_id) → num_peliculas (ids_actores_con_mayne)

-- Filtrar actores que estuvieron en más de una película con Ferdy Mayne
actores_en_dos_o_mas_peliculas = σ(num_peliculas >= 2) (conteo_actores)

-- Renombrar la columna actor_id en actores_en_dos_o_mas_peliculas
actores_renombrados = ρactor_id → actor_id_con_mayne (actores_en_dos_o_mas_peliculas)

-- Hacer el join con la tabla actors usando la columna renombrada
actores_con_nombre_apellido = actores_renombrados ⨝ (actor_id_con_mayne = actors.id) actors

-- Proyectar los campos actor_id_con_mayne, first_name y last_name
actores_con_mayne = πactor_id_con_mayne, first_name, last_name (actores_con_nombre_apellido)
actores_con_mayne- (πid, first_name, last_name( σ (first_name = 'Ferdy' ∧ last_name = 'Mayne') (actors)))

```
Resultado:

| roles.actor_id_con_mayne | actors.first_name | actors.last_name |
| ------------------------ | ----------------- | ---------------- |
| 329794                   | 'André'           | 'Morell'         |
El actor con el que Ferdy Mayne compartió todas sus peliculas es André Morell