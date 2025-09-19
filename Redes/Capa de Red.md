---
Dia: 2025-09-19
dg-publish: true
---
La capa de red la vamos a poder construir siempre basandonse en identificaciones unicas. Similitud con direcciones postales, son unicas. No hay dos direcciones 100% iguales ya que estas involucran departamento piso calle barrio codigo postal ciudad privincia pais continente. 

La idea es que nosotros salidmos d cierta direcciones B UNICA en el planeta. Armamos nuestro paquete con cierto protocolo de [[Capa de Aplicacion|aplicacion]], lo envolvemos en un paqute de [[Capa de Transporte]] y lo enviamos adentro de un paquete IP en la [[Capa de Red]]. Luego eso pasa por una capa de enlace al medio fisico. Cuando recibo hago el proceso inverso. 

>[!Important] Con leer solamente la parte de la capa de red ya sabemos que hacer con ese paquete. Si pasarlo o desempaquetarlo.



| Red | Host |
| --- | ---- |
|     |      |
|     |      |
|     |      |


Se separa la direccion en Red y Host. Solo tengo que mirar la red porque todos los hostos van a estar en el mismo lugar. Under the same address. Es como que diga Mar del Plata. Si quiero darle a la direccion San Martin en Mar del Plata primero me fijo como llegar a MDQ.

El router tiene una tabla donde mapea prefijos de hosts. Cuando le llega un paquete con un IP destino, mira ahi para ver donde mandarlo

hay 3 grupos de IP

Estos se identifican con mascaras que tienen 11111 en la parte de red y 00000 en la parte de host. Uno cuenta la cantidad de numeros y asi indica cual es largo en bytes del host

| Red    | Host   | Identificacion (como empieza) | Clase | Mascara |
| ------ | ------ | ----------------------------- | ----- | ------- |
| 1 Byte | 3 Byte | 0                             | A     |         |
| 2 Byte | 2 byte | 10                            | B     |         |
| 3 Byte | 1 Byte | 110                           | C     |         |
