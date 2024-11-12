---
dg-publish: true
---
# Merge
Juntar dos archivos distintos que "hablen" sobre lo mismo. Como precondicion, ambos archivos tienen que estar ordenados por al menos un campo. 
Si ademas de estar ordenado no se repiten los valores del campo ordenado, ni siquiera se hace un while
Leemos ambos campos ordenados en ambos archivos. Y nos quedamos con el mínimo. Seguimos avanzando con ESE archivo hasta encotrar que el campo cambie de valor. Ahi pasamos al segundo archivo y seguimos sumando valores asociados al valor inicial del campo. Cuando este vuelva a cambiar, volvemos al archivo inicial y arrancamos con el segundo valor. 

![[Merge.mp4]]
#### Ejemplo cuentas de tarjeta
Dos archivos, uno de debito y uno de credito con cuentas de banco. 
Miramos las primeras lineas y seteamos la cuenta minima, cuando encontramos que ambos archivos tienen la misma cuenta empezamos a leer la plata y la acumulamos, cuando vemos que no hay mas cuentas 1 cortamos el while, pasamo a un nuevo archivo y volvemos a empezar con la cuenta siguiente

```py
codigoArchivo1, valorArchivo1 = leer_archivo(archivo1)
codigoArchivo2, valorArchivo2 = leer_archivo(archivo2)
codigoArchivo3, valorArchivo3 = leer_archivo(archivo3)

while not finArchivo1 or not finArchivo2 or not finArchivo3:
	acumulador = 0
	minCod = min(codigoArchivo1, codigoArchivo2, codigoArchivo3)

	while not finArchivo1 and minCod == codigoArchivo1:
		acumulador += valorArchivo1
		codigoArchivo1, valorArchivo1 = leer_archivo(archivo1)
		
	while not finArchivo2 and minCod == codigoArchivo2:
		acumulador += valorArchivo2
		codigoArchivo2, valorArchivo2 = leer_archivo(archivo2)
		
	while not finArchivo3 and minCod == codigoArchivo3:
		acumulador += valorArchivo3
		codigoArchivo3, valorArchivo3 = leer_archivo(archivo3)

	
```