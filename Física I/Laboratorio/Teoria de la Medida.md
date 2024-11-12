---
dg-publish: true
---
#Física_I 
# Teoría de la Medida
Factores a la hora de medir: Objeto, instrumento, unidad o patron de comparacion, medio y operador.

Una medición se expresa como "$<x>+\pm \triangle x$". Siendo $<x>$ el valor representativo de la magnitud y $\triangle x$ la incerteza absoluta de la magnitud.

### Clasificación de las mediciones
**Medición directa**: Lectura de un instrumento aplicado a medir cientra cantidad de magnitud (ej: regla)
**Medición indirecta**: Resulta de vincular mediciones directas a través de relaciones matemátocas. (ej: calculo de densidad con masa y volumen).

### Clasificación de incertezas:
**Sistemáticas**: Provenientes de una imperfeccion o un ajuste inadecuado del instrumento de medicio, de la accion de una causa externa, etc. Afectan a todas las mediciones por igual. (ej: desgualdad en los brazos de una balanza)
**Accidentales o casuales**: Si se mide muchas veces lo mismo, ciertas diferencias pueden provenir del error de apreciacion o de pequeañas variaciones en condiciones ambientales (T°, p, etc.), cambios en el observador y en el instrumento.

### Valor representativo de incertezas
Cuando se mide una variable solo se pueden determinar una franja de posible valores, hay probabilidad de que lo que mida esa variable esté dentro de ese rango

### Mediciones comparables
Aquellas cuyas bandas de incertezas tiene una franja en común.
![[Pasted image 20210914115344.png]]

### Cifras Significativas: 
El número de cifras significativas de la medición es igual al número de dígitos contenidos en
el resultado de la medición que están a la izquierda del primer dígito afectado por el error,
incluyendo este dígito.
1) Todos los dígitos distintos de cero son cifras significativas.
Ejemplo: 2,76 g tiene 3 cifras significativas.
2) Los ceros que están entre dos dígitos distintos de cero son cifras significativas.
Ejemplos: 2,078 g tiene 4 cifras significativas
400,47 g tiene 5 cifras significativas.
3) Los ceros situados a la derecha de la coma y después de un dígito distinto de cero son
cifras significativas.
Ejemplo: 0.700 g. tiene 3 cifras significativas.
4) Los ceros situados a la izquierda de la primera cifra distinta de cero, no son cifras
significativas, sólo indican la posición del punto decimal.
Ejemplos: 0,006 m tiene una cifra significativa
0,02028 g tiene 4 cifras significativas.
5) Para numeros enteros: Si se escribe $3 x 10^2$ significa que tiene una cifra significativa; $3,0 x 10^2$ dos cifras significativas y $3,00 x 10^2$, tres cifras significativas. (Ej: Si se dice que la distancia de la tierra al sol es $199600000 km$ esto significaría
que se conoce este dato con una incertidumbre 1 km. Sin embargo supóngase que realmente el dato se conoce es con una incertidumbre de $10000 km$; esto obliga a escribir esta distancia como $19.960x10^24 km$.)

### Precisión y exactitud
**Precision**: Sensibilidad o minima variacion de la magnitud que se puede detectar con dicho instrumento o método. (ej: un cronometro es mas preciso que un reloj común.)
**Exactiud**: Calidad de calibracion del mismo. Si un cronometro se adelanta 2 minutos por hora mientras que un reloj de pared solo 30 segundos, el reloj es mas exacto, pero menos preciso.
Precisión da la calidad de la lectura en el instrumento, la exactitud compara a la lectura con un patrón de referencia. Una medición de alta calidad, como las que se utilizan para definir los estándares, es precisa y exacta.

### Error relativo y procentual.

Se calcula dividiendo el error absoluto por el valor de la variable medida
## $$ \epsilon = \frac {\triangle t}{t}$$
Si la multiplciamos por 100 obtenemos el relativo porcentual:
## $$ \epsilon = \frac {\triangle t}{t}*100*$$

## Cálculo de Incertezas
### Medidas Directas
#### Incertezas del promedio
![[Pasted image 20210914175758.png]]

#### Moda
Se toma el valor más repetido. (Ej: si de 5 mediciones 4 dieron 16 y 1 dio 17, elegiremos 16 como la moda con una incerteza de 1cm

#### No se como se llama usando max y min

Si ninguna medida esta repetida se puede tomar la medicion maxima y la minima y sumarlas para luego dividirlas por dos
![[Pasted image 20210914180127.png]]

### Medidas indirectas
#### Una sola variable
![[Pasted image 20210914180223.png]]

#### Más de una Variable
![[Pasted image 20210914180242.png]]
![[Pasted image 20210914180257.png]]

![[Pasted image 20210914180335.png]]

## Tablita de incertezas 
![[Pasted image 20210914180350.png]]

## Cifras apropiadas para una constante.
Se despreciará el error de $\pi$ siempre que $10. \varepsilon (\pi) <= 2. \varepsilon (d) +\varepsilon (h)$. Para ello es conveniente
confeccionar un cuadro como el siguiente:
![[Pasted image 20210914203000.png]]

## Criterio de equivalencia entre dos series de mediciones
si tenemos dos mediciones:
Medicion 1: $X1 = X1 \pm \triangle X1$
Medicion 2: $X2 = X2 \pm \triangle X2$
Definimos el limite de incertezas como: $\triangle X =(\triangle X1+\triangle X2)/2$