---
dg-publish: true
---
## Funcionamiento Interno de Malloc 
`ap = malloc(n)`
malloc nos devuelve un puntero al inicio del bloque de memoria. Si hacemos ap-1 casteado a header te devuelve el header. 
el header tiene metadata:
```c
struct header{
header *ptr;
unsigned int size;
}
```
- unsigned int size;
- `header *ptr`;
El puntero a header apunta al prox header de la memoria
Es una [[Lista#Lista circular|lista enlazada circular]]  


Cuando busco un bloque, si cae justito lo enviamos, sino dividimos y lo enviamos

Cuando hacemos free y lo que hacemos es asignar el puntero next del bloque anterior de la lista al next del actual siguiente. (ver [[Lista#Borrar|como borrar un elemento de una lista enlazada]])

Si se necesita pedirle mas memoria al sistema porque no podes hacer entrar el malloc en ningun lugar de la memoria, llamamos a sbrk o brk que te mueve el break y te devuelve el lugar en el que estaba antes de ser movido 


### Implementacion en RISC V 
... 