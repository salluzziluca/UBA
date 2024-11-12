---
dg-publish: true
---
Ser $V-R$ un espacio vectorial, un Producto Interno (PI) es una funcion del tipo $< \  , \ > : V \times V -> R$ si cumple:
1) $<u,v> = <v,u>$
2) $<\alpha u+ \beta v, w> = \alpha <u,w> +  \beta <v,w>$
3) $<u,v> \geq 0$ y $<u, u> = 0 \iff u = 0_v$ 

## Generalización para Complejos
Sea $V-C$ un espacio vectorial, un Producto Interno (PI) es una funcion del tipo $< \  , \ > : V \times V ->C$ si cumple:
1) $<u,v> = \overline{<v,u>}$ (conjugado)
2) $<\alpha u+ \beta v, w> = \alpha <u,w> +  \beta <v,w>$
3) $<u,v> \geq 0$ y $<u, u> = 0 \iff u = 0_v$ 

# Observaciones y caracteristicas
- $<0_v, u>= 0$
- $<u, \alpha v + \beta w>= \bar \alpha <u,v> + \bar \beta <u, w> 0$
- El producto escalar es un subconjunto del Producto Interno en $R^n$
- $u \perp v \iff <u, v> = 0$ 
- $||u|| = \sqrt{<u,v>}$
- distancia de u a v$=d(u,v)=||u-v|| = ||v-u|| = \sqrt{u-v, u-v}$
---
Sea B base de V todo P.I. queda definido
$<x, y> = ([x]^B)^t \ Gb \ \bar {[y]}^B$ ; $GB \in K^{n \times n}$  
Donde G_B:
 - En R: Simetrica definida positiva ($A^t =A$)
 - En C: Hermítica definida positiva ($\bar A^t =A$) Hermítica
 Para chequear que sea Hermítica
 > Cualquier matriz hermítica y definida positiva define un producto interno
 ![[Pasted image 20221024192437.png]]

## V espacio vectorial con PI
### Propiedades
### Cauchy-Bunyakovsky-Schwarz Inequality
$|<x, y>| \le ||x|| \ ||y||$
#### Si x,y son Linealmente Dependientes→ $|<x, y>| = ||x|| \ ||y||$
$\exists k/y = kx$ para $<x, y> =$ $<x, kx>$ = $\bar k <x,x>$  → $|<x,y>|$ = $|\bar k| \ |<x, x>|$ = $|k| \ |x|^2$ = $||x|| \ |k| \ ||x||$ 
#### Si x e y son  [[1.4 Independencia Lineal|linealmente independientes]] 
$0<||x+ky||$
$0<||x+ky||^2 = <x+ky, x+ky> = <x, x +ky> +k < y, x+ ky>$  aca pasan cosas y llegamos a 
$||x+ky||^2 > 0$; $\forall k \in R$  

$|<x, y>| < ||x|| \ ||y||$ 
#### Desigualdad triangular
$||x+y|| \leq ||x||+||y||$
Si $u \perp w$ $(v, w \neq 0)$ ->||v+w||² = ||v||² + ||w||²
$$cos(\theta) = \frac {<u,v>}{||u|| \ ||v||}$$
$$\alpha(u,v) = \theta$$
para theta entre 0 y pi



# Ortogonalidad
> Se dice que {v1, ..., vk} es ==ortogonal== si $<v_i, v_j> = 0$ $\forall i \neq j$  
> Es ortonormal si es ortogonal y norma 1 $<v_i, v_j> = 1$ $\forall i = j$


## Propiedades
- Si un conjunto es ortogonal y no contiene al 0_v es [[1.4 Independencia Lineal|linealmente independiente]]

## Complemento ortogonal
Si $S \subseteq V$, (V como PI), $S \neq 0$
Se llama Complemento Ortogonal de S al conjunto $S^{\perp} = \{v \in V / v \perp s, s \in S \}$ $S^{\perp}$= $\{ v \in V / <v, s> = 0 \}$


### Observaciones
1) $S^{\perp}$ es sub de V para $<0_v, v>=0-><0_v, s>= 0$ , $\forall s \in S -> 0_v \in S^{\perp}$, Por propiedad de PI: $v_1>v_2 \in S^{\perp} -> v_1 +v_2 \in S^{\perp}$. $\lambda v_1, si \ v_1 \in S^{\perp} -> \lambda v_1 \in S^{\perp}$ 
2) Si S=V $S^{\perp} = \{0_v\}$, Si $S^{\perp} = {0_v} = S^{\perp} = V$
3) SI $S = gen \{v1, ..., vk\}-> S^{\perp}$ = $$\{x\in V / \begin{bmatrix}
<x, v_1> = 0 \\
. \\
. \\
. \\
<x, v_1¿k> = 0
\end{bmatrix}\}$$
4) En R^n con el PI Canónico (PIC): SI $A \in R^{m \times n}$ $Nul(A)= [Fil(A)]^\perp$ . $$Nul(A): X/Ax = 0_{R^m} \iff \begin{bmatrix}
F_1\\
. \\
. \\
. \\
F_m
\end{bmatrix} x = \begin{bmatrix}
0 \\
. \\
. \\
. \\
0
\end{bmatrix}$$

