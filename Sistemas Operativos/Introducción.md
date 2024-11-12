---
dg-publish: true
---
> El rol de un sistema operativo es el de compartir una computadora entre varios programas de forma tal de proveer un conjunto de servidores útiles de los que el hardware por si mismo expone
> Este maneja y abstrae el hardware de bajo nivel, de forma tal que todo sea bonito para los programas y para el usuario

Este sistema provee servicios a los programas mediante una API, manejando los recursos de la computadora (hardware).

usuario-> app->OS

Un OS tambien tiene que encargarse de que la ejecución de los programas prezca facil, que estos solo tengan que preocuparse por funcionar. Para esto se utiliza la __virtualizacion__, el OS toma un recurso fisico (la memoria, el procesador, el disco) y lo transforma en algo virtual mas general, poderoso y facil de usar
![[Pasted image 20240315144932.png]]

Un OS es
Referee: Coordina y gestiona recursos compartidos entre diferentes apps.
Ilusionista: Provee abstraccion del hardware para simplificar el diseño de las apps
Pegamento: Provee servicios comunes que faciliten un mecanismo que permita compartir, por ejemplo, info entre las apps. (e.g: copypaste)


Servicios comunes: 
● API general (Application Program Interface)
● Library Call
● System Call