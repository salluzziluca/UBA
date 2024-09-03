![[Pasted image 20240903111642.png]]

| Relacion                                                  | CK     | PK                                  | FK                     |     |
| --------------------------------------------------------- | ------ | ----------------------------------- | ---------------------- | --- |
| Alumno(telefono, padron, nombre, codigo_inst_secundari)   | padron | padron                              | codigo_inst_secundaria |     |
| institucion(codigo, nombre)                               |        | codigo                              |                        |     |
| carrera(codigo, nombre, legajo_director, nombre_director) |        | codigo                              |                        |     |
| inscripto(padron, carrera, fecha)                         |        | padron, carrera                     | padron, carrera        |     |
| materia(codigo, departamento)                             |        | codigo_materia, codigo_departamento | codigo_departamento    |     |
| departamento(codigo_nombre)                               |        | codigo                              |                        |     |
| profesor(legajo, )                                        |        |                                     |                        |     |
