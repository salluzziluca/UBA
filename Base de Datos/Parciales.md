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

π (PILOTOS.nombre, PILOTOS.apellido, PILOTOS.nro_piloto, CARRERAS.ms_mejor_vuelta) 
(σ (ms_mejor_vuelta = MIN(ms_mejor_vuelta)) (CARRERAS) ⋊⋉ (CARRERAS.cod_equipo = PILOTOS.cod_equipo AND CARRERAS.nro_piloto = PILOTOS.nro_piloto) (PILOTOS))
![[Pasted image 20241008111108.png]]

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

![[Pasted image 20241008101403.png]]
```SQL 
SELECT 
    c.nombre circuito,
    p.nombre,
    p.apellido,
    p.nacionalidad,
    e.nombre equipo,
    r.ms_mejor_vuelta
FROM 
    CIRCUITOS c
JOIN 
    CARRERAS r ON c.id_circuito = r.id_circuito 
JOIN 
    PILOTOS p ON p.cod_equipo = r.cod_equipo 
    AND p.nro_piloto = r.nro_piloto
JOIN 
    EQUIPOS e ON p.cod_equipo = e.cod_equipo
WHERE 
    (r.id_circuito, r.ms_mejor_vuelta) IN (
        SELECT 
            id_circuito, MIN(ms_mejor_vuelta)
        FROM 
            CARRERAS
        GROUP BY 
            id_circuito
    );

```


![[Pasted image 20241008105837.png]]
i
```SQL 
SELECT r.cod_equipo, r.nro_piloto, c.vueltas_finalizadas * c.longitud_km as cantidad_km
FROM carreras r 
JOIN CIRCUITOS c on r.id_circuito = c.id_circuito 
GROUP BY r.cod_equipo, r.nro_piloto
HAVING r.vueltas_finalizadas * c_longitud_km > 500000
```


![[Pasted image 20241008111112.png]]
![[Pasted image 20241008111121.png]]
$\pi(EQUIPOS.cod_equipo, PILOTO.nroo_piloto, PILOTO.nombre, PILOTO.apellido, PILOTO.nacionalidad)(\sigma(veces_campeon = max(veces_campeon))(EQUIPOS)  ⋊⋉ (EQUIPOS.codEquipo = PILOTOS.codPiloto)(PILOTO))$
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

![[Pasted image 20241008204445.png]]

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

# 2024 recu 2

Obtener el nombre, n´umero de piloto, nombre de circuito, y cantidad de vueltas de aquellos pilotos que hayan hecho la vuelta m´as r´apida, en los circuitos que tengan m´as de 60 vueltas.
![[Pasted image 20241009170555.png]]
![[Pasted image 20241009152946.png]]

| Relación              | Clave Primaria   | Claves Candidatas | Claves Foraneas                              |
| --------------------- | ---------------- | ----------------- | -------------------------------------------- |
| H(H1)                 | {H1}             | {H1}              |                                              |
| C(C1, B1, A1, C2)     | {C1, B1, A1}<br> | {C1, B1, A1}      | {B1} REF b,{A1} ref<br> A                    |
| B(B1, A1, B2)         | {B1, A1}         | {B1, a1}          | {A1} ref A                                   |
| G(H1, C1, B1, A1)     | {H1,C1, B1, A1}  | {H1,C1, B1, A1}   | {H1} ref H1, {C1} ref C, {B1}ref B {A1}ref A |
| A(A1, A2)             | A1               | A1                | -                                            |
| E(E1, E2)             | E1               | E1                |                                              |
| F(F1, F2)             | {F1, F2}         | {F1, F2}          |                                              |
| D(E1, F1, F2, A1, D1) | {E1, F1, F2}     | {E1, F1, F2}      | E1 REF E {F1, F2} ref F                      |
:DDDDDD


![[Pasted image 20241009153709.png]]
B ES INDEPENIENTE 
E es solo implicante


EA= EA, H, D, C, G ES CLAVE
EC = EC, A, H, D, G ES CLAVE
ED = ED
EH= EH
implicantes implicados: C, A, D, H

ECA=  superclave de EA y EC
ECD = superclave de EC
ECH= superclave
EAD = superclave EA
EAH = superclave EA
EDH = EDH, C, A, G es clave

ECAD superclave
ECAH superclave 
EADH superclave 
EDHC superclave 

CC: EDHB, EAB, ECB


![[Pasted image 20241009155431.png]]

AB->D 
R1 = AB⁺= AB, D,G. F2; AB->D, D->G, G->A
AB, BG y BD clave
NO ES FNBC
3FN
R2 = A, B, E,C. F2: E->B, ABC->E
CAB es clave
CAE es clave

3FN


![[Pasted image 20241009161623.png]]

charlas, articulos->workshop
articulo->escritor 
charla->expositor
workshop->fecha
escritor->fecha
expositor->fecha
# 2C 2023 
![[Pasted image 20241008212050.png]]
```SQL 
SELECT v.matricula, v.marca, v.modelo
FROM VEHICULO v 
JOIN MULTA m ON m.matricula = v.matricula
JOIN PROPIETARIO p ON v.matricula = p.matricula
JOIN PERSONA pe on pe.DNI = p.DNI
WHERE m.importe > 50000 and BETWEEN '2022-01-01' AND '2022-12-31' and pe.ciudad = 'Rosario'
```

