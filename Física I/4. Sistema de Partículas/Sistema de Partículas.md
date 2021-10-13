# Sistema de Partículas
- En cada instante se necesitan 6 valores (3 componentes para la posicion y 3 para la velocidad) ==para cada partícula==-> 6.N valores.
- Muchos valores se calculan directamente en el [[4.1 Centro de Gravedad|centro de gravedad]] o en el [[4.1 Centro de Gravedad#Centro de masa CM|centro de masa]], otros valores son propios del sistema. 

## Tipos de sistemas de partículas
### istemas de partículas discretos
con pocas particulas, contables y diferenciables
### sistemas de partículas continuo
Con muchas particulas, un objeto del dia a dia como una goma de borrar, infinitas partículas

## Cantidad de movimiento de un Sistema de Partículas (SP)
Se utiliza la [[4.1 Centro de Gravedad#Velocidad del centro de masa|velocidad del centro de masa]] multiplicada por la sumatoria de las masas o la [[4.1 Centro de Gravedad#Masa|masa total]]
![[Pasted image 20211013085502.png]]
Esto sería igual al caso en el que toda la masa estuviese concentrada en el CM y se moviera con la velocidad del CM 

## Primera ecuación fundamental del centro de masa
![[Pasted image 20211013090457.png]]
### demostración
![[Pasted image 20211013090846.png]]
$\vec F_1$ y $\vec F_2$ son fuerzas externas
$\vec F_{12}$ y $\vec F_{21}$ son fuerzas internas. Con $\vec F_{12}=- \vec F_{21}$.
Luego $\LARGE \frac {d \vec p_1}{dt} = \vec F_{1} +\vec F_{12}$ y $\frac {d \vec p_2}{dt} = \vec F_{2} +\vec F_{21}$.
Entonces $\LARGE \frac {d \vec P}{dt} =\frac {d \vec p_1}{dt} +\frac {d \vec p_2}{dt} = \vec F_1 + \vec F_2$ Porque $\vec F_{12}$ y $\vec F_{21}$ se cancelan.
Por ultimo $\LARGE \frac {d \vec P}{dt} = M \frac {d \vec v_{CM}}{dt} = m. \vec a_{CM}$

### resultados de la primera ecuación fundamental de los SP
- El movimiento del CM está determinado exclusivamente por las fuerzas externas
- Si elsistema está aislado, las fuerzas externas son nulas, por las cantidad de movimiento del SP es constante. El vector P es una constante de movimiento. ![[Pasted image 20211013092104.png]]
- En un sistema aislado, la velocidad del centro de masa es constante. (un MRU) ![[Pasted image 20211013092524.png]]
- Si en un SP aislado la velocidad del centro de masa es nula, esta seguira siendo siempre nula por lo que la posición del CM permanece constante en el tiempo.

## Aislacion de un sistema no aislado
Si un sistema no está aislado pero tomamos instantes muy cercanos justo antes y despues del evento a estudiar, podemos decir que esta aislado ya que las integrales de las fuerzas externas (que son las que condicionan la variacion de la cantidad de movimiento) quedan practicamente igualadas a cero. ![[Pasted image 20211013101709.png]]
Se pueden usar en casos de choques, explosiones, etc