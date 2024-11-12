---
dg-publish: true
---
Una computador puee hacer tareas complejas con modos de operaciones MUY simples

La componen:

- Unidad arimético-lógica
- I/O
- memoria de instrucciones
- memoria de datos


Todo esto está gestionado por la CPU
![[Pasted image 20231107180202.png]]


### Estructura tipo BUS 
Un sistema de comunicacin de transferencia de datos, un solo cable sale de la PC y este lo comunica con, por ejemplo, todos las posiciones de memoria (indexadas por numero)
![[Pasted image 20231107180626.png]]

Esto, sumada a la arquitectura von neumann![[Pasted image 20240113191233.png]]
el objetivo de este bus es reducir la interconeccion entre el CPU y sus subsistemas. 
No todos los componentes estan contectados de igual manera a los buses, el CPU envia direcciones que son recibidas por la memoria o por el IO, pero nunca va a recibir direcciones. Es por esto que el CPU no tiene las conexiones correspondientes para realizar dicha tarea.
>An important consideration is that the instructions are executed inside of the ALU, even though all of the instructions and data are initially stored in the memory. This means that instructions and data must be loaded from the memory into the ALU registers, and results must be stored back to the memory from the ALU registers


Otro modelo de buses, con buses independientes
![[Pasted image 20231107181939.png]]

RISC utiliza un solo bus, simple y optimizable
![[Pasted image 20231107182204.png]]


