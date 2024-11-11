---
Dia: 2024-10-29
---
las [[bases de datos NoSQL]] buscan aumentar la velocidad de procesamiento y la capacidad de almacenar información, explotando las ventajas que brindan las redes de computadoras y ne particular en internet. Para esto usa un [[SGBD Distribuido]]

## Fragmentacion 
>[!info] Tarea de dividir un conjunto de [[Agregado|agregados]] entre un conjunto de nodos 

Como separo la data entre diferentes servidores.

Busca almacenar conjuntos muy grandes de datos que no caben en un unico nodo
Paralelizar el procesamiento, permitiendo que cada nodo ejecuta una parte de las consultos para integrar despues los resultado s

Se suele usar una combinacion de ambas
### fragmentacion horizontal 
Cada nodo almacena un subconjunto de [[Agregado|agregados]]

### Fragmentacion vertical 
Distintos nodos guardan un subconjunto de [[Base de Datos/Atributos|atributos]] de cada [[agregado]]. Todos suelen compartir los [[Base de Datos/Atributos|atributos]] que conforman la clave. 



## Replicacion 
>[!info] Almacenar multiples copias de un mismo [[dato]] en distintos nodos del sistema


A veces me conviene tener las cosas en mas de una computadora. 
Para [[fallas]] y para poder servir los datos de manera amas rapida (distribuir la carga)

Esto nos genera un problema,<mark style="background: #FF5582A6;"> (in)consistencia de los datos</mark>. Puede haber distintos valores para un mismo dato, y eso a veces es un problema.
### Replicas secundaria 
solo de backup

### Replicas primarias 
Las que pueden procesar datos

## Lookup
En que servidor esta el [[dato]] que yo necesito 


## Metodos de acceso 
Cuando ya se en que servidor esta, dentro de ese sv, tengo que saber donde está

## Modelos de consistencia 
