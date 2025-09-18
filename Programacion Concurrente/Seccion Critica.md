---
Dia: 2025-09-09
dg-publish: true
---
## Definición del Problema
Cada proceso se ejecuta en un loop infinito, cuyo código se divide en:
- **Parte crítica**
- **Parte no-crítica**

### Especificaciones de corrección
- **Exclusión mutua**: no deben intercalarse instrucciones de la parte crítica.
- **Ausencia de [[Deadlock]]**: si dos procesos intentan entrar a la parte crítica, eventualmente alguno debe tener éxito.
- **Ausencia de [[Starvation]]**: si un proceso intenta entrar a la parte crítica, eventualmente debe tener éxito.

## Observaciones
- La parte crítica debe **progresar** (finalizar eventualmente).
- La parte no-crítica **no requiere progreso** (el proceso puede terminar o entrar en loop infinito).

Estos problemas se resuelven usando [[Locks]].
