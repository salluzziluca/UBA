
# Manejo de Memoria
## malloc()
Para pedir x cantidad de memoria en el heap (dinámica) usamos malloc(valor). Ese valor va a ser la cantidad de bytes que nos de. 
ej `void *mi_bloque = malloc(500)` o  `void *mi_bloque_2 = malloc(sizeof(int))`
malloc devuelve un puntero a ese bloque de memoria.
SIEMPRE SIEMPRE SIEMPRE hay que chequear
```c
if (mi_bloque != NULL){

}
```
Y siempre hay que liberar el bloque despues 

`free(mi_bloque)`

Si necesitamos MAS memoria (o sea, el malloc te tira NULL) en el medio de nuestro programa, usamos. 
Internamente funciona como se aclara en [[Malloc y Brk#Funcionamiento Interno de Malloc]]
## realloc()

`realloc(*bloque, tamaño final que queremos)`
realloc le suma x cantidad de memoria a un bloque ya existente
```c
int *bloque=malloc(sizeof(int));
realloc(*bloque, 2*sizeof(int));
```

Si el puntero que le pasamos a realloc es NULL funciona igual que [[Manejo de Memoria#malloc|malloc()]]

En el caso de [[Archivos en C|lectura de archivos en C]], no sabemos cuanta memoria vamos a necesitar. Si cada linea ocupa 200 bytes podemos ir sumando cada 2 lineas 400 bytes o asi.

