---
dia: 2024-10-29
aliases:
  - NoSQL
dg-publish: true
---
Las SGBD no relaciones nacieron alrededor del 2000 con la masificación de web y cambios tecnológicos 

Se buscaban soluciones nuevas al problema del almacenamiento de datos que tuvieran:

Escalabilidad para trabajar grandes volúmenes de datos:
- Se necesita almacenar y procesar cantidades masivas dedatos 
- Iba de la mano de la digitalizacion y de la disponibilidad de datos en la red

Mayor performance en apps web:

Flexibilidad de datos: 
Estructura de datos que evolucione con el tiempo 
los [[Sistemas de Gestion de Bases de Datos|SGBD]] relacionales son muy rigidos. Agregar una columna puede ser muy costosos
El desarollo web busca darle mayor libertad al desarrollador para organizar los datos en una form semiestrucutrada. 
Esta flexibilidad tiene mucho que ver con metodologias [[Agile|agiles]] y [[Minium Viable Product|MVP]] 


### Distribucion 
Las grandes [[Sistemas de Gestion de Bases de Datos|SGBD]] relaciones no habian sido pensadas con distribucion en mente 
Se busca una mayor disponibilidad y tolerancia a fallas 
Se requieren mecanismos de replicacion y fragmentacion automatica de datos 
Se prioriza la capacidad de procesamiento distribuido.
<mark style="background: #BBFABBA6;">Era algo necesario, no se podia hacer la vista gorda</mark>
ver [[Bases de Datos Distribuidas]]

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
Almacenan vectores asociativos o [[Diccionarios]], Guardan conjuntos asociados
Las claves son únicas (es decir, no puede haber dos pares que posean la misma clave), y el único requisito sobre su dominio es que sea comparable por igual (=)

Ej: Dynamo (amazon)
#### primitivas
Insertar (put)
eliminar (delete)
update 
get
#### ventajas 
##### Simplicidad 
No se definen esquemas
No hay DDLs, restricciones de integridad, ni dominios 
El [[agregado]] es mínimo limitado al par
Se buscar guardar y consultar grandes cantidades de datos pero no [[interrelaciones]]
##### Velocidad 
se prioriza la eficiencia sobre la integridad de los datos

##### Escalabilidad 
Provee replicacion y permite repartir consultas entre nodos 

#### Dynamo 
Dynamo es el key-value store de Amazon. Está diseñado siguiendo una [[arquitectura]] orientada a servicio (SoA): la [[Bases de Datos|base de datos]] está distribuida en un server cluster que posee servidores web, routers de agregación y nodos de procesamiento (Dynamo instances). Utiliza un método de lookup denominado hashing consistente que reduce la cantidad de movimientos de pares necesarios cuando cambia la cantidad de nodos S. Esto hace que sea muy sencillo agregar nodos en forma dinámica, con un impacto mínimo. Utiliza un modelo de consistencia denominado consistencia eventual, que tolera pequeñas inconsistencias en los valores almacenados en distintas réplicas

##### Hashing consistente
Tenemos una función de [[hash]] que dada una clave devuelve un valor h(k)  entre 0 y 2^M -1 en donde M representa la cantidad de bits del resultado

![[hash consistente]]

sI hasheo y me da 50, voy en sentido de las agujas del reloj hasta el nodo mas cercano, n1. Si me hashea en 130, vamos a n3. 220? n4 y asi.

Es facil crear replicar. Puedo hacer que si uno cae en el 50, se guarde en el nodo 1 y se replique en el n2. Puedo hacer que replique en todos los nodos que quiero

Si quiero agregar un nodo nuevo y cae, por ejemplo, entre 192 y nodo4, este le tiene que pasar todos los datos correspondientes (si cae en 193, darle desde n3 a 193) y guardarse los suyo.

Fragmentacion horizontal en base al hash de la clave

Busqueda: aplico hash a la clave y se que en el proximo sv está


[[Modelos de consistencia]]
  
### Orientadas a documentos 
Un documento es una unidad estructural de informacion(agregado) que almacena datos bajo una cierta estructura.

Sin necesidad de definir un esquema rígido para la estructura del documento, estas bases de datos ofrecen la posibilidad de manejar estructuras un poco más complejas que un simple par clave: valor.

generalmente un documento tiene conjuntos de clave:valor que representan atributos de documento y sus valores. Se admiten atributos multivaluados, se admite que el valor de un atributo sea tmb un documento. Las estructuras de un documento se describen con HTML, XML, JSON, YAML

Ej: MongoDB

```json
Hamburguesa = { 
" nombre ": " BigBacon ",
" ingredientes ": ["pan", "carne", " lechuga ", "salsa", "pan", "carne", "tocino", "queso", " pepinillos ", "salsa", "pan" ],  " precio ": 129.99, 
"calorías": 930 
}
```
### Wide Column 

[[Bases de Datos Wide Colum]]
Cassandra
![[Pasted image 20241029211651.png]]
### Basadas en [[Grafos]] 


### Map Reduce
![[Pasted image 20241029211956.png]]


