---
Dia: 2025-09-19
dg-publish: true
aliases:
  - Routers
  - Router
  - router
  - routers
---
# Router

Un router es como una **rotonda**, tiene diferentes salidas. Para ver por dónde salir uno mira los carteles y se orienta.

## Componentes y Tiempos de Procesamiento

Un router tiene:

- **Tiempo de procesamiento** - Para determinar la salida
- **Queue/Buffer** - Para manejar congestión
- **Tiempo de espera** (encolado) - Depende de la cantidad de paquetes en el buffer
- **Tiempo de inserción** - Entre que el paquete se procesó y entra al enlace
- **Tiempo de propagación** - Lo que tarda en viajar

## Arquitectura Básica

El paquete entra por el **input port**, pasa por la **switch fabric** que mapea a dónde tiene que mandarlo y sale por el **output** correspondiente. Esto es [[Network layer#Forward|forwarding]].

![[Pasted image 20250919201347.png]]

> [!warning] **Congestión HOL Blocking** Puede haber congestión si dos paquetes tienen que ir al mismo output, generando HOL blocking (paquetes rojos).

## Funcionamiento del Hash

1. Llega un paquete al router
2. Mira el **hash**, si da nulo se lo tira al **routing processor**
3. Este hace el [[Network layer#Routing|routing]]
4. Una vez que tiene el resultado, escribe en la función de hash que para esta IP tenés que ir a la salida X
5. La próxima vez que llegue esa IP ya conocida, directamente se hace [[Network layer#Forward|forwarding]]

![[Pasted image 20250919202727.png]]

> [!tip] Si está mal mapeado y se queda dando vueltas entre routers, eventualmente muere por el TTL (ver [[IPv4]])

Se busca **minimizar el routeo** y **optimizar la tabla** para mejorar las [[Metricas de Performance]].