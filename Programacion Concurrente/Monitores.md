---
Dia: 2025-09-22
dg-publish: true
---
>[!example] Herramientas de sincronización que permite a los hilos tener exclusión mutua y la posibilidad de esperar (block) por que una condición se vuelva falsa. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple

Un monitor consta de:
I Nombre
I Variables internas
I Procedimientos del monitor: rutinas que acceden directamente
a las variables internas
I Una interfaz pública para que los procesos puedan acceder a
las variables internas
I Inicialización de las variables internas
I Un conjunto de condition variables que incorporan sincronismo
al monito