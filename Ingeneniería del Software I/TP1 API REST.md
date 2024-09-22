# API 

## Endpoints de usuario:

### 1. Registros de usuarios:
-  POST: /api/v1/user/registers
- BODY: 
  ```json 
  {
  "email": "email@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "birthdate": "1990-01-01",
  "gender": "male",
  "avatar": "avatar_url"
}
```
- Response: 201 Created, 400 Bad Request si hay datos inválidos o el email ya está registrado.
### 2. Login
Descripción: Permite que los usuarios inicien sesión.
Request:
- Headers: `Authorization: Basic {base64(email:password)}`
- POST `/api/v1/users/token`
Response:
Código HTTP: `200 OK
```json 
{
"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
"refresh_token": "m9obiBEb2UiLCJpYXQiOjE1MTYyMzkwMj..."
}
```
Código HTTP: `401 Unauthorized si las credenciales son incorrectas.`


### 3. Ver Perfil 
- GET: `/api/v1/user/me`
- AUTH: bearer token 
- Response: 200 OK con la info del usuario logeado

### 4. Editar perfil
-  PUT: `/api/v1/users/me`
- AUTH: bearer token
- Request Body:
```json 
{
  "first_name": "John",
  "last_name": "Doe",
  "avatar": "new_avatar_url"
}
```
- Response: 200OK, 400 Bad Request si hay datos invalidos 

### 5. Eliminar cuenta
- DELETE: `/api/v1/users/me`
- AUTH: bearer token
- Response: 204 No content

### 6. Seguir a otro user: 

- POST `/api/v1/users/{id}/follow` (anteriormente podriamos obtener el ID de ese user mediante un get con una busqueda. Por ejemplo: `GET /api/v1/users/search?name={nombre}`
)
- AUTH: Bearer Token
- Response: 200 OK si se envió la solicitud de seguimiento 

### 7. Aceptar/Rechazar Solicitud de Seguimiento
- PUT: `/api/v1/user/{id}/follow-request
- AUTH: Bearer token
- Request Body 
```json 
{
"status": "accepted"//or rejected
}
```
Response: 200 OK

## Endpoints de Peliculas 
### 1. Listar películas con filtros:

- GET `/api/v1/movies?title={title}&actor={actor}&category={category}`
Query Params: `title, actor, category`
Paginación: `page, limit
Response: 200 OK con una lista paginada de pepliculas

### 2. Calificar pelicula
- POST `/api/v1/movies/{id}/rating`
- Authorization: Bearer Token
- Request Body:
```json
{
  "rating": 8
}
```
- Reponse: 201 Created, 400 bad request si el rating es invalido

## Endpoints ADMIN:

1. CRUD de películas:
    
    - POST `/api/v1/admin/movies`
    - PUT `/api/v1/admin/movies/{id}`
    - DELETE `/api/v1/admin/movies/{id}`
2. CRUD de actores:
    
    - POST `/api/v1/admin/actors`
    - PUT `/api/v1/admin/actors/{id}`
    - DELETE `/api/v1/admin/actors/{id}`
3. CRUD de categorías:
    
    - POST `/api/v1/admin/categories`
    - PUT `/api/v1/admin/categories/{id}`
    - DELETE `/api/v1/admin/categories/{id}`
4. Gestión de usuarios ADMIN:
    - `POST /api/v1/admin/users`
    - `PATCH /api/v1/admin/users/{id}`
    - `DELETE /api/v1/admin/users/{id}`
    - Response: `201 Created`, `200 OK`, `204 No Content`


# Propuesta de Arquitectura preliminar
Me parece que una buena opcion debido a la simplicidad de la aplicacion movil en cuestion es la utilizacion de el patron de arquitectura de software `Layers`. Esto nos permitira diseñar una arquitectura simple, con una curva de dificultad muy baja y que se adaptará facilmente a los requerimientos tecnicos que necesitamos.
Contariamos, entonces, con 3 capas principales

## Capa de Presentación (controller layer)
Aca se gestionaran las solicitudes HTTP, como el login o la busqueda de peliculas. Los diferentes controladores recibiran las peticiones y las enviaran mediante los endpoints declarados anteriormente a la capa de negocio.

## Capa de negocio.