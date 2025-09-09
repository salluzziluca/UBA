---
Dia: 2025-09-09
dg-publish: true
---
Los **[[Locks]]** sirven para realizar **exclusión mutua** entre procesos y proteger la [[Sección Crítica]].

## Concepto
- Se implementan mediante variables de tipo *[[Locks|lock]]*, que contienen su estado.
- Métodos principales:
  - `lock()`: el proceso se bloquea hasta poder obtener el [[Locks|lock]].
  - `unlock()`: el proceso libera el [[Locks|lock]] previamente tomado.

## Requisitos
- Se necesita soporte del **hardware** y del **sistema operativo**.

Existen implementaciones específicas como [[Locks en UNIX]] y [[Locks en Rust]].
