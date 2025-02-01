---
Dia: 2025-01-17
dg-publish: true
---
## Repaso de [[8.0 Ecuaciones Diferenciales]]

Si tenemos $\frac{dy}{dx}=y^2$ buscamos encontrar la funcion que cumple que su derivada es = a y^2. Con eso ya podemos extraer informacion, ya que tenemos la pendiente 
![[Pasted image 20250117171105.png]]
Esa seria la pendiente en cadaa uno de los puntos

Entonces $\frac{dy}{dx}=f(x,y)$ por lo que $$\int^{y}_{y_{0}}dy= \int^{x}_{x_{0}}f(x,y)dx$$
finalmente ${y}-y_{0} = \int^{x}_{x_{0}}f(x,y)dx$ que es algo que justamente no  podemos resolver porque no tenemos fx,y

si $\frac{d\times}{dy}=f(x)$ realmente no nos preocupa, porque se puede integrar en x facil.

## Metodo de orden 1 
![[Método de Euler]]

## Metodos de orden 2
el orden del metodo va a ser igual a la cantidad de veces que evaluo f (hasta orden 4)
### Punto Medio 
$$y_{1}=y_{0}+hf\left( x_{0}+\frac{h}{2}, y_{0} + \frac{h}{2} f(x_{0}, y_{0}) \right)$$
### Runge - Kutta
$$y_{1}=y_{0}+\frac{1}{2}[h(f(x_{0}, y_{0}) + h\ f(x_{0}+h, y_{0}+h\ f(x_{0}, y_{0})))]$$
siendo $h(f(x_{0}, y_{0}) =q_{1}$ y $h\ f(x_{0}+h, y_{0}+h\ f(x_{0}, y_{0})))= q_{2}$

![[Metodo de Crank-Nicolson (trapecio)]]


## Metodo de orden 4
aca el q2 no la calculo al final del intervalo, sino en la mitad. 
$$y_{i+1}=y_{i} \frac{q_{1}+2q_{2}+2q_{3}+q_{4}}{6}$$
$q_{1}=hf(x_{i}, y_{i})$
$q_{2}=hf\left( x_{i}+\frac{h}{2}, y_{i}  +\frac{q_{1}}{2}\right)$
$q_{3}=hf\left( x_{i}+\frac{h}{2}, y_{i}  +\frac{q_{2}}{2}\right)$
$q_{1}=hf(x_{i}+h, y_{i}+q_{3})$


# Ecuaciones de orden >1
![[Pasted image 20250118155701.png]]![[Pasted image 20250118155712.png]]

no entendi ni sota
![https://en.wikipedia.org/wiki/Brandon_Sanderson](https://en.wikipedia.org/wiki/Brandon_Sanderson) 

