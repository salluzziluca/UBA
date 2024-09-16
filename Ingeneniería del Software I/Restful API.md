> Una manera de poenr la cpa de servicio para poder ser comunicada por otro proceso 

No es un standard, no es un protocolo, no es un reemplazo de SOAP, no es una biblioteca

Surge de la tesis de Roy Fielding en el 2000. Significa representational State Transfer. Busca que la vista no cambie. En vez de pedirle al server una vista nueva con la info cambiada se le pide solo la info.

Se presenta en 3 niveles de madurez. 

Se utiliza en arquitecturas cliente-servidor 
El servidor es stateless. Evitar que el servidor tenga que guardar sessions IDs del cliente, hacer que el cliente se encargue de sus sesiones. 
Es cacheable.
Expone recursos (URIs)
Utiliza los vervos HTTP (get, post, put)
Es navegable (por ahi una respuesta nos da una url a otro recurso para seguir navegando)

## Stateless
Cada request se ejecute de forma independiente del resto 
Cada req contieen toda la info necesaria para completarse
La api no matiene sesion
Se promueve el uso de tokens por seguiridad


## Cacheable 
El metodo mas sencillo para mejorar la performance. Si se utiliza mucho la misma respuesta, la cacheo. Utilizando etiquetas en los headers para saber si es cacheable, por cuanto tiempo, etc