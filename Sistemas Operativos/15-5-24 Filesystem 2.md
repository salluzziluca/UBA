El VFS tiene 4 cosas:
El dentry, el file, el inodo y e SB

Un inodo es la representacion de un file en disco,
Tenemos 12 bloques de datos, 1 que almacena un datablock, 1 que almacena un datablocks de datablocks y uno que almacena un datablocks de datablocks de datablocks


## API 
## open()
convierte el nombre de un archivo en na entrada de la tabla de file descriptors y devuelve dicho valor. SIempre devuelve el descriptor mas pequeño que no esté abiertos
`fd = open(path)`
