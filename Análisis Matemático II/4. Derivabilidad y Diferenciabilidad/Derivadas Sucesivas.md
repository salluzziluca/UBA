---
dg-publish: true
---
# Derivadas sucesivas
Es seguir haciendo [[4.2 Derivadas Direccionales#Derivadas Parciales|derivadas parciales]] como si la funcion ya derivada fuera una nueva función normal.
![[Pasted image 20211010104352.png]]
![[Pasted image 20211010104404.png]]
esto es puro formalizmo, lo hacemos con [[4.2 Derivadas Direccionales#Derivada Parcial regla práctica|la regla practica de las derivadas parciales]]. Estos se podria seguir derivando en $x$ y en $y$, 0 problema.
#### Derivadas Cruzadas
Las derivadas cruzadas son derivadas iguales que se obtienen por diferentes caminos cuando hacemos derivadas sucesivas.

![[Pasted image 20220413152718.png]]

$f:D⊂R^2→R$ ; f es C¹ si F es continua en D y las derivadas parciales primeras son continuas en D. 
ej: ![[Pasted image 20211010105219.png]]

## Teorema de Schwarz
Si tenes un campo escalar y en algun entorno de cierto punto existe la derivada segunda xy y es continua entonces la derivada segunda yx eciste y va a valer lo mismo.
> Dado $f:D⊂R^2→R$, campo escalar y A∈D, si en un entorno del punto A existe D_12 f y es continua en A, entonces:
> existe D_21 f y se cumple que D_12 f(A)=D_21 f(A).


#### notas
- Si D_12 f(A)=D_21 f(A) no asegura que las derivadas sean continuas

- El teorema se cumple para todas las [[Derivadas Cruzadas|derivadas cruzadas]], ejemplo: f_xxz^′′′=f_xzx^′′′=f_zxx^′′′