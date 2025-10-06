---
Dia: 2025-09-18
dg-publish: true
---
Separar un paquete de datos en fragmentos mas pequeños para una transmision sin interrupciones. Eso es necesario cuando el paquete es mas grande que el [[MTU]]

Cada fragmento es un paquete IP diferente y tratado individualmente, no se va a poder ensamblar en el camino.

La informacion que detalla la fragmentacion se encuentra en el header IP. 

fragment offset (porque los fragmentos pueden no llegar en orden, se da el offset para hacer el reensamblado)
flags en general. Su offset con respecto al paquete original. 

Se ensamblan antes de entregarlos a [[TCP]]/UDP

Si uno o mas fragmentos no llegan, se descarta la secuencia

![[Pasted image 20250918182553.png]]
El flag de do not fragment le dice a ip que NO fragmenet este paquete. Si no pasa porque es mas grande que el [[MTU]], no lo fragmentes, descartalo.


Ej:

supongamos [[MTU]] 550B
530B payload + 20B header
● Quiero enviar un payload 800B


busco el mayor valor posible a 550 divisible por 8.
![[Pasted image 20250918182919.png]]
= 528B

primer fragmento = 528, segundo fragmento 800-528=272



| nr fragment     | offset | total len | payload len | MF  | DF  |
| --------------- | ------ | --------- | ----------- | --- | --- |
| 1 (pasa por L1) | 0      | 976+20    | 976         | 1   | 0   |
| 2 (pasa por L2) | 122    | 48+20     | 48          | 0   | 0   |
| 2 (pasa por L2) | 0      | 1024+20   | 1024        | 0   | 0   |
|                 |        |           |             |     |     |
