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
## RK2 
![[Pasted image 20250314203721.png]]


## Punto medio 
![[Pasted image 20250314203751.png]]

## Comparacion 
![[Pasted image 20250314203818.png]]


# 2A
![[Pasted image 20250314203841.png]]

## 2b
![[Pasted image 20250314203914.png]]

## 2c
![[Pasted image 20250314203905.png]]
## Pregunta 1 
El método de bisección y el método de Newton son dos técnicas iterativas utilizadas para encontrar raíces de ecuaciones, pero presentan diferencias significativas en su comportamiento. El método de bisección es un procedimiento robusto que garantiza la convergencia si la función cambia de signo en un intervalo dado. Su convergencia es lineal, lo que implica que el número de cifras correctas aumenta lentamente con cada iteración. En contraste, el método de Newton tiene una convergencia cuadrática, lo que significa que se acerca a la raíz mucho más rápido siempre que se parta de una buena aproximación inicial. Sin embargo, el método de Newton depende de la derivada de la función y puede fallar si la derivada es cero o si la estimación inicial está demasiado lejos de la raíz. En general, el método de bisección se elige cuando no se dispone de una buena aproximación inicial o cuando la función no es diferenciable, mientras que el método de Newton es preferible cuando la función es suave y se tiene una estimación razonable de la raíz.


## Pregunta 2
El método de interpolación de Lagrange y el método de interpolación de Newton también presentan diferencias fundamentales. El método de Lagrange se basa en la construcción directa de un polinomio interpolador utilizando una combinación lineal de funciones base llamadas polinomios de Lagrange. Este método es fácil de entender y aplicar, pero si se añaden nuevos puntos, es necesario recalcular todo el polinomio desde el principio. En cambio, el método de Newton utiliza diferencias divididas para construir el polinomio de interpolación de manera más eficiente, permitiendo agregar nuevos puntos sin necesidad de recomputar todo el polinomio. Además, el método de Newton tiende a ser más estable numéricamente cuando se trabaja con un gran número de puntos, reduciendo errores de redondeo. En general, el método de Lagrange es útil cuando se trabaja con un número pequeño de puntos y no se necesita modificar la interpolación, mientras que el método de Newton es más eficiente cuando los datos se van incorporando progresivamente o cuando se necesita un mejor control numérico.