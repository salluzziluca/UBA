---
dg-publish: true
---
# Archivos
Se necesita una ruta y un modo.

##### Como funciona la lectura de archivos.
El archivo está en memoria disco, al abrirlos se pasa a RAM, se modifica, se llee o lo que se tenga que hacer, etc. Cuando se CIERRA, vuelve a memoria disco, no nos olvidemos de CERRARLO.

## Apertura
```archivo = open(RUTA, MODO)```
o
```with open(RUTA, MODO) as archivo:```
## Ruta de un archivo
La ruta(path) puede ser absoluta o relativa
### Ruta absoluta de un archivo
```C:\Users\sallu\Documents\GitHub\Algo1Guarna\Ejercitación\archivo.txt```

### Ruta relativa de un archivo
```Algo1Guarna\Ejercitación\archivo.txt```


## Modo
`archivo = open(RUTA, r)`-->read
`archivo = open(RUTA, w)`-->write
`archivo = open(RUTA, r+)`--> read and write
`archivo = open(RUTA, a)`-->append
`archivo = open(RUTA, b)`-->binary

### Tipos de read
`read(bytes)`: lee n bytes del archivo (1 byte = 1 caracter)
`readline()` lee una linea del archivo(si el archivo entra en memoria)
`readlines()` devuelve una lista con las líneas del archivo(si el archivo entra en memoria)
`for linea in archivo:` itera por cada una de las lineas


DOOONT YOU FORGET ABOUT MEEEEEE:
![[Pasted image 20211116192306.png]]

## Tell and seek
`teel()` indica la siguiente posicion en la que está el puntero del archivo (segun bytes/caracteres). Si estamos en el caracter 20, nos devuelve 21. 

`seek(CUANTOS, DESDE)`Sirve para mover el puntero desde un byte/caracter x bytes/caracteres para adelante o para atrás.

Lo más comun es leer archivos .csv porque estos son formas sencillas de guardar y almacenar informacion. Los .csv estan compuestos por campos, cada campo es una columna y se separan entre ellos por ;. Si tenemos un .csv con al menos un campo ordenado podemos llevar a cabo un [[Corte de Control]]. 

Si nos dan dos o mas archivos con informaciones diferentes pero relativas al mismo tema, podemos condesarlos usando tanto [[Merge]](si ambos archivos son igual de importantes) como [[Apareo]](si un archivo es actualizado con cosas de un segundo.)
