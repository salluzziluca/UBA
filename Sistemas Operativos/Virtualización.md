---
dg-publish: true
---
> Crear una **abstracción** que haga que un **dispositivo de hardware** sea mucho más **fácil de utilizar**.

Los sitemas operativos modernos proporncionan dos tipos de virtualizacion:

- Virtualizacion de memoria
- Virtualizacion de Procesador 

## Virtualizacion de Memoria
Le hace creer al [[proceso]] que tiene toda la memoria disponible para ser reservada y usada como si él solo estuviera usando la computadora(ilusion). Todos los procesos en [[Linux]] estan divididos en 4 segmentos:

- Text: Instrucciones del Programa 
- Data: Variables Globales (extern y static en C)
- Heap: Memoria dinamica alocable 
- Stack: Variables Locales y trace de las llamadas

![[Pasted image 20240405152008.png]]

Para ejecutar el programa, el SO: 
1. Copia ls instrucciones en la seccion .code y los datos en la seccion .data. 
2. El SO setea una region de memoria llamada execution stack (.stack) que mantiene el estado de las varibles locales durante las llamadas a los procedimientos.
3. El SO tambien setea una region de memoria llamada heap, destinada a alojar cualquier estructura de datos alocada en forma dinamica que el programa pueda necesitar.


### Proteccion de Memoria
Para que un prceso se ejecute, tanto él como el SO tiene que estar en memoria. El SO para iniciar la ejecución, manejar las interrupciones y/o atender syscalls. 
El SO, cuando hay varios procesos en memoria, tiene que preocuparse por que cada uno pueda escribir solamente en su propia memoria (no la del SO ni la de otros procesos).  Para ello el Hardware debe proveer un mecanismo de protección de memoria.

Uno de estos mecanismos es denominado Memoria Virtual. La memoria virtual es una **asbtracción** por al cual la **memoria física** puede ser compartida por diversos procesos.

Un componente clave de la memoria virtual son las **direcciones virtuales**, con las direcciones virtuales, para cada [[proceso]] su memoria inicia en el mismo lugar, la dirección 0.

Cada [[proceso]] piensa que tiene toda la memoria de la computadora para si mismo, si bien obviamente esto en la realidad no sucede. El hardware traduce la dirección virtual a una dirección física de memoria.


### Traduccion de Direcciones 
Se traduce una **Dirección Virtual** (emitida por la CPU) en una **Dirección Física** (la memoria). Este mapeo se realiza por hardware, más específicamente por **Memory Management Unit (MMU)**.


## Virtualizacion de Procesador 
Consiste en dar la ilusión de la existencia de un único procesador par cualquier programa que requiera de su uso. 

Simplicidad en la programación:
- Cada [[proceso]] cree que tiene toda la cpu
- Cada [[proceso]] cree que todos los dispositivos le pertenecen 
- Distintos dispositivos parecen tener el mismo nivel de interfaces 
- Las interfaces con los dispositivos son mas potents que el bare metal

Aislamiento frente a fallas: 
- Los procesos no pueden directamente afectar a otros procesos
- Los errores no colapsan a toda la maquina

Como se provee esta ilusion??

![[Pasted image 20240405154215.png]]


## Procesos dentro del SO 
Un [[proceso]] necesita permisos del [[kernel]] para: 
- Acceder a memoria perteneciente a otro [[proceso]] 
- Leer o escribir en el disco 
- cambiar algun seteo de hardware del equipo 
- enviar info a otro [[proceso]] 

Para esto utiliza la API de procesos 

### API de procesos 
1. Create:  todo SO debe incluir la forma de crear un nuevo [[proceso]] 
2. Destruccion: Para destruirlo por la fuerza 
3. Wait: esperar a que el [[proceso]] termine la ejecucion 
4.  **Control Vario (Miscellaneous Control)**: Además de esperar o matar a un [[proceso]] **otros tipos de operaciones** deben poder realizarse. Por ejemplo, suspender su ejecución por un tiempo y luego reanudarla.
5. Status: una forma de saber sobre la situacion del [[proceso]] 

