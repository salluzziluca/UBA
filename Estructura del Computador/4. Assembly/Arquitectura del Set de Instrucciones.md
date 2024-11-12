---
dg-publish: true
---
## Memoria
Hay que tener en cuenta donde se guardan fisicamente las variables, como accedo a los perifericos, donde seguarda fisicamente el programa
==como está organizada la memoria==

La memoria esta organizada en tablas cuyas filas son cada una de 8 bits

| n°  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   |     |     |     |     |     |     |     |     |
| 2   |     |     |     |     |     |     |     |     |
| 3    |     |     |     |     |     |     |     |     |

Hay dos formas de ordenar la informacion
- Little-endian: el byte menos significativo en la direccion mas baja
- Big-endian: el byte menos significativo en la direccion mas alta![[Pasted image 20231203125442.png]]
a) Sus parámetros son interpretados por el ensamblador y reemplazados por lo que corresponda en cada lugar que es invocada la macro. En una subrutina sus parámetros (valores) le llegan en tiempo de su ejecución (pila o registros).

b) Su código de máquina está repetido tantas veces como la macro fue invocada. En una subrutina su código de máquina está localizado en un lugar específico y único en memoria.

c) la velocidad de ejecución con macros es mayor dado que no tiene que pegar salto a otra parte del programa.
## Espacio direccionable
deerminado por el tamaaño del Registro del procesador
$2^n$ con n= tamaño
Luego mediante un mapa de memoria representamos la asignacion del mismo.
el tamaño del espacio direccionable es especifico del procesdor
el mapa de memoria es especifico de un sistema (dos sistemas con el mismo procesador no tienen el mismo mapa de memoria)

# Arqitectura ARC ( A Risc Computer)
Espacio de direcciones: 2^{32}
big endian
![[Pasted image 20231129165743.png]]

### Set de instrucciones
es un subconjunto de SPARC
todas las instrucciones ocupan 32 bits
32 registros de 32 bits
Program Status Register guarda los flags
Solo dos instrucciones acceden a memoria principal (RAM): read and write

## Mapa de memoria
![[Pasted image 20231017165203.png]]
0 hasta 2047 OS
$2048 \ hasta \ (2^{31}-4)$ Memoria de usuario: Memoria ocupada por codigo de maquina y variables.  system stack
$2^{31} \ hasta \ 2^{32}-1$ I/O

>It is important to keep the distinction clear between what is an address and what is data. An address in this example memory is 32 bits wide, and a word is also 32 bits wide, but they are not the same thing. An address is a pointer to a memory location, which holds data. 

## I/O
Los pedidos de lectura y escritura en Arc de un periférico, el procesador envía una orden a la dirección signada del periférico el cual se almacena en el registro de dirección I/O (la segunda mitad de la RAM). La interfaz de controlador de periféricos recibe esta orden y la procesa, buscando el periférico correspondiente en la tabla de dispositivos. Una vez identificado, se realiza la operación correspondiente.

La escritura a un periférico implica enviar información desde el procesador hacia el periférico. Por ejemplo, el procesador puede escribir una dirección en un registro de un periférico para configurarlo o proporcionarle datos para su procesamiento.

La lectura de un periférico implica obtener información del periférico y enviarla al procesador. Por ejemplo, el procesador puede leer el estado de un periférico para determinar su funcionamiento actual o obtener los resultados de un procesamiento previo realizado por el periférico.

La escritura en RAM proceso realizado por el procesador para almacenar información en la memoria RAM para su posterior acceso y uso. La memoria RAM es un componente de almacenamiento temporal y volátil que se utiliza para almacenar datos y programas mientras el sistema está en funcionamiento.
## Algunas instrucciones de ARC 
![[Pasted image 20231017170626.png]]
si  dice `cc` es porque altera los flags
el branch always y el call son conceptualmente diferentes, el `call` se utiliza para una subrutina, guardando la posición actual para luego volver utilizando `jpml` 
Para acceder a memoria, utilizo `ld %rn`, de esa forma le estoy diciendo al programa que acceda a la dirección `rn` en memoria. Es decir, si en `rn` yo tengo un 2030, voy a acceder a la direccion 2030 en memoria
The shift instructions shift the contents of one register into another. The srl (shift right logical) instruction shifts a register to the right, and copies zeros into the leftmost bit(s)

![[Pasted image 20231203125126.png]]
# Registros
![[Pasted image 20231017171718.png]]
El %r15 guarda el registro desde el que llamamos la funcion en la que estamos actualmente. El %r14 la posición de la pila

PSR = Processor State Register 
PC = Program Counter

## Sintaxis
![[Pasted image 20231129171450.png]]
Operands in an assembly language statement are separated by commas, and the destination operand always appears in the rightmost position in the operand field. Thus, the example shown in Figure 4-8 specifies adding registers %r1 and %r2, with the result placed in %r3. If %r0 appears in the destination operand field instead of %r3, the result is discarded. The default base for a numeric operand is 10, so the assembly language statement: 
```asm
lab_1: adcc, %r1, %r2, %r3   !suma r1 y r2, lo guarda en r3
```
hexa-> 0x o terminar con h
bin-> termina con b

## Directivas del ensamblador (pseudo-ops)
le dicen al ensamblador como procesar una sección del programa
lasinstrucciones son especificas de un procesador, las pseudo-instrucciones o directivas son especificas de un programa ensamblador. 
Alguas generan informacion   en la memoria, otras no
![[Pasted image 20231017175405.png]]

## Subrutina
Si tengo que llamar una subrutina adentro de otra, backupeo el r15 cuando arranca la subrutina y lo vuelvo a traer antes del jmpl, siguiendo la convención utilizada ![[Pasted image 20231130084654.png]]
### Por registro
![[Pasted image 20231129174733.png]]
### Por stack
![[Pasted image 20231129174741.png]]
El `r14` tiene la posicion 1 del stack. De ahi cargo el primero del stack en `r1`y avanzo una posicion en el stack, cargando eso en `r2`
## Macro
Es ponerle nombre a un segmento de código. Pero le puedo pasar argumentosw

![[Pasted image 20231130084531.png]]
## Localización de variables
- registros
- Segmento de datos (RAM)
- Stack (RAM)


## Arquitectura del set de instrucciones
Set = Conjunto de instrucciones + registros disponibles

caracteristicas:
- tamaño de instruccionestipo de operaciones admitidas
- tipos de operandos
- tipos de resulttados
- formas de indicar la ubi de los datos = "modos de direccionamiento"

CISC era un modelo de intstruccioes muy complejas ya que habia poca memoria, valia la pena bajar una sola instruccion muy grosa y listo

RISC (reduced instruction set computer) = le doy mas laburo al programador pero las instrucciones son mas faciles

![[Pasted image 20231031173830.png]]


