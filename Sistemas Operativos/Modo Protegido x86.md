---
dg-publish: true
---

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
El modo protegido permite direccionar a datos y programas más allá de 1 Mb de memoria física, así como también dentro del primer mega de memoria física.

### Global Descriptor Table (GDT):  
tabla guardada en memoria, apuntada por  el regstro GDTR. Una por todo el sistema, siempre accesible. Kernel y mem compartida

### Local Descriptor table; LDT
una por tarea, programa o proceso. Solo una activa por vez

### Segment Selector:
Indice en la GDT que apunta a un segment desc. Cada tabla tiene 8192 entradas

### Segment desc


Cuand tiene un segment o va y agarra los primeros 13 bits. Se fija ell TI (tipo de tabla) y los privilegios que se necesitan.



## 80386 Segmetn Descriptor
![[Pasted image 20240417115116.png]]
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
