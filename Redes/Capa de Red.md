---
Dia: 2025-09-19
dg-publish: true
---
La capa de red la vamos a poder construir siempre basandonse en identificaciones unicas. Similitud con direcciones postales, son unicas. No hay dos direcciones 100% iguales ya que estas involucran departamento piso calle barrio codigo postal ciudad privincia pais continente. 

La idea es que nosotros salidmos d cierta direcciones B UNICA en el planeta. Armamos nuestro paquete con cierto protocolo de [[Capa de Aplicacion|aplicacion]], lo envolvemos en un paqute de [[Capa de Transporte]] y lo enviamos adentro de un paquete IP en la [[Capa de Red]]. Luego eso pasa por una capa de enlace al medio fisico. Cuando recibo hago el proceso inverso. Ya sea un [[Router]] o un host final

>[!Important] Con leer solamente la parte de la capa de red ya sabemos que hacer con ese paquete. Si pasarlo o desempaquetarlo.


ver [[Mascara de Red]]


Se separa la direccion en Red y Host. Solo tengo que mirar la red porque todos los hostos van a estar en el mismo lugar. Under the same address. Es como que diga Mar del Plata. Si quiero darle a la direccion San Martin en Mar del Plata primero me fijo como llegar a MDQ.

El [[router]] tiene una tabla donde mapea prefijos de hosts. Cuando le llega un paquete con un IP destino, mira ahi para ver donde mandarlo



![[IPv4]]


![[IPv6]]
