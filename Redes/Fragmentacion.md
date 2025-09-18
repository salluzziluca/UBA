---
Dia: 2025-09-18
dg-publish: true
---
Separar un paquete de datos en fragmentos mas pequeños para una transmision sin interrupciones. Eso es necesario cuando el paquete es mas grande que el [[MTU]]

Cada fragmento es un paquete IP diferente y tratado individualmente, no se va a poder ensamblar en el camino.

La informacion que detalla la fragmentacion se encuentra en el header IP. 

fragment offset