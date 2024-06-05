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
Hay un base and bound para heap, otro para stack y otro para el codigo.
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
la page directory posee 1024 entradas. ![[Pasted image 20240417110821.png]]
- Present (P): Este bit indica si la entrada de la tabla de páginas está presente en la memoria física. Si está establecido (1), la entrada está presente y se puede utilizar para traducir direcciones virtuales. Si está desactivado (0), la entrada no está presente y cualquier intento de acceso a ella causará un fallo de página.
- Read/Write (R/W): Este bit controla si la región de memoria mapeada por esta entrada es de solo lectura (0) o lectura/escritura (1). 
- User/Supervisor (U/S): Este bit determina los privilegios de acceso a la región de memoria mapeada. Si está configurado, la región es accesible en modo usuario y modo supervisor. Si está desactivado, solo es accesible en modo supervisor. 
- Write-through (W/T): Este bit controla la política de escritura en caché para la región de memoria. Si está establecido, las escrituras se realizan a través de la caché. Si está desactivado, las escrituras se pueden realizar directamente en la memoria principal. 
- Cache Disable (C): Este bit se utiliza para desactivar la caché para la región de memoria mapeada. Si está establecido, la caché está desactivada para la región. Si está desactivado, la caché puede utilizarse. 
- Accessed (A): Este bit se establece por hardware cada vez que se accede a la región de memoria mapeada. Es útil para la gestión de la memoria y la optimización de algoritmos de reemplazo de páginas. 
- Dirty (D): Este bit se establece por hardware cada vez que se escribe en la región de memoria mapeada. Indica que la página ha sido modificada desde la última vez que se limpió. 
- Large Page (PS): Si este bit está configurado, indica que la entrada PDE apunta a una tabla de páginas de tamaño grande (4 MB en lugar de 4 KB). Esto se utiliza para el soporte de páginas grandes y puede mejorar el rendimiento en ciertos casos. 
- Global (G): Este bit se utiliza para páginas globales. Si está establecido, la página no se elimina del caché de traducción de direcciones (TLB) cuando se cambia el contexto del proceso. 
- Available(Avail):Estos bits están disponibles para el uso del software y pueden ser utilizados para almacenar información

#### Page table entry
idem. Cada page table ocupa 4 bytes, hay 1024 entries 
![[Pasted image 20240417110922.png]]

# Control Registries

##### `CR0`
El registro CR0 es esencial para inicializar el procesador al arrancar.
Alberga varios flags que controlan operaciones del procesador. Sirve para habilitar y deshabilitar paginacion y modo protegido.
PE: modo protegido (1) modo real (0)
WP: Si está establecido, determina el comportamiento de las paginas de solo lectura en modo supervisor
PG: Habilita la paginacion, si no, el procesador una traduccion de direccion lineal a fisica directa.
> Si el bit mas a la izq del CR0 es 0 determina que la lineal adress se convierte drectamente en physical adress para acceder a la memoria. Si PG esta en 1 la linea adress debe ser convertida en physicial adress a traves del mecanismo de paginacion
![[Pasted image 20240417111204.png]]

#### `CR3`
 contene page directory base que contiene 1024 entradas de 4 bytes cada una. Cada entrada del Page Direc ocupa 4 bytes y direaccona a una page table que contiene 1024 entrads

PDB: contienen al direc base de la tabal de directorios de paginas. La tabla de directorios de páginas es la estructura de datos de nivel superior en el mecanismo de paginación de x86, que a su vez apunta a tablas de páginas individuales.
PCD (Page Level Caché Disable, bit 4): si es 1, la paginacion no se cachea. A veces es ignorado, con las caracteristicas de cacheo determinadas por las entradas individuales de las tablas de paginas.
PWT (Page-Level Write Through, bit 3): Controla las caracteristicas de caching para las tablas de paginas. Si es 1, se utiliza la politica de cacheo Write-Through, sino, se utiliza Write-Back.

Cada vez que se escribe en CR3, la caché de la tabla de búsqueda (TLB) se invalida automáticamente. Esto se debe a que la TLB podría contener entradas antiguas basadas en la antigua estructura de paginación, y al cambiar CR3, estas entradas ya no serían válidas

Los bits que no se usan luego fueron utilizados en versiones mas recientes de x86
![[Pasted image 20240417111217.png]]



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


### TLB
La TLB (translaton lookaside buffer) es la [[7.0 Memoria#Caché|caché]] del MMU (addr translator), guarda cacheada las traducciones de memoria virtual a fisica. Si ya hice la traduccion antes le sumo el offset y me ahorro traducir.
![[Pasted image 20240417120657.png]]
Tiene que ser rapida, es una memoria estatica on chip muy cerca del procesador
Hay implmentaciones con 2 TLB. Pongo Miss en la primera TLB, si no uso alguno por mucho tiempo lo bajo a la TLB2, si no lo uso por mas tiempo se va.

allá le estan espaciando las localidades


>Cada vez que se introduce un cache en el sistema, se necesita considerar la forma de asegurar la consistencia del cache con los datos originales cuando las entradas en el mismo son modificadas. 
>Una TLB no es la excepción. Para una ejecución correcta y segura de un programa, el sistema operativo tiene que asegurarse que cada programa ve su propia memoria y la de nadie más.


- Context switch: Las direcciones virtuales del viejo proceso ya no son más válidas, y no deben ser válidas, para el nuevo proceso.
- Reducción de Permiso: Qué sucede cuando el sistema operativo modifica una entrada en una page table?Normalmente no se provee consistencia por hardware para la TLB; mantener la TLB consistente con la page table es responsabilidad del sistema operativo.
- TLB shutdown: En un sistema multiprocesador cada uno puede tener cacheada una copia de una transacción en su TLB. Por ende, para seguridad y correctitud, cada vez que una entrada en la page table es modificada, la correspondiente entrada en todas las TLB de los procesadores tiene que ser descartada antes que los cambios tomen efecto.