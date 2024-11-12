---
aliases:
  - SQL
  - sql
  - Sql
dg-publish: true
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


## Insercion


```SQL
INSERT INTO nombre_tabla [ ( nombre_col1 , ... , nombre_colN ) ] VALUES ( valor1, valor2, ... , valorN ) [, ( valor1, valor2, ... , valorN ) ... ] ;
```

Tambien puedo insertar mediante un select. TOdo lo que me devuelva ese select lo inserto.
```SQL
INSERT INTO nombre_tabla [ ( nombre_col1 , ... , nombre_colN ) ] SELECT ...;
```

Utilizando la opcion RETURNING (no standard) se nos devolvera el valor de las filas insertadas, esto es util para asber los IDs

## Modificacion

```SQL
UPDATE nombre_tabla SET columna1 = expresion1 [ , columna2 = expresion2 ... ] [ WHERE condicion ];
```

## Borrado 
```SQL
DELETE FROM nombre_tabla [ WHERE condicion ];
```


## Transacciones
Cuando queremos que varias operaciones se ejecuten
únicamente en su totalidad, usamos transacciones, indicando con comandos el inicio y fin de la transacción

```SQL
BEGIN TRANSACTION; comando1; [ comando2; ... comandoN ] COMMIT;
```
Puedo uisar ROLLBACK para volver atras los cambio


## Control de Acceso a los datos
Distintos usuarios deben tener acceso a distintos subconjuntos de los datos
○ No todas las tablas
○ No todas las columnas
○ No todas las filas

También se debe poder restringir operaciones a realizar. No todos deberian poder modificar / crear / insertar 

en postgres 
```SQL 
CREATE USER nombre_usuario WITH PASSWORD 'pass';
CREATE ROLE nombre_usuario WITH LOGIN PASSWORD 'pass';
DROP ROLE nombre_usuario;
GRANT nombre_rol TO nombre_usuario;
```
El comando GRANT permite dar privilegios a roles:
```SQL
GRANT privilegio1 [, privilegio2, ... , privilegioN ]
 ON [ nombre_tabla | DATABASE nombre_base_de_datos ]
 TO nombre_rol
 [ WITH GRANT OPTION ];
 ```
  La opción GRANT OPTION permite que el rol también pueda dar los privilegios a otros roles utilizando GRANT
Para revocar privilegios
```SQL
REVOKE [ GRANT OPTION FOR ]
 privilegio1 [, privilegio2, ... , privilegioN ]
 ON [ nombre_tabla | DATABASE nombre_base_de_datos ]
 FROM nombre_rol;
 ```
