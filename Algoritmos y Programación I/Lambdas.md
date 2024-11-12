---
dg-publish: true
---
# Lambdas
Sirven para hacer funciones simples condensadas en una linea. Para cosas rutinarias como x == y, es_par, y asi.
```py
from math import sqrt
modulo = lambda x: sqrt(x**2)
modulo(-20) #devuelve 20.0
son_iguales = lambda x, y: x == y
son_iguales(1, 2) #devuelve false

```