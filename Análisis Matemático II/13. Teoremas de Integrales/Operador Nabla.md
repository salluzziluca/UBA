---
dg-publish: true
---
# Operador Nabla
Llamaremos operador ==nabla== en R³ al "vector":
$$\LARGE\triangledown =(\frac {\partial}{\partial x }, \frac {\partial}{\partial y }, \frac {\partial}{\partial z })$$
Si aplicamos nabla a un campo escalar f obtenemos 
$$\triangledown f =(\frac {\partial f}{\partial x }, \frac {\partial f}{\partial y }, \frac {\partial f}{\partial z })=grad(f)$$
Si tomamos el producto escalar de nabla con un campo vectorial $\vec f = (P, Q, R)$ obtenemos
$$\triangledown . \vec f =(\frac {\partial}{\partial x }, \frac {\partial}{\partial y }, \frac {\partial}{\partial z }).(P, Q, R) = P'_x +Q'_y + R'_z = div(\vec f) = divergencia$$