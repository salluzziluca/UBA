## Etapa 1

### Calendario

- [x] En un **calendario** se pueden crear, modificar y eliminar **************eventos************** y **************tareas**************
- [x] Tanto los **eventos** como **tareas** pueden tener un **título** y una **descripción**.
- [x] Las **tareas** pueden marcarse como **completadas**.

### Evento

- [ ] Hay **eventos** de día completo
- [ ] Hay **eventos** que comienzan en una fecha y hora y tener una duración arbitrarios.
- [ ] En ambos casos, el evento puede comenzar en un día y terminar en otro.

### Tareas

- [ ] Las **tareas** no tienen duración
- [ ] Hay **tareas** de día completo
- [ ] Hay **tareas** que tienen una fecha y hora de vencimiento.

### Repeticiones

- [ ] Los **eventos** se pueden **repetir** con frecuencia diaria, semanal, mensual o anual.
- [ ] En caso de frecuencia diaria, es posible definir un intervalo (ej: "cada 3 días")
- [ ] En caso de frecuencia semanal, es posible definir los días de la semana (ej: "todos los martes y jueves").
- [ ] La repetición puede ser infinita
- [ ] La repetición puede terminar en una fecha determinada (ej: hasta el 13 de enero)
- [ ] La repetición puede terminar luego de una cantidad de repeticiones dada (ej: luego de 20 ocurrencias).
- [ ] Al modificar o eliminar un evento con repetición, el cambio o eliminación se aplica a todas sus repeticiones.

### Alarmas

- [ ] En un **evento** o **tarea** se pueden configurar una o más **alarmas**:
- [ ] La alarma se dispara en un instante de tiempo, que se puede determinar segun una fecha y hora absolutas
- [ ] La alarma se dispara en un instante de tiempo, que se puede determinar segun un intervalo de tiempo relativo a la fecha y hora del evento/tarea (ej: "30 minutos antes").
- [ ] El efecto producido al dispararse la alarma es configurable:
- [ ] Se puede mostrar una notificación
- [ ] Se puede reproducir un sonido
- [ ] Se puede enviar un email.

## Pautas generales

- [ ] Se espera que el código sea razonablemente elegante y legible, y que no violen demasiados principios de diseño.
- [ ] Se espera que haya pruebas unitarias para la lógica con al menos 50% de cobertura, y tienen que estar relativamente bien planteadas.
- [ ] Las pruebas tienen que pasar.
- [ ] Se espera que hagan un buen uso del paradigma de objetos y de los patrones de diseño (aunque no es obligatorio que usen ningún patrón).

## Otros errores que generan reentrega

- [ ] Variables globales / Singleton
- [ ] Clases o métodos demasiado largos
- [ ] Código spaghetti
- [ ] Invocaciones a `LocalDateTime.now()` o `System.out` o cualquier otro método o variable estática

## Checklist post correccion

- [ ] En caso de que la entrega no cumpla alguno de los requisitos mínimos, pedir reentrega enviando mensaje por Slack/Mail/Github
- [ ] En caso de pedir reentrega, especificar los requisitos mínimos no cumplidos y dar una fecha límite.
- [ ] La corrección de esta etapa no lleva nota, en la planilla marcar Aprobado o Reentrega.