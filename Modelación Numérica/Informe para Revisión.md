---
Dia: 2025-03-14
dg-publish: true
---

Gracias por enviarme el temario del examen y las fotos correspondientes. 

De acuerdo con su sugerencia, he preparado un informe detallado en el que incluyo la resolución correcta. He comparado ambas soluciones (la de mi examen y la correcta) para poder señalar las diferencias y explicar de manera clara las similitudes entre ellas.
Adjunto las imágenes con ambas resoluciones para facilitar la comparación y poder identificar de manera precisa las áreas en las que se podría haber cometido un error en la corrección.


# punto 1

## Euler
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

![[Pasted image 20250314204003.png]]
Tal y como se puede apreciar, llego al mismo resultado. Según los valores numéricos que subió Portocarrero al campus, el resultado es correcto.
## RK2 
![[Pasted image 20250314203721.png]]
![[Pasted image 20250314204023.png]]
Al igual que en el punto anterior, ambos resultados son similares y, hasta donde llega mi memoria, concuerdan con lo publicado en el campus por el docente.
## Punto medio 
![[Pasted image 20250314203751.png]]
![[Pasted image 20250314204048.png]]
En este caso, ya sabía que no había llegado a la solución correcta. Incluso lo aclaro en el punto siguiente. Tuve un error de cálculo en la primera iteración que arrastré en las demás, pero el planteamiento del método y las iteraciones (más allá del resultado analítico) están bien desarrollados.
## Comparacion 
![[Pasted image 20250314203818.png]]
![[Pasted image 20250314204056.png]]
Analizo los resultados de las aproximaciones y aclaro que es incorrecto el cálculo del método de punto medio. Intento empezar de 0 el proceso, pero aclaro que me quedé sin tiempo. De todas formas, soy consciente y capaz de analizar los resultados, y precisamente aclaro que el método de PM no debería dar un error tan grande como Euler.
# 2A
![[Pasted image 20250314203841.png]]
![[Pasted image 20250314204114.png]]
Al igual que Euler y RK2, los resultados son similares y concordantes con los de la cátedra.

## 2b
![[Pasted image 20250314203914.png]]
![[Pasted image 20250314204129.png]]
![[Pasted image 20250314204144.png]]
El mismo análisis que en el punto anterior.
## 2c
![[Pasted image 20250314203905.png]]
![[Pasted image 20250314204202.png]]

La misma explicacion.
## Pregunta 1 
El método de bisección y el método de Newton son dos técnicas iterativas utilizadas para encontrar raíces de ecuaciones, pero presentan diferencias significativas en su comportamiento. El método de bisección es un procedimiento robusto que garantiza la convergencia si la función cambia de signo en un intervalo dado. Su convergencia es lineal, lo que implica que el número de cifras correctas aumenta lentamente con cada iteración. En contraste, el método de Newton tiene una convergencia cuadrática, lo que significa que se acerca a la raíz mucho más rápido siempre que se parta de una buena aproximación inicial. Sin embargo, el método de Newton depende de la derivada de la función y puede fallar si la derivada es cero o si la estimación inicial está demasiado lejos de la raíz. En general, el método de bisección se elige cuando no se dispone de una buena aproximación inicial o cuando la función no es diferenciable, mientras que el método de Newton es preferible cuando la función es suave y se tiene una estimación razonable de la raíz.


## Pregunta 2
El método de interpolación de Lagrange y el método de interpolación de Newton también presentan diferencias fundamentales. El método de Lagrange se basa en la construcción directa de un polinomio interpolador utilizando una combinación lineal de funciones base llamadas polinomios de Lagrange. Este método es fácil de entender y aplicar, pero si se añaden nuevos puntos, es necesario recalcular todo el polinomio desde el principio. En cambio, el método de Newton utiliza diferencias divididas para construir el polinomio de interpolación de manera más eficiente, permitiendo agregar nuevos puntos sin necesidad de recomputar todo el polinomio. Además, el método de Newton tiende a ser más estable numéricamente cuando se trabaja con un gran número de puntos, reduciendo errores de redondeo. En general, el método de Lagrange es útil cuando se trabaja con un número pequeño de puntos y no se necesita modificar la interpolación, mientras que el método de Newton es más eficiente cuando los datos se van incorporando progresivamente o cuando se necesita un mejor control numérico.


![[Pasted image 20250314203941.png]]

Explicacion menos detallada pero igualmente concordante.


# Conclusion 
Tras revisar los resultados, considero que se puede apreciar la concordancia entre ambas resoluciones. Es por esta razón que no comprendo la calificación asignada

Agradezco su tiempo y quedo a su disposición para cualquier aclaración adicional.