>[!quote] Los bloques fundamentales de nuestro sistema. Dentro de esos bloques despues codeamos.
## Definicion de Arquitectura 
Conceptos o propiedades fundamentales  de un sistema en su entorno encarnando en su elementos, relaciones y en los principios de su diseño y evolucion

>[!quote] La arquitectura del sofwtare son aquella decisiones que son importantes y dificiles de cambiar. Martin Fowler.



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
>[!important] Hay que diseñar para que varias personas entiendan (usuarios, gente que recien llega a la empresa, contaduria, los devs, etc)




### Vista logica 
Requisitos funcionales. Cosas logicas que nos permiten abstraer la solución.  permiten identificar mecanismos y elementos de diseño comunes entre diversas partes del sistema. Las soluciones al los problemas propuestos al escenario

### Vista de procesos 
Toma en cuenta requisitos no funcionales como rendimiento y disponibilidad.

Procesos que se estan corriendo en memoria. Se enfoca en concurrencia y distribución, integridad del sistema, tolerancia a fallas. Los procesos que declare en componentes los pongo a correr

### Vista fisica o de despliegue 
Toma en cuenta los requisimos no funcionales como disponibilidad, confiabilidad (tolerancia a fallas), rendimiento y escalabilidad. 

El software se ejecuta sobre una red de computadores o nodos de procesamiento. Los variados elementos identificados –redes, procesos, tareas y objetos– requieren ser mapeados sobre los nodos. 

Esperamos que diferentes configuraciones puedan usarse: algunas para desarrollo y pruebas, otras para mostrar el sistema en varios sitios para distintos usuarios. Por lo tanto, la relación del software en los nodos debe ser altamente flexible y tener un impacto mínimo sobre el código fuente.
### Vista de componentes  
Se centra en la organizacion real de los modulos del del softwre en el ambiente de desarrollo del software. Se empaqueta en partes pequeñas que pueden ser desarolladas por una persona o por grupos pequeños de desarrolladores. 

Tiene en cuenta los requisitos internos

Separo todo en componentes


### Vista escenario
Los elementos de las cuatro vistas trabajan conjuntamente en forma natural mediante el uso de un conjunto pequeño de escenarios relevantes. Los escenarios son de alguna manera una abstracción de los requisitos más importantes. 
Sirve a dos propósitos principales:
• Como una guía para descubrir elementos arquitectónicos durante el diseño de arquitectura
• Como un rol de validación e ilustración después de completar el diseño de arquitectura, en el papel y como punto de partido de las pruebas de un prototipo de la arquitectura.

### Conclusiones

- Permite a través de diferentes vistas analizar distintas perspectivas del problema, focalizándose en el problema en cuestión
- Concentra en un único documento las principales decisiones tomadas sobre el sistema 
- Permite a nuevos integrantes del equipo entender la arquitectura del sistema y ubicarse dentro de la solución
- Permite discutir con todos los stakeholders las distintas decisiones y validarlas en una etapa temprana

[[Patrones de Arquitectura del Software]]



