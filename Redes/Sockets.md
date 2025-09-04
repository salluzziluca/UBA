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
- Socket d