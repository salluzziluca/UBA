---
Dia: 2025-09-05
dg-publish: true
---
# TCP (Transmission Control Protocol)

![[Pasted image 20250905214306.png]]

Los paquetes de TCP se llaman **segmentos** porque tienen relación el uno con el otro.

## Numeración de Secuencia

Cuando envío mi paquete mando un **SN (Sequence Number o NS)**, este es el número del último byte. En el ACK por parte del receiver me va a llegar en **NR (Número de Reconocimiento)** el número SN+1. Es decir, el próximo que yo quiero escuchar.

> [!example] Si yo envío mi paquete con el SN = 1000. El NR en el ACK del receiver debería valer 1001. Como el ACK no envía data, no modifica su SN en cada valor. Simplemente pone un número random.

> [!important] En una comunicación emisor-receptor en la que siempre una envía y la otra solo tira ACK. El NR de emisor y el NS del receptor nunca deberían cambiar.

## Ventana de Transmisión

Si la [[Capa de Transporte#Continuo|ventana de transmisión]] fuese fija, a veces estaría enviando por encima y otras por debajo de la capacidad de tráfico de la red.

Tener siempre en cuenta el [[MSS]]. En el aire yo puedo tener 2Gb. Porque a partir de ahí ya se me pisan los números de NS en la ventana. Tengo overflow.

![[Pasted image 20250905202248.png]]

## Reporte de Errores

Si a mí como receptor me llega un paquete cuyo NS no coincide with el NR que yo espero, reenvío el último ACK que mandé. Es decir el del paquete que SÍ llegó.

![[Pasted image 20250905202209.png]]

## Temas Relacionados

- [[TCP Conexiones]] - Establecimiento y cierre de conexiones
- [[TCP Control de Flujo]] - Manejo de ventanas y congestión
- [[MSS]] - Maximum Segment Size