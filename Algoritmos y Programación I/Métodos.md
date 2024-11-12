---
dg-publish: true
---
# Métodos
Son [[Funciones]] que se utilizan dentro de una clase, son creadas solo en ese ambito y reciben ese nombre en particular.
Dentro de los metodos tenemos los 
![[Magic Metods (Métodos Magicos)]]

y los
## Metodos normales
Iguales que las funciones, la ventaja es que se le puede pasar solo `self` como parametro y luego llamar a los diferentes atributos directamente
```py
class Item:
	def __init__(self, nombre, precio, cantidad, descuento = 0):
		self.nombre = nombre
		self.precio = precio
		self.cantidad = cantidad
		self.descuento = descuento
	def valor_total(self):
		return (self.cantidad * self.precio) 
		
item_1 = Item('Computadora, 50000, 23')
item_2 = Item('Celular', 20000, 10) 
item_1.flash = True

print(item_2.valor_total()) #1150000
print(item_1.valor_total()) #200000
```

### Especificación y validacion atributos
Podes (y debemos) aclararle al constructor que tipo de dato vamos a recibir en cada uno de los atributos, esto permite ordenar de una mejor manera nuestro código. Esto lo hacemos utilizando ` : tipo_de_dato` luego de el atributo. Ej: `precio: float`. 
- Si tenemos algun atributo designado por defecto ya esta especificado su tipo
Tambien podemos validarlos por si no queremos recibir un atributo con valor menor a cero o con alguna caracteristica indeseable. Para eso usamos `assert atributo condicion, f'mensaje de error'`

```py
class Item:
	def __init__(self, nombre: str, precio: float, cantidad: int, descuento = 0):
		assert precio >= 0, f'El precio debe ser mayor o igual que cero, ingresaste {precio}'
		assert cantidad >= 0 f'La cantidad debe ser mayor o igual que cero, ingresaste {cantidad}'
		assert descuento > 0 f'El descuento debe ser mayor que cero, ingresaste {descuento}'
		self.nombre = nombre
		self.precio = precio
		self.cantidad = cantidad
		self.descuento = descuento
	def valor_total(self):
		return (self.cantidad * self.precio) 
		
item_1 = Item('Computadora, 50000, 23')
item_2 = Item('Celular', 20000, 10) 
item_1.flash = True

print(item_2.valor_total()) #1150000
print(item_1.valor_total()) #200000
```