#### Flujo 

 $$\int\int_S \vec F.\hat n\ ds= \int\int_D \hat F(\vec g(u ,v)).\vec (g'_u(u, v) \times \vec g'_v(u, v))dudv$$
  Con $\hat n = \frac {\vec F'_u(u, v) \times \vec F'_v(u, v)}{||\vec F'_u(u, v) \times \vec F'_v(u, v)||}$ y  $ds=||\vec F'_u(u, v) \times \vec F'_v(u, v)||$

  ##### gauss
  - Sólido compacto (cerrado y acotado)
- frontera orientada hacia afuera y cerrada
- $\vec f \in C^1$
 $$ ∯_{\partial D}\vec f . \hat n . ds = \int \int \int_D div(\vec f) dxdydz $$
$$P'_x +Q'_y + R'_z = div(\vec f) = divergencia$$

 #### circulacion
$$\int_C \vec F ds= \int_a^b \vec F (\vec g(t))\vec g'(t)dt=\int_a^b \vec F (\vec g(t)).\hat T ds $$
con $\hat T = \frac {\vec g'(t)}{||\vec g'(t)||}$

##### green
D region compacta de R^2 con $\partial D$ como frontera
$\partial D$ curva cerrada positivamente orientada
F es c1

$$\oint_{\partial D⁺} \vec f.d\vec s= \int \int_D (Q'_x(x,y)-P'_y(x,y))dxdy$$
si $(Q'_x(x,y)-P'_y(x,y))dxdy$ da cero, aplicamos

##### potencial
Si la matriz jacobiana de f en R³ es simetrica y continua entonces admite funcion potencial.
Si el dominio de f es simplemente conexo (no se corta en ningun momento el dominio)

$$\int_{C_{AB}}\vec F d \vec s = \phi(\vec B)- \phi(\vec A)$$
$\vec F = \triangledown \phi$ si $\triangledown \phi (x,y) = (\phi'_x(x, y), \phi'_y(x, y))=\vec F(x, y)$

##### stokes
- C es frontera de S
- C es orientable respecto a S
- C es curva cerrada
- S orientable 
- $\vec f \in C^1$

$$\LARGE \oint_{\Gamma^+} \vec f .d\vec s=\int \int_S rot(\vec f) .\hat n ds$$

$$\LARGE rot(\vec f) = \triangledown \times \vec f = \begin{matrix}  
{\hat i} & {\hat j} & {\hat k}\\  
{\frac{\partial}{\partial x}} & {\frac{\partial}{\partial y}} & {\frac{\partial}{\partial z}} \\
P & Q & R
\end{matrix} = $$

masa de una sup 
$$\oint_{ H} densidad.d\vec s= \int \int_D densidad.||N||dxdy$$
area de una sup
$$\oint_{ H}d\vec s= \int \int_D||N||dxdy$$