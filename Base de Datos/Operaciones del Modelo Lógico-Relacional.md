
Los operaciones del modelo relacionas se especifican a traves del algebra relacional o el calculo relacional

## Consulta 
No modifica ninguna relacion y no viola ningun tipo de [[Restricciones del modelo Logico Relacional|restricción]]
## Actualización

### Inserción
tengo que validar las 4 reglas. EL [[Sistemas de Gestion de Bases de Datos|SGBD]] deberá rechazar una inserción que viole algún tipo de [[Restricciones del modelo Logico Relacional|restriccón]]
### Eliminación
tengo que validad la [[Restricciones del modelo Logico Relacional#Restriccion de integridad referencial|restricción de integridad referencial]]
(Cuando R referencia a S, y se intenta eliminar una [[tupla]] de S que es referenciada por alguna/s [[tupla]]/s en R.)
Si borro un actor y estaba en varias pelis quedan todas esas con un actor no valido 

Se puede resolver usando cascada ( borro todas sus apariciones)
O de forma restrictiva (primero borrame la actuacion y despues te dejo borrar el actor). Rechazo la eliminación
Pongo en null los [[Base de Datos/Atributos|atributos]] referenciales a actor


## Modificacion 
Tengo que revisar dominio (que este bien el [[dato]])
Tengo que revisar unicidad tambien si cambio algun valor de la [[clave primaria]]
idem con [[Entidades|entidad]]
[[Restricciones del modelo Logico Relacional#Restriccion de integridad referencial|restricción de integridad referencial]] tambien. Si modifico un valor referenciado tengo que fijarme que no se rompan sus referencias. PUedo hacer cascada

Si se modifica una clave foránea, se debe verificar que sus nuevos valores referencien a una [[tupla]] existente de la relación
# Transacción
Serie de operaciones que o bien se hacen enteras o no se hacen.(ej: transaccion)
Yo defino esta serie de operaciones como transaccion
