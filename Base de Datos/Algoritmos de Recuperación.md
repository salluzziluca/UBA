En los 3 se asumen que los solapamientos son recuperables y que evitan rollbacks en cascada (ver [[Recuperabilidad]])

## Algoritmo UNDO (inmmediate update) 
1. Cuando al transaccion T_i modifica el item X reemplazando su valor v_old por v, se escribe (WRITE, T_i, X, v_old) en log. Luego se hace flush al log del disco