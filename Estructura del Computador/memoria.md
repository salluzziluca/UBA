# Caché 
90% de ejecución correspondena 10% del código

### Principio de localidad
- Localidad temporal: si accedo a una direc, en poco tiempo lo volveré a hacer
- Localidad espacial: Si accedo a una direct, hay chances de que vaya acceder a una direc vecina
## Caracteristicas 
- Muy rapida
- De poca capacidad
- cercana al CPU

memoria dividida en bloques, al acceder un dato de la mem principal, bajo el bloque completo
En el proximo acceso verifico si la posicionbuscada está en caché, sino busco otro bloque. Al buscar ese nuevo bloque, devuelvo el anterior actualizado a RAM

## Estructuras
### Cache especializado
- caché de datos
- caché de instrucciones
### caché multinivel
- caché + grande = +lento pero con más indice de aciertos (caché multinivel)