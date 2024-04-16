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
Trampolin:

