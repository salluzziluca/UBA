Se busca aproximar mediante polinomios una ecuación
Definicion de interpolacioon: El polonomio inerpolante evaluado en el punto de interpolacion vale lo mismo que la funcion en ese punto
![[Pasted image 20241008132507.png]]
Si el polinomio tiene muchos datos x_i se hace un ajusto al grado dle polinomio 

# [[3.5 Mínimos Cuadrados]]
F = funcion que queremos ajustar ([[dato]])
F^* polinomio que vamos a ajusgar 
$F^*= \sum^{m}_{j=0}c_{j}\varphi_{j}(x)$

entonces, cuadrados minimos-> $$\sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))^2$$![[Pasted image 20241008133759.png]]
$||f-f^*||^2=(f-f^*, f-f^*)= \sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))(f(x_{k})-f^*(x_{k})=\sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))^2$

Siendo $(f-f^*, f-f^*)$ el [[Produto interno]] de $f -f^*$



# Interpolacion 

## metodo de Vandermonde 

El polinomio evaluado en x_i es igual que la funcion evaluada en x_i
![[Pasted image 20241008135126.png]]el determinante de A es distinto de 0 si los x_i son distintos. Siendo A![[Pasted image 20241020200039.png]]
La idea seria interpolar sin tener que hacer un sistema de ecuaciones 


## Metodo de Lagrange 
### Grado 1
Tengo dos polinomios de grado 1. $\delta_{0} \ y \ \delta_{1}$
delta0 vale 1 en x_0 y delta1 vale 1 en x_1
![[Pasted image 20241020201312.png]]

el polinomio de grado 1 se construye tal que: 
$$p_{1}(x_{0})= f(x_{0})\delta_{0}(x_{0})+f(x_{1})\delta_{1}(x_{0})$$

si lo evaluo en $x_{0}$ (caso de arriba) se me anula la parte de x_1 (ya que $\delta_{1}(x_{0})=0$
Si lo evaluo en x1 se me anula la parte de x0 (ya que $\delta_{0}(x_{1})=0$)


$$\delta_{0}(x)=\frac{x-x_{1}}{x_{0}-x_{1}}$$
$$\delta_{1}(x)= \frac{x-x_{0}}{x_{1}-x_{0}}$$


### Grado 2
![[Pasted image 20241020202144.png]]$$p_{2}(x)= f(x_{0})\delta^2_{0}(x)+f(x_{1})\delta^2_{1}(x)+f(x_{2})\delta^2_{2}(x)$$
$$\delta^2_{0}= \frac{(x-x_{1})(x-x_{2})}{(x_{0}-x_{1})(x_{0}-x_{2})}$$
$$\delta^2_{1}= \frac{(x-x_{0})(x-x_{2})}{(x_{1}-x_{0})(x_{1}-x_{2})}$$
$$\delta^2_{1}= \frac{(x-x_{0})(x-x_{1})}{(x_{2}-x_{0})(x_{2}-x_{1})}$$

![[Pasted image 20241020202714.png]]

## metodo de interpolacion de Newton 

$\phi_{0}(x)=1, \phi_{1}(x)=(x-x_{0}), \ \phi_{2}=(x-x_{0})(x-x_{1})$

$$p_{2}(x)= c_{0}\phi_{0}(x)+c_{1}\phi_{1}(x)+c_{2}\phi_{2}(x)$$
$$p_{2}(x)= c_{0}+c_{1}(x-x_{0})+c_{2}(x-x_{0})(x-x_{1})$$

$$p_{2}(x_{0})= c_{0}=f(x_{0})$$
$$p_{2}(x_{1})= c_{0}+c_{1}(x-x_{0}) \to c_{1}= \frac {f(x_{1})-f(x_{0})}{(x_{1}-x_{0})}=\frac {f(x_{1})-c_{0}}{(x_{1}-x_{0})}$$
y asi despejo c2

Pero es mucho lio, para eso uso 

### Tabla de diferencia divididas 

![[Pasted image 20241020204133.png]]

#### Relacion entre derivadas y diferencias divididas
$$f(x_{0},x_{1},x_{2}, \dots, x_{m})= \frac{f^{m}(x)}{m!}$$

EJ: $f[x_{0}, x_{0} ]= f'$