#### API de procesos de UNIX-like, las system calls.
 Un proceso en unix sólo puede ser creado por otro proceso
 En unix, el contexto de un proceso está dado por la union de user level context (text, data, stack, heap), registar context:
 1.  Program counter
 2. Registro de estado del procesador 
 3. stack pointer 
 4. general purpose register 
  y system level context: 
  1. emtrada en la Process Table Entry 
  2. La user area
  3. La Process Region Entry, region table y page table que definen el mapeo de la memoria virtual vs fisica del proceso. 


###### User Area contains :
- La Process Control Block - guarda el hardware context cuando el proceso no se esta ejecutando
- Un puntero a la proc structure del proceso
- El UID y GID real
- Argumentos para, y valores de retorno o errores hacia, la system call actual
- Manejadores de Señales
- Información sobre las areas de memoria text,data, stack, heap y otra información.
- La tabla de descriptores de archivos abiertos (Open File dscriptor Table).
- Un puntero al directorio actual
- Datos estadísticos del uso de la cpu, información de perfilado, uso de disco y limites de recursos.

###### Estructura Proc: 
- Identificación: cada proceso tiene un identificador único o _process ID_ (PID) y ademas perteneces a un determinado grupo de procesos.
- Ubicación del mapa de direcciones del Kerner del u area del proceso.
- Estado actual del proceso
- Un puntero hacia el siguiente proceso en el planificador y al anterior.
- Prioridad
- Información para el manejo de señales.
- Información para la administración de memoria.

## API de UNIX resumida
1. **[[fork()]]**: Crea un proceso y devuelve su id.
2. **[[exit()]]**: Termina el proceso actual.
3. **[[wait()]]**: Espera por un proceso hijo.
4. **kill(pid)**: Termina el proceso cuyo pid es el parámetro.
5. **getpid()**: Devuelve el pid del proceso actual.
6. **[[exec(filename, argv)]])**: Carga un archivo y lo ejecuta.
7. **[[sbrk(n)]]**: Crece la memoria del proceso en n bytes.


## Metamorfosis, de programa a proceso
1. El SO carga el programa, su codigo y cualqueri dato estatico en la memoria (antes de form aeagerly, todo junto, ahora lazily, cuando se lo necesita)
2. Se crea la pila (stack) reservando cierta cantidad de memoria.
3. Se crea el heap reservando otra cierta cantidad de memoria, este sirve para la memorai dinamica (malloc y free)
4. El SO realiza otras opreaciones, relacionados con la entrada y salida de datos (std in, std out, std err, etc)
5.  Una vez que todo lo anterior sucedió, un última cosa sucede, se setea el punto de entrada (entry point) de ejecución de las instrucciones del programa en el main().



## Gestion de Procesos del Kernel 
El kernel almacena la lista de procesos mediante una lista circular doblemente enlazada llamada task list
![[Pasted image 20240405174018.png]]
Cada elemento de la task list es un descriptor de proceso (_process descriptor_) del tipo task_struct, definida en in `<linux/sched.h>`
![[Pasted image 20240405174757.png]]
Esta estructura es relativamente pesada, unos 1.7 Kb en 32-bit [^7]_.

Los procesos se identifican en linux al igual que en unix via el PID (_process identification_), este es un valor numérico de 0 a 32768, si bien este puede ser cambiado (<linux/threads.h>) hasta 4 millones. Puede verse ejecutando >$ cat /proc/sys/kernel/pid_max.

Normalmente, se asignan a partir del número 500.

..[^1]: Algo estático, sin vida. ..[^3]:cuando se ejecuta un comando en el shell o se hace doble click en un icono de una aplicación este comando debe ser ejecutado ..[^4]: Si bien la mayoria de los procesos se inician y se destruyen por sí mismo ..[^2]: ¿Qué se guarda en el heap y en el stack? .. [^4]: espacio de usuario. .. [^5]: En x86, el tamaño de la pila es configurable en tiempo de compilación y puede ser de 4 KB u 8 KB. .. [^6]: Symmetrical Multiprocessing .. [^7]: Bastante pequeña si se considera que possee todos los datos requeridos por el kernel sobre un proceso