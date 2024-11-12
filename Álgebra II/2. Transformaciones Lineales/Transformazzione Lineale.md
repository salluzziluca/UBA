---
dg-publish: true
---
# Definición de Transformación Lineal

> Una funcion $F : V-> W$ es una transformación lineal si cumple:
a) $F(u+v)=F(u)+F(v)$
b) $F(\lambda v)= \lambda F(v)$

## Observaciones
Sea $F:V->W$ 
1) $F(0_v)=0_w$
2) $F(\alpha_1 v_1 + \alpha_2v_2+...+\alpha_nv_n) = \alpha_1 F(v_1)+...+\alpha_n F(v_n)$
3) $V = dom(F)$, $W = codom(F)$, $Img(F) = T(V) \in W$
4) Si S es sub de $V  ->$ $F(S)$ es sub de W
5) Si U es sub de $W ->$ $F^{-1}(U)$ es sub de V
## Imagen y núcleo
$Im(F) = \{w \in W / \exists \ v \in V, F(v) = w\}$
$Nu(F)=\{v \in V / F(v) = 0_w \}$

$T^{-1}(w) = v_p + Nu(T)$
Si $T(A) = A . x$ -> $Im(T) = Col(A)$
$Nu(T) = Nul(A)$

# Matriz de Transformación Lineal

Es la [[1.6 Coordenadas#Matriz de cambio de base|Matriz de Cambio de Base]] pero aplicada a las transformaciones lineales.
Teniendo V y W espacios vectoriales tal que $dim(V) = n$ y $dim(W)=m$ 
y $T: R^n -> R^m$ transformación lineal

$B_V = \{v_1, v_2, ..., v_n\}$ y $B_W = \{w_1, w_2, ..., w_m\}$ <-><->

$$\forall x \in V \iff x =\alpha_1 v_1 + \alpha_2v_2+...+\alpha_nv_n -> [x]^B = \begin{bmatrix}
\alpha_1 \\
\alpha_2 \\
. \\
. \\
. \\
\alpha_n 
\end{bmatrix} $$

$$ T(x) = \alpha_1 T(v_1) + \alpha_2 T(v_2) + ... + \alpha_n T( v_n) \in W$$
$$[T(x)]^{B'}=\alpha_1 [T(v_1)]^{B'} + \alpha_2 [T(v_2)]^{B'} + ... + \alpha_n [T(v_n)]^{B'} \in K ^m$$

$$[T(x)]^{B'} = |[T(v_1)]^{B'}|[T(v_2)]^{B'}|...|[T(v_n)]^{B'}|\begin{bmatrix}
\alpha_1 \\
\alpha_2 \\
. \\
. \\
. \\
\alpha_n 
\end{bmatrix} = [T]^{B'codom}_{B dom} [x]^B$$

## Propiedades
T es monomorfismo si y solo si $nul([T]^{B'}_B)= \{0\}$
T es epimorfismo si y solo si $col([T]^{B'}_B)= K^m$
T es isomorfismo si y solo si $[T]^{B'}_B$ es inversible

# Cambio de Base de Matriz de Transformación Lineal

Si yo tengo 
$$[T]_B^{B'}$$ y quiero obtener su equivalente en una nueva base no tengo mas que hacer
$$[T]_B^{B'} M_C^B = [T]_C^{B'}$$
o
$$M_{B'}^C[T]_B^{B'}  = [T]_{B}^{C}$$

También podemos combinar ambos cálculos y cambiar las bases de una matriz de cambio por completo

$$M_{B'}^{C'}[T]_B^{B'} M_C^B = [T]_{C'}^{B'}$$


---

Luego, para cualquiera de estos calculos 
$$[T]_{C'}^{B'} [v]^{C'} = [T(v)]^{B'}$$

# Matriz de la Composición

Si T: V->W y  G : W->U siendo B base de V B' base de W y B'' base de U
tenemos
$$[T]_B^{B'} \ y \ [G]_{B'}^{B''}$$
tal que 
$$[G \ o \ T]_B^{B''} = [T]_B^{B'} [G]_{B'}^{B''}$$

# Simetrías y Proyecciones Según una Dirección
![[simetriaas y proyecciones.excalidraw]]

Tomo x, trazo una paralela a D, donde corta con S tengo la proyección
- $S \bigoplus D$= R² en este caso
- Todo $x : R² / x = x_s + x_p ; T(x) = x_s \{$ 
$T(x) = 0 \ si \ x \in D$
$T(x) = x \ si \ x \in S$
$\}$

- Si $S \bigoplus D = V$, la proyección sobre S en Dirección  D: $T: V->V$ donde $T(v) = v \ \forall \  v \in S$ y $T(v)=0 \ si \ v \in D$ 
- Si $S \bigoplus D = V$ -> $B_S + B_D = B_v \{$
	$T(v) = 0 \ \forall \ v \in D$ 
	$T(w) = w \ \forall \ w \in S$
	$\}$
	$Im(T)=S$
	$Nu(T)=D$

> La característica que distingue a la proyección sobre quien proyecta se ve buscando su imagen. $Im(T)= S$
> En que dirección proyecta se ve restándole su transformación $x-T(x)=D$


## Simetrías con Respecto a S Según la dirección D
- $x = x_S + x_D$
$\sum_{S\ D}(x)= x_s -x_d \{$
$\sum_{S\ D}(x)=v \ si\  v \in S$
$\sum_{S\ D}(x)=-v \  si \ v \in D$
$\}$
- Si T es una simetria o reflexion $T o T = I$
- Para saber sobre quien proyecta $x +T(x) \in S$ . Si pertenece a S, Proyecta sobre S. Si da que pertenece a D, proyecta sobre D
- Para saber en que direccion proyecta $x-T(x) \in D$. Idem que arriba.

### Comentarios
-$\sum_{S_1 \ S_2}(v) = v- 2T_{S_1 \ S_2}(v)$
$B_S = \{v_1, v_2, ..., v_k\}$ y $B_D = \{w_1, w_2, ...w_{n-k}\}$ entonces  $B= B_s \cup B_d = \{v_1, v_2, ..., v_k, w_1, w_2, ...w_{n-k} \}$ BASE DE V
![[Pasted image 20220927145634.png]]

# Tipos de Funciones
## Monomorfismo/inyectiva
- con Nu(T)$dim(V) = dim(Im(T)) \leq dim(W)$
- $dim(Nu(T))+dim(Im(T)) = dim(V)$
- Va de LI a LI
- El nucleo da cero
si x_1 != x_2 entonces F(x_1) != F(x_2). Si x_1, x_2, x_3 son base de un subespacio F(x_1), F(x_2), F(x_3) tambien lo serán

## Epimorfismo/sobreyectiva
- $dim(V) \geq dim(W)$
- $dim(Nu(T))+dim(Im(T))=dim(V)$ 
La imagen me tiene que dar todo W

## Isomorfismo/biyectiva 
Inyectiva + sobreyectiva
- dim(v)= dim(w)
- Va de LI a LI