# Teorema de Green
Sea D una region plana con frontera $\partial D$ y $\vec f(x, y)=(P(x,y),Q(x,y))$ un campo vectorial
1. sI $D \subset R^2$ se puede subdividir en una cantidad finita de regiones de tipo 3
2. $\partial D$ es una curva cerrada, suave a trozos y simple ==positivamente orientada== (La orientacion de una curva se puede [[Orientacion de una Curva|calcular]])
3. $\vec f \in C^1$ en  $D\cup \partial D$ o en un abierto que los incluye
$$\oint_{\partial D⁺} \vec f.d\vec s= \int \int_D (Q'_x(x,y)-P'_y(x,y))dxdy$$

## Aplicación del teorema de Green al cálculo de áreas 
tomando:
una $\vec f(x, y)$ tal que $Q'x(x,y)+P'y(x,y)=k$, 
$$Area(D)=\frac 1 k \oint_{\partial D⁺} \vec f . d\vec s$$
Y, finalmente, $\vec f(x,y)=(0,x)$ 
nos queda que 
$$Área(D)=\oint_{\partial D^+} \vec f . d\vec s$$
==SOLAMENTE CON $\vec f(x,y)$ CUYOS $Q'x(x,y)+P'y(x,y)=k$ DEN CONSTANTE==