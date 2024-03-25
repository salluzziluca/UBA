 La **programacion concurrente** es cuando difernetes partes de nuestro programa se ejecutan independientemente.
 La **programacion paralela** es cuando diferentes partes del programa se ejecutan exactamente al mismo tiempo
 ![[Pasted image 20240325201847.png]]
Se utiliza la concurrencia porque la ley de moore quedo obsoleta y es mejor este metodo, ya que se puede explotar el multi core system. Es un tipo de programacion que sirve mucho para gestionar servidores que reciben solicitudes que distintos clientes (APIs??)


Un programa concurrente consiste en un conjunto finitoi de procesos secuenciales. Estos procesos estan compuestos por a su vez un conjunto de instrucciones finitas atomicas
Ejecución del programa concurrente: resulta al ejecutar una secuencia de instrucciones atómicas que se obtiene de intercalar arbitrariamente las instrucciones atómicas de los procesos que lo componen. 
- El intercalamiento es arbitrario ya que quién decide qué proceso se va a estar ejecutando en un instante de tiempo es el SO. 
- El módulo del SO se denomina scheduler. I Existen distintos algoritmos y políticas de scheduling. 
- Cada vez que el SO cambia el proceso en ejecución, ocurre un context-switch.

La concurrencia necesita de **sincronizacion** y **comunicacion**, ya que el orden en el que se ejecutan los procesos es inconsistente. La salida NO es derministica porque dependen del orden de ejecucion de las instrucciones de los procesos (interleaving) 

Deadlocks: dos hilos en ejecución estan esperando el uno al otro para avanzar, requieren un recurso que el otro tiene. Esto previene que ambos avancen. No progresa el programa. Aparte, son bugs dificiles de reproducir 


## proceso
- Programa: instrucciones que conforman el programa
- Datos del usuario: Espacio de mem modificable por el ususario (datos, heap)
- Stack del sistema
- Estructruas de datos del kernel (PCB)
	En el PCB se almacena: 
	- El PID, el PID del padre, ID del usuario y del grupo. 
	- Datos del estado del proceso: permite suspender y retomar el proceso I Registros de propósito general de la CPU I Stack pointer I Instruction pointer I Datos de control del proceso I Estado del proceso y otra información de scheduling (p.ej. prioridad) I 
	- Estructura del proceso: identificadores de los hijos I Datos de IPC (señales, mensajes) I Contadores de tiempo de uso de CPU

==un proceso es una instancia de un programa en ejecución"