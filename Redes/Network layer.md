---
Dia: 2025-09-18
dg-publish: true
---
## Forward 
Cuando un paquete le llega al router en su input link, este lo forwardea al proximo router en la cadena de mensaje. Este termino refiere a la accion local de cada router de transmitir un paquete desde input hasta su output link interface



## Routing 
Este termino refiere al proceso end to end de elegir la mejor ruta para que viaje el paquete. 
Vendria a ser como la planificacion del viaje que el apquete va allevar a cabo

The network layer must determine the route or path taken by packets as
they flow from a sender to a receiver. The algorithms that calculate these paths
are referred to as routing algorithms. A routing algorithm would determine, for
example, the path along which packets flow from H1 to H2 in Figure 4.1. Routing
is implemented in the control plane of the network layer.


## Forwarding Table 
A router forwards a  packet by examining the value of one or more fields in the arriving packet’s header,
and then using these header values to index into its forwarding table. The value stored
in the forwarding table entry for those values indicates the outgoing link interface at
that router to which that packet is to be forwarded. For example, in Figure 4.2, a packet

with header field value of 0110 arrives to a router. The router indexes into its forward-
ing table and determines that the output link interface for this packet is interface 2.

The router then internally forwards the packet to interface 2.



