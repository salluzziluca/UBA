---
Dia: 2025-09-05
dg-publish: true
---
Los paquetes de TCP se llaman segmentos porque si tienen relacion el uno con el otro 

Cuando yo envio mi paquete mando un SN (sequence number), este es el numero dle ultimo byte. Y en el ACK por parte del reciever me va a llegar el numero SN+1.

>[!example] Si yo envio mi paquete con el SN= 1000. El ACK del reciever deberia valer 1001

Si la [[Capa de Transporte#Continuo|ventana de envio]] fuese fija. A veces estaria enviando por encima y otras por debajo de la capacidad de trafico de la red.


NS = Numero de secuencia 
NR = Numero de reconocimiento 