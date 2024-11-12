---
dg-publish: true
---
## Etapa2 
Ejecutar el programa y probarlo. Al menos probar lo siguiente:

- [x] Crear un evento con repetición cada 2 días
- [x] Crear una tarea de día completo
- [ ] Mostrar en la vista principal la vista de 1 día, 1 semana, 1 mes. Verificar que se muestra correctamente el evento y la tarea con repetición.
- [x] Cerrar y abrir el programa. Verificar que se persistieron los datos. Verificar que el archivo se crea en el "directorio actual"
- [x] Crear una alarma. Verificar que se dispara. 

- Con respecto al código:

- [x] Verificar que están bien separadas las capas lógica y GUI. En la capa lógica no debe haber ninguna dependencia de GUI.
- [ ] Verificar que el diseño de la GUI está razonablemente bien y no hay violaciones graves de los principios de diseño.
## Etapa 1

### Calendario

- [x] En un **calendario** se pueden crear, modificar y eliminar **************eventos************** y **************tareas**************
- [x] Tanto los **eventos** como **tareas** pueden tener un **título** y una **descripción**.
- [x] Las **tareas** pueden marcarse como **completadas**.

### Evento

- [x] Hay **eventos** de día completo
- [x] Hay **eventos** que comienzan en una fecha y hora y tener una duración arbitrarios.
- [x] En ambos casos, el evento puede comenzar en un día y terminar en otro.

### Tareas

- [x] Las **tareas** no tienen duración
- [x] Hay **tareas** de día completo
- [x] Hay **tareas** que tienen una fecha y hora de vencimiento.

### Repeticiones

- [x] Los **eventos** se pueden **repetir** con frecuencia diaria, semanal, mensual o anual.
- [x] En caso de frecuencia diaria, es posible definir un intervalo (ej: "cada 3 días")
- [x] En caso de frecuencia semanal, es posible definir los días de la semana (ej: "todos los martes y jueves").
- [x] La repetición puede ser infinita
- [x] La repetición puede terminar en una fecha determinada (ej: hasta el 13 de enero)
- [x] La repetición puede terminar luego de una cantidad de repeticiones dada (ej: luego de 20 ocurrencias).
- [x] Al modificar o eliminar un evento con repetición, el cambio o eliminación se aplica a todas sus repeticiones.

### Alarmas

- [x] En un **evento** o **tarea** se pueden configurar una o más **alarmas**:
- [x] La alarma se dispara en un instante de tiempo, que se puede determinar segun una fecha y hora absolutas
- [x] La alarma se dispara en un instante de tiempo, que se puede determinar segun un intervalo de tiempo relativo a la fecha y hora del evento/tarea (ej: "30 minutos antes").
- [x] El efecto producido al dispararse la alarma es configurable:
- [x] Se puede mostrar una notificación
- [x] Se puede reproducir un sonido
- [x] Se puede enviar un email.

## Pautas generales

- [x] Se espera que el código sea razonablemente elegante y legible, y que no violen demasiados principios de diseño.
- [x] Se espera que haya pruebas unitarias para la lógica con al menos 50% de cobertura, y tienen que estar relativamente bien planteadas.
- [x] Las pruebas tienen que pasar.
- [x] Se espera que hagan un buen uso del paradigma de objetos y de los patrones de diseño (aunque no es obligatorio que usen ningún patrón).

## Otros errores que generan reentrega

- [x] Variables globales / Singleton
- [x] Clases o métodos demasiado largos
- [x] Código spaghetti
- [x] Invocaciones a `LocalDateTime.now()` o `System.out` o cualquier otro método o variable estática

## Checklist post correccion

- [ ] En caso de que la entrega no cumpla alguno de los requisitos mínimos, pedir reentrega enviando mensaje por Slack/Mail/Github
- [ ] En caso de pedir reentrega, especificar los requisitos mínimos no cumplidos y dar una fecha límite.
- [ ] La corrección de esta etapa no lleva nota, en la planilla marcar Aprobado o Reentrega.