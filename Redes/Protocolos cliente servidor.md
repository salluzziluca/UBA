---
Dia: 2025-08-22
dg-publish: true
---
## HTTP HyperText Transfer Protocol
Es Cliente Servidor. 
Permite transmitir texto formateado, imagenes, multimedia y mil cosas mas. 
- conexiones:
	- no persistentes (1 conexion por elemento)
	- persitente: puede mandar varios elementos juntos. Queda abierta hasta que se envia un mensaje para cerrarla.
- Cacheo de webs. Permitia utilizar copias locales. En servidores de cacheos.



## DNS 
Traduce o linkea un nombre con una IP. El nombre es faicl de recordar para nosotros. La IP es facil de recordar para las maquinas.
Es una [[Bases de Datos]] jerarquica y distribuida.
para la misma IP puede haber diferentes nombres.

Brinda tambien:
- host aliasing 
- Mail server aliasing
- Load distribution 

### Top Levels Domains TDLs
![[Pasted image 20250822205330.png]]

Al estar todo distribuido cada uno se encarga de su propias direcciones. Le pregunto a .AR donde estan los .UBA, le pregunta a .UBA donde estan los .FI... y asi... Eso es una consulta iterativa. Uno va preguntando uno por uno.


Cuando uno le pregunta al DNS local, este si no lo tiene cacheado, hace eso.

Para nosotros, usuario final, estariamos haciendo una consulta recursiva. Se lo pedimos y el nos devuelve.

Los roots no consultan recursivas, si uno les consulta simplemente dan la direccion a la que ir a consultar. Pero nunca te van a resolver la consulta ellos.

### Tipos de consultas 
#### Autorizadas o no 


#### Recursivas o iterativas 
Recursiva->Mi server averigua la respuesta y me la da, no se que hizo.
Iterativa-> Ir uno por uno buscando. 

### Tipo
- **A**: Mapea **hostname → dirección IPv4**.
    - Ej: `(relay1.bar.foo.com, 145.37.93.126, A)`
    - “Si pido la IP de relay1.bar.foo.com, obtengo 145.37.93.126”.

- **NS**: Indica qué servidor DNS es **autoritativo** para una zona.
    - Ej: `(foo.com, dns.foo.com, NS)`
    - “Para info de foo.com, preguntá a dns.foo.com”.

- **CNAME**: Define un **alias** de un hostname.
    - Ej: `(foo.com, relay1.bar.foo.com, CNAME)`
    - “foo.com es un alias de relay1.bar.foo.com”.

- **MX**: Específico para correo. Indica el servidor de mail oficial.
    - Ej: `(foo.com, mail.bar.foo.com, MX)`
    - “Los mails de foo.com se entregan a mail.bar.foo.com”.



### Multicast DNS 


## QUIC (Quick UDP Internet Connections)

Protocolo de google que busca reemplazar a TCP, ya viene encriptado

Corre sobre UDP. Poruqe los chequeos los hace internamente. Y era mas facil usar UDP que definir su propio protocolo.



## TLS (Transport Layer Security) 

Protocolo de encriptacion para TCP. Corre sobre TCP.