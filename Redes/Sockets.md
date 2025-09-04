---
Dia: 2025-09-04
dg-publish: true
---
Son puertas que reciben entrada de un proceso y salen a otro. Este necesita saber donde recibe y un puerto.


## Sockets UDP

socket(addr_family, type)

addr_family define el tipo de direcciones que se utilizaran:
- AF_INET es para IPV4 
- No se cual se usa para IPv6 

Type especifica el tipo que vamos a crear:
- Socket dgrm para UDP 

socket.bind(addrs)

asocia el socket a una direccion local. Addres indica la direccion IP y puedo que el servidor o el cliente escucharan

socket.sendto(data, addrs)

Envia datos a traces dl socket 

data son los datos en forma de byte 

como no hay conexion, se debe especificar a donde mandarlo usando la addr 
devuelve la cantidad de bytes enviados 

socket.recvfrom(bufsize)

bloquea e huloi de ejecucion hasta que le llegue una conexion. Se le especifica el 