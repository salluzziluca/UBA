## Creacion de nuevos features
que no existian en nuestro set de datos y que nosotros decidimos agregar:
- Lagged features (basados en tiempo)
- Features estadisticos (mean, median, std, max, min)
- Features basados en KNN (ej promedio de 'x' para los 'k' vecinos mas cercanos)
- Features basados en texto (contains, tf-ldf, etc)

## Transformación de features existentes
- Log transformation: Transforma una funcion de tipo exponencial en una normal (la normaliza)
- $x = \sqrt{x}$, $x=\sin⁻1(x)$, $x=x^{-1}$