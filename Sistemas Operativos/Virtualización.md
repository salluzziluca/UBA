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

Un componente clave de la memoria virtual son las **direcciones virtuales**, con las direcciones virtuales, para cada proceso su memoria inicia en el mismo lugar, la dirección 0.

Cada proceso piensa que tiene toda la memoria de la computadora para si mismo, si bien obviamente esto en la realidad no sucede. El hardware traduce la dirección virtual a una dirección física de memoria.


### Traduccion de Direcciones 
Se traduce una **Dirección Virtual** (emitida por la CPU) en una **Dirección Física** (la memoria). Este mapeo se realiza por hardware, más específicamente por **Memory Management Unit (MMU)**.


## Virtualizacion de Procesador 
Consiste en dar la ilusión de la existencia de un único procesador par cualquier programa que requiera de su uso. 

Simplicidad en la programación:
- Cada proceso cree que tiene toda la cpu
- Cada proceso cree que todos los dispositivos le pertenecen 
- Distintos dispositivos parecen tener el mismo nivel de interfaces 
- Las interfaces con los dispositivos son mas potents que el bare metal

Aislamiento frente a fallas: 
- Los procesos no pueden directamente afectar a otros procesos
- Los errores no colapsan a toda la maquina

Como se provee esta ilusion??

![[Pasted image 20240405154215.png]]


## Procesos dentro del SO 
Un proceso necesita permisos del kernel para: 
- Acceder a memoria perteneciente a otro proceso 
- Leer o escribir en el disco 
- cambiar algun seteo de hardware del equipo 
- enviar info a otro proceso 
