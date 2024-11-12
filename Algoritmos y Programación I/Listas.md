---
dg-publish: true
---
# Listas
- Son mutables, se les pueden reasignar valores a cada uno de los items
```py
lista = [item0, item1, item2, item3]
lista_de_lista = [[item0.0, item0.1, item0.2],[item1.0, item1.1, item1.2]]
print('lista[0]')  #va a devolver item0
lista[0]= 22
print('lista[0]') # va a devolver 22
```

## Funciones de listas 
```py
lista = [0, 1, 2, 3]
len(lista) # devuelve 4
lista.append(8)
lista+=[12]
print(lista)  #va a devolver[0, 1, 2, 3, 8, 12]
lista.extend(range(4))
print(lista) #devuelve [0, 1, 2, 3, 8, 12, 0, 1, 2, 3]
lista.insert(2,9) 
print(lista) #devuelve [0, 1, 9, 3, 8, 0, 1, 2, 3]
del(lista[0]) 
print(lista) #devuelve [1, 9, 3, 8, 0, 1, 2, 3]
print(lista.pop(3)) # devuelve 8 y lo borra
lista.remove(2) #borra la primer concurrencia de 2
lista.clear #borra todo
lista.count(2) #devuelve la cantidad ed veces que aparece 2
lista.reverse # da vuelta todos los elementos
```

## Sorting
```
lista.sort(reverse = True/False, key= ) #ordena la lista
lista_ordenada = sorted(lista, reverse = True/False, key=) #crea una nueva lista ordenada
```
para crear las keys o criterios combiene usar [[Lambdas]]
## Slices
```py
lista = [0, 1, 2, 3]
print(lista[0:2]) # imprime [0, 1, 2]
del(lista[0:2]) #borra [0, 1, 2] de la lista
```

## Recorrer

```py
lista = ['Apa', 'pepo', 'papa', 'perro']
for i in range(len(lista)):
	print(i) #devuelve las posiciones "0 1 2 3"
for i in lista:
	print(i) # devuelve el contenido "Apa pepo papa perro"
```


## Empaquetado
![[Pasted image 20211005212317.png]]

## List comprehension 
```py
	numeros = [x for x in range(1, 101)] #arma una lista del 1 al 100
numeros = [x**2 for x in range(1, 101)] # los numeros del 1 al 100 al cuadrado
numeros = [x**2 for x in range(1, 101) if x % 2 == 0] # lista de los numeros pares del 1 al 100}

def impares_al_cuadrado(lista):

 lista_impares_cuadrado=[]

 lista_impares_cuadrado+=[x**2 if x%2 != 0 and x**2 not in lista_impares_cuadrado else x for x in lista] # si son impares ponelos al cuadrado, si son pares dejalos como estan, todo eso en la lista que nos den
``` 

