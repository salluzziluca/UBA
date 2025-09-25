---
Dia: 2025-09-19
dg-publish: true
aliases:
  - Routers
  - Router
  - router
  - routers
---

Un router es como una rotonda, tiene diferentes salidas. Para ver por donde salir uno mira los carteles se orienta 

Un router tiene un tiempo de procesamiento. Un router tiene una queue. 

Hay un tiempo de espera, el tiempo del buffer o de encolado. Depende de la cantidad de paquetes que hay en el buffer. 

Una vez que el paquete entra al router tiene que mirar para que lado va, ese es el tiempo de procesamiento. 

Una vez que ya se sabe la salida, el enlace, se tarda un tiempo entre que el paquete se termino de procesar y entra en el enlace. Ese es el tiempo de insercion

Luego esta el tiempo de propagacion. Lo que tarda en viajar.
## Data plane
que dbee hacer cada paquete para encontrar su destino

utiliza la
### Tabla de routeo 

| Prefijo   | Next Hoṕ   |
| --------- | ---------- |
| x.x.x.x/4 | a donde ir |
s

El paquete entra por el input port, pasa por la switch fabric que mapea a donde tiene que mandarlo y sale por el output correspondiente. Esto es [[Network layer#Forward|forwarding]]
![[Pasted image 20250919201347.png]]

Puede haber congestion si dos paquetes tienen que ir al mismo output. se genera un HOL blocking (paquetes rojos)


Llega un paquete al router. Este mira el hash, si da nula se lo tira al routing processor. Este hace el [[Network layer#Routing|routing]] y una vez que tiene el resultado escribe en la funcion de hash que para esta IP tenes que ir a la salida x. De ahi en mas la proxima que llegue esa IP ya conocida directamente se hace [[Network layer#Forward|forwarding]]

![[Pasted image 20250919202727.png]]


Las colas de entrada se pueden leer mediante [[Scheduling#Round Robin(RR)|Roudn Robin]], [[Scheduling#Cola FIFO|FIFO]] o colas de prioridad. Tambien se le puede dar un tiempo no aleatorio de procesamiento asegurado. Es decir en un tiempo total t todas las colas de los puertos van a haber recibido un total de cputotal/cant_input_ports de CPU.

Si esta mal mapeado y se queda dando vueltas entre routers eventualmente muere por el TTL (ver [[IPv4]])

Se busca minimizar el routeo 

### Congestion
La idea es que antes de que se congestione la red se maten paquetes aleatorios de cada uno de los buffers y se nevien a esos respectivos usuarios un mensaje avisando sobre congestion de red. De esa forma todas las colas se libera un poco y los usuarios son avisados.

## Control plane 
Como vialidad nacional que pinta los carteles en las rutas nacionales. 

Es quien escribe la tabla de routeo