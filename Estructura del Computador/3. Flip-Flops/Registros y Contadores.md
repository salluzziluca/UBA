## Registro
Es la memoria interna del procesador, muy acotada (64,32,16 u 8 bits).
### Registros de almacenamiento
![[Pasted image 20230926164833.png]]

### Registros de desplazamiento
![[Pasted image 20230926165555.png]]

| Q0  | Q1  | Q2  | Q3  |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 0   |
|  1   |   1  |  1   | 1    |

Suponiendo que la entrada SI siempre sea 1

## Carga de datos en paralelo
![[Pasted image 20230926171353.png]]
Dependiendo del valor de LD la entrada/salida es en serie o paralelo

Por ejemplo: una impresora recibe informacion en serie de la pc y al llegar a 16 bits, cambia y los hace salir (internamente) en paralelo.

Para saber cuando se llega a 16 bits, utilizamos...

## Contadores
Los contadores tienen $2^{flip-flop}$ estados. Siempre avanza secuencialmente.
Si yo necesito 10 estados lo minimo que puedo usar son 4 flipflops, por lo que me sobran 6 estados