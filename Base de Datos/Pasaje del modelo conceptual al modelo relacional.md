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

## Ternarias (NNN)
![[Pasted image 20240902174349.png]]
