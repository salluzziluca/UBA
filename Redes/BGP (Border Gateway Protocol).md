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

Se guardan todos los caminos posibles, pero la salida que elegida va a ser la de menor [[AS (Autonomous System)|AS]] en el [[AS (Autonomous System)|AS]]-path

Yo como [[AS (Autonomous System)|AS]] puedo hacer [[prepending]], repitiendo mi direccion multiples veces para que esa ruta sea menos atractiva para el trafico.


## Politicas de BGP 
![[Pasted image 20251003201411.png]]

Para evitar que un peer competencia use mis rutas gratis, las rutas que aprendo de mis proveedores las enseño solo a mis clientes. A mis vecinos solo les transmito las rutas que aprendo de mis clientes