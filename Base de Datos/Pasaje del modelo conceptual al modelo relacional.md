[[Modelo Logico-Relacional Conceptual]]


Una buena practica para crear claves atomicas es usar los atributos raices. De esa forma e aseguras que esta todo bien descompuesto.

Si hay participacion total de uno de los lados puedo incluir una de las entidads participanetes como claves foraneas.
EJ: tengo gernte dirige departamenteo y la cardinalidad de departamenteo es 1,1 (todo gerente tiene departamenteo). Entonces gerentes puede tener como clave foranea la calave primaria del depto.

Ambas participacio total. Hago una tabla gerenteDepartamento(nombre_gerente, codigo depto)

Con cardinalidad N 

N futbolistas juegan en 1 club 

