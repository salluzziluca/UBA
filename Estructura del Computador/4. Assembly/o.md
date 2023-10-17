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
$2^n$ con n= tamaño
Luego mediante un mapa de memoria representamos la asignacion del mismo.
el tamaño del espacio direccionable es especifico del procesdor
el mapa de memoria es especifico de un sistema (dos sistemas con el mismo procesador no tienen el mismo mapa de memoria)

# Arqitectura ARC ( A Risc Computer)
Espacio de direcciones: 2^{32}
big endian
![[Pasted image 20231017164636.png]]

### Set de instrucciones
es un subconjunto de SPARC
todas las instrucciones ocupan 32 bits
32 registros de 32 bits
Program Status Register guarda los flags
Solo dos instrucciones acceden a memoria principal (RAM): read and write

## Mapa de memoria
![[Pasted image 20231017165203.png]]
0-2047 OS
2048-2^{31}-1 Memoria de usuario: Memoria ocupada por codigo de maquina y variables y system stack
2^{31}-1 - 2^{32}-1