## Etapa 1
- [x] En un **calendario** se pueden crear, modificar y eliminar **************eventos************** y **************tareas**************
- [x] Tanto los **eventos** como **tareas** pueden tener un **título** y una **descripción**.
- [x] Las **tareas** pueden marcarse como **completadas**.
- Los **eventos** pueden ser:
- [x] De día completo
- [ ] Comenzar en una fecha y hora y tener una duración arbitrarios.

En ambos casos, el evento puede comenzar en un día y terminar en otro.

6.  Las **tareas** no tienen duración, pudiendo ser:

- [x] De día completo
- [ ] Tener una fecha y hora de vencimiento.

8.  Los **eventos** se pueden **repetir**:

- [ ] Con frecuencia diaria, semanal, mensual o anual.
- [ ] En caso de frecuencia diaria, es posible definir un intervalo (ej: “cada 3 días”)
- [ ] En caso de frecuencia semanal, es posible definir los días de la semana (ej: “todos los martes y jueves”).
- La repetición puede ser:

- [ ] infinita
- [ ] Terminar en una fecha determinada (ej: hasta el 13 de enero)
- [ ] Terminar luego de una cantidad de repeticiones dada (ej: luego de 20 ocurrencias).

- [ ] Al modificar o eliminar un evento con repetición, el cambio o eliminación se aplica a todas sus repeticiones.

10.  En un **evento** o **tarea** se pueden configurar una o más **alarmas**:

- [ ] La alarma se dispara en un instante de tiempo, que se puede determinar de dos maneras:

- [ ] Una fecha y hora absolut
- [ ] Un intervalo de tiempo relativo a la fecha y hora del evento/tarea (ej: “30 minutos antes”).

3.  El efecto producido al dispararse la alarma es configurable:

- [ ] Mostrar una notificación
- [ ]  Reproducir un sonido
- [ ] Enviar un email.



- [ ]   Se espera que el código sea razonablemente elegante y legible, y que no violen demasiados principios de diseño.
- [ ]   Se espera que haya pruebas unitarias para la lógica con al menos 50% de cobertura, y tienen que estar relativamente bien planteadas.
- [ ]   Las pruebas tienen que pasar.
- [ ]   Se espera que hagan un buen uso del paradigma de objetos y de los patrones de diseño (aunque no es obligatorio que usen ningún patrón).
- [ ]   Prohibido:

- [ ]   Variables globales / Singleton
- [ ]   Clases o métodos demasiado largos
- [ ]   Código spaghetti
- [ ]   Invocaciones a `LocalDateTime.now()` o `System.out` o cualquier otro método o variable estática

- [ ]   En caso de que la entrega no cumpla alguno de los requisitos mínimos, pedir reentrega.
- [ ]   En caso de pedir reentrega, especificar los requisitos mínimos no cumplidos y dar una fecha límite.
- [ ]   La corrección no lleva nota, en la planilla marcar Aprobado o Reentrega. (Habrá una nota única al final de las 3 etapas).