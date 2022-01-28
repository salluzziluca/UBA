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
 $$\int\int_S \vec F.\hat n\ ds= \int\int_D \hat F(\vec g(u ,v)).\vec (g'_u(u, v) \times \vec g'_v(u, v))dudv$$
 Con $\hat n = \frac {\vec F'_u(u, v) \times \vec F'_v(u, v)}{||\vec F'_u(u, v) \times \vec F'_v(u, v)||}$ y  $ds=||\vec F'_u(u, v) \times \vec F'_v(u, v)||$

 
## Teoremas
### Gauss
#### Hipotesis
- $D \subset R^3,$ sea $\partial D$ su sup frontera, la supongo orientada al exterior
- Si hay alguna funcion (supongamos h) dentro de $\vec F(\vec X)$ debe ser $h'$ continua $-> h\in C^1 -> \vec F \in C¹$
- De existir la funcion potencial de \vec f, la la matriz jacobiana D\vec f es simetrica. (ej: $\vec f=(2x, 2y)$ $potencial=\phi = x^2, y^2$

Cuando no podemos resolver el flujo de una superficie de forma "normal"  podemos intentar usando divergencia.
Esto es equivalente a decir que el flujo de $\vec f$ a traves de la superficie frontera de D (hacia afuera) es igual a la integral triple de la [[Divergencia|divergencia]] de $\vec f$ sobre D.
$$ ∯_{\partial D}\vec f . \hat n . ds = \int \int \int_D div(\vec f) dxdydz $$

$$P'_x +Q'_y + R'_z = div(\vec f) = divergencia$$

### Green 
![[Teorema de Green]]

### Stokes
![[Teorema del Stokes (Rotor)]]