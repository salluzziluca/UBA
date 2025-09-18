---
Dia: 2025-09-18
dg-publish: true
---
Separar un paquete de datos en fragmentos mas pequeños para una transmision sin interrupciones. Eso es necesario cuando el paquete es mas grande que el [[MTU]]

Cada fragmento es un paquete IP diferente y tratado individualmente, no se va a poder ensamblar en el camino.

La informacion que detalla la fragmentacion se encuentra en el header IP. 

fragment offset (porque los fragmentos pueden no llegar en orden, se da el offset para hacer el reensamblado)
flags en general 

Se ensamblan antes de entregarlos a TCP/UDP

Si uno o mas fragmentos no llegan, se descarta la secuencia

![[Pasted image 20250918182553.png]]
El flag de do not fragment le dice a ip que NO fragmenet este paquete. Si no pasa porque es mas grande que el MTU, no lo fragmentes, descartalo.

Ej:

supongamos MTU 550B
530B payload + 20B header
● Quiero enviar un payload 800B


busco el mayor valor posible a 550 divisible por 8.
![[Pasted image 20250918182919.png]]
= 528B

primer fragmento = 528, segundo fragmento 800-528=272