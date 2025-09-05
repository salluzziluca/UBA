---
Dia: 2025-08-29
dg-publish: true
---
>[!attention] Permite *multiplexar* y *demultiplexar*. Esa es su funcion principal.

Se rige por la maxima del best effort (intenta lo mejor que puede). Una propiedad heredad de la capa de Red. Facilita el diseño de red porque permite usar equipos mas simples y protocolos menos complejos. 

Las dos cosas mas importanes son:
- Mutiplexado
- verificacion de erorres (minima)

Tambien puede proveer:
- Confiabilidad de las comunicaciones 
- Control de flujo (la capa de transporte da aviso de si el flujo es optimo o si algunos de los ends se encuentra ocupado)
- Seguridad (asegurarnos de que la info no fue modificada, verificacion de extremos, etc)



## Puertos y sus servicios
443 -> HTTPs 
80-> HTTP


## UDP 
![[Pasted image 20250829202425.png]]


## Principios de comunicacion confiable

- Conectadas (se ejecutan un par de pasos para asegurar conexion) vs no conectadas (DNS, whatsapp)
- Asegurar entrega 
- Asegurar el orden
- Asegurar integridad
- Desempeño o performance. Mandar cosas y recibirlas rapido.
- Control de flujo (hace esperar a las partes hasta que la red este disponible para la comunicacion. da avisos)
- Compartir el canal equitativamente (esto es importante porque siempre nos regimos por el best effort. Si no fuese equitativo volaria todo por los aires)

### Tipos de Flujo 
#### Stop and wait 
Mando y espero el ack. Hasta que no me llega el ack no envio otro paquete. Es lento e insoportable 

#### Continuo 
Tengo una ventana de x paquetes. Solo puedo mandar x paquetes sin que me llegue el ack. Si mi ventana es de 10 y yo mande 10. Hasta que no me llegue el ack del primero no voy a poder seguir mandando. A medida que me llegan los acks voy desplazando la ventana. 

#### Go back N
Si alguno se pierde (es decir, no me llega el AKC). Vuelvo a ese y mando de ese hacia adelante tooodos los packets. 

#### Selective repeat 
Reenvio solo del que no me llego el ack. No todos


Actualmente lo que se hace es tener una ventana que se adapta segun las perdidas. Si hay muchas perdidas quiere decir que la red esta muy congestionada. Si yo achico mi ventana, bajo mi velocidad. Ese es, en criollo, el control de congestion que hace TCP



## Variables y mecanismos del flujo confiable de datos 

- Checksum o CRC (Cyclical redundancy check): Verificacion de integridad 
- Timer para detectar paquetes perdidos (si no me llega el ack en x tiempo, reenvio)
- Numero de secuencia para mantener el flujo de paquetes y detectar perdidos 
- ACK 
- NACK (para avisar que el paquete llego corrupto), no se usa en TCP 
- Ventana deslizante (ver arriba).

## [[TCP]]
