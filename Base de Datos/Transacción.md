---
aliases:
  - transacciones
---
Serie de operaciones que o bien se hacen enteras o no se hacen.(ej: transacción)
Yo defino esta serie de operaciones como transaccion

Si una transacción no puede terminar de realizarse porque una de sus operaciones viola alguna restricción de integridad, entonces debe dejarse la [[Bases de Datos|base de datos]] en el estado anterior al inicio de la misma. Mariano Beiró | Dpto. de Comput


## Transaccion en SQL 
```SQL 
BEGIN TRANSACTION;
SELECT nombre, saldo FROM cuentas WHERE cod_cli = 2564;
Nombre | saldo
---------------------------------
Alberto | 2.200
UPDATE cuentas SET saldo = 8.000 WHERE cod_cli = 2564 ;
COMMIT;
SELECT nombre, saldo FROM cuentas WHERE cod_cli = 2564;
Nombre | saldo
---------------------------------
Alberto | 8.000
```