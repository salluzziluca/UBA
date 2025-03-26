---
Dia: 2025-03-26
dg-publish: true
---
## Ingenería de Requisitos 
### Requisito vs requerimiento 
¿Requisito?
m. Circunstancia o condición necesaria para algo.
Sin.: condición, requerimiento, exigencia, obligación, formalidad, estipulación, cláusula.
¿Requerimiento?
m. Acción y efecto de requerir.
(barbarismo derivado de “requirement”)
Asociado a demandar, exigir…


## Alcance 
Hay muchas cosas que nos pueden hacer cambiar el alcance, cambios por parte del cliente o externos (desapareció git).
El alcance planificado no va a ser el mismo al final logrado

### Cambio de vision tradicional a agil:
el alcance es adaptativo, tiene que ser cambiable sin tanta burocracia. No debe haber (como dice el PMBook) un comite burocratico que decida como afrontar los cambios. Se deben dar organicamente. 
Los cambios entran por el backlog, el equipo "no se entera" porque solo mira su proxima tarea en el backlog

#### Mantenimiento de sistemas legacy 
es tecnicamente un cambio de alcance. Algo que ya habia quedado estatico, se vuelve a modificar.

>[!quote] han alcanzado un grado de éxito relativo, pero que resulta difícil de mantener porque se ha perdido el conocimiento que permitiría hacerlo (Carlos Fontela)


Han sido desarrollados por equipos de trabajo que ya no trabajan en él
No hay pruebas de aceptación ni técnicas que permitan probar el funcionamiento del código o entender cómo funciona
Escasa documentación funcional, técnica o para usuarios
Funcionalidades desconocidas por desarrolladores y usuarios
Gran volumen de [[deuda técnica]] impide probarlos y comprenderlos

### Scope Creep 
Agregar características y ampliar el alcance sin tener en cuenta el efecto

No es necesariamente malo. Depende mucho de los tiempos, el presupuesto, etc 


### Gold Plating 
Hacer cosas que el cliente no me pidió. "Mejoras" sin el consentimiento del usuario, no fue validado, es un problema. Es un tema mas a mantener. No tengo criterio de aceptación, contra quien lo valido?


### Descomposicion del alcance 
llegar de las necesidades a las características y tareas 
análisis del problema y comprension de partes 
estimaciones de tiempo y costos 
division del trabajo 
delimitacion de las responsabilidades 
luego me pregunto 
esta todo? no sobra nada? cada componente es necesario y definidio? Puede estimarse costo y tiempo en forma confiable?


## Agenda 
Pruebas tecnicas (unitarias) -> prubeas que escriiben los programadores para ver si lo que yo queria construir lo construi como yo queria
Pruebas funcionales-> le demuestra al cliente que es lo que él quería
- Kent Beck, XP 1999

Luego aparecio TDD y la gente solo lo uso para unit test, no para functional tests.