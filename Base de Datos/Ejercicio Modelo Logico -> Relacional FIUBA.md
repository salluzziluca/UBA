![[Pasted image 20240903111642.png]]

| Relacion                                                          | CK     | PK                                             | FK                                  |     |
| ----------------------------------------------------------------- | ------ | ---------------------------------------------- | ----------------------------------- | --- |
| Alumno(telefono, padron, nombre, codigo_inst_secundari)           | padron | padron                                         | codigo_inst_secundaria              |     |
| institucion(codigo, nombre)                                       |        | codigo                                         |                                     |     |
| carrera(codigo, nombre, legajo_director, nombre_director)         |        | codigo                                         |                                     |     |
| inscripto(padron, carrera, fecha)                                 |        | padron, carrera                                | padron, carrera                     |     |
| materia(codigo, departamento)                                     |        | codigo_materia, codigo_departamento            | codigo_departamento                 |     |
| departamento(codigo_nombre)                                       |        | codigo                                         |                                     |     |
| profesor(legajo, nombre)                                          |        | legajo                                         |                                     |     |
| dicta(legajo_profesor, dia, turno, depto, numero)                 |        | legajo, dia, turno                             | legajo, depto, numero materia       |     |
| oportunidad(padron, codigo_depto,codigo_materia)                  |        | padron, N° op, codigo_depto,codigo_materia     | padroo, codigo depto codigo materia |     |
| correccion(padron_,c_materia,c_depto, N°op, Cuatri, legajo, nota) |        | Padrón, N° Op, c_mat, c_depto, cuatri          | padro, cmateria, cpto, legajo, N Op |     |
| final(N Op, Cuatri, Codigo Materia, Cod Departamento)             |        | N Op, Cuatri, Codigo Materia, Cod Departamento | Codigo Materia, Cod Departamento    |     |


![[Pasted image 20240903120746.png]]

| relacion              | ck  | pk        | fk       |     |
| --------------------- | --- | --------- | -------- | --- |
| E(e1, e2, e3, h1, f1) |     | e1,e2, h1 | h1, f1   |     |
| H(h1, h2)             |     | h1        |          |     |
| G(e1,e2, h1)          |     | e1,e2,h1  | e1,e2,h1 |     |
| B(B1, B2, H1)         |     | B1, H1    | H1       |     |
| A(a1, a2)             |     | s1        |          |     |
