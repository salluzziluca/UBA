## Creacion de nuevos features
que no existian en nuestro set de datos y que nosotros decidimos agregar:
- Lagged features (basados en tiempo)
- Features estadisticos (mean, median, std, max, min)
- Features basados en KNN (ej promedio de 'x' para los 'k' vecinos mas cercanos)
- Features basados en texto (contains, tf-ldf, etc)

## Transformación de features existentes
- Log transformation: Transforma una funcion de tipo exponencial en una normal (la normaliza)
- $x = \sqrt{x}$, $x=\sin⁻1(x)$, $x=x^{-1}$
- Normalizar (restando su promedio)
- Normalizar y estandarizar (restar promedio, dividir por std)
- Normalizar por rango 
- Binning: podemos crear bins en los que repartimos nuestra variable numerica para transformarla en categoricas ![[Pasted image 20231023101543.png]]
#### Encoding de variables categóricas
##### One Hot Encoding
Tenemos que codificar variables categóricas
![[Pasted image 20231023101943.png]]
Tenemos tantas columnas binarias como posibles valores tenia mi variable categórica original

##### Binary encoding
en vez de una columna por valor, voy a tener $\log_{2}(cantidad \ de \ valores \ posibles \ de \ la \ variable)$
![[Pasted image 20231023102812.png]]

##### Mean encoding
- Codificar las variables categoricas en base a los labels. Se filtra info de los lables, lo cual puede llegar a traer problemas de overfitting, ya que el modelo podria intentar adivinar por el mean el label. ![[Pasted image 20231023103834.png]]![[Pasted image 20231023103840.png]]
Una forma de no usar el label del registro en si es hacen un ==Cross Validation mean encoding==. En este caso, no tomo el label del registro actual, sino que lo calculo en base a todos los Moscu menos sobre la que estamos parados.
![[Pasted image 20231023104240.png]]

###### Smoothing
$$\frac{mean(target)*nrows+globalmean*\alpha}{nrows+\alpha}$$
donde alpha controla la cantidad de regularizacion a usar