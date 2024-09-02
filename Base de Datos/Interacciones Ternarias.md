> Son aquellas en que participan 3 tipos de [[Entidades|entidad]] distintos.

Ejemplo: En un concurso de canto se organizan rondas temáticas en las que se inscriben algunos participantes. En cada ronda, los cantantes que participan son calificados por una serie de jurados
![[Pasted image 20240820212706.png]]

Aquí la cardinalidad de un tipo [[Entidades|entidad]] determina la cantidad de instancias de interrelación en que puede aparecer, fijadas las instancias de los otros dos tipos de [[Entidades]].

Fijo jurado y ronda. Un jurado puede puntuar a N jugadores en una ronda.
Fijo ronda y cantante. En una ronda un cantante puede tener puntajes de N jurados
Fuhi cantante y jurado: Un jurado puede puntuar al mismo jugador durante varias rondas.


## Agregación
El disño anterior no nos permite registrar cantantes en rondas si no fueron evaluados por ningun jurado. Para esto puedo crear una agregacion "participacion. Es decir, en este caso, englobar la participacion del cantante
![[Pasted image 20240820213454.png]]

## Generaliazacion y Especializacion 
Es basicamente [[2.7 Herencia|herencia]] 
![[Pasted image 20240820213921.png]]
Si es total, todas las personas tienen que ser alumnos o docentes. De lo contrario es parcial.
Si es superpuesta, puede haber personas que sean alumnos y docente. SI es disjunta, no. 

## Union 
Un concepto abarca a dos subconceptos. 
No estoy obligado a que todos los subtipos sean parte del supetipo
![[Pasted image 20240820214741.png]]