![[Pasted image 20241008213351.png]]
```SQL 
SELECT p.DNI p.matricula SUM(importe) as total_a_pagar
FROM PROPIETARIO p 
JOIN MULTA m on p.matricula = m.matricula and p.DNI = m.DNI
WHERE m.fecha BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY p.DNI, m.matricula
ORDER BY total_a_pagar DESC;
```


![[Pasted image 20241009102553.png]]


![[Pasted image 20241009115128.png]]


![[Pasted image 20241009122658.png]]

R1: {D, A, B, C} F1 = D->A, D->B, D->C, B->C, A->B CC = D
Esta en 2FN
R2: D, E G F2: DE->G.
CC DE 
Está en FNBC
Se pierte g->C. 

El algoritmo no se detiene
![[WhatsApp Image 2024-10-09 at 12.56.03.jpeg]]
```SQL
AnimalesFelis = σ(genero = 'Felis')(animal)
animalEnReservaFelis = animal_en_reserva ⋊⋉ animal_en_reserva.nombre_cientifico = AnimalesFelis.nombre_cientifico AnimalesFelis
ReservasConFelis = reserva_natural ⋊⋉ reserva_natural.id_reserva = animalEnReservaFelis.id_reserva animalEnReservaFelis
ReservasConFelis1995 = σ(año_creacion > '1995')(animalEnReservaFelis)
NombreyCapacidad = pi(ReservasConFelis1995)
```



![[Pasted image 20241009142846.png]]


```SQL
WITH
    tiempos_ciclistas AS (
        SELECT
            c.cod_ciclista,
            SUM(m.tiempo) AS tiempo_total,
            SUM(m.puntaje) AS puntaje_total
        FROM
            CICLISTAS c
            JOIN MARCAS m ON c.cod_ciclista = m.cod_ciclista
            JOIN ETAPAS e ON e.num_etapa = m.num_etapa
        GROUP BY
            c.cod_ciclista
    )
SELECT
    cod_ciclista,
    tiempo_total,
    puntaje_total
FROM tiempos_ciclistas
WHERE
    tiempo_total = (
        SELECT MIN(tiempo_total)
        FROM tiempos_ciclistas
    );
```

- - **Objetivo:** Verifica que **no exista ninguna etapa** en la tabla `ETAPAS` que el ciclista no haya completado. Si existe alguna etapa que el ciclista no ha registrado en `MARCAS`, entonces esa etapa se devuelve por la subconsulta interna, y la condición `NOT EXISTS` fallaría.
    - **Efecto:** Si un ciclista ha participado en todas las etapas, entonces **no se devolverán resultados** de la subconsulta, lo cual satisface la condición `NOT EXISTS`.
- - **Objetivo:** Esta subconsulta se utiliza para cada etapa (`e`) y verifica si **no existe** una marca (`MARCAS`) correspondiente para ese ciclista en esa etapa.
- **Explicación:**
    - **`m2.cod_ciclista = c.cod_ciclista`**: Compara si el código del ciclista en la tabla `MARCAS` coincide con el ciclista actual.
    - **`m2.num_etapa = e.num_etapa`**: Compara si el número de etapa en la tabla `MARCAS` coincide con la etapa actual en la tabla `ETAPAS`.
- **Efecto:** Si **no existe una marca** para ese ciclista en esa etapa, entonces la subconsulta devuelve un resultado, y esto hace que la condición `NOT EXISTS` sea verdadera, indicando que el ciclista **no ha completado** esa etapa.

```SQL
SELECT 
    'Ganadores por etapas' AS etapas,
    m1.cod_ciclista AS Etapa1,
    m2.cod_ciclista AS Etapa2,
    m3.cod_ciclista AS Etapa3
FROM 
    MARCAS m1,
    MARCAS m2,
    MARCAS m3
WHERE 
    m1.num_etapa = 1 AND m1.tiempo = (SELECT MIN(tiempo) FROM MARCAS WHERE num_etapa = 1) AND
    m2.num_etapa = 2 AND m2.tiempo = (SELECT MIN(tiempo) FROM MARCAS WHERE num_etapa = 2) AND
    m3.num_etapa = 3 AND m3.tiempo = (SELECT MIN(tiempo) FROM MARCAS WHERE num_etapa = 3);

```
o
```SQL
with mayor_puntaje_por_etapa as (
	select m.num_etapa, max(m.puntaje) as max_puntaje
	from marcas m
	group by (m.num_etapa))

select c.nombre_ciclista as ganador, c.cod_ciclista, me.num_etapa, me.max_puntaje
from ciclistas c
inner join marcas m using (cod_ciclista)
inner join mayor_puntaje_por_etapa me using (num_etapa)
where m.puntaje = me.max_puntaje
```


