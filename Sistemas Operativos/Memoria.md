---
materia: Sistemas Operativos
capitulo: 
dia: 2024-03-04
---

La memoria tal y como la veia en [[Manejo de Memoria|algo2]] o en [[7.0 Memoria|estructura]] (un arreglo de reicciones de memoria una detrás de la otra) es manejable mientras la cantidad de memoria necesitada sea acotada.

Cuando se empezó a laburar cantidades mucho mas grandes de memoria, se necesitaron otros recursos. 


## Multiprograming 
El SO ejecuta una parte de un prograama, luego una parte de otro, luego una parte del tercero, vuelve al primero, and so on. Realmente no se corren programas en paralelo, solo se da la ilusion
![[Pasted image 20240416104001.png]]

## Time Sharing
Diferentes usuarios comparten de forma concurrente un recurso computacional (CPU, memoria, etc.) mediante multiprogramacion e interrupciones de reloj por parte del SO


## Virtualización de Memoria

La memoria virtual es agarrar a memoria fisica (fea y desordenada y mediante un software (mmu), simplificar todo para el [[Proceso]].  El mmu está adentro del cpu (`registro satp: <tabla_A>`)
Cuando activas la memoria virtual, el procesador ya no puede ver mas la memoria fisica. Para él solo existe la virtual
Es literalmente una funcion matetmática
El mmu tambien puede dar aclaraciones sobre diferentes direccines de memoria

Tiene que ser eficiente, no se puede permitir que los programas requieran mas lentos o requieran mas espacio.

El sistema operativo tiene que asegurarse de proteger a los procesos unos de otros como también proteger al sistema operativo de los proceso

El [[ Proceso]] tiene un user thread, si cambio de proceso, elnuevo proceso va a tener ese mismo user thread, se lovan a pasar

![[context switch]]

### Adress Translatiion
Transforma la virtual addres en su equivalente en la mem fisica. 
Formalmente, es un mapeo
![[Pasted image 20240416112800.png]]
#### Base and Bound (segmentacion)
Para implementar este tipo de addres tanslation solo se necesitan dos registros: Registro base y registro bound (limite o segmento).
Esto permite que el addres sea ubica en cualquier lugar de la memoria fisica.
![[Pasted image 20240416113147.png]]
##### implementacion en x86
AX, BX, CX, DX : Registros Generales 
CS, DS, SS, ES : Registros de Segmentos, manejan la traducción en modo real.( Code Segment, Data Segment, Extra Data Segment) 
SI, DI, BP, SP, IP: Registros de Punteros y Registro de Índices. (Base Pointer, Stack Pointer y Instruction Pointer

CS:IP localiza la próxima instrucción a ser ejecutada en modo real. 
SS:SP localiza la dirección del puntero al stack, a veces también puede ser SS:BP. 
DS: BX,DI,SI localizan el puntero a una dirección de memoria dentro del data address. 
ES:DI puntero al extra data address donde van los strings.
![[Pasted image 20240416113542.png]]

#### Tabla de Segmentos
==Cuando se necesita mas memoria, se alarga el chunk de memoria que se le da a ese proceso en particular==
EL problema con base and bound qes que se tiene solo un reg base y un reg segmento. La esolucion es que cada proceso tenga asignado un base and bound. 
El número de segmento es el índice de la tabla para ubicar el inicio del segmento en la memoria física. El registro bound es chequeado contra la suma del registro base+offset para prevenir que el proceso lea o escriba fuera de su región de memoria.

> los bit de más alto orden son utilizados como índice en la tabla de segmentos. El resto se toma como offset y es sumado al registro base y comparado contra el registro bound. El número de segmentos depende de la cantidad de bits que se utilizan como indice



==El error de Segmentation Fault era un error que se daba cuando, en las máquinas que implementan segmentación, se quería direccionar una posición fuera del espacio direccionable.==

![[Pasted image 20240416113950.png]]


#### Memoria Paginada
==cuando se necesita mas memoria, se le dan 1 o más paginas (de mt==