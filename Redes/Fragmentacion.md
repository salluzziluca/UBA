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