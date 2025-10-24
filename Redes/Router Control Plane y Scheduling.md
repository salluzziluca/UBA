---
Dia: 2025-09-26
dg-publish: true
---
El **Control Plane** es como **Vialidad Nacional** que pinta los carteles en las rutas nacionales.

**Función principal:** Escribir la tabla de routeo.

Define **cómo** se construyen y actualizan las tablas que usa el [[Router Data Plane|Data Plane]].

## Scheduling de Colas

### Métodos de Lectura de Colas de Entrada

Las colas de entrada se pueden leer mediante:

- **[[Scheduling#Round Robin(RR)|Round Robin]]** - Turno rotativo entre colas
- **[[Scheduling#Cola FIFO|FIFO]]** - Primero en llegar, primero en salir
- **Colas de prioridad** - Según importancia del tráfico

### Tiempo de CPU Garantizado

Se le puede dar un **tiempo no aleatorio** de procesamiento asegurado:

En un tiempo total `t`, todas las colas de los puertos van a haber recibido un total de:

$$\frac{\text{CPU total}}{\text{cantidad de input ports}}$$

de tiempo de CPU.

## Manejo de Congestión

### Estrategia Preventiva

**Antes de que se congestione la red:**

1. Se **matan paquetes aleatorios** de cada uno de los buffers
2. Se **envían mensajes** a los respectivos usuarios avisando sobre congestión de red
3. **Resultado:** Todas las colas se liberan un poco y los usuarios son avisados

### Beneficios

- **Prevención proactiva** de colapso total
- **Distribución equitativa** del impacto
- **Notificación temprana** a los usuarios
- **Liberación gradual** de recursos

## Enlaces

- [[Router]] - Archivo principal
- [[Router Data Plane]] - Tabla de routeo y forwarding
- [[Scheduling]] - Algoritmos de scheduling
- [[Métricas de Performance]] - Optimización del rendimientos ent

