---
Dia: 2025-10-08
dg-publish: true
---
---

**1. TCP – Congestión & Retransmisiones (Reno vs Tahoe)**  
Elija la opción correcta:  
A. A la recepción de un triple ACK duplicado, TCP Tahoe hace un fast retransmit y entra en congestion avoidance.  
B. El tamaño de ventana se ve siempre limitado por el tamaño del congestion window (CWND).  
C. El campo Window Size del header TCP se utiliza para evitar el congestionamiento de la red.  
D. TCP utiliza la estrategia “cumulative acknowledgements”.  
E. Un triple ACK duplicado implica que el mismo ACK fue recibido 3 veces.

---

**2. CDN**  
¿Qué técnica se usa comúnmente en una CDN para decidir desde qué servidor enviar el contenido a un usuario?  
A. Round Robin DNS  
B. Anycast IP routing  
C. Medición activa de latencia  
D. Localización por IP (GeoDNS)  
E. Todas las anteriores

---

**3. Subnetting**  
Dada la red 180.16.0.0/20. Cuántas subredes de tamaño de bloque de IPs igual a 64 pueden existir sabiendo que:

- Se necesita reservar espacio para una red /21
    
- Se necesitan 600 hosts en una misma subred
    
- Se necesita reservar espacio para 2 subredes cuyo tamaño de bloque sea 32
    
- Se necesitan 8 subredes punto a punto para conectar routers entre sí
    

A. 10  
B. 9  
C. 8  
D. 7  
E. 5  
F. No se puede subnetear redes /25 acorde a las especificaciones  
G. No cuento con toda la información necesaria para poder responder

---

**4. Fragmentación IPv4**  
Un datagrama IPv4 de 4000 bytes (incluyendo un encabezado de 20 bytes) se fragmenta en una red con MTU de 1500 bytes.  
El datagrama original tiene el flag DF=0. Los fragmentos llegan al destino en orden inverso (último fragmento primero).  
Marque todas las afirmaciones correctas sobre el comportamiento del host emisor:

A. Ante un escenario de pérdida de paquetes, el host emisor siempre reenvía sólo los fragmentos que se pierden en el camino y no el paquete original dado que el receptor ya cuenta con algunos fragmentos.  
B. En caso de pérdida de algunos fragmentos, el host emisor reenvía todos los fragmentos, no solo los que se pierden.  
C. Ante un escenario de pérdida de paquetes, el host emisor reserva sólo los fragmentos que se pierden en el camino y no el paquete original dado que el receptor ya cuenta con algunos fragmentos, si se usa TCP.  
D. El emisor recibe más ACK debido al proceso de fragmentación del receptor en vez de recibir el paquete original.  
E. El emisor recibe más ACK duplicados debido al proceso de fragmentación del receptor en vez de recibir el paquete original.  
F. El emisor recibe más ACK duplicados debido al proceso de fragmentación del receptor y envía retransmisión cuando se utiliza TCP.  
G. Ninguna de las anteriores.

---

**5. Tablas de Ruteo (crítico)**  
Una tabla contiene las siguientes rutas:
Destino      Máscara         Gateway
10.160.0.0   255.255.80.0    10.0.0.4
10.160.0.0   255.255.255.0   10.0.0.3
10.0.0.0     255.255.255.224 10.0.0.2
0.0.0.0      0.0.0.0         10.0.0.1
Si un paquete con destino **10.168.1.194** llega, ¿a qué gateway se envía?  

A. 10.0.0.1  
B. 10.0.0.2  
C. 10.0.0.3  
D. 10.0.0.4  
E. No hay coincidencia en la tabla  

---

**6. DNS**  
Un cliente realiza una consulta DNS recursiva para **www.paginaweb.com** a un resolver local.  
La respuesta del servidor autoritativo devuelve una dirección IP con un TTL de 1800 segundos.  
Cinco minutos después, otro cliente en la misma red realiza la misma consulta, y el resolver responde instantáneamente sin contactar al servidor autoritativo.  
¿Que explica este comportamiento?  

A. El servidor autoritativo reenviará la respuesta al resolver local antes de la segunda consulta.  
B. La segunda consulta usó una resolución iterativa en lugar de recursiva.  
C. El resolver local almacenó la respuesta en caché y la sirvió directamente.  
D. El TTL de 1800 segundos se ignoró porque el resolver local está configurado para actualizar la caché frecuentemente.  
E. Ninguna de las anteriores.  

---

**7. Tablas de Ruteo (II)**  
Dada la siguiente tabla de ruteo: }

Network destination | Netmask | Interface | Next Hop

220.33.217.128 | 255.255.255.128 | if0 | 10.57.22.10  
220.33.217.0 | 255.255.255.0 | if3 | 10.57.192.85  
220.33.220.0 | 255.255.255.0 | if3 | 10.57.192.85  
220.33.216.0 | 255.255.255.0 | if3 | 10.57.192.85  
220.33.219.0 | 255.255.255.0 | if3 | 10.57.192.85  
220.33.220.0 | 255.255.255.255 | if3 | 10.57.192.85  
0.0.0.0 | 0.0.0.0 | if3 | 10.57.22.10

¿Cuántas entradas tiene la tabla óptima?  

A. 5  
B. 4  
C. 2  
D. 7  
E. 6  
F. 3  
G. Ninguna de las anteriores  

---

**8. Latencia**  
¿Cuál de las siguientes afirmaciones es correcta sobre la latencia?  
A. A menor tamaño, menor latencia  
B. La latencia aumenta si la red se congestiona  
C. La latencia disminuye si la distancia se reduce  
D. El tiempo de encolado siempre es el dominante en el cálculo de la latencia  
E. El tiempo de propagación siempre es el dominante en el cálculo de la latencia  
F. ICMPv4 es utilizado para estimar la latencia  
G. ICMPv6 no se utiliza en IPv6 para estimar la latencia por vulnerabilidades del protocolo  
H. Ninguna de las anteriores  

---

