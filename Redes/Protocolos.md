---
Dia: 2025-08-22
dg-publish: true
---
## HTTP
Es Cliente Servidor. 
Permite transmitir texto formateado, imagenes, multimedia y mil cosas mas. 
- conexiones:
	- no persistentes (1 conexion por elemento)
	- persitente: puede mandar varios elementos juntos
- Cacheo de webs. Permitia utilizar copias locales. En servidores de cacheos.

## DNS 
Traduce o linkea un nombre con una IP. El nombre es faicl de recordar para nosotros. La IP es facil de recordar para las maquinas.
Es una [[Bases de Datos]] jerarquica y distribuida.
para la misma IP puede haber diferentes nombres.

Brinda tambien:
- host aliasing 
- Mail server aliasing
- Load distribution 

### Top Levels Domains TDLs
![[Pasted image 20250822205330.png]]

Al estar todo distribuido cada uno se encarga de su propias direcciones. Le pregunto a .AR donde estan los .UBA, le pregunta a .UBA donde estan los .FI... y asi... Eso es una consulta iterativa. Uno va preguntando uno por uno.


Cuando uno le pregunta al DNS local, este si no lo tiene cacheado, hace eso.

Para nosotros, usuario final, estariamos haciendo una consulta recursiva. Se lo pedimos y el nos devuelve.

Los roots no consultan recursivas, si uno les consulta simplemente dan la direccion a la que ir a consultar. Pero nunca te van a resolver la consulta ellos.

### Tipos de consult