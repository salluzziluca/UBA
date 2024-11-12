---
dg-publish: true
---
Para linux, todo es un archivo. Casi todo se puede manejar como si se tratara de un archivo. Incluso una comunicación entre computadoras

El FS permite a los ususarios organizar sus daos para que se persistan a traves de un largo periodo de tiempo.Es una abstracion que provee datos persistentes bajo un nombre

Permite que una vez que un programa termina d generar un archivo, otro puede utilizarlo

Archivos: compuestos por datos
directorios: definen nmbres para los archivos
![[Excalidraw/FILE SYSTEM]]

bin donde se guardan los ejecutables
etc archivos de config
usr archivos ejecutables
temp ves todos los dispositivos que tiene la maquina
## Virtual File system
Un subsistema del kerne que implementa la interfaz que tiene que ver con los archivos y el sistema de archivos provistos a los programas corriendo en modo usuario. TODOS los sitemas deben basarse en VFS para coexsistir e inter operar. 


==El file system tiene que adaptarse a VFS, no al revés== 


Todos los filesystem independientemente del tipo que implemente se comunican al VFS, este gestiona las syscall y gestiona los read y writes con cada uno de los fs fisicos

write en c -> sys_write() en VFS->filesystem write method (depende de c/u)->memria fisica


![[Pasted image 20240508191542.png]]

### Objetos del VFS
El Super Bloque representa un sistema de archivos 
El inodo que representa a un archivo en particular (totalidad del archivo en el sistema, sabe en que parte del disco fisicamene está el archivo)
El DEntry representa una entrada de directiorio. (el PATH)
`/home/usr/file.c 
/ es un dentri (root)
home, usuario y file.c son dentries
![[Pasted image 20240508192814.png]]

Los directorios se representan como dentries, cada uno con un inodo asociado, si hago cd home voy al directorio cuyo inodo corresponde. Este va a tener otra tabla (directorio) con los archivos que contiene representados con dentries con inodos correspondientes, vendra a ser como su ID. Todos con su inodo en caso de querer acceder a ellos

![[Pasted image 20240508194011.png]]
![[Pasted image 20240508195202.png]]


### Metadata 
Info a cerca del archivo que es comprendida por el sisop 
tamaño
fecha de modificacion
propietario 
informacion de seguridad


## INODO

Un inodo apnta aun bloque

Un inodo guarda data. Tiene un arreglo de 15 punteros
Los primeros 12 apuntan diferentes data blocks. El 13 apunta a un bloque que apunta a diferentes data blocks. El 14 a un bloque que apunta a un bloques que apunta a un data blocks



Si intentamos abrir un archivo no existente, para lectura nos va a dar error, para escritura lo va a crear. Vacio pero con la metadata

espacio total de la tabla dividido espacio del bloque da la cantidad de bloques
Si cada bloque ocupa 4bytes y las tablas ocupan 4k bytes. hay 1000 bloques por tabla. Luego c/u de esos bloques pueden apuntar a 


ej bloque = 4096 bytes 
ptr_blo = 4bytes 
4096(12+1024+(1024)^2 + 1024^3)


Hard links es la relacion entre un path y un inodo. Ambos path apuntan al mismo inodo 

Un softlink es cuando un archivo apunta a otro. (acceso directo)