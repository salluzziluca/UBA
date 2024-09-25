> Los bloques fundamentales de nuestro sistema. Dentro de esos bloques despues codeamos.
## Definicion de Arquitectura 
Conceptos o propiedades fundamentales  de un sistema en su entorno encarnando en su elementos, relaciones y en los principios de su diseño y evolucion

> La arquitectura del sofwtare son aquella decisiones que son importantes y dificiles de cambiar. Martin Fowler.

Es dividir el sistema en componentes.
- Dcisiones significativas
- costosas de modificar
- divide el sistema en componentes 
- estos se comunican entre ellos
![[Pasted image 20240912192539.png]]
## UML
Tipos de diagramas: 
- diagramas de clase
- diagrama de paquetes 
- diagrama de objetos
- diagrama de componentes 
- diagrama de despliegue

![[2.10 Tipos de Relaciones]]

## Modelo de Vistas de Arquitectura
Puedo encontrar diferentes tipos de dibujitos para representar la arquitectura segun se vaya requiriendo




## Modelo de vistas 4+1 
![[Pasted image 20240909202130.png]]
Como hay que diseñar para que varias personas entiendan (usuarios, gente que recien llega a la empresa, contaduria, los devs, etc)

### Vista escenario
aca van a estar los requerimientos, los problemas que me van a modificar mi arquitectura

### Vista logica 
Requisitos funcionales. Cosas logicas que nos permiten abstraer la solución.  permiten identificar mecanismos y elementso de diseño comunes entre diversas partes del sistema. Las soluciones al los problemas propuestos al escenario

### Vista de procesos 
Procesos que se estan corriendo en memoria. Se enfoca en concurrencia y distribución, integridad del sistema, tolerancia a fallas. Los procesos que declare en componentes los pongo a correr

### Vista fisica o de despliegue 

![[Pasted image 20240909201831.png]]
### Vista de componentes  
la vista de desarrollo se centra en la organizacion real de los modulos de software en el ambiente de desarrollo. 
![[Pasted image 20240909201209.png]]

Separo todo en componentes

![[Pasted image 20240909202957.png]]


[[Patrones de Arquitectura del Software]]

