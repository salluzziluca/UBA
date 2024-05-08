## Workload
> La carga de un trabajo de un proceso corriendo en e sistema

Determinar como calcular el workload es fundamental para determinar partes de las politicas de planificacion. A mejor calculo, mejor politica.

Suposiciones (irreales):
- cada prceso tarda la misma cantidad de tiempoo
- todos los jobs llegan al mismo tiempo
- una vez que empieza el ob sigue hasta completarse
- usan solo cpu
- el runtime es conocido


## Tipos de Politicas

### [[Cola|FIFO]]
![[Pasted image 20240417201213.png]]
Time Around  = $\frac{10+20+30}{3}=30$
#### Ventajas
Facil de implementar
Simple 
Funciona bien para suposiciones iniciales

#### Desventajas
![[Pasted image 20240417201407.png]]

### Shortest Job First (SJF)
Se ejecuta primero el mas corto
$T_{around}=\frac{{10+20+130}}{3}=50$
Pero si llega primero el A, pasa lo mismo que arriba

### Shortest Time to Completitin
Si llega un programa cortito corta el actual y despues lo continua
![[Pasted image 20240417201826.png]]
$T_{arround}=\frac{{120−0+20−10+30−10}}{3}=50$

## Response Time 
El tiempo de respuesta o response time surge con el advenimiento del **time-sharing** ya que los usuarios se sientan en una terminal de una computadora y pretenden una interacción con rapidez. Por eso nace el **response time** como métrica:
$T_{response}= T_{firstrun} - T_{arrival}$
![[Pasted image 20240417202437.png]]

### Round Robin(RR)
Se ejecuta un proceso por una slice de tiempo, cambia al proximo, cambia al proximo, etc

![[Pasted image 20240417202552.png]]

Si el time slice es muy chikito, pierdo mucho recursos en el context switch


## Multi Level Feedback Queue (MLFQ)
Intenta optimizar el turnaround time, se intenta ejecutar la tarea mas corta primero. MLFQ intenta que el planificador haga sentir al sistema con un tiempo de respuesta interactivo para los usuarios por ende minimizar el ***response time***

### Problemas
No se sabe nada sobre el proceso, mucho menos cuanto va a tardar
Hay muchas queues de diferente prioridad, todas corren en [[Scheduling#Round Robin(RR)]]

### Starvation
1.  **Starvation** : Si hay demasiadas tareas interactivas en el sistema se van a combinar para consumir todo el tiempo del CPU y las tareas de larga duración nunca se van a ejecutar.
    
2.  Un usuario inteligente podría reescribir sus programas para obtener mas tiempo de CPU por ejemplo: Antes de que termine el time slice se realiza una operación de entrada y salida entonces se va a relegar el uso de CPU haciendo esto se va a mantener la tarea en la misma cola de prioridad. Entonces la tarea puede monopolizar toda el tiempo de CPU.
Para esto se crea la regla 5

Con esto se logran dos cosas
1.  Se garantiza que los procesos no se van a starve: Al ubicarse en la cola tope con las otras tareas de alta prioridad estos se van a ejecutar utilizando **round-robin** y por ende en algún momento recibirá atención.
    
2.  si un proceso que consume CPU se transforma en interactivo el planificador lo tratara como tal una vez que haya recibido el boost de prioridad.
![[Pasted image 20240417205204.png]]
### Reglas
-   **REGLA 1**: si la prioridad (A) **es mayor** que la prioridad de (B), (A) se ejecuta y (B) no.
    
-   **REGLA 2**: si la prioridad de (A) **es igual** a la prioridad de (B), (A) y (B)se ejecutan en _Round-Robin_.
    
-   **REGLA 3**: Cuando una tarea entra en el sistema se pone con la mas alta prioridad
    
-   **Regla 4**: Una vez que una tarea usa su asignación de tiempo en un nivel dado (independientemente de cuantas veces haya renunciado al uso de la CPU) su prioridad se reduce: ( Por ejemplo baja un nivel en la cola de prioridad).
    
-   **Regla 5**: Después de cierto periodo de tiempo **S**, se mueven las tareas a la cola con mas prioridad.


## linux
Un buen planificador tiene que tender a no tardar tiempo en decidir quien sigue, esa decision tiene que tardar el menor tiempo posible. Tiene que tener bajar la [[Complejidad de Algoritmos|complejidad algoritmica]] 
En Linux 1.2 Se utilizaba una cola circular con round robin
en linux 2.2 se introduce las scheduling cvlasses (real-time, non-real-time)
en linux 2.4 se crea el O(N) scheduler
Entre el linux 2.5 y el 2.6 se rehizo de cero el scheduler, volviendolo [[Complejidad de Algoritmos|O(1)]]. Su nombre es 
### Completely Fair Scheduler
Diseñado por Ingo Molnar. Este shceduler está basado en el concepto de planificacion proporcional (fair scheduling). Donde se intenta dar a cada proceso una cantidad de tiempo de CPU proporcional a su prioridad. CFS utiliza una estructura de datos de tipo [[Arbol Rojo Negro|arbol rojo negro]]. 

**Equidad**: El CFS busca ofrecer a cad aproceso una porcion justa de CPU. No se asignan time slices, sino que que se les da una porcion de tiempo de CPU proporcional a su peso de prioridad
**Virtual Runtime:** cada proceso tiene asociado un contador llamad vrtuntime, que representa la cantidad de tiempo que el proceso lleva ejecutandose. Los que tienen menos vruntine son los que tienen mayor prioridad para ser ejecutados. 
$$vruntine +=\frac{delta\_{exec}}{weight}\times load\_weight$$
**Pesos de Prioridad**: Los procesos de linux pueden tener diferentes proridades, que en el CPS implica pesos. Un peso mas alto implica mayor prioridad


Cada task_struct tiene un struct de sched_identity ( con todo lo de la task referida al sched).
Dentro de ese sched_identity struct hay un puntero a un nodo del [[Arbol Rojo-Negro]].

