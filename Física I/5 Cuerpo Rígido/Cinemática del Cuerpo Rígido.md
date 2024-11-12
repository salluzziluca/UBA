---
dg-publish: true
---
## Movimientos del Cuerpo Rígido

### Traslación Pura
Todos los puntos del CR tienen igual velocidad y cambian de la misma forma con el tiempo. 
![[Pasted image 20211025082638.png]]
Es equivalente a pensar al CR como un solo punto. Si nos dan solo la velocidad  del centro de masa ya podemos calcular todo el CR
#### Campo o perfil de velocidades
(visto desde arriba)
![[Pasted image 20211025082909.png]]

#### Perfil de [[Aceleración de un Cuerpo Rígido|Aceleración]]
![[Pasted image 20211027092848.png]]

---
### Rotación Pura
El Rígido tiene un eje inmóvil y todo el cierpo rota alrededor del eje.
Tomando la velocidad angular en el eje de rotacion podemos calcular las velocidades en los puntos que querramos, los puntos del CR no tienen la misma velocidad ni cambian igual. 
![[Pasted image 20211025083352.png]]

#### Perfil de velocidades
![[Pasted image 20211025084514.png]]

#### [[Aceleración de un Cuerpo Rígido|Aceleración]]

$$\LARGE \vec a_p = \vec \gamma \times \vec r^*_{p} + \vec \omega \times (\vec \omega \times \vec r^*_{p} )$$
Siendo $\vec \gamma \times \vec r^*_{p}$ la aceleración tangencial y $\vec \omega \times (\vec \omega \times \vec r^*_{p} )$ la aceleración normal. Y siendo $\gamma$ velocidad angular
![[Pasted image 20211027093920.png]]
![[Pasted image 20211027094049.png]]
#### Perfil de aceleraciones
![[Pasted image 20211027093956.png]]

---
### Rototraslación
Un cuerpo que avanza a la vez que rota
![[Pasted image 20211025085013.png]]
Para obtener la velocidad en el punto, sumamos la velocidad de traslacion del eje más la velocidad de rotación alrededor del eje 

$$\LARGE \vec v_{p/o} = \vec v_{eje} + \vec \omega \times \vec r_{P/o}$$

#### Perfil de velocidades
![[Pasted image 20211025085707.png]]
Para la rototraslación, tener en cuenta los [[Tipos de Movimientos|tipos de movimientos]]


![[Propiedades de la cinemática del Cuerpo Rígido|Propiedades]]