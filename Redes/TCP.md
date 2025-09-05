---
Dia: 2025-09-05
dg-publish: true
---
Los paquetes de TCP se llaman segmentos porque si tienen relacion el uno con el otro 

Cuando yo envio mi paquete mando un SN (sequence number o NS), este es el numero dle ultimo byte. Y en el ACK por parte del reciever me va a llegar en NR (numero de reconocimiento) el numero SN+1. Y en el NS del ACK envio 

>[!example] Si yo envio mi paquete con el SN= 1000. El NR en el ACK del reciever deberia valer 1001

Si la [[Capa de Transporte#Continuo|ventana de envio]] fuese fija. A veces estaria enviando por encima y otras por debajo de la capacidad de trafico de la red.



