---
Dia: 2025-01-19
dg-publish: true
---
![[Pasted image 20250123182335.png]]
Sabemos los valores de y(x) en los extremos pero no en el interior. En el interior sabemos que $$y''=f(x, y, y')$$

El problema de PVC se resuelve siempre con un sistema de ecuaciones 

## Diferencias Finitas

parto el intervalo en n+1 partes. 
![[Pasted image 20250123183103.png]]
el N+1 es el borde que ya conozco
Entonces se resuelve con un sistema de ecuaciones de n incognitas


### PVC 1D lineales 

$$y_{0}0=p(x)y'+f(x)y+\pi(x)$$
con $a<x<b$ 
$y(a)=\alpha, \ y(b)=\beta$

$p(x), q(x), \pi(x) \in \mathbb{C}[a, b]$
$q(x)>0, \notforall \ x \in [a, b]$
Las condiciones de unicidad son entonces que p, q y r sean continuas y que q no cambie de signo


$$\frac{y(x_{i+1})-2y(x_{i})+y(x_{i-1})}{h^2}=p(x_{i})\left[ \frac{y(x_{i+1})-y(x_{i-1})}{2h} \right]+q(x_{1})y(x_{i})+r(x_{i})-\frac{h^2}{12}[2p(x_{i})y^m (\eta_{i})-y^4(\xi_{i})]$$


#### Operadores 
 ![[Pasted image 20250124154004.png]]

![[Pasted image 20250124154310.png]]
en el caso de i = 1 el primer termino se vuelve mas simple ya que -w_2+2w_1-w_0(que es alpha). Lo mismo pasa con w_N+1 que es beta