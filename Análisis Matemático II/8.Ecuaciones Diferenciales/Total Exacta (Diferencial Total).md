---
dg-publish: true
---
# Total Exacta (Diferencial Total)
Sea z=f(x,y) diferenciable en $R: (x,y)∈[a,b] x [c,d]$, entonces, su diferencial total es $dz= f_x' dx+ f_y' dy$.
ej: 
   

$z=f(x,y)=x^2 y-3x e^y$
$dz=(2xy-3e^y) dx+(x^2-3xe^y)dy$

> Una ecuación diferencial $P(x,y) dx+Q(x,y) dy=0$ es total exacta si la expresión del primer miembro es un diferencial total.
> Se puede pensar como   $∇f(x,y)=(P(x,y), Q(x,y))$

Para chequear si una ecuacion diferencial es total exacta tenemos que comprobar las derivadas cruzadas son iguales.$P'x(x,y)$ debe dar igual que $Q'y(x,y)$ (ya que $z=(x,y)$ es $C^2$

### Obtener z teniendo P(x,y) y Q(x,y)
Primero integramos P o Q en su variable (si es P integramos en x si es Q, en y)
supongamos $P(x,y)=x^2-2xy$
Una vez terminada la integracion, en vez de definir una constante, definimos una funcion de y.
$f(x,y)=\int (x^2-2xy)dx = \frac 1 3 x^3-x^2y +\alpha(y)$
Para despejar $\alpha (y)$ derivamos en funcion de y a la funcion obtenida y la igualamos a Q(x,y). 
$f_y'(x,y)=-x^2+α'(y)=-x^2-3y+1$
Luego, obtenemos el valor de $\alpha' (y)$.
Para finalizar, integramos $\alpha' (y)$ con respecto a y reemplazamos en la f(x,y) que teniamos.
$\int (-3y+1)dy=-\frac 3 2 y^2+y+c$
$$\LARGE f(x,y)= \frac 1 3 x^3-x^2y + -\frac 3 2 y^2+y+c$$
