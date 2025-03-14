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
y_3 = -0.413337
$$

Para $t_3 = 0.75$:

$$
y_4 = y_3 + 0.25 \left( \cos(y_3) + \frac{1}{2} (0.75) \right)
$$

$$
y_4 = -0.61337 + 0.25 (\cos(-0.61337) + 0.375)
$$

$$
y_4 = -0.49067
$$
