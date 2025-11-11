---
Dia: 2025-11-06
dg-publish: true
---
Generala topologia de red con switches. 

Cada switch va a tener su propia IP. 

La topologia la creamos en python y despues la levantamos. 

Hay muchos ejemplos de tipos de topologia y se piden mchos requisitos. 

Se nos va a pedir una con unhost en cada extremo y n switches variables en el medio. 

Una vez que esta la topologia hay que configurar un controlador open flow. 

La SDN que armemos le vamos a setear reglas. Le vamos a armar un firewall. 


Configurar unswitch de esa topologia (elegir y explicar cual y por que).

Le vamos a teener que implementar las siguientes reglas 


Se deben descartar todos los mensajes cuyo puerto de destino sea 80. CUALQUIER TIPO DE PAQUETE QUE LLEGUE A ESE PUERTO. No importa si no es HTTP

Se debe descartar todos los mensajes que vengan del host 1, tengan puerto de destino 5001 y qu eesten utilizando udp


se deben elegir dos hosts cualquier y los mismos no deben poder comunicarse de ninguna forma


que el firewall NO sea el controlador. JAMAS


Si el switch no sabe que hacer con ese paquete, se lo envia al controlador 



ARRANCAR POR LA TOPOLOGIA, DE AHI IR A LAS INTERFACES Y POR ULTIMO EL FIREWALL




mininet> h2 python3 -m http.server 80 &
mininet> h1 curl http://10.0.0.2:80


mininet> h2 iperf -s -u -p 5001 &
mininet> h1 iperf -c 10.0.0.2 -u -p 5001 -t 5


mininet> h1 ping -c 3 10.0.0.3
