Una computador puee hacer tareas complejas con modos de operaciones MUY simples

La componen:

- Unidad arimético-lógica
- I/O
- memoria de instrucciones
- memoria de datos


Todo esto está gestionado por la CPU
![[Pasted image 20231107180202.png]]


### Estructura tipo BUS 
Un sistema de comunicacin de transferencia de datos, un solo cable sale de la PC y este lo comunica con, por ejemplo, todos las posiciones de memoria (indexadas por numero)
![[Pasted image 20231107180626.png]]

Esto, sumada a la arquitectura von neumann
![[Pasted image 20231107180912.png]]
El procesador avisa mediante el address bus que dispositivo levantar

Otro modelo de buses, con buses independientes
![[Pasted image 20231107181939.png]]

RISC utiliza un solo bus, simple y optimizable
![[Pasted image 20231107182204.png]]


## Arquitectura de un microprocesador
Bajo un mismo set de instrucciones puedo tener +1 Implementaciones:
- Hardware para mayor velocidad
- Hardware para menor costo 
hardware para menos consumo

Su funcion es ejecutar programas, es decir:
#### Ciclo de fetch
1. Buscar en memoria la instruccion
2. decodificar el codigo de la misma
3. ejecutarla
4. volver a 1
### Microarquitectura
![[Pasted image 20231107183723.png]]
Unidad de control
unidad arimetico-logica
registros visibles al programador (ej: r0 a r31)
registros adicionales necesaris para el control pero invisibles al programador


## ALU 