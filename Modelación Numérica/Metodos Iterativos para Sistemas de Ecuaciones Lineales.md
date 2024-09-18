Ventajas:
- Poca propagacion de errores de redondeo
- Muy eficientes en calculo en paralelo
![[Pasted image 20240917122631.png]]

## Jacobi 
de cada ecuacion se despeja la incognita que corresponde a la diagonal

$$x_{1}^{n+1}= \frac{{b_{1}-a_{12x_{2}}^n-a_{13}x_{3}^n }}{a_{11}}$$

Si la matriz A es estrictamente diagonal dominante -> Jacobi va a converger

![[Pasted image 20240917124414.png]]
Donde los leementos de la diagonal en valor absoluto son mas grandes que la suma en valor absoluto que el resto de elementos de la misma fila


T_j es la matriz de Jacobi. ![[Pasted image 20240917182522.png]]

El metodo de jacobi converge si el radio espectral (mayor autovalor) tiene que ser menor que 1

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