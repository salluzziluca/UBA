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

El paquete entra por el input port, pasa por la switch fabric que mapea a donde tiene que mandarlo y sale por el output correspondiente.
![[Pasted image 20250919201347.png]]

Puede haber congestion si dos paquetes tienen que ir al mismo output. se genera un HOL blocking (paquetes rojos)


Llega un paquete al router. Este mira el hash, si da nula se lo tira al routing processor. Este hace el routing y una vez que tiene el resultado escribe en la funcion de hash que para esta IP tenes que ir a la salida x

![[Pasted image 20250919202727.png]]

## Control plane 
Como vialidad nacional que pinta los carteles en las rutas nacionales.