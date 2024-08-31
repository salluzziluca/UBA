## Fuentes de error:
- 
- 
- truncamiento -> metodos numericos. Ej: cualquier serie/sumatoria infinita, dicretizacion de espacios continuos (pasar de algo continuo a algo continuo)

### Inherentes
mediciones fisicas

### Redondeo y/o almacenamiento en [[memoria]]
### Truncamiento 
- Sumatoria/serie infinitas
- Discretizacion de espacios continuos. Cuando transformo por ejemplo una medida en metros (que es continua) en diferentes puntos a un cm de distancia (discreto)
- Proceso iterativo al cual eventualmente interrumpo


## Teoria lineal de errores
Se poropagan los errores linealizando la relacion entre las variables.   

![[Pasted image 20240831124551.png]]

Busco calcular el error ($\Delta A$). Sabiendo que $\Delta D$ es 30. 
![[Pasted image 20240831124745.png]]

Entonces 
$$\Delta A \approx |\Delta D . \tan \theta| =| \Delta D \frac{dA}{dD}|= |\Delta D . \frac{\pi D}{2}|_{D=D_{m}}= |\Delta D  \frac{\pi D_{m}}{2}|$$
Los modulos se agregan para evitar restar modulos (en peor caso posible)
Es la parte lineal del error. Sin la parte cuadratica, tiene sentido porque estamos usando la [[Ecuacíon de la Recta Tangente|recta tangente]]

Criterio para propagar error de PI
$$\pi = \pi_{m} \pm \Delta \pi = 3.14 \pm 0.005$$ Se pone 0 por cada cifra que conozco y 5 en cada uno que no conozco