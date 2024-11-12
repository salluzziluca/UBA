---
dg-publish: true
---
Gradiente = $∇f(x,y)=(f'_x (x,y),f'_y (x,y))$
Derivada direccional --> Gradiente por Versor
Polinomio de taylor de primer grado = plano tangente = $f(x_0, y_0)+f'x(x_0, y_0)(x-x_0)+f'y(x_0, y_0)(y-y_0)$
maxima derivada direccional = norma del gradiente
$$h=f ° g$$
$$h(x,y)=f(g(x,y))=f(x+2y,e^xy )=(x+2y)^2 e^xy$$
- ==$$Dh(X)=Df(g(X)) Dg(X)$$==
- El gradiente en el punto es perpendicular a la linea/curva de nivel
- Vector normal a una superficie parametrizada = F'u x F'v



##### Extremos
Si el gradiente de la funcion en un punto da (0,0). Ese punto evaluado es punto crítico
Si f no es diferenciable en en el punto
![[Pasted image 20211104100703.png]]

Si nos dan una funcion f(x,y) y nos piden los extremos tenemos que buscar las derivadas parciales y ver el punto en el que ambas se igualen a 0. Despejamos de una y reemplazamos en la otra hasta encontrar esos valores de x,y. Ahi va a haber puntos criticos
![[Pasted image 20211104101648.png]]


Para hayar los extremos absolutos de un conjunto compacto buscamos los valores para los que se anule el gradiente y luego parametrizamos  el borde del conjunto. Reemplazando f(x, y) por f(x(t), y(t)). Una vez resuelta esta ecuacion, evaluamos su gradiente a 0 para saber cuales puntos no pueden dar puntos criticos y ( de ser necesario, lo reemplazamos en la funcion parametrizada). Ver [Ejercicio 4 - Definitivo - YouTube](https://www.youtube.com/watch?v=rmAfdBE76-0&ab_channel=MartinMaulhardt)



Plano normal a cruva interseccion de 2 superficies:
Encontramos la curva parametrizando las superficies, luego buscamos el t que nos de el punto pedido y la derivada de la curva , evaluamos la derivada en el punto (nos da el vector director del plano normal). Armamos la ecuacion tal que: $(x−x_0,y−y_0,z−z_0)⋅σ'(t_0)=0$ y al multiplicar nos da la respuesta
![[Pasted image 20211105134604.png]]


##### interesección recta plano
1. Llevamos la recta a una ecuacion parametrica de un solo valor, ej: t
2. Luego la igualamos a un punto (t,0,0) si buscamos con el plano x, (0,t,0) is buscamos interseccion con Y y (0,0,t) si buscamps cpn Z