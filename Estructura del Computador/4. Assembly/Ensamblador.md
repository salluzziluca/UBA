---
dg-publish: true
---
Su laburo es mucho más sencilo que el del compilador, es menos complejo
![[Pasted image 20231130090922.png]]

Proceso de ensamblado en 2 pasadas:
1. Detecta identificadores y les asigna una posicion de memoria. Crea la ==tabla de simbolos==, en la cual se registran todos los simbolos que se necesitan para ejecutar el programa
2. Cada instrucción es convertida a código de maquina. Cada identificador es reemplazado por su ubicación en memoria (usando la tabla de símbolos). Cada linea es procesada completamente antes de avanzar a la sig.  Genera el código obj y el listado

##  Opcode
![[Pasted image 20240113210618.png]]
Es, basicamente, la forma en la que se pasan a lenguaje de máquina las [[Arquitectura del Set de Instrucciones#Algunas instrucciones de ARC|instrucciones de ARC]] 

![[Pasted image 20231130090949.png]]
# Linker 
> combina dos o más modulos que fueron ensamblados separadamente
## Relocalizacion
Si yo tengo más de un modulo (ej main y pepe), aunque ambos digan `org 2048` el assembler, mediante el linker, va a desplazar a pepe, a relocalizarlo, a otra direccion de memoria, generando una tabla de valores de 2048+n 
de esa forma crea el paquete con todo ordenado sin que se pise

![[Pasted image 20231130093031.png]]
En el ejemplo de arriba, el valor de ONE no puede ser modificado, ya que con la instruccion .equ estamos pidiendo que ONE valga siempre 1. Es por eso que no es relocalizable
# Linking loader
Cuando llega la hora de cargar al programa, si el sistema tiene multitasking el compilador tiene que ver donde hay espacio libre, dificilmente empiece en el 2048, asi que tiene que volver a relocalizar todas las etiquetas


finalmente:
![[Pasted image 20231130093459.png]]


### DLL  
> the concept has a number of attractive features. Commonly used routines such as memory management or graphics packages need be present at only one place, the DLL library. This results in smaller program sizes because each program does not need to have its own copy of the DLL code, as would otherwise be needed. All programs share the exact same code, even while simultaneously executing.