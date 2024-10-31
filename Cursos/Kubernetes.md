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

Los pods pueden tener 1 o mas containers adentro. Este tiene una sola IP.

Como el pod es efimero, preferimos siempre desplegar 

### Deployments 
Un recutrso que nos permite instanciar pods de un mismo tipo 

Kubernetes te asegura que una determinada cantidad de Pods (campo replicas) este corriendo al mismo tiempo. Siempre voy a tener las replicas que pedi, 

Se pueden cambiar la cantidad de replicas (operacion `scale`) de manera continua usando `rolling updates`
Kubernetes va a estar guardando las versiones del mismo de deployement y va a ir swapeando entre la vieja y la nueva version.
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  strategy:
    rollingUpdate:
      maxUnavailable: 50%
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.25
        name: nginx
        resources:
          requests:
            cpu: 100m
            memory: 800Mi
          limits:
            cpu: 100m
            memory: 800Mi
                            
```




## Service 
Abstracciones que permiten direigir el trafico de un grupo de podes que provee un microservicio