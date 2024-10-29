---
dia: 2024-10-29
---
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
<mark style="background: #BBFABBA6;">Era algo necesario, no se podia hacer la vista gorda</mark>

--- 
Los joins de tablas son COSTOSOS 
el manejo de transacciones en forma distribuida no escala 


En los ultimos años aumento mucho la velocidad de almacenamiento, su latencia y bajo mucho su costo. Tanto en RAM como en almacenamiento. tambien aumento la velocidad del internet
Lo que no mejoro fue la velocidad de procesamiento 
![[Pasted image 20241029192254.png]]

Por eso era importante hacer sistemas distribuidos

## Tipos de de SGBD No-SQL 
En cada una cambia la definicion de agregado, es decir como los conmjuntos de objetos relacionados se agrupan en colecciones para ser tratados como unidad y ser almacenados en un mismo lugar 
- El conjunto de datos perosnales de un cliente de una empresa 
- Un post de facebook (con comentarios, posteo en si, usuarios)

### Clave Valor 

### Orientadas a documentos 
### Wide Column 

### Basadas en Grafos 

