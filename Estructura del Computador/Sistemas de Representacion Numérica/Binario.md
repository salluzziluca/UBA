El sistema binario es un [[Sistema Numerico Posicional|sistema numérico posicional]] 

sus pesos son

| 128 | 64  | 32  | 16  | 8   | 4   | 2    | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |


Ej: 42 en binario

| 128 | 64  | 32  | 16  | 8   | 4   | 2    | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 0   | 1   | 0   |  1   | 0   |


- De cualquier base a base 10 -> multiplico las potencias y las sumo(en el ej de arriba $32*+8*1+2*1$)
- De base 10 a cualquier base -> busco los pesos y lo hago a ojo o divido n veces por la base
- entre dos bases diferentes a 10-> paso por 10 jeje
- Bases potencias-> agrupar o desagrupar

ej: a ojo para saber cuantos digitos va a tener el 262 en binario miro los pesos (256, 128, 64, 32, 16,  8, 4, 2, 1) y me doy cuenta de que si o si voy a tener que incluir el 256. Por lo que voy a tener 9 digitos. 
==Los digitos de la derecha se llaman "mas significativos"

## Rango de representacion
El rango de representación de un procesador de:
- 8 bits: $2^8=256$
- 16 bits: $2^{16}=65536$
- 32 bits: 2^32= mucho
----
# Decimales (representación de números con parte fraccionaria)
### sistemas de punto fijo
la coma siempre esta en el mismo lugar. ej: el decimal. 
$$\sum^{n}_{i=0}di.bi+\sum^{n}_{i=1}di.b^{-1}$$
### sistemas de punto flotante
cuando opero con binarios y tengo por ej 8 bits, yo puedo elegir que la parte fraccionaria empiece a partir de cualquiera de las posiciones

| 4   | 2   | 1   | 0.5 | 0.25 | 0.125 |
| --- | --- | --- | --- | ---- | ----- |
| 0   | 1   | 1   | 1   | 0    | 0     |
como corri la coma dos lugares, estoy dividiendo el numero por $2^5$
Estaríamos hablando del 3.5, pero esos mismos espacios los podríamos haber asignado a otros pesos, según conveniencia

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

---
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

![[Pasted image 20230823143152.png]]
==agregar foto del twos complement ones complement table que estaba en las diapos del profe==

El complemento a la base es reversible, ya que puedo buscar de vuelta e complemento y restar 1

---
# Suma de numeros binarios
Al sumar binarios nos puede pasar que nos pasemos de la cantidad de bits totales que tenemos disponibles. En un procesador de 8 podemos llegar a tener un 1 en la posicion 9
![[Pasted image 20230824115044.png]]

Cuando a un procesador se le pide una suma, devuelve el valor final, un carry y un overflow. si el carry es 1 es que nos pasamos, si es 0 no hay nada. Idem con overflow para signed .

El overflow funciona de la siguiente forma: compara el carry de entrada con el carry de salida de la ultima posición. Si son iguales da 0, sino da 1

### Z flag
si el flag z (zero) es 1 -> el resultado es cero. Sino, es cualquier otra cosa

### N flag
si dio 1 el resultado es neg, sinoes pp