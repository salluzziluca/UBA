---
Dia: 2025-09-26
dg-publish: true
---
---

## Definición

El **Data Plane** define qué debe hacer cada paquete para encontrar su destino.

Utiliza la **Tabla de Routeo**.

## Tabla de Routeo

|Prefijo|Next Hop|
|---|---|
|x.x.x.x/4|a dónde ir|

## Proceso de Forwarding

1. **Paquete entra** por el input port
2. **Switch fabric** mapea a dónde tiene que mandarlo
3. **Sale** por el output correspondiente

Este proceso se llama [[Network layer#Forward|forwarding]].

![[Pasted image 20250919201347.png]]

## Problemas de Congestión

**HOL Blocking (Head-of-Line Blocking):**

- Ocurre cuando dos paquetes tienen que ir al mismo output
- Se representan como paquetes rojos en el diagrama
- Genera colas y demoras

## Optimización

**Hash Lookup:**

- Primera vez: paquete va al routing processor
- Se actualiza la tabla hash con el resultado
- Próximas veces: lookup directo sin procesamiento adicional

![[Pasted image 20250919202727.png]]

**Objetivos:**

- Minimizar el routeo
- Optimizar la tabla para mejorar las [[Métricas de Performance]]

## Enlaces

- [[Router]] - Archivo principal
- [[Router Control Plane]] - Escritura de tablas
- [[Router Scheduling]] - Manejo de colas