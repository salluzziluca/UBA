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

|                                                                      |             |                |
| -------------------------------------------------------------------- | ----------- | -------------- |
| movies.name                                                          | movies.year | movies.quality |
| Metropolis                                                           | 1927        | 1              |
| City Lights                                                          | 1931        | 1              |
| It Happened One Night                                                | 1934        | 1              |
| Modern Times                                                         | 1936        | 1              |
| Gone with the Wind                                                   | 1939        | 1              |
| Mr. Smith Goes to Washington                                         | 1939        | 1              |
| Citizen Kane                                                         | 1941        | 1              |
| Casablanca                                                           | 1942        | 1              |
| Double Indemnity                                                     | 1944        | 1              |
| It s a Wonderful Life                                                | 1946        | 1              |
| Notorious                                                            | 1946        | 1              |
| Kind Hearts and Coronets                                             | 1949        | 1              |
| Sunset Blvd.                                                         | 1950        | 1              |
| Strangers on a Train                                                 | 1951        | 1              |
| High Noon                                                            | 1952        | 1              |
| Ikiru                                                                | 1952        | 1              |
| Singin in the Rain                                                   | 1952        | 1              |
| Roman Holiday                                                        | 1953        | 1              |
| Stalag 17                                                            | 1953        | 1              |
| Dial M for Murder                                                    | 1954        | 1              |
| Rear Window                                                          | 1954        | 1              |
| 12 Angry Men                                                         | 1957        | 1              |
| Paths of Glory                                                       | 1957        | 1              |
| Vertigo                                                              | 1958        | 1              |
| Anatomy of a Murder                                                  | 1959        | 1              |
| Ben-Hur                                                              | 1959        | 1              |
| North by Northwest                                                   | 1959        | 1              |
| Psycho                                                               | 1960        | 1              |
| Judgment at Nuremberg                                                | 1961        | 1              |
| Yojimbo                                                              | 1961        | 1              |
| To Kill a Mockingbird                                                | 1962        | 1              |
| Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb | 1964        | 1              |
| Persona                                                              | 1966        | 1              |
| Who s Afraid of Virginia Woolf?                                      | 1966        | 1              |
| Cool Hand Luke                                                       | 1967        | 1              |
| 2001: A Space Odyssey                                                | 1968        | 1              |
| Rosemary s Baby                                                      | 1968        | 1              |
| Chinatown                                                            | 1974        | 1              |
| Barry Lyndon                                                         | 1975        | 1              |
| Dog Day Afternoon                                                    | 1975        | 1              |
| Monty Python and the Holy Grail                                      | 1975        | 1              |
| One Flew Over the Cuckoo s Nest                                      | 1975        | 1              |
| Network                                                              | 1976        | 1              |
| Rocky                                                                | 1976        | 1              |
| Taxi Driver                                                          | 1976        | 1              |
| Annie Hall                                                           | 1977        | 1              |
| Alien                                                                | 1979        | 1              |
| Apocalypse Now                                                       | 1979        | 1              |
| Life of Brian                                                        | 1979        | 1              |
| Manhattan                                                            | 1979        | 1              |
| Raging Bull                                                          | 1980        | 1              |
| Star Wars: Episode V - The Empire Strikes Back                       | 1980        | 1              |
| Raiders of the Lost Ark                                              | 1981        | 1              |
| Blade Runner                                                         | 1982        | 1              |
| Gandhi                                                               | 1982        | 1              |
| Scarface                                                             | 1983        | 1              |
| Star Wars: Episode VI - Return of the Jedi                           | 1983        | 1              |
| Amadeus                                                              | 1984        | 1              |
| Back to the Future                                                   | 1985        | 1              |
| Aliens                                                               | 1986        | 1              |
| Stand by Me                                                          | 1986        | 1              |
| Full Metal Jacket                                                    | 1987        | 1              |
| Die Hard                                                             | 1988        | 1              |
| Indiana Jones and the Last Crusade                                   | 1989        | 1              |
| Goodfellas                                                           | 1990        | 1              |
| Beauty and the Beast                                                 | 1991        | 1              |
| Terminator 2: Judgment Day                                           | 1991        | 1              |
| Reservoir Dogs                                                       | 1992        | 1              |
| Unforgiven                                                           | 1992        | 1              |
| Groundhog Day                                                        | 1993        | 1              |
| Schindler s List                                                     | 1993        | 1              |
| Forrest Gump                                                         | 1994        | 1              |
| Pulp Fiction                                                         | 1994        | 1              |
| Braveheart                                                           | 1995        | 1              |
| Heat                                                                 | 1995        | 1              |
| Se7en                                                                | 1995        | 1              |
| Twelve Monkeys                                                       | 1995        | 1              |
| Fargo                                                                | 1996        | 1              |
| Trainspotting                                                        | 1996        | 1              |
| Good Will Hunting                                                    | 1997        | 1              |
| American History X                                                   | 1998        | 1              |
| Saving Private Ryan                                                  | 1998        | 1              |
| American Beauty                                                      | 1999        | 1              |
| Fight Club                                                           | 1999        | 1              |
| Magnolia                                                             | 1999        | 1              |
| Amores perros                                                        | 2000        | 1              |
| Gladiator                                                            | 2000        | 1              |
| Memento                                                              | 2000        | 1              |
| Requiem for a Dream                                                  | 2000        | 1              |
| Donnie Darko                                                         | 2001        | 1              |
| Big Fish                                                             | 2003        | 1              |
| Finding Nemo                                                         | 2003        | 1              |
| Kill Bill: Vol. 1                                                    | 2003        | 1              |
| Mystic River                                                         | 2003        | 1              |
| Oldboy                                                               | 2003        | 1              |
| Eternal Sunshine of the Spotless Mind                                | 2004        | 1              |
| Batman Begins                                                        | 2005        | 1              |
| Sin City                                                             | 2005        | 1              |
La pelicula de categoria comedia mas vieja es Metrópolis

Muestre el nombre y apellido de los actores que actuaron en las mismas pel´ıculas que el actor Ferdy Mayne.