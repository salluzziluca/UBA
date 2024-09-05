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

|   |   |   |   |
|---|---|---|---|
|movies.id|movies.name|movies.year|movies.quality|
|212097|Metropolis|1927|1|
|64833|City Lights|1931|1|
|163288|It Happened One Night|1934|1|
|216964|Modern Times|1936|1|
|131240|Gone with the Wind|1939|1|
|221130|Mr. Smith Goes to Washington|1939|1|
|64729|Citizen Kane|1941|1|
|56044|Casablanca|1942|1|
|91758|Double Indemnity|1944|1|
|163485|It s a Wonderful Life|1946|1|
|235676|Notorious|1946|1|
|177138|Kind Hearts and Coronets|1949|1|
|319181|Sunset Blvd.|1950|1|
|316323|Strangers on a Train|1951|1|
|144861|High Noon|1952|1|
|156234|Ikiru|1952|1|
|302696|Singin in the Rain|1952|1|
|280803|Roman Holiday|1953|1|
|312934|Stalag 17|1953|1|
|85669|Dial M for Murder|1954|1|
|273543|Rear Window|1954|1|
|969|12 Angry Men|1957|1|
|250612|Paths of Glory|1957|1|
|352639|Vertigo|1958|1|
|15936|Anatomy of a Murder|1959|1|
|33923|Ben-Hur|1959|1|
|235062|North by Northwest|1959|1|
|266574|Psycho|1960|1|
|169942|Judgment at Nuremberg|1961|1|
|371844|Yojimbo|1961|1|
|334212|To Kill a Mockingbird|1962|1|
|92616|Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb|1964|1|
|253440|Persona|1966|1|
|364329|Who s Afraid of Virginia Woolf?|1966|1|
|70404|Cool Hand Luke|1967|1|
|1711|2001: A Space Odyssey|1968|1|
|281937|Rosemary s Baby|1968|1|
|62076|Chinatown|1974|1|
|30431|Barry Lyndon|1975|1|
|89147|Dog Day Afternoon|1975|1|
|218599|Monty Python and the Holy Grail|1975|1|
|241347|One Flew Over the Cuckoo s Nest|1975|1|
|230151|Network|1976|1|
|280270|Rocky|1976|1|
|326155|Taxi Driver|1976|1|
|17760|Annie Hall|1977|1|
|10830|Alien|1979|1|
|18960|Apocalypse Now|1979|1|
|190166|Life of Brian|1979|1|
|204163|Manhattan|1979|1|
|270971|Raging Bull|1980|1|
|313478|Star Wars: Episode V - The Empire Strikes Back|1980|1|
|271095|Raiders of the Lost Ark|1981|1|
|40199|Blade Runner|1982|1|
|123572|Gandhi|1982|1|
|289558|Scarface|1983|1|
|313479|Star Wars: Episode VI - Return of the Jedi|1983|1|
|12937|Amadeus|1984|1|
|26844|Back to the Future|1985|1|
|10920|Aliens|1986|1|
|313059|Stand by Me|1986|1|
|121538|Full Metal Jacket|1987|1|
|86274|Die Hard|1988|1|
|159172|Indiana Jones and the Last Crusade|1989|1|
|131780|Goodfellas|1990|1|
|32178|Beauty and the Beast|1991|1|
|328277|Terminator 2: Judgment Day|1991|1|
|276217|Reservoir Dogs|1992|1|
|346949|Unforgiven|1992|1|
|134672|Groundhog Day|1993|1|
|290070|Schindler s List|1993|1|
|117874|Forrest Gump|1994|1|
|267038|Pulp Fiction|1994|1|
|46169|Braveheart|1995|1|
|141544|Heat|1995|1|
|291698|Se7en|1995|1|
|342384|Twelve Monkeys|1995|1|
|109093|Fargo|1996|1|
|337830|Trainspotting|1996|1|
|131665|Good Will Hunting|1997|1|
|13978|American History X|1998|1|
|289109|Saving Private Ryan|1998|1|
|13789|American Beauty|1999|1|
|112290|Fight Club|1999|1|
|200521|Magnolia|1999|1|
|14942|Amores perros|2000|1|
|129185|Gladiator|2000|1|
|210511|Memento|2000|1|
|276085|Requiem for a Dream|2000|1|
|90772|Donnie Darko|2001|1|
|37057|Big Fish|2003|1|
|113504|Finding Nemo|2003|1|
|176711|Kill Bill: Vol. 1|2003|1|
|224842|Mystic River|2003|1|
|239851|Oldboy|2003|1|
|104338|Eternal Sunshine of the Spotless Mind|2004|1|
|30959|Batman Begins|2005|1|
|302329|Sin City|2005|1|
La pelicula de categoria comedia mas vieja es Metrópolis

Muestre el nombre y apellido de los actores que actuaron en las mismas pel´ıculas que el actor Ferdy Mayne.