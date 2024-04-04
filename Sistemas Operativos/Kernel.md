> EL usuario puede acceder al kernel, pero se busca limitar siempre la ejecución directa.
> 

Cada vez que el procesador pasa de modo kernel a modo usuario, el kernel antes de irse pone un timer. Despues de ese tiempo el kernel se despierta

IOPL (I/O Privilege Level): son 4 bits que te muestran en que lvl de privilegio estas. 0 es kernel 3 es user. Permite saber si quien tiene en este momento acceso al procesador puede ejecutar determinadas acciones
El IOPL se puede cambiar usando POPF (D) e IRET (D) solo cuando el nivel de privilegio actual es Ring 0.

Además de IOPL, los permisos de puerto de E/S en el TSS (Task State Segment) también participan en la determinación de la capacidad de una tarea para acceder a un puerto de E / S.
![[Pasted image 20240320194817.png]]

> TOdo loq ue corra en modo kernel es seguro, todo lo que corra en mod ousuario es no seguro


## Modo de transferencia 
> como pasar de un modo a otro 

Cada modo ocurre en un entorno por separado

#### User mode ->kernel mode
Mediante syscals, excepciones (division por cero), interrupciones o timer del kernel (la interrupcion 0 es la de que terminó el timer). Estos tres eventos son, respectivamente: externos, generados intencionalmente o internos inesperados
El kernel chequea periodicamente lo que ocurre mientras los programas estan siendo ejecutados, en caso de que tenga que desalojarlo. Esto se hace mediante un mecanista llamado "hardware counter"

Paso a paso de las syscalls: 


1. Llamo al wrapper (una funcion de la lib standar de C que sabe como llamar a la siscall)
2. el wrapper pone todo los args en los registros y copia el número de la system call a un determinado registro de la CPU (%eax).
3. La función _wrapper_ ejecuta una instrucción de código maquina llamada **trap machine instruction** (int 0x80), esta causa que el procesador pase de _user mode_ a _kernel mode_ y ejecute el código apuntado por la dirección 0x80 (128) del vector de traps del sistema.
4. En respuesta al trap de la posición 128, el kernel invoca su propia función llamada _syste_call()_ (arch/i386/entry.s) para manejar esa trap. Este manejador:
    
    1. graba el valor de los registros en el stack del kernel.
        
    2. verifica la validez del numero de system call.
        
    3. invoca el servicio correspondiente a la system call llamada a través del vector de system calls, el servico realiza su tarea y finalmete le devuelve un resultado de estado a la rutina _system_call()_.
        
    4. se restauran los registros almacenado en el stack del kernel y se agrega el valor de retorno en el stack.
        
    
    5. se devuelve el control al wraper y simultáneamente se pasa a user mode.
5. Si el valor de retorno del la rutina de servicio de la system call da error, la función wrapper setea el valor en _errno_
6.  Si el valor de retorno del la rutina de servicio de la system call da error, la función wrapper setea el valor en _errno_.
#### Kernel mode -> user mode
Nuevo proceso
Continuar despues de una interrupcion, una excepcion o una syscall
cambiar entre difernetes procesos

## Booteo
1. **Booteo**: este proceso es denominado bootstrap, y generalmente depende del hardware de la computadora. En el se realizan los chequeos de hardware y se carga el **bootloader**, que es el programa encargado de cargar el Kernel del Sistema Operativo. Este proceso consta de tres partes.
	1. Cargar el BIOS
	2. Crear el Interrupt Vector Table
	3. La BIOS genera una interrupcion de 19 int lo cual hace apuntar a CS:IP 0x0E6F2
	4. esto hace que se ejecute el serivicio de interrupciones, se lee el primero sector de 412 bytes del disco a memoria

1. Carga del kernel: el bootloader pasa a modo supervisor, va a buscar el kernel, lo carga a mameoria, setea el registro en proxima instruccion y ejecuta la primera instruccion del kernel

## Carga del kernel
Se carga desde un archivo zImage, no es un archivo ejecutable normal, está cargado de otra forma.