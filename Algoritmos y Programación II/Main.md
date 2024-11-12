---
dg-publish: true
---
```c
int main(int argc, char const *argv[])

{

/* code */

return 0;

}

```
argc son valores que le pasamos cuando lo corremos. una vez compilado. cuando corremos hola.o, si lo corremos juntos con otros parametros, estos van a ser el vector argc.

ej:
si corremos: 
```
./hola.o hola pepe cuando
```
argc va a ser un vector conformado por `[hola], [pepe],[cuando]`