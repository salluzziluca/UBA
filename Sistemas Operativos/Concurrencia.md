---
dg-publish: true
---
Los threads y los procesos son muy parecidos, tienen de hecho una API casi equivalente. Esto es porque en Linux en vez de implementar procesos y threads por lados diferentes juntaron las implementciones y se usa el mismo scheduler para ambos

hay una clase padre llamada task de las cuales heredan proceso y thread

![[Pasted image 20240503192216.png]]

Los threads tambien tienen estados


Cuando yo creo un proceso (PID 2001) con un solo thread, se setea el Thread Group ID = 2001 y con un Thread ID = 2001. Si dentro de ese procso creo mas threads, se crean con el mismo TGID y con diferente TID ![[Pasted image 20240503193111.png]]


## Interprocess Communication
era lo que se usaba para comunicar procesos antes de la existencia de threads, todavia se usa un monton, un tipo de interprocess communication es mediante pipes, otro es sockets de red

Otro es mediante memoria compartida, le decimos que la visibilidad de la memoria tiene que ser compartida


## Sincronizacion
### Race contidions
>Los threads juegan una carrera entre sus operaciones, y el
resultado del programa depende de quién gane esa carrera.

Se da cuando el resultado de un programa depende del orden en el que se ejecuutan los procesos, en como se intercalan. 
Esto se da porque los threads no se esperan entre ellos 
CAso en el que se rompe:
![[Pasted image 20240503195140.png]]


### Seccion Crítica 
Una seccion criticia es una seccion del codigo donde solo puede haber un thread en ejecución a la vez 


### Locks
Un lock es una variable que permite la sincronización mediante la
exclusión mutua, cuando un thread tiene el candado o lock ningún
otro puede tenerlo.

```c
while(true){
int transferencia= nextTranferencia();
obtener(lock);
//seccion critica
dejar(lock);
}
```
Mutual Exclusion: Un solo thread puede usar el lock a la vez
Progress: Si nadie tiene el lock y alguien lo quiere, alguno debe poder obtenerlo
Bounded Waiting: si un thread quire acceder aun thread y existen varios en la misma situacion, los demas tienen una cantidad finita (un limite) de posibles accesos antes que T lo haga. 

#### Operaciones atómicas
este tipo de operaciones no pueden dividirse en otras
y se garantiza la ejecución de la misma sin tener que intercalar ejecución.

#### Implementaciones de lock:
##### Spinlock:
Un lock que se impementa usando busy wait. El proceso o hilo en ejecuciion espera activamente en un loop a que ocurra un evento en lugar de dormirse o bloquearse
 Verifca repetidamente que el evento haya ocurrido 

##### Sleeplock:
Este duerme hasta que pasa x tiempo y cuando se despierta y chequea si tiene el deadlock
