---
dg-publish: true
---
	68uaaqdefrtgftn mm<z cvn# Atributos
Los atributos son variables de un objeto. Pueden (o suelen) ser caracteristicas de este. Para ver todos los atributos usamos el atributo magico `__dict__`, nos devuelve los atributo como un diccionario.
## Asignación de Atributos
```py
item_1.nombre = 'Celular'
item_2.nombre= 'Compu'
item_2.precio = 30000
print(item_2.__dict__) #{nombre : 'Compu', precio : 3000}
```
Los atributos tambien pueden ser asignados a la propia clase de la siguiente forma(pensarlo como una  atributo por defecto pero que puede ser reescrito):
```py
class Item:
	atributo_default = 3
	def __init__(self, nombre: str, precio: float): 
		self.nombre = nombre 
		self.precio = precio 
	def multiplicacion:
	return self precio = self.precio * Item.atributo_default
		
	
item1 = Item('Compu', 300)
item2 = Item('Compu', 300)
print(Item.atributo_default) #3
item2.atributo_default = 4
item1.multiplicacion()
item2.multiplicacion()
print(item1.precio()) #900
print(item2.precio()) #1200
```

Para iterar entre atributos usamos Class.all
```py
class Item:
	Item.all.append(self)
	
for objeto in Item.all:
print(objeto.nombre) #todos los nombres de los objetos
```

