[[Modelo Logico-Relacional Conceptual]]


Una buena practica para crear claves atomicas es usar los atributos raices. De esa forma e aseguras que esta todo bien descompuesto.

Si hay participacion total de uno de los lados puedo incluir una de las entidads participanetes como claves foraneas.
EJ: tengo gernte dirige departamenteo y la cardinalidad de departamenteo es 1,1 (todo gerente tiene departamenteo). Entonces gerentes puede tener como clave foranea la calave primaria del depto.

Ambas participacio total. Hago una tabla gerenteDepartamento(nombre_gerente, codigo depto)

Con cardinalidad N 

N futbolistas juegan en 1 club 

futbolista(nombre pais)
clubes(nombreclub, pais)
JuegaEn(nombre, nombreclub, pais)

Entidades debilles
hoteles(nombre_hotel)
habitaciones(numtero, nombre_hotel, capacidad)


generalizacion 
Persona(DNI, nombre)
Alumnos(DNI, padron)
docentes(DNI, legajo, fecha de alta)
Uso en todos los DNI. 
SIrve solo cuando es total y es recomendable que sea disjunta
