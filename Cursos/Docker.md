> Docker makes development efficient and predictable

Docker nos permite trabajar con un estandar para que en el servidor y lo que esta en nuestro pc tenga las mismas caracterisiticas. 
Emula el Sistema Operativo en el que se van a correr las cosas y redistribuye sabiamente los recursos (no como una VM)

## Imagenes 
El original de la app que queremos correr
Podemos crear las nuestras y customizarlas

Una imagen esta constuida en capas.
## Contenedores
Cerrado y aislados, pensados para ser despreciables
Es muy eficiente que varios contenedores corran en paralelo en la misma pc. Con VMs eso es bastante demandante para el sistema

## Dockerfile
A partir de él se crea nuestra imagen, nos permite customizar.

## Dockercompose
Nos permite ejecutar varios contenedores al mismo tiempo.


# Desafios de implementar docker 
- Conectividad entre contenedores entre diferentes maquinas
- Rollback en todos los hosts en caso de [[fallas]] 
- Despliegue de conetndores en varios hosts 
- balanceo de carga 
- actualizacion de los servicios con control de downtime. No esta bueno tener que hacer docker stop y docker run 