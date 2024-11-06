---
Dia: 2024-11-06
---
En vez de tablas usamos [[Grafos]]
Son muy buenas para datos dinamicos, donde los datos son dificiles de predecir. Las relaciones entre los datos contribuyen a dar significado a los datos


## Neo4j
Logra cumplir con las [[Bases de Datos NoSQL#AC]]

Cumple con el paradigma ACID, **Atomicity, Consistency, Isolation, and Durability**.

Es muuuy rapida
Tiene un sistema de clustering que le permite operar en momentos criticos 

tiene muchos drivers oficiales a travez de http

Tamaño sin limite, super escalable

modelo de propiedades, si saco un dato en particular no pongo nulo, simplemente no existe y listo 

Cypher Query Language

Son muy facheros de visualizar

### Modelo de grafo etiqueta-propiedad 

#### Nodos: 
Pueden tener etiquetas para su clasificacion 
Las etiquetas tienen indiices nativos 

#### Relaciones 
Relacionan nodos por tipo y direccion 

#### Propiedades 
Atributos de nodos y relaciones.
Almacenados como clave valor 
Pueden tener inidices e indices compuestos

