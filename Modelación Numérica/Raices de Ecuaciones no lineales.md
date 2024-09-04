Para que exista una raiz en $f(x)$:
Esta tiene que ser continua en $[a,b]$
$f(a).f(b)<0$

Para que haya unicidad
$f_{1}(x)\neq 0 \ \forall  \ x \in [a,b]$


## Metodo de Bisección 
Consite en hallar el punto medio $[a,b]$, al que llamaremos $p_1$
$$p_{1} =\frac{ a_{1}+b_{1}}{2}$$
SIendo $a_1 = a$ y $b_{1} = b$
Evaluamos f(p1) y puede pasar que $f(p_{1}).f(a_{1})=0$. En cuyo caso p_1 es la raiz
si $f(p_{1}).f(a_{1})>0$. Definimos al intervalo $[a_{2}, b_{2}]=[p_{1}, b_{1}]$
si $f(p_{1}).f(a_{1})<0$. Definimos al intervalo $[a_{2}, b_{2}]=[a_{1}, p_{1}]$
![[Pasted image 20240904113611.png]]

itero n veces, en cada iteración me voy acercando mas y mas a la raiz. Converge a esa unica raiz de f(x) entre a y b.

![[Pasted image 20240904114851.png]]

La cota de error absoluto nos la da el problema que estamos resolviendo


## Metodo de Newton-Rawson
Consiste en elegir un valor $x_{0}$, que denominaremos valor inicial, y aprocimar la funcion f(x) por los dos primeros termiinos de la serie de taylor. AKA ![[Ecuacíon de la Recta Tangente]]
Es decir, aproximo la funcion f(x) por la recta tangente que pasa por x_0, f(x_0)

luego $$0 =f'(x_{0})(x_{1}-x_{0})+f(x_{0}) $$
$$x_{1}=x_{0}-\frac{f(x_{0})}{f'(x_{0})}$$

### Sucesion de Newton-Raphson 
$$x_{k+1}=x_{k}- \frac{f(x_{k)}{f'(x_{k})}})$$