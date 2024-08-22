## Deuda Técnica
Si logro hacer que el codigo funcione muy muy muy (que me tome poco tiempo de desarorollo), segurametnee estemos tomando deuda tecnica. Vamos a tener que despues invertir tiempo en refactorizar y dejalo lindo.

Regla del boy scout: cuando me voy de un lugar de acampe, dejar de dejarlo mejor de lo que lo encontré

## Objetivos
- Mantenibilidad
 - Simplicidad: Siempre simpleza antes de complejidad
 - Claridad 
- Flexibilidad
- Legibilidad
## Recursos 

#### Nombres significativos y pronunciables
Preferir nombres claros a comentarios. Preferible que sea largo a `d`.
Usar nombres que revelen la intención de esa variable
Usar nombres buscables


#### Notaciones
no hace falta usar prefijos de miembros
![[Pasted image 20240822194302.png]]

Usar un concepto por nombre (get, retrieve). Usar los nombres del 

#### Funciones
Deben tener 8 lineas aprox por funcion 

Cumple con el [[4.1 SOLID#S SRP (Single Responsibility Principle)|Single Responsibility Principle]]

Un solo nivel de abstraccion por funcion 

Que se pueda leer de arriba hacia abajo (como un periodico)

Evitar el switch: rompe el [[4.1 SOLID#S SRP (Single Responsibility Principle)|Single Responsibility Principle]]. Ya que cada camino hace una cosa diferente

Recibir pocos argumentos. Uno es bueno, cero es mejor`
 `writeFile(fileName)`

No tener un booleano (flag) que te ramifique el codigo, usar dos funciones![[Pasted image 20240822195640.png]]

- [[4.0 Principios de Diseño#DRY (Dont Repeat Yourself)|Dont Repeat Yourself]]

- [[2.6 Abstracción#Principle of least astonishment|Principle of least astonishment]]

## Comentarios
![[Pasted image 20240822200430.png]]

- Advertencias de consecuencias
- Ampliar informacion
##### Malas practicass
Redundancia
Comentarios erroneos (pueden conducir a errores)
Comentarios obligatorios (no siempre es necesario comentar)
