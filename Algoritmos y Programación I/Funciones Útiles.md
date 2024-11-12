---
dg-publish: true
---
# Funciones Útiles

## filter()
`filter(funcion usada para filtrar, lista/string/tupla)`

Ej: 
```py 
numeros = [0, 1, -3, 23, -1293, 123, 9423, -238271, -3181]
def es_negativo(x):
	return x<0
negativos = filter(es_negativo, numeros)
list(negativos)
```
Con [[Lambdas]]:
```py 
numeros = [0, 1, -3, 23, -1293, 123, 9423, -238271, -3181]

positivos = filter(lambda x: x>0, numeros)
list(positivos) #[1, 23, 123, 9423]
```