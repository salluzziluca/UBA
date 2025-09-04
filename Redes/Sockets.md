---
Dia: 2025-09-04
dg-publish: true
---
Son puertas que reciben entrada de un proceso y salen a otro. Este necesita saber donde recibe y un puerto.


## Sockets UDP

`socket(addr_family, type)

addr_family define el tipo de direcciones que se utilizaran:
- AF_INET es para IPV4 
- No se cual se usa para IPv6 

Type especifica el tipo que vamos a crear:
- Socket dgrm para UDP 

`socket.bind(addrs)`

asocia el socket a una direccion local. Addres indica la direccion IP y puedo que el servidor o el cliente escucharan

`socket.sendto(data, addrs)`

Envia datos a traces dl socket 

data son los datos en forma de byte 

como no hay conexion, se debe especificar a donde mandarlo usando la addr 
devuelve la cantidad de bytes enviados 

`socket.recvfrom(bufsize)`

bloquea e huloi de ejecucion hasta que le llegue una conexion. Se le especifica el bufsize

Devuelve la información recibida en forma de bytes y la dirección que envió los datos


## Sockets TCP
![[Pasted image 20250904185057.png]]


socket(address_family, type) 
Crea un nuevo socket utilizando los parámetros seleccionados.
- address_family define el tipo de direcciones que se utilizaran. 
	- Normalmente se utiliza AF_INET para direcciones IPv4. 
- type es el tipo de que vamos a crear. 
	- Se utiliza SOCK_STREAM para TCP


socket.bind(address) ○ Asocia el socket a una dirección local. ○ address indica la dirección IP y puerto que el servidor escuchará


socket.listen() ○ Indica al socket que debe aceptar conexiones. ○ De no llamarse, todas las conexiones entrantes serán rechazadas}


socket.accept() ○ Bloquea el hilo de ejecución hasta que se establece una nueva conexión TCP. ○ Devuelve un nuevo socket, representando la conexión y la dirección del host conectado.

socket.connect(address) ○ Bloquea el hilo de ejecución hasta que se establece una conexión TCP con un socket remoto. ○ address indica la dirección IP y puerto donde el socket remoto está escuchando