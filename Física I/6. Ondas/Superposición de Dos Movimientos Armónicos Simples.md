---
dg-publish: true
---
# Superposición de Dos Movimientos Armónicos Simples
tenemos los dos movimientos:
$$𝑌_1 = 𝐴_1. 𝑠𝑒𝑛 𝜔.𝑡 + 𝜑_1$$
$$𝑌_2 = 𝐴_2. 𝑠𝑒𝑛 𝜔.𝑡 + 𝜑_2$$
Su superposición se expresa como: 
$$\LARGE 𝑌_1 + 𝑌_2 = 𝐴_1. 𝑠𝑒𝑛(𝜔.𝑡 + 𝜑_1) + 𝐴_2. 𝑠𝑒𝑛 (𝜔.𝑡 + 𝜑_2)$$
Graficamente se expresa como:
![[Pasted image 20211115083428.png]]

## Casos (los dos movimientos armónicos simples tienen...)
### Igual direccion y frecuencia
![[Pasted image 20211115083625.png]]
$$𝐴 = \sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2. 𝑐𝑜𝑠(𝛿)}$$ 

### Misma 𝜑
$𝜑_1=𝜑_2$---->$𝛿 = 0$
Ambos movimientos estan en fase
$$𝐴 = \sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2. 𝑐𝑜𝑠(0)}$$
![[Pasted image 20211115084033.png]]



### Con $𝜑_1=𝜑_2 + \pi$
Si $𝜑_1=𝜑_2 + \pi$ entonces $𝛿 = \pi$
Los dos movimientos están en oposición
$$\LARGE 𝐴 = \sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2. 𝑐𝑜𝑠(\pi)}$$
por lo que $A = A_1 - A_2$


### Con $𝜑_1=𝜑_2 + \frac {\pi}{2}$
Si $𝜑_1=𝜑_2 + \frac {\pi}{2}$ entonces $𝛿 = \frac {\pi}{2}$
Los movimientos estan en cuadratura
$$\LARGE 𝐴 = \sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2. 𝑐𝑜𝑠( \frac {\pi}{2})}$$
$$\LARGE A = \sqrt {A_1^2+A_2^2}$$
y $$\LARGE 𝜑 = 𝜑_1 + 𝑎𝑟𝑐𝑡𝑔 (\frac {𝐴_2} {𝐴_1})$$

### Misma dirección y diferente frecuencia
El desplazamiento va a estar dado por $$\LARGE 𝑌_1 + 𝑌_2 = 𝐴_1. 𝑠𝑒𝑛(𝜔.𝑡 + 𝜑_1) + 𝐴_2. 𝑠𝑒𝑛 (𝜔.𝑡 + 𝜑_2)$$. Pero el angulo $(𝜔_2-𝜔_1).t$ entre los vectores rotantes no es constante. Por lo que el vector resultante OP no tiene longitud constante y no rota con frecuencia angular constante
Entonces $𝒀 = 𝒀_𝟏 + 𝒀_2$ no es un MAS.
$$\LARGE 𝐴 = \sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2. 𝑐𝑜𝑠[(𝜔_2-𝜔_1).t]+(𝜑_2-𝜑_1)}$$
La amplitud oscila entre 
$𝑐𝑜𝑠[ (𝜔2 − 𝜔1) .𝑡] + (𝜑2 − 𝜑1) = 1$ y $𝑐𝑜𝑠[(𝜔2 − 𝜔1) .𝑡] +( 𝜑2 − 𝜑1) = −1$

#### Con $𝑐𝑜𝑠[ (𝜔2 − 𝜔1) .𝑡] + (𝜑2 − 𝜑1) = 1$
$$\sqrt {𝐴_1^2 + 𝐴_2^2 + 2𝐴_1. 𝐴_2}$$
$$A_{Tmax}= A_1+A_2$$
$$[(𝜔2 − 𝜔1) .𝑡] + 𝜑2 − 𝜑1 = 2. 𝑘. \pi$$
#### Con$𝑐𝑜𝑠[ (𝜔2 − 𝜔1) .𝑡] + (𝜑2 − 𝜑1) = -1$

$$\sqrt {𝐴_1^2 + 𝐴_2^2 - 2𝐴_1. 𝐴_2}$$
$$A_{Tmax}= A_1-A_2$$
$$[(𝜔2 − 𝜔1) .𝑡] + 𝜑2 − 𝜑1 = (2. 𝑘+1). \pi$$

Se dice entonces que ==la amplitud es modulada== 
![[Pasted image 20211115090935.png]]

### Misma amplitud y frecuencias muy parecidas pero no iguales
$$\LARGE 𝑌_1 + 𝑌_2 = 𝐴.[𝑠𝑒𝑛 (𝜔_1.𝑡 + 𝜑_1) + 𝑠𝑒𝑛 (𝜔_2.𝑡 + 𝜑_2)]$$
Frecuencia de vibracion = $\LARGE \frac {\omega_1 + \omega_1}{2}$
Amplitud de vibracion = 
$$\LARGE A_T = 2.A.cos[(\frac {\omega_1 - \omega_1}{2})]$$
Siendo $\LARGE \frac {\omega_1 - \omega_1}{2}$ la frecuencia de modulacion de la amplitud.
Finalmente, el MAS nos quedaria tal que:
$$\LARGE 𝑌_𝑇 = 𝐴_𝑇. 𝑠𝑒n[(\frac {\omega_1 + \omega_1}{2})t]$$