ENTONCES: $$x \in Nul(A) \iff \begin{bmatrix}
v_1^{\perp}.x = 0 \\
v_2^{\perp}.x = 0  \\
. \\
. \\
v_n^{\perp}.x = 0 
\end{bmatrix} -> x \perp a \ cada \ fila \ de \ A$$
ENTONCESSSS $$Nul(A) = [Fil(A)]^{\perp}$$
Si s es subespacio $S \cap S^{\perp}  = \{ 0_v\}$

# Proyección Ortogonal
1) $proy_S^X = x' \in S$
2) $x-x' \in S^{\perp}$
## Observaciones
1) Si existe la proyección, es única
2) $S x' = proy_S^X  \iff d(x, x') \leq d(x, s) \forall s \in S$  y $d²(x,x') \leq d²(x, s)$ La igualdad solo se cumple si s = x'
3) $x-proy_s^x= proy_{s^{\perp}}^x$  
4) $x = proy_s^x + proy_{s^{\perp}}^x$ -> $S \bigoplus S^{\perp} = V$ ($proy_s^x \in S, \  proy_{s^{\perp}}^x \in S^{\perp}$)
5) $Proy_S^x$ es [[Transformaciones Lineales|transformacion lineal]] 
	1) $Proy_s(x+y) = proy_s^x + proy_s^y$
	2) $proy_s^{(\lambda x)} = \lambda proy_s^x$
	3) $Im P_s = S$
	4) $Nul(P_S) = S^{\perp}$
	5) $Proy_s^v = v \iff v \in S$
	6) $Proy_s^v = v \iff v \in S$
	7) $Proy_s^w =0_v \iff w \in S^{\perp}$

## Formula para encontrar proyeccion
$$Proy_s^x= \frac {<x, v_1>}{||v_1||^2}v_1+\frac {<x, v_2>}{||v_2||^2}v_2+...+\frac {<x, vk>}{||v_k||^2}v_k = \alpha_1 v_1 + \alpha_2 v_2+...+\alpha_k v_k$$
## Distancia de un punto a un conjunto
$d(x, S)$ siendo x punto y S conjunto  = $min \{d(x,s) s \in S\}$
Si S es subespacio, entonces:
$d(x,S)= min d(x,s) = d(x, proy_s^x)= ||x-proy_s^x|| = ||proy_{s^{\perp}}^x||$

## Matriz de proyección ortogonal con respecto a la base canónica
SOLO CUANDO ES PIC
(cuando  $S \subseteq R^n$)
Si Base ortogonal de S = $B_s = \{u_1, u_2, ..., u_k\}$ 
$$proy_s^x = [u1, u2, ..., uk] \begin{bmatrix}
u_1 \\
. \\
. \\
. \\
u_k
\end{bmatrix} x= Q.Q^t.x$$
Esa es la matriz de la proyección ortogonal sobre la base canónica


### Teorema de Gram-Schmidt
B = $\{v_1, v_2, ..., v_k\}$  
$B_{\perp}$ = $\{u_1, u_2, ..., u_k\}$  base ortogonal.
u_k = v_k - $\frac {<x, v_1>}{||v_1||^2}v_1+\frac {<x, v_2>}{||v_2||^2}v_2+...+\frac {<x, vk>}{||v_k||^2}v_k$  

# Mínimos Cuadrados
$$\bar A^t A \hat x = \bar A^t b$$
$\hat x = \hat x_p + x_n / x_n \in Nul(\bar A^t A) = nul(A)$ Siendo $\hat x_p$ y  $x_n$ ortogonales
Como $fil(A)=[nul(A)]^{\perp}$; $fil(A)\bigoplus nul(A) = R^n$ 
$A\hat x_f = proy_{col(A)}^b$ 
$\forall \hat x / A \hat x > proy_{col(A)}^b$
$||\hat x|| \leq ||\hat x_f||$
$\hat x_f \in fil(A)$
$A \hat x_f = proy_{col(A)}^b$
Si $\hat x =\hat x_p + x_n \in fil(A) \iff (\hat x_p +x_n) \perp nul(A)$. Asi encuentro la solución de mínimos cuadrados de norma mínima.  
## Observaciones
1) El problema de mínimos cuadrados siempre tiene solución
2) $Nul(\bar A^t .A)= Nul(A)$ $\forall A \in K^{mxn}$.$Nul(A) \subset Nul(\bar A^t A)$. $Nul(\bar A^t A) \in Nul(A)$. $Nul(\bar A^t A) = Nul(A)$
3) Si $rg(A) = Rg(\bar A^t A)$
Entonces $\bar A^t A \hat x = \bar A^t b$ tiene solución única $\iff rg(A)= m$ (rango col max) $\hat x = (\bar A^t A)^{-1} . \bar A^t b$
Si Rg(A)=n pseudo inversa de A = A^{#} $= (A^{⁻t}A)^{-1} \bar A^t$ 
