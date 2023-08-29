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


Para la representacion del exponente se una a cosa esa del 7 ya qe premite una comparacion mas sencila. El problema de este sistema es que podemos tener tanto overflow como underflow. 
Cuando hay overflow decimos que es infinito
Cuando estamos en underflow decimos que es 0

si divido por infinto nos da cero, pero no se puede representar en punto flotante asi que el sistema lo decla

listafuiba6670@gmail.com