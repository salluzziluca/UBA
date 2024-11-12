---
dg-publish: true
---
# Composición de Funciones
![[Pasted image 20211018155938.png]]

Ej: 
$$f(u,v)=u^2 v$$
$$g(x,y)=(x+2y,e^xy )$$
No podemos meter el resultado de f en g, pero si el resultado de g en f. Entonces: 
$$h=f ° g$$
$$h(x,y)=f(g(x,y))=f(x+2y,e^xy )=(x+2y)^2 e^xy$$

   
## Regla de la cadena
Sea $g :S⊂R^n→R^m$ y $f :T⊂R^m→R^p / Img⊂T$, y si $g$ es diferenciable en $A⊂S$ y f es diferenciable en $B=g(A)$, entonces: 
- $$h=f ° g$$ es diferenciable en A siendo $$h :S⊂R^n→R^p$$
- $$Dh(X)=Df(g(X)) Dg(X)$$


El gradiente en ese punto es tangente a la curva de nivel en ese punto.

si g es diferenciable y $\triangledown g(\vec x_0) != 0$. Entonces $\triangledown g(\vec x_0)$ es perpendicular a la curva de nivel de f que pasa por $x_0$

