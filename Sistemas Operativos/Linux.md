---
dg-publish: true
---

![[Pasted image 20240315145622.png]]
![[Pasted image 20240315145647.png]]

## Kernel 
La capa de gestion de dispositivos especifico + servicios par la gestion de dispositivos agnosticos del hardware que son utilizados por las apps
![[Pasted image 20240315145801.png]]
![[Pasted image 20240315145813.png]]
![[Pasted image 20240315145826.png]]
![[Pasted image 20240315150018.png]]

### System Calls 
Es un punto de entra da controlado al kernel, permitiendo que un proceso le pida al kernel que realice alguna operacion en su nombre. El kernel expone una gran cantidad der servicios via el Application Programming Interface (API) de system calls
Un system call: 
- Cmabia el modo de preocsdor de user mode a kernel mode (ahora la CPU puede acceder al area protegida)
- Cada system call tien un inico numero, es un conjunto fijo
- Cada system call tiene parametros
### Procesos 
- Un proceso es un programa en ejecuccion
- es algo dinamico (el heap lo vuelve dinamico)
- tiene una estructura interna propia
- todos los procesos menso el kernel viven en user land
#### Partes de un proceso:
1. PID: Process (ID)
2. Nombre del programa
3. File Descriptors
4. Memoria: codigo, datos, stack, heap

El kernel posee una tabala llamada process tables, donde se guarda infro de cada proceso, cuya entrada es el PID del proceso
![[Pasted image 20240315150829.png]]

#### File descriptors
Los procesos tienen asociados los archivos abiertos que estan usando. Estos se identifican por un numero denominado file descritor, un entero positivo. Estos se almacenan en una tabla en el kernel llamada File Descriptor Table, hay una por proceso
![[Pasted image 20240315151357.png]]


## API 
![[Pasted image 20240315152005.png]]

### System Call fork()
La unica forma de que un usuario cree un proceso en el sistema UNIX es mediante system call fork. El [[Proceso]] que lo invoca es llamado proceso padre, el nuevo proceso creado es llamado hijo. Son una copia exacta que solo se diferencian por el PID (el padre se queda con una copia del PID del hijo para saber cual es)
Todos los procesos pueden crear procesos (en unix)
![[Pasted image 20240315152840.png]]Notas:
1. Padre e hijo son copias exactas. 
2. despues de fork() ambos se ejecutan por separado. 
3.  la única forma de saber quien es quien es mediante su pid. 
4. el orden de ejecución de los procesos después del fork() no puede saberse![[Pasted image 20240315153024.png]]

```c
int pid = fork(); 
if(pid == 0){ 
printf("child: exiting\n"); 
} else if(pid > 0){ 
printf("parent: child=%d\n", pid); 
} else { 
printf("fork error\n"); 
}
```


Paso a paso:
1. Crea y asigna una nueva entrada en la Process Table para el nuevo proceso. 
2. Asigna un número de ID único al proceso hijo (pid). 
3. Crea una copia del proceso padre. 
4. Realiza ciertas operaciones de I/O, abre stdin, stdout,stderr. 
5. Devuelve el número de ID del hijo al proceso padre, y un 0 al proceso hijo