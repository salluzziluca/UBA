---
Dia: 2025-09-26
dg-publish: true
---
Busca separar el [[Router Data Plane]] del [[Router Control Plane y Scheduling | control plane]]


Antes se ponia la direccion destino y listo, con eso se iba guiando al paquete a su destino final. Ahora se brinda msa informacion para que no haya que hacer recalculos en cada uno de los routers. 

El [[Network layer#Routing]] es muuuy lento, entonces cuando llega una IP que no esta en la [[Router Control Plane y Scheduling| tabla de routeo]] hay que hacer calculos que en el mejor de los casos es O(n)

SDN busca resolver esto.

![[Pasted image 20250926193359.png]]
![[Pasted image 20250926193415.png]]