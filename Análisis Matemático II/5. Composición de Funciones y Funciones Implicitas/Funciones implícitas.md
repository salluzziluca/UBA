# Funciones implícitas
![[Pasted image 20211020160006.png]]
Despejamos un valor de la funcion y la reemplazamos en la funcion original, si nos da cero decimos que encontramos la funcion explicita de la ecuación

## Teorema de Cauchy – Dini
  Sea $F :D⊂R^(n+1)→R$, $n≥1$, $F(x_1,x_2,…,x_n,y)=0$ y $A=(A_n,b)$ interior a D, donde $A_n=(a_1,a_2,…,a_n)$, si se cumple que (hipótesis):
1. F(A)=0

2.  F ∈ C^1 en un entorno de A (fijarse si el gradiente es continuo (no tiene problemas) cerca del punto)

3. $F'_y(A)≠0$

entonces (tesis):

• $F(x_1,x_2,…,x_n,y)=0$ define implícitamente a $y=f(x_1,x_2,…,x_n )$ en $E(A_n )$

• $f$ es única y diferenciable en $A_n$ (aunque no se pueda despejar)

• $\LARGE f'_{(x_i)} (A_n )=- \frac {(F'_{x_i}(A)}{(F'_y(A)} ∀ i=1, 2,…, m$