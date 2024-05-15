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
Hace intentos de lectura hasta un nmero dado de ytes de un archivo. La lectura comienza en a posicion señalada por el fd y se incrementa el numero de bytes leidos

## write()

## lseek(int fd, off_t offset, in whence)
reposiciona el desplazamiento de un archivo abierto cuyo fd pasamos como parametro a la fncon de acuerdo con el parametro whence
SEEK_SET: el desplazamiento
SEEK CUR: EL desplazamiento  es sumado a la posicion  actua de n archivo
SEEK END: el desplazamiento se suma a aprtir del final del archivo

## dup() y dup2()
![[Pasted image 20240515185656.png]]
## Link(oldpath, newpath)
Crea un hardlink entre ambos path. 


## unlink()
hace falta que te lo diga?
eliminan un nombre de archivo del sistema de archivo. SI era el ultimo link o nombre del archivo lo borra

# Directorios
## mkdir()


## dirent.h
Estructura de daos provista para poder eer las entradas a ls directorios 
![[Pasted image 20240515191253.png]]
## opendir(dirname)
are el dir y devuelve un stream correpsondiente al directorio que se está leendo en dirname

## readdir()
lee la prox entrada de un dir 
devuelve un punteor a una estructura que contene la informacion sobre el archivo

## closedir(DIR* dirstream)
cierra el stream del tipo dir cuyo nombre es dirstream

# Metadatos

## stat()
devuelve informacion sobre un archvo en el buffer apontado por statbuf. No se requiere ningún permiso sobre el archivo en cuestión, pero sí en los directorios que conforman el path hasta llegar al archivo.

## access()

