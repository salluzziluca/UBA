---
Dia: 2025-09-26
dg-publish: true
---

## Establecimiento de Conexión (3-Way Handshake)

1. **Emisor** envía el paquete para abrir la conexión:
    
    - Manda su NS
    - Aclara cuál es el [[MSS]] que va a usar
    - Manda el flag de SYN
    - Envía el rwin (receive window) - cuánto puede recibir el emisor _en ese momento_
2. **Receptor** envía un ACK:
    
    - NR = NS del emisor + 1
    - Envía el MSS propio
    - Envía el rwin propio
3. **Emisor** envía ACK final:
    
    - Mismo NS
    - NR + 1
    - rwin _en ese momento_

> [!important] El rwin se manda en cada paquete, siempre. Le digo cuál es el tamaño de mi buffer en ese momento. Mi disponibilidad para recibir.

![[Pasted image 20250905210054.png]]

## Cálculo del Timeout

**Tiempo promedio estimado:** $$T(i) = RTT(i) \cdot \alpha + T(i-1) \cdot (1-\alpha)$$

Donde $0 \leq \alpha \leq 1$. Se suele elegir $\alpha = \frac{1}{8}$

**Desvío:** $$D = |RTT(i) - T(i)| \cdot \beta + D(i-1) \cdot (1-\beta)$$

Con $\beta = \frac{1}{4}$

**Retransmission Timeout (RTO):** $$RTO = T(i) + 4 \cdot D(i)$$

## Enlaces

- [[TCP]] - Archivo principal
- [[TCP Control de Flujo]] - Manejo de ventanas y congestión