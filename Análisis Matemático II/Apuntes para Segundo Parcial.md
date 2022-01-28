# Apuntes para Segundo Parcial
## Potencial
$\vec F = \triangledown \phi$ si $\triangledown \phi (x,y) = (\phi'_x(x, y), \phi'_y(x, y))=\vec F(x, y)$
Ej: si $\vec F(x,y)=(2x, 3y^2)-> \phi (x,y) = x^2+y^3$
$\triangledown \phi (x,y) =(2x, 3y^2)$
## Cirulacion
$$\int_C \vec F ds= \int_a^b \vec F (\vec g(t))\vec g'(t)dt=\int_a^b \vec F (\vec g(t)).\hat T ds $$
con $\LARGE \hat T = \frac {\vec g'(t)}{||\vec g'(t)||}$


Si vos le sacas un solo punto a este dominio ![[Pasted image 20220128122911.png]]
la circulacion por ambas todas las curvas con el mismo sentido de circulacion vale lo mismo, si cambia de sentido cambia de singo
![[Pasted image 20220128123039.png]]
![[Pasted image 20220128123007.png]]
Siendo que la curva rodee al punto A
Si da 0, el campo es de gradiente, si no da cero, el campo no lo es
## Flujo
sea $\vec f:H \subset R³ -> R³$ un campo vectorial continuo en $H \subset R³$ se llama integral de superficie o flujo del campo vectorial $\vec f$a traves de S
 $$\int\int_S \vec f.\hat n\ ds= \int\int_D \hat f(\vec F(u ,v)).\vec F'_u(u, v) \times \vec F'_v(u, v)dudv$$
 Con $\hat n = \frac {\vec F'_u(u, v) \times \vec F'_v(u, v)}{||\vec F'_u(u, v) \times \vec F'_v(u, v)||}$ y  $ds=||\vec F'_u(u, v) \times \vec F'_v(u, v)||$
## Teoremas


- De existir la funcion potencial de \vec f, la la matriz jacobiana D\vec f es simetrica. (ej: $\vec f=(2x, 2y)$ $potencial=\phi = x^2, y^2$