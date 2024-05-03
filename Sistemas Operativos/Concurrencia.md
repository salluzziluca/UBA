Los threads y los procesos son muy parecidos, tienen de hecho una API casi equivalente. Esto es porque en Linux en vez de implementar procesos y threads por lados diferentes juntaron las implementciones y se usa el mismo scheduler para ambos

hay una clase padre llamada task de las cuales heredan proceso y thread

![[Pasted image 20240503192216.png]]