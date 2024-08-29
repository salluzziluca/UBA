La ==aridad== ó ==grado== de un tipo de interrelación es la cantidad de tipos de [[Entidades|entidad]] que coparticipan del mismo.
La ==cardinalidad== es la maxima cantida de instancias de cada tipo de [[Entidades|entidad]] que pueden relacionarse con una instancia concreta de los tipos de [[Entidades]] rstantes
![[Pasted image 20240820201819.png]]
Un futbolista se puede vincular a un solo Pais
Un país a muchos futbolistas
Futbolista tiene una ==participación total== (todos los futbolistas nacieron en un país)
País tiene una ==participación parcial== (en el vaticano no nació ningún futbolista)

Las cardinalidades posibles son 1:1, 1:N, N:1, N:M

--- 

## [[Análisis Matemático II/Base de Datos/Atributos|Atributos]] de las interrelaciones 
Estas tambien pueden tener [[Análisis Matemático II/Base de Datos/Atributos|atributos]] 
![[Pasted image 20240820202538.png]]

## Restricciones de Participacion 
Tambien debemos identificar los [[Atributos Clave]]. Sólo pueden formar parte de los [[Atributos Clave]] de una interrelación los [[Atributos Clave]] de los tipos de [[Entidades|entidad]] que participan de la misma.

![[Pasted image 20240820204048.png]]
Tanto el legajo como el codigo son [[Análisis Matemático II/Base de Datos/Atributos|atributos]] calves de las dos [[Entidades]] de la interrelacion. 

![[Pasted image 20240820204234.png]]
En este modelo al forma de identificar el escribió es mediante el [[Análisis Matemático II/Base de Datos/Atributos|atributo]] clave nombre