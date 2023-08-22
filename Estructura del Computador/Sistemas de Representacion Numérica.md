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


# Decimales (representacion de numeros con parte fraccionaria)
### sistemas de punto fijo
la coma siempre esta en el mismo lugar. ej: el decimal. 
$$\sum^{n}_{i=0}di.bi+\sum^{n}_{i=1}di.b^{-1}$$
### sistemas de punto flotante
cuando opero con binarios y tengo por ej 8 bits, yo puedo elegir que la parte fraccionaria empiece a partir de cualquiera de las posiciones
| 4   | 2   | 1   | 0.5 | 0.25 | 0.125 |
| --- | --- | --- | --- | ---- | ----- |
| 0   | 1   | 1   | 1   | 0    | 0     |
| 
Estariamos hablando del 3.5, pero esos mismos espacios los podriamos haber asignado a otros pesos, segun conveniencia

Para pasar de decima a binario un numero fraccionario:
1) paso a binario la parte entera
2) la parte decimal la mutiplico n veces por dos, ahora ej
11, 32 a binario
parte entera 1011
parte binaria
$$0,32*2=0.64$$ $$0.64*2=1.28$$
$$0.28*2=0.56$$
$$0.56*2=1.18$$
Finalmente, la parte decimal se podria escribir como 0101, con un $2^{-4}$ de error (cota, error maximo

# Representacion de numeros con signo

## complemento a la base menos 1
el numero negativo lo represento como lo que le falta al numero para llegar total que tengo disponible (rango)

ej en binario:
00110101=53
el -53 va a ser el contrario, 11001010. A esto se lo llama complemento a la base menos 1

## complemento a la base 
en vez de tener como referencia el 11111111, va a tener el numero siguiente, el 100000000.
como tiene un bit mas, se hace la cuenta anterior y se le suma 1
11001011

==agregar foto del twos complement ones complement==

El complemento a la base es reversible, ya que puedo buscar de vuelta e complemento y sumar 1