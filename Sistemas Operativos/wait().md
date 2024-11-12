---
dg-publish: true
---
Un proceso puede sincronizar su ejecución con la finalización de un proceso hijo mediante la ejecución de _wait()_

- En ciertos casos el proceso padre necesita esperar que el proceso hijo realice cierta tarea para continuar con su ejecución.
- Para ello existe la system call _wait()_ que retrasa la ejecución del proceso padre hasta que el proceso hijo termine su ejecución.