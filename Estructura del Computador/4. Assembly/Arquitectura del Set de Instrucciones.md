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
0-2047 OS
2048-2^{31}-1 Memoria de usuario: Memoria ocupada por codigo de maquina y variables.  system stack
2^{31}-1 - 2^{32}-1 I/O

de 0 a 2^{31}-1 RAM.


## Algunas instrucciones de ARC 
![[Pasted image 20231017170626.png]]
si  dice `cc` es porque altera los flags
el branch always y el call son conceptualmente diferentes, el `call` se utiliza para una subrutina, guardando la posición actual para luego volver utilizando `jpml` 
Para acceder a memoria, utilizo `ld %rn`, de esa forma le estoy diciendo al programa que acceda a la dirección `rn` en memoria. Es decir, si en `rn` yo tengo un 2030, voy a acceder a la direccion 2030 en memoria

![[Pasted image 20231203125126.png]]
# Registros
![[Pasted image 20231017171718.png]]
El 15 guarda el registro desde el que llamamos la funcion en la que estamos actualmente. El 14 la posición de la pila

## Sintaxis
![[Pasted image 20231129171450.png]]
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

