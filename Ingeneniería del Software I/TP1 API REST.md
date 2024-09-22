# API 
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