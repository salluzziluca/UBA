---
dg-publish: true
---
## Proceso Puntual 
Un Proceso Puntual Aleatorio es un conjunto enumeardo de puntos aleatorios ubicoado sobre la recta real. En la mayoria de las aplicaciones un punto de un proceso puntual es un instante en el que ocurre algún evento
![[Pasted image 20231024114517.png]]

Vamos a llamar $N(t)$ al numero de eventos durante un intervalo especifico [0,t]
1. El numero de evento durante intervalos de tiempo no superpuestos son VA independdientes![[Pasted image 20231024114629.png]]
2. La proba de cada eventoo en particular es la misma para todos los intervalos de longitud $t$, independientemente de la ubicacion de cada intervalo y de la historia pasada del sistema. ![[Pasted image 20231024114959.png]]
3. La proba de obtener 2 o mas eventos en un intervalo lo suficientemente pequeño es despreciable

La funcion de proba de N(t) está dada por $$p_N(n)=\frac{(\lambda t)^{n}}{n!}.e^{-\lambda t}$$
Ya que $N(t) \sim Poi(\lambda t)$Con $n \in \mathbb{N}_{0}$. Donde lambda>0, entonces N(t) tiene distribución de Poisson de parametro $\mu=\lambda t$.
![[Pasted image 20231031105641.png]]

Para intervalos: ![[Pasted image 20231031122145.png]]

Propiedad:
La variable aleatoria N(t)("cantidad de eventos en un int de longitud t") tiene distribucion de Poisson $\iff$ la variable T("tiempo entre 2 eventos consecutivos") tiene distribución exponencial. 
Ej: tiempo entre evento 1 y 2 menor a 2 minutos: $T_{12}>2$ con $T_{12}\sim \varepsilon(\lambda)$


Definimos G: "tiempo hasta el k-esimo evento de Poisson"![[Pasted image 20231024122330.png]]
![[Pasted image 20231031114824.png]]

### Adelgazamiento o Coloreo
Cada vez que ocurre un evento se lo clasifica como de tipo I con proba p o de tipo $II$ con proba $1-p$
En este caso $\varPi_{1}(\lambda p)$ y $\varPi_{2}(\lambda(1-p))$

Teorema. bajo la condicion de que ocurrieran exactamente n arribos en el intervalo $[0,t]$, los tiempos de los n arribos $S_{1}, S_{2}, \dots, S_{n}$, consideradas como variables aleatorias desordenadas, son independientes y están distribuiidas uniformemente sobre $[0,t]$   


![[Pasted image 20231024140015.png]]


![[Pasted image 20231024140048.png]]




![[Pasted image 20231102185122.png]]