---
Dia: 2025-09-22
dg-publish: true
---
>[!example] Herramientas de sincronización que permite a los hilos tener exclusión mutua y la posibilidad de esperar (block) por que una condición se vuelva falsa. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple

Un monitor consta de:
- Nombre
- Variables internas
- Procedimientos del monitor: rutinas que acceden directamente a las variables internas
- Una interfaz pública para que los procesos puedan acceder a las variables internas
- Inicialización de las variables internas
- Un conjunto de condition variables que incorporan sincronismo al monitor

Los procesos pueden tomar distintos estados:
- Esperando para entrar al monitor
- Ejecutando el monitor (sólo un proceso a la vez - exclusión mutua)
- Bloqueado en FIFO de variable de condición
- Recién liberado de la wait condition
- Recién completó una operación signalC


| Semaforo                                                                        | Monitor                                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| wait puede o no bloquear                                                        | waitC siempre bloquea                                                                       |
| signal siempre tiene efecto                                                     | signalC no tiene efecto si la                                                               |
| signal desbloquea un proceso arbritrario                                        | signalC desbloquea el proceso del tope de la cola                                           |
| un proceso desbloqueado con signal, puede continuar la ejecución inmediatamente | un proceso desbloqueado con signalC debe esperar que el proceso señalizador deje el monitor |
