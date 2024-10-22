Si nos encontramos ante una [[Fallas|falla]] del tipo 1 o 2, cuando el sistema se reinica, la base de datos tiene que ser llevado al estado inmediato anterior al comienzo de la transaccion. Para eso necesitamos tener informacion en el log acerca de los cambios que la transaccion fue realizando. 

Para cada iins