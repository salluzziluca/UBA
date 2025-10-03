---
Dia: 2025-09-26
dg-publish: true
---
Es una modalidad, pensado para redes no demasiado grandes (usualmente se usa solo para redes locales)

Busca separar el [[Router Data Plane]] del [[Router Control Plane y Scheduling | control plane]]

El plano de control esta centralizado en una nube

Antes se ponia la direccion destino y listo, con eso se iba guiando al paquete a su destino final. Ahora se brinda msa informacion para que no haya que hacer recalculos en cada uno de los routers. 

El [[Network layer#Routing]] es muuuy lento, entonces cuando llega una IP que no esta en la [[Router Control Plane y Scheduling| tabla de routeo]] hay que hacer calculos que en el mejor de los casos es O(n)

SDN busca resolver esto. Es un controlador central para evitar que cada router tenga un [[Router Control Plane y Scheduling | control plane]]. De esa forma los routers solo se encargaria de enviar las cosas. Es una configuracion centralizada

![[Pasted image 20250926193359.png]]
![[Pasted image 20250926193415.png]]


## Partess del SDN
![[Pasted image 20251003192655.png]]

Intefaz norte en azul y sur en verde. 

Tiene un aparte de comunucauin que oibe las confugraciones a los routers

Luego el control y por encima las aplicaicones tales como NAT, rooting, firewall, access control