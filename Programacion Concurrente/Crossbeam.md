---
Dia: 2025-08-26
dg-publish: true
---
Crossbeam es un crate de concurrencia muy utilizado, provee estructuras de datos y funciones para concurrencia y paralelismo. crossbeam::scope crea un nuevo entorno de thread que garantiza que los threads terminan antes de retornar el closure que se le pasa como argumento a esta función. Todos los threads que no fueron manualmente esperados (join), son esperados antes de que nalice la invocación de la función. Si todos terminan exitosamente, se retorna Ok, si alguno ejecutó panic, se retorna Err