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
$$x_{k+1}=x_{k}- \frac{f(x_{k})}{f'(x_{k})}$$

![[Pasted image 20240904121345.png]]
Usamos el x_{k+1} como nuevo x_k.
La cantidad de dijitos correctos se duplica de una iteracion a la otra


### PRoblemas con newton Rawson
Que pasa si f'(x_k)= 0? Entonces me encuentro con una division por 0 y no puedo resolver. No va a converger
![[Pasted image 20240904122004.png]]
entonces:

### Condiciones para que Newton Rapshon esté bien definida y converja a la raiz de f(x) en $[a,b]$

![[Pasted image 20240904122106.png]]


### Error, convergencia cuadrática
![[Pasted image 20240904122542.png]]


## Método de punto fijo 
El punto fijo es aquel que cuando se evalua la funcion en ese punto devuelve el mismo valor
tengo una funcion F(x) de la que quiero obtener las raices, este metodo nos permite buscar los puntos fijos de una funcion g(alpha) cuyos puntos fijos van a ser raices de F(x)

por ejemplo $g(\alpha) \alpha -f(\alpha)=\alpha -0=\alpha$
Otra forma es despejando segun la f(x) que tengamos 
![[Pasted image 20240909130859.png]]
 en estos casos g seria $\alpha³ -5$ o $3\sqrt{ \alpha+5 }$ o $\frac{5}{\alpha² -1$