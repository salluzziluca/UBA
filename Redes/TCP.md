---
Dia: 2025-09-05
dg-publish: true
---
Los paquetes de TCP se llaman segmentos porque si tienen relacion el uno con el otro 

Cuando yo envio mi paquete mando un SN (sequence number o NS), este es el numero dle ultimo byte. Y en el ACK por parte del reciever me va a llegar en NR (numero de reconocimiento) el numero SN+1. Es decir, el proximo que yo quiero escuchar.

>[!example] Si yo envio mi paquete con el SN= 1000. El NR en el ACK del reciever deberia valer 1001. Como el ACK no envia data. No modifica su SN en cada valor. Simplemente pone un numero random. 


>[!important] En una comunicacion emisor receptor en la que siempre una envia y la otra solo tira ACK. El NR de emisor y el NS del receptor nunca deberian cambiar.

x|

Si la [[Capa de Transporte#Continuo|ventana de transmision]] fuese fija. A veces estaria enviando por encima y otras por debajo de la capacidad de trafico de la red.


Tener siempre en cuenta el [[MSS]]. En el aire yo puedo tener 2Gb. Porque a partir de ahi ya se me pisan los numeros de NS en la vetana. Tengo overflow (revisar)
![[Pasted image 20250905202248.png]]


## Reporte de errores

Si a mi como receptor me llega un paquete cuyo NS no coincide con el NR que yo espero. Reenvio el ultimo ack que mande. Es decir el del paquete que SI llego
![[Pasted image 20250905202209.png]]

## Calculo del timeout 
$T(i)= RTT(i) \alpha+T(i-1)(1-\alpha)$ con $0\leq \alpha \leq 1$ Se suele elegir $\alpha=\frac{1}{8}$

$D=|RTT(i)-T(i)| \beta + D(i-1) (1-\beta$. Esto seria el desvio. Con beta = 1/4

Retransmition Timeout (RTO)= T(i) + 4 D(i)


## Establecimiento de conexion y desconexion

El emisor envia el paquete para abrir la conexion. Le manda su NS y le aclara cual es el MSS que va a usar. Le manda el flag de SYN y el rwin(recieve window), cuando puede recibir el emisor.
![[Pasted image 20250905210054.png]]