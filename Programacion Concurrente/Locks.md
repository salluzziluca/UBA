---
Dia: 2025-09-09
dg-publish: true
---
Los **[[Locks]]** sirven para realizar **exclusión mutua** entre procesos y proteger la [[Sección Crítica]].
Un lock es una variable que permite la sincronización mediante la
exclusión mutua, cuando un thread tiene el candado o lock ningún
otro puede tenerlo.

```c
while(true){
int transferencia= nextTranferencia();
obtener(lock);
//seccion critica
dejar(lock);
}
```
Mutual Exclusion: Un solo thread puede usar el lock a la vez
Progress: Si nadie tiene el lock y alguien lo quiere, alguno debe poder obtenerlo
Bounded Waiting: si un thread quire acceder aun thread y existen varios en la misma situacion, los demas tienen una cantidad finita (un limite) de posibles accesos antes que T lo haga. 

## Concepto
- Se implementan mediante variables de tipo *[[Locks|lock]]*, que contienen su estado.
- Métodos principales:
  - `lock()`: el proceso se bloquea hasta poder obtener el [[Locks|lock]].
  - `unlock()`: el proceso libera el [[Locks|lock]] previamente tomado.

## Requisitos
- Se necesita soporte del **hardware** y del **sistema operativo**.

Existen implementaciones específicas como [[Locks en UNIX]] y [[Locks en Rust]].
