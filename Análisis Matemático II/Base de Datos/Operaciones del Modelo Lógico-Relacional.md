
Los operaciones del modelo relacionas se especifican a través del algebra relacional o el calculo relacional

## Consulta 
No modifica ninguna relación y no viola ningún tipo de [[Restricciones del modelo Logico Relacional|restricción]]
## Actualización

### Inserción
tengo que validar las 4 reglas. EL [[Sistemas de Gestion de Bases de Datos|SGBD]] deberá rechazar una inserción que viole algún tipo de [[Restricciones del modelo Logico Relacional|restricción]]
### Eliminación
tengo que validad la [[Restricciones del modelo Logico Relacional#Restriccion de integridad referencial|restricción de integridad referencial]]
(Cuando R referencia a S, y se intenta eliminar una [[tupla]] de S que es referenciada por alguna/s [[tupla]]/s en R.)
Si borro un actor y estaba en varias pelis quedan todas esas con un actor no valido 

Se puede resolver usando cascada ( borro todas sus apariciones)
O de forma restrictiva (primero borrame la actuación y después te dejo borrar el actor). Rechazo la eliminación
Pongo en null los [[Análisis Matemático II/Base de Datos/Atributos|atributos]] referenciales a actor


## Modificacion 
Tengo que revisar dominio (que este bien el [[Dato]])
Tengo que revisar unicidad también si cambio algún valor de la [[clave primaria]]
idem con [[Entidades|entidad]]
[[Restricciones del modelo Logico Relacional#Restriccion de integridad referencial|restricción de integridad referencial]] también. Si modifico un valor referenciado tengo que fijarme que no se rompan sus referencias. Puedo hacer cascada

Si se modifica una [[Claves foráneas (FK)|clave foránea]], se debe verificar que sus nuevos valores referencien a una [[tupla]] existente de la relación.


A veces es necesario realizar una serie de operaciones por completo, o bien no realizarlas. Surge el concepto de ![[Transacción]]

