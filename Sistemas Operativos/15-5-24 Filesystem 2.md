El VFS tiene 4 cosas:
El dentry, el file, el inodo y e SB

Un inodo es la representacion de un file en disco,
Tenemos 12 bloques de datos, 1 que almacena un datablock, 1 que almacena un datablocks de datablocks y uno que almacena un datablocks de datablocks de datablocks


## API 
## open()
convierte el nombre de un archivo en na entrada de la tabla de file descriptors y devuelve dicho valor. SIempre devuelve el descriptor mas pequeño que no esté abiertos
`fd = open(path)`

El usuario ve un vector con los numeros de los fd, pero la info esta en kernel space

| numero | FDT           |
| ------ | ------------- |
| 0      | info en bytes |
| 1      | info en bytes |
| 2      | `| 0| 1 | 2 | 3 | 4 | 5 |`              |

## creat()
equivale a llamar un open con los flags O_CREAT|O_WRONLY|O_TRINC
si no existe te lo cree

## Close

## read()
Read lee pero nunca asegura que aa leer la cantidad de datos que vos le pedis que lea 
Hace intentos de lectura hasta un nmero dado de ytes de un archivo. La lectura comienza en a posicion señalada por el fd y 