---
dg-publish: true
---

un proceso peude terminar por un defecto del programa o por un allamada a exit().
Algoritmicamente hace lo siguiente:
- Ignora todas las signals.
- Cierra todos los archivos abiertos
- En consecuencia se liberan todos los locks mantenidos por este proceso sobre esos archivos
- Libera el directorio actual
- Los segmentos de memoria compartida del procesos se separan
- los contadores de los semáforos son actualizados
- Libera todas las secciones y memoria asociada al proceso
- Registra información sobre el proceso (accounting record)
- Pone el estado del proceso en “zombie”
- Le asigna el parent PID de los procesos hijos al PID de _init_
- le manda una signal o señal de muerte al proceso padre
- context switch

Usualmente no se utiliza y se llama a la funcion exit de la std lib de C, esta: 

- llama a los Exit Handler que son dos funciones llamadas _on_exit()_ y _atexit()_
- los streams de stdio son flusheados ( buffer–>disco )
- se llama a la system call __exit()_.