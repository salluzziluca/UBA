---
Dia: 2025-10-03
dg-publish: true
---
Es un protocolo que se una para transportar informacion de enrutamiento entre los [[AS (Autonomous System)|sistemas autonomos]]. Solo se una uno. Actualmente estamos en la version 4.

>[!important] Es el encargado del enrutamiendo a nivel global.


Agrega un campo a la tabla de routeo

![[Pasted image 20251003194950.png]]

Aclara el camino/path que hay que hacer desde el [[AS (Autonomous System)|AS]] inicial para poder llegar al final  atraves de todos los [[AS (Autonomous System)|AS]] intermedios.

![[Pasted image 20251003195502.png]]


Las comunicaciones importantes se dan entre los [[Router|routers]] bordes

Se guardan todos los caminos posibles 
La salida que elegida va a ser la de menor AS en el AS-path