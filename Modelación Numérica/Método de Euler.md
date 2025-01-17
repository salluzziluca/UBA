---
dg-publish: true
---
Se utilizan [[8.0 Ecuaciones Diferenciales|ecuaciones diferenciales]]
$$x_{n}=x_{0}+nh $$
Error_{global} = 


## Explicito
$$y_{i+1}=y_{i}+hf(x_{i}, y_{i})$$

### Ejemplo 
![[Pasted image 20250117183059.png]]
### Estabilidad del metodo de euler: analisis de la propagacion de una perturbacion.

![[Pasted image 20250117181939.png]]

La perturbacion va a "explotar" cuando $\frac{df}{dy}<0$. ya que deja de variar la solucion y hay que evitar el crecimiento de la perturbacion. EN el caso de $\frac{df}{dy}>0$ crecen tanto la perturbacion como la solucion

## Implicito 
$$y_{i+1}=y_{i}+hf(x_{i+h}, y_{i+1})$$

La diferencia es que en este caso se plantea que no se conoce cuando va a ser el final del intervalo. Es Implicito porque nos pide lo que neceista. Nos pide y_i+1 para calcular y_i+1

En el caso de que sea lineal no es tanto lio, como se puede ver en el siguiente ejemplo 

![[Pasted image 20250117183924.png]]
![[Pasted image 20241022114025.png]]

