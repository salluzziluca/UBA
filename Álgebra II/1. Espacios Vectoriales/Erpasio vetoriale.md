---
dg-publish: true
---
# Definicion de Espacio Vectorial
Un espacio vectorial debe cumplir 8 condiciones. 4 relacionadas con la suma y 4 relacionadas con el producto
s1: Conmutativad. $u+v = v+u$ $∀u, v ∈ V$
s2: Asociatividad. $u + (v + w) = (u + v) + w, ∀u, v, w ∈ V$
s3: Existe el elemento neutro $0_V ∈ V$ , tal que $u + 0V = u, \forall u ∈ V$ 
s4: Para cada $u ∈ V$ existe un opuesto, denotado $-u$ tal que $u + (−u) = 0_V$

p1: $k(u+v) = ku +kv$
p2: $(k+h)u = ku+kh$
p3: $(kh)u = k(uh)$
p4: $1.u= u$

# Subespacios vectoriales
Los subespacios vectoriales deben cumplir las condiciones enunciadas en [[1.1 Definición de Espacio Vectorial]] y, adicionalmente, tres más
Sea S un subespacio de un espacio vectorial V

1. S no es vacio / $0_v \in S$
2. Si u y v pertenecen a S entonces u+v pertenece a S
3. $u \in S$ y $\lambda \in R$: $u* \lambda \in S$ 
# Generadores
 $$S = gen\{v1,v2,...,vk\}$$
 El subespacio S está generado por los vectores $v1,v2,...,vk$. Estos son a su vez los generadores de S.
Ej: Si el subespacio es $S = X \in R³ : x_1 +2x_2+3x_3$ 
Primero despejamos lo máximo posible y obtenemos $x_1 = -2x_2-3x_3$. Asi obtenemos que podemos definir el subespacio como $(-2x_2-3x_3, x_2, x_3)$. Luego, desacoplamos y obtenemos 
$x_2 * (-2, 1, 0)$ y $x_3(-3, 0, 1)$. Finalmente, nuestro generador seria $$gen\{(-2, 1, 0)^T, (-3, 0, 1)^T\}$$

# Independencia Lineal
Un conjunto $\{v1, v2, ...,v_n\}$ es linealmente independiente si ningún vector se escribe como combinación lineal del otro. 

## Formas de comprobar (in)dependencia lineal
### Forma default
$$\alpha_1 v_1 + \alpha_2v_2+...+\alpha_nv_n = 0_v$$ Si al igualar el sistema a cero da que $\alpha$ tiene una solución única, el sistema es LI.

### Triangulación
Teniendo los vectores armo la matriz con cadavector como fila. Si soy capaz triangularla, es LI. Tambien es LI si det(A)!=0
### Wronskiano (solo para polinomios)
- Igualo una combinación lineal al cero del conjunto vectorial
- Derivo esa igualación hasta que me quede una matriz cuadrada. 
- De esa matriz busco el determinante
- Si el $det \neq 0$ para un $x$ particular, los polinomios son LI. 
Ej: 
Es $\{1,sen(x), cos(x)\}$ LI? 
$$	W= \begin{bmatrix}1 & sen(x) & cos(x)\\ 0 & cos(x) & -sen(x)\\ 0 & -sen(x) & -cos(x) \end{bmatrix}$$

# Bases
Un conjunto $B = \{v_1, v_2, ..., v_n\}$ es base de V si cumple con: 
1. B [[1.3 Generadores|genera]] V. Es decir que $V = gen\{v_1, v_2, ..., v_n\}$
2. B es [[1.4 Independencia Lineal|linealmente independiente]]  
Adicionalmente, n es la dimension de V. ($dim(V)=n$)

# Coordenadas
Existe $B= \{v_1, v_2, ..., v_n\}$ [[1.4 Independencia Lineal|linealmente independiente]], por [[1.5 Bases|definición]]. Entonces en $V = \alpha_1 v_1 + \alpha_2v_2+...+\alpha_nv_n$ los escalares son únicos. Se llama coordenadas de x respecto a B a la n-upla $$ \begin{bmatrix}
\alpha_1 \\
\alpha_2 \\
. \\
. \\
. \\
\alpha_n 
\end{bmatrix} = X=\alpha_1 v1+\alpha_2 v_2 + ...+ \alpha_n v_n = [x]^B  $$  
## Observaciones
si $\alpha_1 v_1 + \alpha_2 v_2+...+\alpha_n v_n =0_v\iff \alpha_1 +\alpha_2 + ...+ \alpha_n$ = 0. Luego $\{v_1, v_2, ..., v_n\}$ son LI
$[u+v]^B = [u]^B+[v]^B$ 
$[ku]^B= k[u]^B$ 
$\{v_1, v_2, ..., v_n\}$ es LI $\Leftrightarrow \{[v_1]^B , [v_2]^B + [v_n]^B\}$ es LI

