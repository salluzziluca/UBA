---
Dia: 2025-09-26
dg-publish: true
---
## Tipos de Ventanas
 
$$W=min⁡(rwin,cwin)W = \min(\text{rwin}, \text{cwin})W=min(rwin,cwin)$$

Donde:

- **W** = ventana de transmisión
- **rwin** = receive window del otro lado
- **cwin** = congestion window

> [!tip] Si me envían rwin = 0, cada tanto le puedo mandar un paquete con el flag push

## Slow Start

- La **ventana de congestión** arranca en **1 MSS**
- El **ssthresh** arranca en **65535 bytes** (prácticamente +∞)

**Funcionamiento:**

1. Envío 1 MSS
2. Me llega la respuesta → por cada ACK aumento en 1 MSS (1 → 2 MSS)
3. Envío 2 ventanas completas
4. Me llegan las respuestas → por cada ACK aumento en 1 MSS (2 → 4 MSS)
5. Y así sucesivamente...

**Resultado:** Aumenta exponencialmente, muy rápido.

## Congestion Avoidance

**Cuando llegan 3 ACKs repetidos:**

- Bajo rápidamente el tamaño de la ventana **a la mitad**
- Seteo el **ssthreshold** al punto donde estoy (ya dividida)

**Nuevo crecimiento:**

- Aumento **mucho más despacio** el tamaño de la ventana
- Recién cuando recibo la **ventana ENTERA** aumento 1 MSS (no por cada ACK)

**Ajuste dinámico del threshold:** El threshold puede subir o bajar según cuándo se colapse la red nuevamente. Si tengo otro triple ACK pero con una cwin más grande (cwin/2 > ssthreshold), lo aumento.

## Timeout Behavior

**TCP Reno en caso de timeout:**

- Setea **cwin = 1 MSS**
- Setea **ssthreshold = 2 MSS**
- En seguida llega a los 2 MSS y vuelve a entrar en congestion avoidance

![[Pasted image 20250905212416.png]]

## Fast Retransmit y Fast Recovery

**Cuando llegan 3 ACKs del mismo:**

1. **Reenvío** solo el que falló
2. **Aumento la ventana en 3** para poder enviar los 3 paquetes siguientes
3. La agrando rápido para no perder tiempo
4. Envío 3 extras
5. Una vez que me llegan los ACKs que me faltaban, **cierro los 3 slots extras**

## Enlaces

- [[TCP]] - Archivo principal
- [[TCP Conexiones]] - Establecimiento y cierre de conexiones
- [[MSS]] - Maximum Segment Size