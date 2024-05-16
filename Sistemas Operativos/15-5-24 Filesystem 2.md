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

## touch() 
cambia la ultima fecha de modificacin del archivo.

Cuando crea un archivo un touch, no tiene contenido. El inodo te avisa que no tenes que ir al bloque, estas tranqui

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

## chmod()
cambia los bits del modo de acceso
(r, rw, rwx)

## chown() 
cambia el id del propietario del archivo y  el grupo de un archivo


# Implementacion del filesystem
## very sismple file system

### Organizacion General 
Un bloque de memoria es e equivalente a un 4kbytes en disco.
La vision del sistema de archivos debe ser la de una particion de N bloques (0 a n-1) de un tamaño de $N*4KB$ bloques. Un disco de unos 64 bloques tendria esta pinta
![[Pasted image 20240515195349.png]]

==IMPORTANTE, NO SON NECESARIOS 5 BLOQUES DE INODOS, SOLO4 PORQUE EL MAXIMO QUE PODEMS ALOCAR SON 64 INODOS DE UN BLOQUE C/U==
La seccion del filesystem que almacena datos de usuarios se llama DataRegion
![[Pasted image 20240515201156.png]]

La primera parte es se dvide entra superbloque, , e inode bitmap

tengo un superbloque, un bitmap de bloques que me dice si el bloque esta libre o no y un bitmap de inodosque me dice si el inodo está o no

La cantidad de blques debe ser la cantidad de archvos de un bloque que vos podes tener por inodo, si tengo 64 bloques puedo tener como mucho 64, seguriismamente vayas a tener menos, pero de maximo 64
![[Pasted image 20240515201231.png]]

B1+B2+B3 = offset inodo 1
B1+B2+B3+256 = offset inodo 2
B1+B2+B3+256x63 = offset inodo 64


Este sistema funciona muy bien porque es agil para archivos chicos y buena para archivos muy grandes (porque te deja manejar un monton de espacio). Y la gran mayoria de los archivos son chikitos.


==EL INODO NO OCUPA, EL INODO APUNTA==
