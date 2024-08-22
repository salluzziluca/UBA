# Instancias u Objetos
Las intancias u objetos son, justamente, objetos de esa misma clase, se pueden crear tanto como se quiera y a cada uno asignarle los [[Algoritmos y Programación I/Atributos]] que se desee.

## Creación de un objeto
```py
class Item:
	pass
	
item_1 = item()
item_2 = item
```

## Asignación de atributos
```py
item_1.nombre = 'Celular'
item_2.nombre= 'Compu'
item_2.precio = 30000
```

Para obtener una lista con todos los objetos usamos `Class.all`
```py
class Item:
	Item.all.append(self)
	
print(Item.all) #todos los objetos
```
Esto tambien nos permite iterar entre [[Algoritmos y Programación I/Atributos|atributos]]
Tambien podemos utilizar el [[Magic Metods (Métodos Magicos)]] `__repr__`

