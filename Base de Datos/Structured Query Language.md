---
aliases:
  - SQL
  - sql
  - Sql
---
 Lenguaje declarativo basado en cálculo de tuplas, trabajamos con tablas en vez de relaciones
## Data Definiton Language (DDL)
Para crear esquemas uso `CREATE SCHEMA nombre`. 
Para crear tablas, `CREATE TABLE nombre ( [definicion columna1, definicion columna 2, ...], [definicion restriccion1, definicion restriccion2, ...]`

las columnas se definen tal que `nombre_columna tipo_dato [ restricciones ]`, `padron INTEGER NOT NULL CHECK (padron > 10000)`
ademe de los [[Tipos de Datos]]