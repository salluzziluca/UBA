---
dg-publish: true
---
# Resumen de Fórmulas Cuerpo Rígido
$$velocidad \ angular = \omega = \frac V R$$
$$aceleracion \ angular=\gamma $$
$$Momento \ cinetico \ o \ angular = L_{spin}+ L_{orbital} = I_{CM}. \omega + \vec r_{CM} \times  p$$
con $p = M. \vec v_{CM}$ 
$$\sum torques = I_{cm}\ \gamma$$
$$\sum F_{ext} = M.\vec a_{cm}$$
$$a_{cm}= \gamma R$$
$$\vec a_{cm} = \vec a_{cir} + \vec \gamma \times r_{cm/cir} + \vec \omega \times \vec \omega \times r_{cm/cir} $$
$$\frac {dL}{dt}= \tau_F^A = \vec r_{F/A} \times \vec F$$

Esto seria lo mismo que decir que el torque de una fuerza F con respecto a un punto A es lo mismo que la posicion de esa fuerza con respecto a A producto vectorial la fuerza.

---

Si una fuerza esta aplicada sobre el centro de masa, no hace momento en él. Por ende. $L = I \gamma= 0$ y $\gamma = 0$. Finalmente $\omega = cte$. También, $\tau = 0$ porque no hay variación en momento angular

$$v_{a/CM}= \vec v_{CM} + \omega \times r_{a/CM}$$
En la formula de arriba, podemos reemplazar a y CM por cualquier otro punto. depende de lo datos que tengamos, pero si queremos saber la velocidad del cir respecto a un punto b seria
$\LARGE v_{cir/b}= v_b+ \omega \times r_{b/cir}$ 

Condicion de rigidez = $(\vec v_a - \vec v_b).(\vec r_a - \vec r_b) = 0$
![[Pasted image 20220602155321.png]] tomando la velocidad y posicion en el eje que los une. En este caso, en $\hat j$ 


$$I = Momento\  de  \ inercia$$
Es diferente para cada cuerpo y cambia segun el eje que estemos tomando
El ==teorema de steiner== permite obtener el momento de inercia de una figura respecto a cualquier eje paralelo a uno $I$ ya conocido 
$$I_2 = I_1 + M.d^2$$

$$\sum W_{FNC} = \triangle E_{mec}$$
$$\LARGE \triangle E_C = W_{todas las F(int+ext)}$$
$$E_c  = \frac 1 2 M v_{CM}^2 + \frac 1 2 I_c \ \omega^2 = \frac 1 2 I_{cir} \ \omega^2$$
$$E_m  = \frac 1 2 M v_{CM}^2 + \frac 1 2 I_c \ \omega ²+E_p$$


