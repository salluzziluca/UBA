---
Dia: 2025-10-27
dg-publish: true
---
Inyección de dependencias en handlers
Cómo lo haces hoy
`handlers.GetItemHandler(repo *store.Store) gin.HandlerFunc` devuelve un closure que “captura” repo y lo usa para atender la request.
En `main.go: v1.GET("/v1/items/:id", handlers.GetItemHandler(dataStore)).`
Por qué es útil
Desacopla la capa HTTP de la persistencia: el handler no crea el Store, solo lo usa.
Facilita testing: en unit tests puedes pasar un store con datos de prueba (lo haces en handler_test.go).
Cómo lo haría aún mejor
Define una interfaz para el store y usa la interfaz en el handler:
Interfaz, por ejemplo: type ItemRepository interface { GetItem(id string) (models.Item, error) }
Firma: GetItemHandler(repo ItemRepository) gin.HandlerFunc
Beneficios: puedes pasar un mock en tests sin tocar filesystem; cambiar a Postgres/Redis sin tocar los handlers.
>[!tip] Consejo para entrevista: di “uso DI por constructor/closure para reducir acoplamiento; con una interfaz, habilito mocks e intercambiabilidad de backend”.



## Métricas expuestas y etiquetas elegidas

- Qué expones
    - `http_requests_total{method,path,status}` como counter.
    - `http_request_duration_seconds{method,path}` como histogram.
    - Código en [metrics.go](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html).
- Por qué esas etiquetas
    - Bajan cardinalidad: [method](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) y [path](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) tienen pocos valores estables.
    - [path](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) se obtiene con [c.FullPath()](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) que da la ruta parametrizada (ej. `/v1/items/:id`), evitando que IDs distintas creen series infinitas.
    - [status](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) es numérico en `http_requests_total` para diagnósticos finos por código.
- Detalles finos
    - Si la ruta no está registrada, usas [path = "unregistered"](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) para no explotar cardinalidad.
    - Excluyes `/metrics` y `/favicon.ico` para que los scrapes de Prometheus no sesguen las métricas.

>[!important] Consejo: explica la diferencia entre Counter (monótono) y Histogram (distribución + quantiles), y que las etiquetas fueron pensadas para estabilidad de series.



## CORS: headers permitidos y razones

- Config en [main.go](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) usando `github.com/gin-contrib/cors`:
    - Orígenes permitidos: `http://localhost:3000` (dev SPA) y `https://mercadolibre.com.ar` (prod).
    - Métodos: `GET, OPTIONS` (lo que expone tu API).
    - Headers: `Origin, Content-Type, Accept`.
    - Sin credenciales ([AllowCredentials: false](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)) para simplificar seguridad y evitar restricciones de CORS con cookies.
    - [ExposeHeaders: ["Content-Length"]](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) útil para clientes que quieran conocer tamaño.

Notas para entrevista:
>[!warning]  Si en el futuro usas credenciales (cookies/Authorization con credenciales), no puedes usar wildcard y debes declarar orígenes explícitos.
>En despliegues multi-ambiente, estos orígenes deberían venir de configuración (env).


Hcie separation of concers con inyeccion de dependencias en handler
use regex
se podria usar user feature flags para cambiar cosas como el rate limit o el regex en caliente utilizando punteros. se crea una atomic value, si compila. se reemplaza

extraer config data path, ports, CORS, límites

hay un middleware con request id para identificar cada uno de los 


Si hay muchos 429 (rate limit exceeded) hay que subir la ventana de del ratelimit. Tambien tiene de malo que es global y no de cada proceso. Se podria hcer por IP 
Rate limiting por rol/scope/tenant


Gracefu shutdown


liveness vs readiness


Reintentos solo si la operación es idempotente o sabemos que repetirla es seguro. Se podria armar para que los 500 sean retriables

Circuit breaker: corta llamadas a un backend que está fallando de forma sostenida para evitar “martillar” y acelerar la recuperación (fail-fast).

 GET es seguro de reintentar; no reintentes POST/PUT sin idempotency keys.

logs mas profundos desde middleware
- - request_id, timestamp, client_ip (si aplica), path, method, status, latency_ms.
    - Identidad no sensible: user_id/sub (hash/anónimo), tenant, scopes/roles.
- Formato:
    - JSON estructurado consistente; así lo ingerís en SIEM/ELK/CloudWatch fácilmente.