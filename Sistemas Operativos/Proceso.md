>“Un proceso es **la ejecución de un programa** de aplicación con derechos restringidos; el proceso **es la abstracción** que provee el [[Kernel]] del sistema operativo para la ejecución protegida”- [DAH]

>“Es **simplemente** un programa que se está ejecutando en un instante dado” - [ARP]

>“Un Proceso **es la instancia de un programa en ejecución**” - [VAH]

>“Un proceso **es un programa en medio de su ejecución**” - [LOV]

==UN PROCESO ES SOLAMENTE UN PROGRAMA EN EJECUCIÓN"

Un proceso incluye: 
- Los [[archivos]] abiertos
- Las selañes pendientes
- datos internos del [[kernel]]
- el estado completo del procesador 
- un espacio de direcciones de memoria 
- uno o mas hilos de ejecución. Cada thread contiene:
	- Un unico program counter 
	- Un stack 
	- Un conjunto de registros
- Una seccion de datos globales


## Estados de un Proceso 

En una visión simplificada un proceso puede encontrarse en los siguientes estados:

- **Corriendo (Running)**: el proceso se encuentra corriendo en un procesador. Está ejecutando instrucciones.
    
- **Listo (Ready)**: en este estado el proceso está listo para correr pero por algún motivo el SO ha decidido no ejecutarlo por el momento.
    
- **Bloqueado (Blocked)**: en este estado el proceso ha ejecutado algún tipo de operación que hace que éste no esté listo para ejecutarse hasta que algún evento suceda.


#### 1. **Corriendo User Mode(Running User Mode)**: El proceso se encuentra corriendo en un procesador. Está ejecutando instrucciones.
    
2. **Corriendo kernel Mode(Running Kernel Mode)**: d
    
3. **Listo para Corre en Memoria (Ready to Run on Memory)**: En este estado el proceso está listo para correr pero por algún motivo el SO ha decidido no ejecutarlo por el momento.
    
4. **Durmiendo en Memoria (Asleep In Memory)** : El proceso está bloqueado en memoria.
    
5. **Listo para Correr pero Swapeado (Ready to Run but wapped)**: El proceso está bloqueado en memoria secundaria.
    
6. **Durmiendo en Memoria Secundaria (Asleep Swapped)**: El proceso se encuentra bloqueado en memoria secundaria.
    
7. **Preempt(Preempt)**: Es igual a 1 pero un proceso que pasó antes por Kernel mode solo puede pasar a preentive.
    
8. **Creado (Created)**: El proceso está recién creado y en un estado de transición.
    
9. **Zombie (Zombie)**: El proceso ejecutó la S.C. exit(), ya no existe más, lo único que queda es el exit state.