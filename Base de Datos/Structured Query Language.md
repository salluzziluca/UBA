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
ademe de los [[Tipos de Datos]] ya conocidos. Tenemos VARCHAR (string), DATE, TIME, TIMESTAMP (con o sin TimeZone) e INTERVAL (en horas, minutos, segundos)

### Restricciones 
![[Pasted image 20240910203954.png]]
```SQL
CREATE TABLE Persona (
 dni INT PRIMARY KEY,
 nombre VARCHAR(255) NOT NULL,
 fecha_nacimiento DATE
);
CREATE TABLE HijoDe (
 dni_hijo INT,
 dni_padre INT,
 PRIMARY KEY (dni_hijo, dni_padre),
 FOREIGN KEY (dni_hijo) REFERENCES Persona(dni),
 FOREIGN KEY (dni_padre) REFERENCES Persona(dni)
);
```



El ilike esta bueno para buscar cosas pero no para poner en un programa. Porque ademas no utiliza los indices



### Between 'algo' and 'algo'
para valores continuos

Un left join va a tomar todos los elementos de la tabla de la izquiera y los de la derecha que esten en la intersección, es decir, los de la derecha que cumplan la condición

