---
dg-publish: true
---
- A es inversible si todos sus autovalores tienen mg = ma
- A es inversible si todos sus autovalores sin diferentes
- A es simetrica si a autovalores distintos corresponden autovectores ortogonales
$\det= \lambda_{1}*\dots*\lambda_{n}$
$Av_2=\lambda_2 v_2$
Si $A³-5A²$ es singular, entonces $\lambda^3-5 \lambda²=0$
$A²-3A+2I =\begin{matrix} 3\  3  \\ 3 \ 3\end{matrix}=B=q(A)$  con $q(x) =x^2-3x+2$.
Luego, si $\lambda$ autovalor de q(A), es decir, autovalor de B, se cumple que
$$\lambda=q(v)$$con v autovalor de A

Dos matrices son simetricas si $A = Q A_{2} Q^{-1}$ Y/o 
si $A_{1} = BJB^{-1}$ y $A_{2} = PJP^{-1}$ 
Luego, para buscar Q tal que $A_1 = A = Q A_{2} Q^{-1}$, $Q=B.P^{-1}$

Se dice que una matriz P es ortogonal si $P^{-1} =P^T \iff P P^T = I_n$
## Rotacion
si $det(A)=1$ es una rotacion, el eje de rotación es el generado por el vector asociado al autovalor 1. 
Para obtener el angulo planteo estas dos ecuaciones
$$\det(v_{1} \ v_{2} \ Av_{2})=sen(\alpha)$$
con $v1 \perp v2$
$$tr(A)=1+2\cos(\alpha)$$
## Simetría
Si $\det(A)=-1$ es una rotacion. 
$tr(A)=1$
Si -1 o 1 es un autovalor de la matriz, su respectivo polinomio asociado será el eje de rotacion. Luego, el subespacio sobre el que se realiza la simetria es te generaod por v2, v3. Siendo $v_{1}\perp v_2$ y $v_3=v_1 \times v_2$



Una matriz es diagonalizable si y solo si es simetrica


DVS: 
$rg(A)$= cantidad de valores singulares
$$U \Sigma V^T$$![[Pasted image 20230728161941.png]]
Pseudo inversa
$$A^{\dagger}=V \Sigma^{-1} U^t$$
Luego la solucion de norma minima por minimos cuadrados de Ax = b es $x_{minima} = A^{\dagger}b$ y luego $x=x_{min}+Nul(A)$


Si nos dicen que $\max_{||x||=1}||Ax||=25\sqrt{ 2 }$ quiere decir que $25\sqrt{ 2 }$ es el mayor valor singular de A. Si es $min_{||x||=1}$, es el minimo
