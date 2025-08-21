---
Dia: 2025-08-21
dg-publish: true
---
## Packet Lost 

El paquete se origina en un host pero nunca llega a destino.


## Latencia 

Retardo entre estimulo y respuesta 

### Impacta
En la UX. 
Ciertas aplicaciones son sensibles a la latencia (como alarmas que cortan producciones industriales)

### Que la origina?
1. Tiempo de Insercion
	Tiempo que demora el parque en ser insertado en el enlace
	$\frac{Largo\_paquete}{velocidad\_{serializacion}}$
2. Tiempo de propagacion 
	Depende del medio. Es distancia/velocidad en el medio
3. Tiempo de procesamiento 
	Leer el header del paquete y ver a donde lo mando.
4. tiempo de encolado
	Tiempo desde que arriba hasta que es finalmente transmitido.
	Varia con el trafico, no es el mismo para todos, es aleatorio
Insercion vs propagacion
La insercion es lo que tarda la gente en subir al ascensor. Propagacion lo que tardan en llegar al 4to piso

En distancias largas prepondera el tiempo de propagacion 
En distancias largas, el tiempo de insercion

## Packet Lost 

queremos que llegue todo todo el tiempo

Problema: $L*a = R$ la COLA desborda 

Solucion: $L*a<R$
La subutilizamos


## Round Trip Time (RTT) 

Tiempo que tarda en salir un paquete, llegar y volver. 

PING...PONG 

## Throughput/Tasa de envio

Cantidad de datos que se pueden transmitir a traves de la red e un periodo de tiempo determinado. Si tengo toda la red libre, es == a ancho de banda. Si esta siendo muy utilizada va a ser menor al ancho de banda

Tasa a laque stransfieren bits entre transmisor/receptor