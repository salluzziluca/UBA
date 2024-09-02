[[Modelo Logico-Relacional Conceptual]]

Las claves para un buen MR son: mapeo, normalizacion y heurísticas

Una buena practica para crear claves atomicas es usar los [[Base de Datos/Atributos|atributos]] raices. De esa forma e aseguras que esta todo bien descompuesto.

Si hay participacion total de uno de los lados puedo incluir una de las entidads participanetes como [[Claves foráneas (FK)|claves foraneas]].
EJ: tengo gernte dirige departamenteo y la cardinalidad de departamenteo es 1,1 (todo gerente tiene departamenteo). Entonces gerentes puede tener como clave foranea la calave primaria del depto.

Ambas participacio total. Hago una tabla gerenteDepartamento(nombre_gerente, codigo depto)

Con cardinalidad N 

N futbolistas juegan en 1 club 

futbolista(nombre pais)
clubes(nombreclub, pais)
JuegaEn(nombre, nombreclub, pais)

[[Entidades]] debilles
hoteles(nombre_hotel)
habitaciones(numtero, nombre_hotel, capacidad)


generalizacion 
Persona(DNI, nombre)
Alumnos(DNI, padron)
docentes(DNI, legajo, fecha de alta)
Uso en todos los DNI. 
SIrve solo cuando es total y es recomendable que sea disjunta

## union

## Ternarias


## Pasaje de entidad fuerte
![[Pasted image 20240902172200.png]]
## Pasaje interrelacion N:M
![[Pasted image 20240902172802.png]]

## Pasaje N:1 (participacion total)
![[Pasted image 20240902172821.png]]

## Pasaje N:1 (participacion parcial)
![[Pasted image 20240902172943.png]]

## Pasaje 1:1 (ambas participacion total)
![[Pasted image 20240902173157.png]]
## Pasaje 1:1 (una total, una parcial)
![[Pasted image 20240902173424.png]]
## Pasaje 1:1 (ambas participacion parcial)
![[Pasted image 20240902173510.png]]

## Entidades Debiles
![[Pasted image 20240902173927.png]]

## Pasaje de Ternarias (NNN)
![[Pasted image 20240902174349.png]]

## Pasaje de ternarias 1NN
![[Pasted image 20240902174422.png]]
Hay un solo proveedor que me puede vender los articulos


## Pasaje ternarias N11
![[Pasted image 20240902174827.png]]
Tengo +1 clave candidata. Porque si se legajo y horario se la materia, y si se legajo y materia se el horario

## Pasaje de agregación
![[Pasted image 20240902175028.png]]Claves de correcciones: PK = {Padrón, N° Op, c_mat, c_depto, cuatri}


## Pasaje de Jerarquias totales y disjuntas
![[Pasted image 20240902175541.png]]
En ambas se rompe la disjuncion. En la segunda no se puede romper la localidad, no podemos cargar una carrera que no sea ni ing ni posgrado
## Pasaje de jerarquias parciales y superpuestas
![[Pasted image 20240902175614.png]]


## Pasaje de uniones 
![[Pasted image 20240902175854.png]]


## Pasaje de unarias
![[Pasted image 20240902175917.png]]