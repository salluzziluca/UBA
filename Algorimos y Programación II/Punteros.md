Son variables que apuntan a una dirección de memoria. 
Si sabemos que tipo de dato es lo podemos aclarar `char *nombre`. Si no sabemos, podemos utilizar `void *nombre`.

## malloc()
Para pedir x cantidad de memoria en el heap (dinámica) usamos malloc(valor). Ese valor va a ser la cantidad de bytes que nos de. 
ej `void *mi_bloque = malloc(500` 
malloc devuelve un puntero a ese bloque de memoria.
SIEMPRE SIEMPRE SIEMPRE hay que chequear
```c if (mi_bloque != NULL){

}

```
Y siempre hay que liberar el bloque despues 

`free(mi_bloque)`