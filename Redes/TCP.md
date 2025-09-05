---
Dia: 2025-09-05
dg-publish: true
---
Los paquetes de TCP se llaman segmentos porque si tienen relacion el uno con el otro 

Cuando yo envio mi paquete mando un SN (sequence number o NS), este es el numero dle ultimo byte. Y en el ACK por parte del reciever me va a llegar en NR (numero de reconocimiento) el numero SN+1. Y en el NS del ACK sera del ultimo byte que envio.

>[!example] Si yo envio mi paquete con el SN= 1000. El NR en el ACK del reciever deberia valer 1001. Como el ACK no envia data. No modifica su SN en cada valor. Simplemente pone un numero random. 


>[!important] En una comunicacion emisor receptor en la que siempre una 

Si la [[Capa de Transporte#Continuo|ventana de envio]] fuese fija. A veces estaria enviando por encima y otras por debajo de la capacidad de trafico de la red.


Tener siempre en cuenta el [[MSS]]


