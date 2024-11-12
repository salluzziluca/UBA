---
dg-publish: true
---
- Unit testing
- Integration testing
- System testing

### Pruebas de verificacion
El programa funciona como es debido. 
![[Pasted image 20220922143343.png]]
E2E son un subconjunto de System testing

Para estas pruebas se suelen usar objetos ficticios para simular funcionamientos normales del programa (por ejemplo, en vez de usar la [[Bases de Datos|base de datos]], simulamos los protocolos).

Adicionalmente, estas pruebas pueden ser de caja blanca o negra

### Pruebas de usuario o de validación
Chequeamos que el programa sea lo que el usuario quiera.
Suelen ser diseñadas en conjunto o por los usuarios
Dentro de este tipos de pruebas entras las alpha y las betas. Siendo las primeras corridas en un entorno controlado y las segundas siendo corridas en un entorno propio del usuario.

Las pruebas de comportamiento son una subclase de las de usuario en las que simulamos el input del usuario sin ningun tipo de interfaz grafica.
### Pruebas funcionales
Cosas que no pueden pasar

### Pruebas  no funcionales
Cosas que pueden pasar pero que no deben (e.g. el programa no tiene que tardar mas de 1 minuto en cargar. El programa se tiene que ejecutar en todas las plataformas necesarias.)
![[Pasted image 20220922142658.png]]


## Quienes deben formar parte de las pruebas?
![[Pasted image 20220922151545.png]]