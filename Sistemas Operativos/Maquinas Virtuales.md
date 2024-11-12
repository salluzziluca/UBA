---
dg-publish: true
---
>un entorno de computacion completo , con sus propias capacidades de procesamiento, memoria y etc.Virtualizcion el maximo
## Maquinas virtuales de lenguaje 
JVM, Microsoft common lang runtime

## Maquinas virtuales lightweight
[[Docker]]

## Maquinas Virtuales de sistema
Corre un SO completo sin modificaciones (o casi)

### objetivo
Ejecutar multiples SO sobre el mismo hardware
para esto se utlizan virtual machines monitors

### Motivacion 
-  Diversidad de SO
- Consolidacion de Servers (para separar mejor diferentes partes de un sistema en un mismo hardware)
- Aprovisionaiento rapido
- alta disponibilidad
- seguridad
- scheduing de recursos distribuidos
- clud computin

## Requerimientos
Fidelidad: el hardware virtua tiene que ser igua al real que corre por debajo
Seguridad: tienen que estar bien sepaadas
Eficiencia: que corra bien

### Emulacon 
Tranfora instrucciones 

### EJeucin direta