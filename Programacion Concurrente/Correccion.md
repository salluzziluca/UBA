---
Dia: 2025-09-09
dg-publish: true
---
En procesos (programas secuenciales) basta con debuggear para encontrar errores, ya que ante una misma entrada se obtiene siempre la misma salida.  
En programas concurrentes, la salida puede depender del escenario que resultó en la ejecución.

## Propiedades de Corrección

- **Safety** → debe ser verdadera siempre.
- **Liveness** → debe volverse verdadera eventualmente.

### Safety
- **Exclusión mutua**: dos procesos no deben intercalar ciertas subsecuencias de instrucciones. Ejemplo: incremento de variable global en la [[Sección Crítica]].
- **Ausencia de [[Deadlock]]**: un sistema que aún no finalizó debe poder continuar realizando su tarea (avanzar productivamente).

### Liveness
- **Ausencia de [[Starvation]]**: todo proceso listo para usar un recurso debe recibirlo eventualmente.
- **Fairness (justicia)**: un escenario es *débilmente fair* si una instrucción que está continuamente habilitada eventualmente aparece en el escenario.

El problema de la **exclusión mutua** se estudia en la [[Sección Crítica]].
