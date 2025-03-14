---
Dia: 2025-03-14
dg-publish: true
---
![[Pasted image 20250314185748.png]]


Resolucion correcta:

dado $\frac{dy}{dt} = \cos(y) + \frac{1}{2} t, \quad y(0) = -1$ con $t_{0}=1$ y $t_f=1$ si se aplica 4 veces entonces h = 0.25

$$y_{n+1} = y_n + h \left( \cos(y_n) + \frac{1}{2} t_n \right)$$
$$
y_{n+1} = y_n + h \left( \cos(y_n) + \frac{1}{2} t_n \right)
$$

Para $t_0 = 0$, se tiene:

$$
y_1 = y_0 + 0.25 \left( \cos(-1) + \frac{1}{2} (0) \right)
$$

$$
y_1 = -1 + 0.25 (\cos(-1))
$$

$$
y_1 = -0.864992
$$

Para $t_1 = 0.25$:

$$
y_2 = y_1 + 0.25 \left( \cos(y_1) + \frac{1}{2} (0.25) \right)
$$


$$
y_2 = -0.671580
$$

Para $t_2 = 0.5$:

$$
y_3 = -0.41337
$$

Para $t_3 = 0.75$:


$$
y_4 = -0.090677
$$


## Pregunta 1 
Los métodos de **bisección** y **Newton** se utilizan para encontrar raíces de ecuaciones, pero tienen diferencias fundamentales en su comportamiento iterativo.
- **Bisección:** Converge linealmente, lo que significa que la cantidad de cifras correctas aumenta lentamente con cada iteración.
- **Newton:** Converge cuadráticamente cuando la raíz es simple, lo que implica que el error se reduce rápidamente en cada iteración.
Esto es debido a que el método de Newton usa derivadas para aproximar la raíz mediante tangentes, mientras que el método de bisección solo divide el intervalo en mitades sin usar información de la pendiente.

## Pregunto 2 
Ambos métodos sirven para la interpolación de funciones, pero tienen diferencias clave:
Lagrange: Se construye directamente el polinomio de interpolación sin necesidad de cálculos previos de diferencias divididas.
Newton: Se basa en diferencias divididas y permite agregar nuevos puntos sin recalcular todo el polinomio.
El método de Newton permite reutilizar cálculos previos, mientras que Lagrange requiere recalcular todo desde cero si se agrega un punto.
Lagrange: Más intuitivo, pero computacionalmente más costoso y propenso a errores numéricos cuando hay muchos puntos.
Newton: Más eficiente y mejor condicionado para grandes conjuntos de datos.
El método de Newton minimiza los errores de redondeo y evita recalcular todo el polinomio al añadir datos.