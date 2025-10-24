---
Dia: 2025-10-24
dg-publish: true
---
Parte central de [[Capa de enlace]]

Son como las ciudades o barrios de la red. 
A medida que uno va profundizando y adentrandose en la red la mascara deberia ir teniendo mas unos, mas direcciones de host. 

Se utilizan mucho las direcciones MAC (meddium access control). Son el DNI de 48 bits. Con la mitad de la direccion siendo vendor y la otra

Si conozco la MAC y estoy en la misma red puedo hablarle directamente sin pasar por ip.
Puedo hacer broadcast a MAC usando 
`FF:FF:FF:FF:FF:FF`

Una PC solo puede acceder a los paquetes enviados a su direccion o a broadcast


## Switch 
Los switches tienen varias bocas. Leen el paquete ethernet y lo redirigen. Al mismo tiempo puede reutilizar otros caminos
![[switch.excalidraw]]

Se puede ver en rojo un caino y en azul el otro. Ambos ocurren en paralelo. No tiene que esperar a que termine un envio para realizar otro


## Bridge 

Envia mensajes entre estaciones 

![[Drawing 2025-10-24 20.13.54.excalidraw]]


El bridge ve un paquete que sale de destino B y origen A. 
Como el bride no sabe que donde esta el destino. Pasa, pero sabe que A esta de la izq 
Cuando b responde sabe que B esta en la izquierda pero tambien sabe que A sigue ahi, Entonces no deja pasar el mensaje al otro lado. Sabe que es al pedo. 

Un switch hace esto pero con mas de 2 bocas. Solo deja pasar a la zona en la valga la pena ir.