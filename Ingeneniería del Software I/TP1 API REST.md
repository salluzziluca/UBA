# API 

### Endpoints de usuario:

1. Registro de usuarios:**
    
    - **POST /api/v1/users/register**
    - **Request Body:**
        
        json
        
        Copy code
        
        `{   "email": "email@example.com",   "password": "password123",   "first_name": "John",   "last_name": "Doe",   "birthdate": "1990-01-01",   "gender": "male",   "avatar": "avatar_url" }`
        
    - **Response:**
        - 201 Created, 400 Bad Request si hay datos inválidos o el email ya está registrado.

****
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


### v