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



# 1C 2024
![[Pasted image 20241007121021.png]]
```SQL
SELECT p.nombre, p.apellido, p.nacionalidad, e.nombre_equipo, C.nombre, count(*) as cantidad_carreras
FROM 
    PILOTOS P
JOIN 
    CARRERAS R ON P.cod_equipo = R.cod_equipo AND P.nro_piloto = R.nro_piloto
JOIN 
    EQUIPOS E ON P.cod_equipo = E.cod_equipo
JOIN 
    CIRCUITOS C ON R.id_circuito = C.id_circuito
GROUP BY 
    P.nombre, P.nacionalidad, E.nombre, C.nombre_circuito
HAVING 
	COUNT(CASE WHEN r.posicion <4 and R.ms_mejor_vuelta >60000 THEN 1 END) = COUNT(*)

```

![[Pasted image 20241007123833.png]]
```SQL
SELECT AVG(C.puntos_ganados) as promedio_puntos
FROM CARRERAS C
JOIN PILOTOS P on c.nro_piloto = p.numero_piloto AND p.cod_equipo = c.cod_equipo 
GROUP BY p.nombre, p.apellido
HAVING promedio_puntos >= 10
ORDER BY promedio_puntos desc
Limit 3

```


![[Pasted image 20241007124746.png]]



![[Pasted image 20241007100215.png]]

| Relación          | Clave Primaria | Claves Candidatas | Claves Foraneas              |
| ----------------- | -------------- | ----------------- | ---------------------------- |
| H(H1, E1)         | {H1}           | {H1}              | {E1}ref E                    |
| E(E1, E2, E3)     | {E1}           | {E1}              | -                            |
| F(F1, F2)         | {F1, F2}       | {F1, F2}          | -                            |
| G(F1, F2, E1)     | {F1, F2, E1}   | {F1, F2, E1}      | {F1, F2} ref F {E1} ref E    |
| A(A1, A2)         | {A1}           | {A1}              | -                            |
| B(A1, B1, B2)     | {A1, B1}       | {A1, B1}          | {A1} ref A                   |
| D(A1, B1, E1, D1) | {A1, B1, E1}   | {A1, B1, E1}      | {A1} ref A {B1} ref B {E1} E |

![[Pasted image 20241007105434.png]]

R1 (A,B,C)
F1{AB->C, C->B}
$AB^+ = {A, B, C}$
AC^+={A,C}
ABC es redundante
Clave: AB
Esta en 2FN
Esta en 3FN
No está en FNBC

R2(A,C,D,E) 
F2{C->D, D->E, E->D}

Indep = A
Equivalentes A y E

clave ACD y ACE
esta en 3FN

R3(E, G, H)
F3 (EG->H H->E, H->G, E->H, E->G, G->H)
no hay indep
E-> H y H->E son equivalentes 
E->G G-> son equivalentes
H->G y G->H tmb 
claves 
E
G
H

esta en FNCB


![[Pasted image 20241007114703.png]]

Localidad-> codigo postal
Codigo postal ->localidad
Nombre escuela, codigo postal escuela-> direccion_escuela
codigo_postal_escuela->localidad_escuela
Nombre_hijo, dni persona-> edad_hijo



# 1er recu  1C2024

## 1

![[Pasted image 20241008101403.png]]
```SQL 
SELECT c.nombre_circuito, p.nombre, p.apellido, p.nacionalidad, e.nombre, r.ms_mejor_vuelta
FROM c CIRCUITO
JOIN CARRERAS r on c.id_circuito = r.id_circuito 
JOIN PILOTOS p on p.cod_equipo = r.cod_equipo and p.nro_piloto = 
```

![[Pasted image 20241007154120.png]]

| Relación              | Clave Primaria   | Claves Candidatas | Claves Foraneas                    |
| --------------------- | ---------------- | ----------------- | ---------------------------------- |
| H(H1, H2, F1)         | {H1}             | {H1}              | {F1} referencia F                  |
| F(F1, F2)             | {F1}             | {F1}              | -                                  |
| A(A1)                 | {A1}             | {A1}              | -                                  |
| B(B1, A1)             | {B1, A1}         | {B1, A1}          | A1 ref A                           |
| D(B1, A1)             | {B1, A1}         | {B1, A1}          | B1 REF B A1 REF A                  |
| E(E1, E2, E3)         | {E1, E2}         | {E1, E2}          | -                                  |
| G(F1, A1, E1, E2, G1) | {F1, A1, E1, E2} | {F1, A1, E1, E2}  | F1 ref F, A1 ref A, {E1, E2} ref E |
![[Pasted image 20241007155424.png]]



![[Pasted image 20241007155954.png]]
No hay independientes 

A->H y H->A Son redundantes

Nos queda F={A->B, AG->C, DG->E, BC->A, C->E}

K =G,D PERO NO ES CLAVE 

A, C, B. 
GAD⁺={GAD, C, E, B}
GCD⁺= no es clave porque no tengo A para llegar a B
GDB⁺={GDB, E}

ACGD es redundante con GAD
ABGD es redundante con GAD
CBGD⁺={BCGD, A, E}

Les sumo el equivalente

GAD, BCGD, GHD


G->A, E->D, D->B, C->D, AB->C, CE->G

R1 ABCD F1= AB->C, D->B C->D
AB
AC
AD
2FN
es 3FN
No es FNBC


R2 ABEG F2= G->A ABE->G, E->B,
AE
GE

es 1FN





codigo->ronda 
ronda->fecha, horaInicio, legajo, patente
patente->modelo
legajo->nombre

