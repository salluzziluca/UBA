---
Dia: 2025-09-04
dg-publish: true
---
Hay muchisimo contenido y sigue subiendo. 
En 2015 se registro que el 40% del trafico de bajada en hogares de EEUU era de Netflix. Que pasa si todos quieren ver el mismo contenido y en el mismo lugar?


Se busca:
- Minimizar latencia
- maximizar Throughput 
- Maximizar el trafico en el nucleo de internet 
- Usar una plataforma distribuida

Para:
- Mejorar el tiempo de descarga 
- Respuesta de digitalizacion 
- Reducir costos:
	- ancho de banda
	- volumen de transferencia 
- Disponibilidad por redundancia
	- Resiliencia ante DDoS
	- Resiste congestiones


## Arquitectura 
- Edge computing (llevar la computizacion lo mas cerca del cliente posible)
- Puntos de presencia cerca de donde se va a consumir el recurso 
- Servidores de origen son los que estan en el CORE. En los ISP mas abarcativos

Se hace la consulta a DNS y este te devuelve el Point of Presence que mas convenga, el edge server. No te conectas al origen. De esa forma disminuyo el 