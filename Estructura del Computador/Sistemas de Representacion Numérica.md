Un sistema numerico tiene conjunto de simbolos y reglas para su organizacion.

## Sistemas aditivos
Genero nuevos simbolos que representan diferentes numeros. Si palo es 1, talon es 10, etc. 21 es dos talones y una vara.

## Sistema arabigo
identico a actual, cantidad de simbolos limitadas, posicional y decimal. Es decir, de base 10.

# Sistema numerico posicional
queda definido por 
- simbolos
- cantidad de simbolos (base)
- peso de cada posicion(potencias crecientes de la base)
- cantidad de posiciones

En decimal: $digito_{0}.base_{0}+D_{1}.b_{1}$
siendo $b_{0}=10^0, b_{1}=10^1, etc$

>42 en binario

los pesos en binario son 
| 128 | 64  | 32  | 16  | 8   | 4   | 2    | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 0   | 1   | 0   |  1   | 0   |


- De cualquier base a base 10 -> multiplico las potencias y las sumo(en el ej de arriba $32*+8*1+2*1$)
- De base 10 a cualquier base -> busco los pesos y lo hago a ojo o divido n veces por la base
- entre do bases diferentes a 10-> paso por 10 jeje
- Bases potencias-> agrupar o desagrupar

ej: a ojo para saber cuantos digitos va a tener el 262 en binario miro los pesos (256, 128, 64, 32, 16,  8, 4, 2, 1) y me doy cuenta de que si o si voy a tener que incluir el 256. Por lo que voy a tener 9 digitos. 
==Los digitos de la derecha se llaman "mas significativos

# Rango de representacion
El rango de representacion de un procesador de:
- 8 bits: $2^8=256$
- 16 bits: $2^{16}=65536$
- 32 bits: 2^32= mucho


# 