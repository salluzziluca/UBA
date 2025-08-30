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




