---
Dia: 2025-04-09
dg-publish: true
---
>[!quote] “Trying to improve software quality by increasing the amount of testing is like trying to lose weight by weighing yourself more often.”
> (Steve McConnell, “Code Complete”)

## Que es la calidad? 
Es un atributo del producto. 

>[!quote] Quality is the degree to which a set of inherent characteristics … satisfy the customer stated or implied needs”
PMBOK, 7th Edition

>[!quote] “Quality is value to some person”
Weinberg, Gerald M. Quality Software Management. Volume 1: Systems Thinking. New York: Dorset House Publishing, 1992

Lo que nostros usualmente llamamos [[Testeo]] es en realidad Control de Calida (QC)


## Como probamos el producto?
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUepLFZQ80uDdrIR3GRfKG7LvB6HKJpnPtji25pnjMZSZI47D8HUS6SkP_WssLqDkF2FGTCb7SLDv97GVwA1fE3JnNqqWXZfVxlRqnqshb7AVeOqCpwruowPLrmwCpiDgxap4ljgq0mhQU-Q27895z4=s2048?key=C3GRf55xXz4dfeiioTsKxm9H)
Verificacion (yo construi lo que queria construir): 
- revision de pares
- pruebas unitarias 
- pruebas de componentes 

Validacion(yo construi lo que el cliente me dijo que queria tener): 
-  Pruebas de comportamiento (user sin UI)
- UAT (punta a punta)
- Validacion en produccion: A|B, canary, monitoreo, etc.

## Prevencion 
La mejor forma de escribir mejor codigo no es testeando todo mil veces, es mejorando la construccion.
Prevención >> Reparación

Las inspecciones y pruebas generan retrabajo y desperdicio y mayores costos
Hay que usar procesos que incorporen la calidad durante el desarrollo
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeaKtcySvfltMmwRWMQ6UuBBudrJuhqjOD7A95Kzq5fYER5mBPxgDxYGWYvp_42AfFsc7WeMUX0seYc_u_COb6OA4EyGhS21AAbHz340sgiKCXDu4kfHVfCz3a4-4zlzinlicn9KRHo0oj07-u7rK8=s2048?key=C3GRf55xXz4dfeiioTsKxm9H)

### Regresiones 
Fallas debidas a cambios con efectos inesperados

Fallas en producción: una vez que los usuarios ya lo tienen en sus manos

Hay que evidenciarlo con pruebas, primero que falle, despues lo corrijo 

## Costos de la calidad 

### Costos de la prevencion 
Costos para prevenirque los clientes reciban un producto defectuoso. 

#### Costo del proceso 
Definir bien el producto, bien entrenados a los devs, buen equipamiento y herramientas, tiempo para hacerlo bien

#### Costo de evaluacion 
pruebas e inspecciones 
### Costo de reparacion 
Costo de fallas internas (antes de entregar)
