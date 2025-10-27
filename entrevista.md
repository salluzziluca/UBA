---
Dia: 2025-10-27
dg-publish: true
---
Inyección de dependencias en handlers
Cómo lo haces hoy
handlers.GetItemHandler(repo *store.Store) gin.HandlerFunc devuelve un closure que “captura” repo y lo usa para atender la request.
En main.go: v1.GET("/v1/items/:id", handlers.GetItemHandler(dataStore)).
Por qué es útil
Desacopla la capa HTTP de la persistencia: el handler no crea el Store, solo lo usa.
Facilita testing: en unit tests puedes pasar un store con datos de prueba (lo haces en handler_test.go).
Cómo lo haría aún mejor
Define una interfaz para el store y usa la interfaz en el handler:
Interfaz, por ejemplo: type ItemRepository interface { GetItem(id string) (models.Item, error) }
Firma: GetItemHandler(repo ItemRepository) gin.HandlerFunc
Beneficios: puedes pasar un mock en tests sin tocar filesystem; cambiar a Postgres/Redis sin tocar los handlers.
Consejo para entrevista: di “uso DI por constructor/closure para reducir acoplamiento; con una interfaz, habilito mocks e intercambiabilidad de backend”.