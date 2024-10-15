Ventajas:
- Poca propagacion de errores de redondeo
- Muy eficientes en calculo en paralelo
![[Pasted image 20240917122631.png]]

## Jacobi 
de cada ecuacion se despeja la incognita que corresponde a la diagonal

$$x_{1}^{n+1}= \frac{{b_{1}-a_{12x_{2}}^n-a_{13}x_{3}^n }}{a_{11}}$$

Si la matriz A es estrictamente diagonal dominante -> Jacobi va a converger

![[Pasted image 20240917124414.png]]
Donde los elementos de la diagonal en **valor absoluto (modulo)** son mas grandes que la suma en valor absoluto que el resto de elementos de la misma fila


T_j es la matriz de Jacobi. ![[Pasted image 20240917182522.png]]
Si la matriz A es diagonal dominante entonces converge. Si no es diagonal dominante, no sabemos
El metodo de jacobi converge si el radio espectral (mayor autovalor) tiene que ser menor que 1 en modulo

## Gauss Seidel 

tengo al matriz A
![[Pasted image 20240917182836.png]]
Diagonal estrictamente dominante.
Despejo x^{k+1}, y^{k+1}, z^{k+1}  
![[Pasted image 20240917182935.png]]
Pero en y^{k+1} en vez de usar el x^k ya directamente uso el x^{k+1}, porque ya lo tengo
## Descomposicion en matrices L D y U
![[Pasted image 20240917130941.png]]


### Jacobi
![[Pasted image 20240917131405.png]]

### Gauss Seidel 
![[Pasted image 20240917131355.png]]

$$x^{n+1} = c + T x ^n$$

Podemos llevar tanto gauss seidel como jacobi a esa expresion 
![[Pasted image 20240917131824.png]]


## Norma Infinita de una matriz 
en vez de la [[1.6 Algebra Vectorial#Norma de un vector| norma de un vector]] que es la raiz cuadrada de la suma de los elementos del vector al cuadrado

Esta se calcula como $$\mid\mid A\mid\mid_{\infty} = max \sum^{m}_{j=1}\mid a_{ij}\mid$$
Esto seria agarrar todos los elementos de una fila y sumamos sus modulos. Con eso nos queda el vector conformado por la sumatoria de cada fila. De ese vector, nos quedamos con el mas grande.



SI A es diagonal dominante.
y si la norma infinita de la matriz T de jacobi es < 1, entonces converge
$$\mid\mid T_{J}\mid\mid_{\infty}<1$$
Con 
$$T_{J}=D^{-1}(L+U)$$



## Succesive Over Relaxation 

$$\LARGE x_{i_{\omega }}^{k+1}= \omega [x_{gs}^{k+1}-x(k)]+x^k $$ Si vengo convergiendo bien hacia el resultado, acelero ese proceso (componente a componente). Siendo $\omega$ un factor mayor 1

$$T_{\omega}= (D-L_{\omega})^{-1} [(1-\omega)D+U_{\omega}]$$1) $$\rho(T_{\omega})<2\to 0<\omega<2$$
2) Si A es simetrica definida positiva y 0<w<2 -> S.O.R converge. Existe un $\omega$ optimo entre 1 y 2