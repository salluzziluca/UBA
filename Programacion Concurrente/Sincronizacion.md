---
Dia: 2025-09-22
dg-publish: true
---
## Semaforos
Tipo de dato compuesto por dos campos:
- unit `V`
- un set de procesos llamado `L`

Se inicializa con un  `k` mayor a 0 y con el conjunto vacio. 

Se definen dos operaciones atomicas
`wait(S)` y `signal(S)`

Si `V` mayor a 0, recurso disponible 
Si `V` menor a 0, recurso no disponible

El valor del semafoto representa la cantidad de recursos disponibles. Si V vale 0 o 1, es un semaforo binario, tambien conocido como `MUTEX`
`wait(S)` resta 1 al contador y `signal(S)`suma 1 al contador