> Formas de diseñar la arquitectura de nuestro sistema que ya fueron probados y analizados, que sabemos que funcionan.

Estos son de mas alto nivel que los [[5.0 Patrones de Diseño]].

## Layers 

![[Pasted image 20240912192927.png]]
![[Pasted image 20240912193848.png]]

El domain object representan
## Broker 
Es aquel que abstrae la comunicacion entre el cliente y el servidor. Un ejemplo claro es un balanceador de cargas, recibo un request y decido a cual sv se la doy

## Pipe & Filters 
La salida de un procso es la entrada del proximo. Voy armando cadenas de comandos. Un compilador funciona asi.
![[Pasted image 20240912200704.png]]

## Hexagonal architecture
![[Pasted image 20240912205135.png]]
![[Pasted image 20240912212158.png]]

### Domain Layer
![[Pasted image 20240912212211.png]]

### Application Layer 
![[Pasted image 20240912212235.png]]

### Casos de uso 
![[Pasted image 20240912212246.png]]

### Infrastructure layer 
![[Pasted image 20240912212306.png]]

## Dependency inversion principle 
![[4.1 SOLID#D DIP (Dependency Inversion Principle)]]

## Dependency Injection 
Tecnica de diseño que permite cablear dependencias desde afuera
![[Pasted image 20240912203913.png]]
En este caso cuando el usuario se crea le pide al repositorio ser gurdado. Esto nos permite que el user se guarde en diferentes repositorios sin tener que tocar mas el create user.

En algunos frameworks se inyectan diferentes implenetaciones de clases segun como estemos corriendo el sistema. si lo corro para prod se inyectan las clases concretas, si estoy corriendo en test se inyectan los mocks.

## Folder structure
![[Pasted image 20240912204534.png]]



## Microservices 
Pasamos de una arquitectura monolitica a una partida en pedacitos
![[Pasted image 20240912205421.png]]
Desacoplo las diferentes partes de mi sistema. Esto me permite escalar mejor porque puedo darle mas bola a los servicios mas requeridos.
POdria implementar cada servicio en un lenguaje distinto. 
por ejemplo puedo desacoplar la parte de mi sistema que se encarga de la busqueda y hacerlo en funcional

Se pueden comunicar mediante pipes, un sistema de mensajeria

Lo malo es que tenes que levantar n servicios diferentes, que todo se conecte bien, es mas dificil de debuggear

![[Pasted image 20240912210135.png]]

## Micro frontends

Separo las diferentes partes del frontend
![[Pasted image 20240912210610.png]]
en el ejemplo cuando toco browse restaurants se abre otro micro frontend
De esta forma no bajas todo el frontend junto, solo que necesitas
!(https://microservices.io/)
![](https://microservices.io/)

