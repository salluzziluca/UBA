Hay que tenere en cuenta donde se guardan fisicamente las variables, como accedo a los periferios, donde seguarda fisicamente el programa
==como está organizada la memoria==

La memoria esta organizada en tablas cuyas filas son cada una de 8 bits
| n°  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   |     |     |     |     |     |     |     |     |
| 2   |     |     |     |     |     |     |     |     |
| 3    |     |     |     |     |     |     |     |     |

Hay dos formas de ordenar la informacion
- Little-endian: el byte menos significativo en la direccion mas baja
- Big-endian: el byte menos significativo en la direccion mas alta
## Espacio direccionable
deerminado por el tamaaño del Registro del procesador
$2^n$