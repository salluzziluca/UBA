# Tuplas
Conjuntos de datos INMUTABLES. Si se puede concatenar
```py 
tupla=(0, 1, 2, 3, 4, 5)
tupla[1] #devuelve 1
tupla += (6, 7, 8) #la tupla queda como (0, 1, 2, 3, 4, 5, 6, 7, 8)
```

## Funciones
```py 
tupla=(0, 1, 2, 3, 4, 5)
min(tupla) # devuelve 0
tupla.count(2) #devuelve 1
len(tupla) #devuelve 6
2 in tupla # devuelve true
sorted(tupla) #ordena la tupla pero creando una lista
```

## Slices
```py
tupla = (0, 1, 2, 3)
print(tupla[0:2]) # imprime (0, 1, 2)
```