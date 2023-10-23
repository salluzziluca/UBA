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