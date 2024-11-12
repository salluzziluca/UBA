---
dg-publish: true
---
# Magic Metods
Los magic metods son metodos con caracteristicas especiales.
El mas conocido e importante es

## `__init__` o constructor (constructor)
`__init__` se ejecuta siempre y cada vez que se crea un objeto de esa clase.

```py
class Item:
	def __init__(self):
		print('aca se ejecuta el __init__')
item_1 = Item() #aca se ejecuta el __init__
item_2 = Item() #aca se ejecuta el __init__
```

### Usos de `__init__`
Init es CLAVE para asignar atributos directo cuando creamos la instancia. 

```py
class Item:
	def __init__(self, nombre, precio, cantidad, descuento = 0):
		self.nombre = nombre
		self.precio = precio
		self.cantidad = cantidad
		self.descuento = descuento
item_1 = Item('Computadora, 50000, 23')
item_2 = Item('Celular', 20000, 10, 25) 
item_1.flash = True
print(item_2.nombre) #'Celular'
print(item_2.cantidad) #10
print(item_1.decuento) #0
print(item_2.decuento) #25
```

- Como podemos ver con `descuento` se pueden asignar atributos por default en un valor. 
- Aunque estemos asignando atributos dentro del constructor podemos seguir asignandolos por fuera (esto es si queremos asignar atributos propios de algun objeto.)

## `__repr__`
```py
class Item:
	def __init__(self, nombre, precio, cantidad, descuento = 0):
		self.nombre = nombre
		self.precio = precio
		self.cantidad = cantidad
		self.descuento = descuento
		
	def __repr__(self):
		return f'Item('{self.name}, {self.price}, {self.cantidad}, {self.descuento}') #[Item('Computadora, 50000, 23, 0'), Item('Celular', 20000, 10, 25)]
item_1 = Item('Computadora, 50000, 23')
item_2 = Item('Celular', 20000, 10, 25) 
item_1.flash = True
print(item_2.nombre) #'Celular'
print(item_2.cantidad) #10
print(item_1.decuento) #0
print(item_2.decuento) #25
```