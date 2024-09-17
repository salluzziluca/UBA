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


## URIs 
Unifor resource iidentifier
Identificacion univica de recursos con cadenas de carateres 
Identifica los recursos por clase o tipo
Uso de sustantivos en prular por convencion (NO VERBOS)
Distinción de recursos principales y subordinados


/clientes 
/clietnes?nombre=juan (clientes con nombre juan)
clientes/1/compras (las compras del cliente de ID = 1)


## Verbvos HTTP 
- GET: solicita una representación de un recurso específico
- POST: se utiliza para enviar una entidad a un recurso en específico (para crear)
- DELETE: borra un recurso en específico
- PUT: reemplaza todas las representaciones actuales del recurso de destino con la carga útil
de la petición (modificar)
- PATCH: aplica modificaciones parciales a un recurso (a diferencia de PUT)
- OPTIONS: es utilizado para describir las opciones de comunicación para el recurso de
destino

## HTTP status codes - Responses
- 1xx: Informational
 - 2xx: Success
- 3xx: Redirection
 - 4xx: Client Error
- 5xx: Server Error

200 - OK
201 - Created (con el location en el header)
400 - Bad Request
401 - Authorization Required
404 - Not Found
405 - Method Not Allowed
408 - Request Time-Out
409 - Conflict
422 - Unprocessable Entity
500 - Internal Server Error
502 - Bad Gateway
504 - Gateway Time-Out

## REST Security Desing Principles 
- Least Privilege: Tener el menor privilegio requerido para hacer las acciones.
- Fail-Safe Defaults: Por defecto no tener acceso a los recursos
- Complete Mediation: El sistema debe validar los permisos de acceso a todos los recursos
- Keep it Simple
- Https
- Password Hashes: (PBKDF2, bcrypt, y scrypt)
- Never expose information on URLs: Usernames, passwords, session tokens, y API keys deberían no aparecer en la URL para evitar ser logueadas en los logs de web server logs
- Considerar agregar Timestamp en los requests.
- Validación de los parámetros de entrada
- Monitorear transacciones sospechosas. Si se me rompe algo y empiezo a tirar request a lo loco con una API paga puedo llegar a cagarla (tema guita)
## Auth 
### basic auth

encodea en base64 user:password
![[Pasted image 20240916201943.png]]
Es facilmente decodificable, se debe usar con un https/sll
### API Keys
Es un token que el cliente provee cuando hace la llamada

![[Pasted image 20240916202848.png]]

La gracia es que solo el cliente y el SV la saben 
### Bearer Authentication 
Es como una tarjetita de seguridad, con eso podes ir a otros servicios que necesiten auth
### OAuth
delego la autenticacion a un sv de tercero, por ejemplo, google.

![[Pasted image 20240916203902.png]]

## Autenticacion y autorizacion JWT
El token se genera en el primero paso. Se hacer un post /token{user;"", pass:""}
y la respuesta es eltoken. Esta credencial viaja una vez. En token no se almacena del lado del server para validar. Si el sv lo recibe en algun momento él puede chequear que lo envio, si esta firmado por el (si alguien lo modifica esa firma se sobreescribe) ya sabe que estas bien autenticado.y si ![[Pasted image 20240916205335.png]]

cualquiera puede leer su contenido, pero si no se conoce su clave privada no puede ser modificado (porque cuando el sv reciba de nuevo el JWT se va a dar cuenta de que algo está mal)

![[Pasted image 20240916210849.png]]
![[Pasted image 20240916211007.png]]


## Refresh token 
Los acces token tienen tiempo limitado de vida. Es una cred que permite obtner nuevos tokens sin necesidad de que te vuelvas a logear. Cuando se vence la credencial se reenvia el resfresh token (que se usa cada x tiempo)


# Versionado 
Rest no provee mecanidsmo para versuionado per se suelen ver estas estrategias: 

- Usando la URI:
	`https://api.fi.uba.ar/v1`
	`https://apiv1.fi.uba.ar`
	`https://api.fi.uba.ar/20211101/`
- Usando un Custom Header:
	`Accept-version: v1
	`Accept-version: v2
- Usando el Header Accept:
	`Accept: application/vnd.example.v1+json
	`Accept: application/vnd.example+json;version=1.

# Respuestas 
Mantenerlas lo mas estandarizads posibles
Reducir el tamaño de la respuesta a lo necesario 
Utilizar codigo de errores HTTP

```json
HTTP CODE: 401 {
 "success": false, // solo informativo, el error se define por el HTTP CODE
 "message": "Invalid email or password",
 "error_code": 1308,
 "data": {}
}
HTTP CODE: 200 {
 "success": true,
 "message": "User logged in successfully", // optional in success responses
 "data": { }
}
```
 otro 
 ```json 
 {
 "success": true,
 "message": "User found",
 "data": {
 "user": {
 "id": 2,
 "name": "Juan",
 "email": " juan@fi.uba.ar ",
 "city": {
 "id": 3,
 "name": "Buenos Aires",
 "country": {
 "id": 2,
 "name": "Argentina",
 "code_country": "AR",
 "avatar": " //localhost:3000/api/v1/country_AR.png ",
 }
 }
 },
 "role": "client",
 "favorites": ["blue", "red", "white"]
 }
}
```