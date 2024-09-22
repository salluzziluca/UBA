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