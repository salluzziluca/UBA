---
Dia: 2025-09-18
dg-publish: true
---
![[Pasted image 20250918185308.png]]

IHL = largo del paquete 

Identification = Id. Todos los fragmentos de un paquete van a tener el mismo id. Si cambia entre paquetes|

para ver los flags de fragmentacon ver [[Fragmentacion]]

TTL: cuanto saltos puede hacer un paquete antes de ser descartado. Cada vez que pasas por un router, se decrementa en un o ese numerito. Podes usarlo para descubrir la topologia de la red. vas mandando paquetes con un TTL que crece de a 1. el primero te lo rebota el primer router y te manda mensaje, el segundo con TTL 2 te lo rebota el 2do router haciendo lo mismo. Y asi puedes 