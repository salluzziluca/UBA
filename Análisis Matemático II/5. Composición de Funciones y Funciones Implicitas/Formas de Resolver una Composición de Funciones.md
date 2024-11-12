---
dg-publish: true
---
# Formas de Resolver una [[Composición de Funciones]]

Dada $f (u,v) = u + uv$ y $\vec g(x,y) = x^2,xy$, ambas definidas en R2 , calcule $\triangledown h(2,1)$ sabiendo
que $h =  f o \vec g$.
![[Pasted image 20211028162413.png]]
## Componiendo
$$h(x,y)=f(\vec g(x,y))$$
$$f(x^2, xy)$$
$$x^2 + x^2.xy$$
$$x^2+yx^3$$
$$\triangledown h(x,y) =2x+3yx^2, x^3$$
\triangledown h(2,1) = (16,8)

## Aplicando la [[Composición de Funciones#Regla de la cadena|Regla de la Cadena]]
$$Df(u,v)= (1+v \ \  u)$$
$$Dg(x,y)= \begin{pmatrix}  
2x & 0\\  
y & z
\end{pmatrix}$$
$$Dh(x,y)=Df(\vec g(x,y))Dg(x,y)$$
$$Dh(2,1)=Df(\vec g(2,1))Dg(2,1)$$
$$Dh(2,1)=Df(4,2)Dg(2,1)$$
$$Df(4,2)= (1+2 \ \  4)=(3 \ 4)$$
$$Dg(2,1)= \begin{pmatrix}  
4 & 0\\  
1 & 2
\end{pmatrix}$$
$$Dh(2,1)=(3 \ 4) \begin{pmatrix}  
4 & 0\\  
1 & 2
\end{pmatrix} = (16\ 8)$$


## Aplicando la [[Composición de Funciones#Regla de la cadena|Regla de la Cadena]] otra forma

![[Pasted image 20211028162356.png]]

## Regla del Arbolito
1. Planteamos que variables dependen de cuales, en este caso u depende de x y y v tambien depende de x y. 
2. Empezamos a caminar el arbol llegando a x por todos los caminos. Cada vez que nos cruzamos con una variable, derivamos su anterior por la variable actual. (en el camino 1 pasamos por f'u, luego por u'x y en el camino 2 por f'v y v'x). Cada camino se suma al anterior.
3. Hacemos lo mismo para ambas variables necesarias, en este caso x e y. 
4. Luego, evaluamos en el punto y obtenemos los valores
5. 
![[Pasted image 20211028163159.png]]
