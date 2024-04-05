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

Uno de estos mecanismos es denominado Memoria Virtual. L la memoria virtual es una **asbtracción** por al cual la **memoria física** puede ser compartida por diversos procesos.