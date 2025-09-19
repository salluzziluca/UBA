---
Dia: 2025-09-19
dg-publish: true
---

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


Las colas de entrada se pueden leer mediante [[Scheduling#Round Robin(RR)|Roudn Robin]], [[Scheduling#Cola FIFO|FIFO]] o colas de prioridad. Tambien se le puede dar un tiempo no aleatorio de procesamiento asegurado. Es decir en un tiempo total t todas las colas de los puertos van a haber recibido un total de cputotal/cant

## Control plane 
Como vialidad nacional que pinta los carteles en las rutas nacionales.