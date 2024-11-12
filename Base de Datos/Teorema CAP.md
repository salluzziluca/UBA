---
Dia: 2024-10-29
dg-publish: true
---
Mom

o relojero
Osi osi 

En 1998 Brewer postulo la imposibilidad de que un sistema de base de datos distribuido garantice simultaneamente el maximo nivel de 
Consistency 
Availability 
Partition Tolerance 

en 2002 se demostro


## Consistencia 
Que en un instante determinado el sistema muestre un unico valor de cada item de los datos. Esto requiere alto nivel de sincronizacion

## Availability 
En todo momento un nodo tiene que poder responder (por ahi erroneamente, desactualizado, pero tiene que repsonder)


## Tolerancia a particiones 
El sistema pueda repsonder consultas con algunas conexiones caidas.


---

## AP

Si la red está particionada, podemos optar por seguir respondiendo consultas aún cuando algunos nodos no respondan. Garantizaremos disponibilidad, pero el nivel de consistencia no será el máximo.

Si consulto cuando el dato esta viajando, no llego a consistencia total
## CP
Con la red particionada, si queremos garantizar consistencia máxima no podremos garantizar disponibilidad. Es posible que no podamos responder una consulta en forma efectiva porque esperamos mensajes de confirmación desde nodos que no pueden comunicarse.
Si te contesto rapido, no voy a estar respondiendo siempre el mismo, si repsondo siempre el mismo, voy a tardar

## CA

Si queremos consistencia y disponibilidad, entonces no podremos tolerar que una cantidad indeterminada de enlaces se caiga



# Propiedades BASE 

BasicAvailability: EL SGBD esta siempre en funcionamiento, aunque eventualmente puede devolvernos un error, o un valor desactualizado 

Soft State: Estado débil (soft state): No es necesario que todas los nodos réplica guarden el mismo valor de un ítem en un determinado instante. No existe entonces un “estado actual de la base de datos”

Consistencia eventual (eventual consistency): Si dejaran de producirse actualizaciones, eventualmente todos los nodos réplica alcanzarían el mismo estado.

asdajdsj