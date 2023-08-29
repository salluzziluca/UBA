numero representado = $Mx \ base^{exp}$

de un total de n bits:
- 1 bit para el signo de la mantisa
- x bits para a mantisa
- y bits para el exponente (magnitud  y signo)
## Estandar IEEE 754
En 32 bits: 1 bit signo, 8 exponente y 23 para la mantisa
En 64 bits: 1, 11 y 52 para mantisa

Lo que no está estandarizado es lo siguiente: 
-  que base utiliza?
- numeros normalizados
- Formato para guardar exponente (signed int)
- valores "especiales"