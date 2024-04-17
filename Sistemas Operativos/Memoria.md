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
==cuando se necesita mas memoria, se le dan 1 o más paginas (de tamaño fijo) al proceso==

En vez de tener una página de segmentos cuyas entradas contienen punteros a segmentos, hay una tabla de páginas por cada proceso cuyas entradas contienen punteros a las page frames
las entradas en la page table sólo tienen que proveer los bit superiores de la dirección de la page frame. De esta forma van a ser más compactos. No es necesario tener un límite; la página entera se reserva como una unidad

El numero de la pagina virtual es el indice en la page table para obtener el page fram en la memoria fisica.

La direc fisica es la direc fisica del page frame  + el offset de la pagina que se obtiene de la virtual address.

En la mem fisica las paginas no son lineales, la memoria está desparramada

![[Pasted image 20240416115118.png]]

### Memoria paginada en x86
![[Pasted image 20240417105732.png]]
Page Directory entry bits 31-22 (10 bits) apunta al page directory 
Page Table Entry bits 21-12 (10 bits) apunte al page table
Memory Page offset address bits 11-0 (12 bits) apunta a la physical address

![[Pasted image 20240417105805.png]]
#### Page directory entry

Entrada a la page directory, ocupa 4 bytes
la page directory posee 1024 entradas. 

# Control REgistrys
CR0: Si el bit mas a la izq del CR0 es 0 determina que la lineal adress se convierte drectamente en physical adress para acceder a la memria. Si PG esta en 1 la linea adress debe ser convertida en physicial adress a traves del mecanismo de paginacion

CR3 contine page directory base que contiene 1024 entradas de 4 bytes cada una. Cada entrada del Page Direc ocupa 4 bytes y direaccona au na page table que contiene 1024 entrads


#### X86
La arquiterctura 8086 tien un bus d datos de 20 bits, los regs tienenuna long de 16 bits.
Generales: AX BX CX DX

De Segmento: CS (code segment), DS(data segment), SS (Stack segment), y ES (Extra data segment)

CS:IP localiza la prox instruccion
SS:SP localiza la direc del puntero al stack
DS:BX DI, SI localiza el puntero a una direccio  de memoria dentro del data adress
ES:DI ountero a extra data adress ddonde van los strings


1) Shift 4 left = R
2) Sumamos R con offset y obtenemos la direccion de la mem  fisica
Asi se virtualizaba antes de los 80

# MODO protegido x86
empezo en 80286
Un modo que se hizo despues, permite la proteccion de memoria,
Aumentaron el bus de memoria a 32 bits


### Global Descriptor Table (GDT):  
tabla guardada en memoria, apuntada por  el regstro GDTR. Una por todo el sistema, siempre accesible. Kernel y mem compartida

### Local Descriptor table; LDT
una por tarea, programa o proceso. Solo una activa por vez

### Segment Selector:
Indice en la GDT que apunta a un segment desc. Cada tabla tiene 8192 entradas

### Segment desc


Cuand tiene un segment o va y agarra los primeros 13 bits. Se fija ell TI (tipo de tabla) y los privilegios que se necesitan.



## 80386 Segmetn Descriptor
A es el accesed bits
R es el readable bits
C (bit 46) depende de X, si X = 1 C tiene el conforming bit, SI C es 0 solo codigo con el mismo privilege que el DPL puede saltar ahi. Si es 1 codigo con igua o menor privilegio que el DPL puede saltar ahi.
Si X = 0, C es el direction bit. SI C es 0, el segmnto crece hacaia arriba, si es 1 crece hacia abajo.
si X = 1 el segmento es code segment
si es 0 el segmento es data segment 
S es el sgment typbe bit 
DPL esel descritor privilege lvl
P present bit
D deafault operand size
G es granularity bt
Bit 1 is not used by hardware

![[Pasted image 20240410191946.png]]



==Con la misma cantidad de registros pudimos redireccionad 4gb==


---
SI tengo un arreglo de 10 elementos, por cada elemento del array accedo a page directory, page table y al elemento del arrglo. Accedo 3 veces a memoria por elemento 



## Efficent addres translation. 
Este nuevo mecanismo usará un caché (o escondrijo),
que consiste en una copia de ciertos datos que pueden
ser accedidos más de una vez más rápidamente.
El concepto de Cache es ampliamente utilizado en
muchas ramas de las ciencias de la computación:
arquitectura de computadoras, sistemas operativos,
sistemas distribuidos

![[Pasted image 20240410202038.png]]

Hay memoria que está dentro de los cores. Cuando tomo los datos de la memoria por primera vez me dejo los datos relacionados a lo que pedi en la caché por un tiempo

![[Pasted image 20240410202423.png]]

La TLB (translaton lookaside buffer) es la caché del MMU (addr translator), guarda cacheada las traducciones de memoria virtual a fisica. Si ya hice la traduccion antes le sumo el offset y me ahorro traducir.


Hay implmentaciones con 2 TLB. Pongo Miss en la primera TLB, si no uso alguno por mucho tiempo lo bajo a la TLB2, si no lo uso por mas tiempo se va.

allá le estan espaciando las localidades