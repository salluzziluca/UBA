Se busca aproximar mediante polinomios una ecuación
Definicion de interpolacioon: El polonomio inerpolante evaluado en el punto de interpolacion vale lo mismo que la funcion en ese punto
![[Pasted image 20241008132507.png]]
Si el polinomio tiene muchos datos x_i se hace un ajusto al grado dle polinomio 

# [[3.5 Mínimos Cuadrados]]
F = funcion que queremos ajustar (dato)
F^* polinomio que vamos a ajusgar 
$F^*= \sum^{m}_{j=0}c_{j}\varphi_{j}(x)$

entonces, cuadrados minimos-> $$\sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))^2$$![[Pasted image 20241008133759.png]]
$||f-f^*||^2=(f-f^*, f-f^*)= \sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))(f(x_{k})-f^*(x_{k})=\sum^{m}_{k=0}(f(x_{k})-f^*(x_{k}))^2$

Siendo $(f-f^*, f-f^*)$ el [[Produto interno]] de $f -f^*$



# Interpolacion 

## segun vandermonde 

El polinomio evaluado en x_i es igual que la funcion evaluada en x_i
![[Pasted image 20241008135126.png]]el determinante de A es distinto de 0 si los x_i son distintos. Siendo A![[Pasted image 20241020200039.png]]
La idea seria interpolar sin tener que hacer un sistema de ecuaciones 