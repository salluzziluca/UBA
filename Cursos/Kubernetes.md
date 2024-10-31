---
Dia: 2024-10-31
---
Kubernetes es una tecnologia [[Cloud Native]]
Es un [[Docker#Contenedores|container]] orchestration engine
Nace para resolver [[Docker#Desafios de implementar docker|los desafios de implementar docker]]

## Arquitectura de Kubernetes (Alto Nivel)

Kubernetes le asigna dos roles a los servidores, master y workers.
Para interactuar con los servidores uso una API.

Un master (replicado n veces) y varios workers conforman un Cluster.


### Masters
Son la mente central, solo buscan mantener y sincronizar el estado de todo el cluster

Pueden ser varios. Como tiene que ser redundante, [[cloud native]], etc, se usan varios para que sea redundante en caso de [[fallas]].



