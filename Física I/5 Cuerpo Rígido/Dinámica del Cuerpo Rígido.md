---
dg-publish: true
---
# [[2.0 Dinámica|Dinámica]] del Cuerpo Rígido
(Tomando el CR como un sistema continuo de muchisimas partículas con condicion de rigidez.)
![[Pasted image 20211101081839.png]]
![[Pasted image 20211101081749.png]]

## [[Cantidad de movimiento de un Sistema de Partículas (SP)#Primera ecuación fundamental del Sistema de Partículas|Primera ecuación fundamental del Sistema de Partículas]] aplicada a CR.

[[Cantidad de movimiento de un Sistema de Partículas (SP)#resultados de la primera ecuación fundamental de los SP|resultados de la primera ecuación fundamental de los SP]] tambien aplican para el CR.

## [[Segunda Ecuación Fundamental del Sistema de Partículas]]
La relacion entre los torques y la velocidad angular tambien se cumple.
Aparece tambien una nueva fuerza llamada 
#### Momento de inercia
==(vale en ciertas condiciones, cuando Momento Angular(L) y Velocidad angular==($\Omega$) ==son perpendiculares)==
- Nos habla sobre como está distribuida la masa del CR respecto al punto.
- Se puede demostrar que existen para cualquier CR siempre 3 ejes principales para los cuales L es paralelo a $\Omega$
- Se los llama ejes principales de inercia.
- Coincide con los ejes de simetría del cuerpo.
la cual se escribe como 
$$\LARGE _{momento \ de}I_{nercia} = m.R^2$$
Luego: $$\LARGE \vec L_o= I.\vec \omega$$
Y podemos expresar la [[Segunda Ecuación Fundamental del Sistema de Partículas]] como:
$$\LARGE \sum \vec t_{ext}^0=\frac {d\vec L^0}{dt}=\frac {d(I_o\vec \Omega}{dt}$$
$$\LARGE I_o \frac {d \vec \Omega}{dt}= I_o \gamma$$
(con $\gamma$=velocidad angular)

#### Radio de giro
$$\LARGE I = m.K^2$$ Siendo K radio de giro, en algunos cuerpos K coincide con R, pero en otro no, si nos dan el RADIO DE GIRO ya lo reemplazamos directo por K en la cuenta. Si nos dan el radio del cuerpo, depende de que cuerpo estemos tratando.
##### Tabla de radios de giro
![[Pasted image 20211101091313.png]]

## Teorema de Steiner o de ejes paralelos

Si quiero calcular un [[Dinámica del Cuerpo Rígido#Momento de inercia vale en ciertas condiciones cuando Momento Angular L y Velocidad angular Omega son perpendiculares|momento de inercia]] paralelo al del centro de masa, podemos calcualrlo de la siguiente forma:
$$\LARGE I_e = I_{CM} + Md^2$$


### El momento de inercia es aditivo y substractivo
##### Momento de inercia de un martillo
![[Pasted image 20211101092425.png]]
##### Momento de inercia de un cilindro vacío
![[Pasted image 20211101092204.png]]
![[Pasted image 20211101092227.png]]

## Resumen
![[Pasted image 20211101092506.png]]


## Energías
[[Energía Cinética de un Cuerpo Rígido]]