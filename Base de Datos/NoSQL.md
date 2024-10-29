Las SGBD no relaciones nacieron alrededor del 2000 con la masificacion de web y cambios tecnologicos 

Se buscaban slluciones nuevas al probelema del alamcneamiento de datos que tuvieran:

Escalabilidad para trabajar grandes volumenes de datos:
- Se necesita almacenar y procesar cantidades masivas dedatos 
- Iba de la mano de la digitalizacion y de la disponibilidad de datos en la red

Mayor performance en apps web:

Flexibilidad de datos: 
Estructura de datos que evolucione con el tiempo 
los SGBD relacionales son muy rigidos. Agregar una columna puede ser muy costosos
El desarollo web busca darle mayor libertad al desarrollador para organizar los datos en una form semiestrucutrada. 
Esta flexibilidad tiene mucho que ver con metodologias [[Agile|agiles]] y [[Minium Viable Product|MVP]] 


### Distribucion 
Las grandes SGBD relaciones no habian sido pensadas con distribucion en mente 
Se busca una mayor disponibilidad y tolerancia a fallas 
Se requieren mecanismos de replicacion y fragmentacion automatica de datos 
Se prioriza la capacidad de procesamiento distribuido.
Era algo necesario, no se podia hacer la vista gorda

--- 
Los joins de tablas son COSTOSOS 
el manejo de tr