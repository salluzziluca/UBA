---
dg-publish: true
---
## Etapa2 
Ejecutar el programa y probarlo. Al menos probar lo siguiente:

- [x] Crear un evento con repetición cada 2 días
- [x] Crear una tarea de día completo
- [x] Mostrar en la vista principal la vista de 1 día, 1 semana, 1 mes. Verificar que se muestra correctamente el evento y la tarea con repetición.
- [x] Cerrar y abrir el programa. Verificar que se persistieron los datos. Verificar que el archivo se crea en el "directorio actual"
- [x] Crear una alarma. Verificar que se dispara. 

- Con respecto al código:

- [ ] Verificar que están bien separadas las capas lógica y GUI. En la capa lógica no debe haber ninguna dependencia de GUI.
- [ ] Verificar que el diseño de la GUI está razonablemente bien y no hay violaciones graves de los principios de diseño.
## Etapa 1
- [x] En un **calendario** se pueden crear, modificar y eliminar **************eventos************** y **************tareas**************
- [x] Tanto los **eventos** como **tareas** pueden tener un **título** y una **descripción**.
- [x] Las **tareas** pueden marcarse como **completadas**.
- Los **eventos** pueden ser:
- [x] De día completo
- [x] Comenzar en una fecha y hora y tener una duración arbitrarios.

En ambos casos, el evento puede comenzar en un día y terminar en otro.

6.  Las **tareas** no tienen duración, pudiendo ser:

- [x] De día completo
- [x] Tener una fecha y hora de vencimiento.

8.  Los **eventos** se pueden **repetir**:

- [x] Con frecuencia diaria, semanal, mensual o anual.
- [x] En caso de frecuencia diaria, es posible definir un intervalo (ej: “cada 3 días”)
- [x] En caso de frecuencia semanal, es posible definir los días de la semana (ej: “todos los martes y jueves”).
- La repetición puede ser:

- [x] infinita
- [x] Terminar en una fecha determinada (ej: hasta el 13 de enero)
- [x] Terminar luego de una cantidad de repeticiones dada (ej: luego de 20 ocurrencias).

- [ ] Al modificar o eliminar un evento con repetición, el cambio o eliminación se aplica a todas sus repeticiones.

1.  En un **evento** o **tarea** se pueden configurar una o más **alarmas**
2. La alarma se dispara en un instante de tiempo, que se puede determinar de dos maneras:

- [ ] La alarma se dispara en un instante de tiempo, que se puede determinar de dos maneras:

- [x] Una fecha y hora absoluta
- [x] Un intervalo de tiempo relativo a la fecha y hora del evento/tarea (ej: “30 minutos antes”).

3.  El efecto producido al dispararse la alarma es configurable:

- [x] Mostrar una notificación
- [x]  Reproducir un sonido
- [x] Enviar un email.

## Pautas 

- [x]   Se espera que el código sea razonablemente elegante y legible, y que no violen demasiados principios de diseño.
- [x]   Se espera que haya pruebas unitarias para la lógica con al menos 50% de cobertura, y tienen que estar relativamente bien planteadas.
- [x]   Las pruebas tienen que pasar.
- [ ]   Se espera que hagan un buen uso del paradigma de objetos y de los patrones de diseño (aunque no es obligatorio que usen ningún patrón).

## Otros errores que generan reentrega

- [x]   Variables globales / Singleton
- [x]   Clases o métodos demasiado largos
- [x]   Código spaghetti
- [x]   Invocaciones a `LocalDateTime.now()` o `System.out` o cualquier otro método o variable estática

## Checklist post correccion

- [ ]   En caso de que la entrega no cumpla alguno de los requisitos mínimos, pedir reentrega enviando mensaje por Slack/Mail/Github
- [ ]   En caso de pedir reentrega, especificar los requisitos mínimos no cumplidos y dar una fecha límite.
- [ ]   La corrección de esta etapa no lleva nota, en la planilla marcar Aprobado o Reentrega.