## Matriz de cambio de base
Si tengo una coordenada en base B ($[x]^B$). Mediante una matriz de cambio de base puedo obtener las coordenadas equivalentes en una nueva base.
$M_B^{B'}[x]^B = [x]^{B'}$ 
entonces si $B= \{v_1, v_2, ..., v_m\}$ y $B'= \{w_1, w_2, ..., w_n\}$.
la matriz la formaremos tal que: 
$v_1 = \alpha_1 w_1+ \alpha_2 w_2+ ... + \alpha_n w_n$
$v_2 = \alpha_1 w_1+ \alpha_2 w_2+ ... + \alpha_n w_n$
.
.
.
$v_m = \alpha_1 w_1+ \alpha_2 w_2+ ... + \alpha_n w_n$


# Subespacios Fundamentales de una Matriz
Siendo A una matriz de m x n 
$$col(A) = gen\{col_1(A), col_2(A), ..., col_n(A)\}$$
$$fil(A) = gen\{fil_1(A), fil_2(A), ..., fil_m(A)\}$$
$$ nul(A) = \{x \in K^n / A.x=O_{k^n}\}$$
$$ nul(A^T) = \{x \in K^m / A^T.x=O_{k^m}\}$$

## Observaciones 
$$fil(A^T)= col(A)$$
$$col(A^T)= fil(A)$$
$rango = rng(A) = dim(col(A)) = dim(fil(A))$ 
- Tener en cuenta que col y fil no son "las filas" o "las columnas", son subespacios generados por ellas

$$rg(A) + dim(nul(A) = n = cant \ de \ columnas = dim(col(A)) + dim(nul(A)$$

$$ Ax = b \ es \ compatible \Leftrightarrow b \in col(A)$$
$$SCD \ si \ rg(A) = n $$
$$SCI \ si \ rg(A) < n$$

# Operaciones Entre [[1.2 Subespacios Vectoriales|Subespacios]]
Sean A y B dos subespacios de V
![[Pasted image 20220906123002.png]]
$$A \cap B$$ es un subespacio vectorial ya que cumple con las  3 condiciones enunciadas en [[1.2 Subespacios Vectoriales]]: 
1.  $A \cap B$ no es vacio / $0_v \in S$
2. Si u y v pertenecen a $A \cap B$ entonces u+v pertenece a $A \cap B$ 
3. $u \in A \cap B$ y $\lambda \in R$: $u* \lambda \in A \cap B$

Para buscar la interseccion entre dos subespacios planteamos
A = gen\{[v1, v2, v3]^t\}
$$A = gen\{[v1, v2, v3]^t\}$$
$$B = gen\{[w1, w2, w3]^t\}$$
$$\alpha [v1, v2, v3]^t = \beta [w1,w2, w3]^t$$
$$A \cup B$$ No es un subespacio vectorial, ya que no cumple la regla de la suma
> Aunque $u$ y $v$ pertenezcan a $A \cup B$  $u+v$ no pertenece $A \cup B$

Puesto a que puede tratarse de un elemento que pertenezca solo a uno de los conjuntos y no necesariamente a ambos.

Para poder tener una forma de abarcar ambos subespacios A y B, planteamos el subespacio A + B. El cual deberá contenerlos a ambos. 
### Caracteristicas de A + B
- Este subespacio deberá de ser minimal y debera incluir a $A \cup B$  
- Si $A = gen\{v_1, v_2, ..., v_n\}$ y $B = gen\{w_1, w_2,...,w_m\}$ $A+ B = gen\{v_1, ..., v_n, w_1, ..., w_m\}$ 

## Teorema de la dimensión 
$$dim(A) + dim(B) - dim(A \cup B) = dim(A + B)$$
### Suma directa
Si una suma es directa, $dim(A \cup B) = 0$, por lo que $dim(A) + dim(B) = dim(A + B)$ 