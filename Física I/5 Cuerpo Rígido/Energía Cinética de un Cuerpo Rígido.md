---
dg-publish: true
---
 # Energía Cinética de un Cuerpo Rígido
$$\LARGE \triangle E_C = W_{todas las F(int+ext)}$$
## Casos
### Traslación pura
todos los puntos del CR tienen igual velocidad.
$$\LARGE E_c = \int dE_c = \frac 1 2 \rho . v^2 .dVol = \frac 1 2 v_{CM}^2 \int \rho.dVol$$
Finalmente (con $m_i=\rho.dVol$ por lo visto en [[Dinámica del Cuerpo Rígido]])
$$\LARGE\LARGE E_c = \frac 1 2 M.v_{CM}^2$$

### Rotación pura
En este caso, el CR tiene un eje movil y todo el cuerpo rota alrededor del eje. Todos los puntos del CR tienen igual velocidad angular, la misma.
$$E_c = \frac 1 2 \int \rho v^2 dVol$$
con $\vec v_p = \vec \Omega \times \vec r$
$$\frac 1 2 \int \rho(\Omega .r^*)^2 dVol= \frac 1 2 \Omega^2 \int \rho(r^*)^2 dVol= $$
Finalmente
$$\LARGE E_c = \frac 1 2 I_{CM} \Omega^2$$ con $I_{CM} = \int \rho (r^*)^2 dVol$

### Movimiento Rototraslatorio
El movimiento del CR en general es la suma de dos movimientos:
- La traslacion del eje 
- La rotacion del cuerpo alrededor del eje.

$$\LARGE E_c = \frac 1 2 Mv_{CM}^2 + \frac 1 2 I_{CM}\Omega^2$$
Siendo la primer parte de la cuenta energia de traslación y la segunda energia de rotación.


### Movimiento de rodadura sin deslizamiento
El movimiento del CR es la suma de los dos movimientos, de traslacion y de rotacion.
Tambien se puiede pensar como la rotacion pura del cuerpo alrededor del CIR.
$$\LARGE E_c = \frac 1 2 I_{CIR}\omega_f^2 - \frac 1 2 I_{CIR}\omega_i^2= \frac 1 2 Mv_{CIR}^2$$

Esto luego se aplica en la formula de [[Energía de un Cuerpo Rigido]]



$$\triangle E_m = W_{FNC}$$ 