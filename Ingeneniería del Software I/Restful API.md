> Una manera de poenr la cpa de servicio para poder ser comunicada por otro proceso 

No es un standard, no es un protocolo, no es un reemplazo de SOAP, no es una biblioteca

Surge de la tesis de Roy Fielding en el 2000. Significa representational State Transfer. Busca que la vista no cambie. En vez de pedirle al server una vista nueva con la info cambiada se le pide solo la info.

Se presenta en 3 niveles de madurez. 

Se utiliza en arquitecturas cliente-servidor 
El servidor es stateless. Evitar que el servidor tenga que guardar sessions IDs del cliente, hacer que el cliente se encargue de sus sesiones. 
Es cacheable.
Expone recursos (URIs)