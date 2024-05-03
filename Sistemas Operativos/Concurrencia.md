Los threads y los procesos son muy parecidos, tienen de hecho una API casi equivalente. Esto es porque en Linux en vez de implementar procesos y threads por lados diferentes juntaron las implementciones y se usa el mismo scheduler para ambos

hay una clase padre llamada task de las cuales heredan proceso y thread

![[Pasted image 20240503192216.png]]

Los threads tambien tienen estados


Cuando yo creo un proceso (PID 2001) con un solo thread, se setea el Thread Group ID = 2001 y con un Thread ID = 2001. Si dentro de ese procso creo mas threads, se crean con el mismo TGID y con diferente TID ![[Pasted image 20240503193111.png]]