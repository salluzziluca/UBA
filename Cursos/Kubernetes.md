---
Dia: 2024-10-31
---
Kubernetes es una tecnologia [[Cloud Native]]
Es un [[Docker#Contenedores|container]] orchestration engine
Nace para resolver [[Docker#Desafios de implementar docker|los desafios de implementar docker]]

## Arquitectura de Kubernetes (Alto Nivel)
![[arqutectura cluster kubernetes]]

Kubernetes le asigna dos roles a los servidores, master y workers.
Para interactuar con los servidores uso una API.

<mark style="background: #FFB8EBA6;">Un master (replicado n veces) y varios workers conforman un Cluster.</mark>


el kubectl le pega primero al balanceador de carga y este redirige a los masters


### Masters
Son la mente central, solo buscan mantener y sincronizar el estado de todo el cluster

Pueden ser varios. Como tiene que ser redundante, [[cloud native]], etc, se usan varios para que sea redundante en caso de [[fallas]].

### Workers 

Corren los pods de nuestras apps.

Los pods pueden



