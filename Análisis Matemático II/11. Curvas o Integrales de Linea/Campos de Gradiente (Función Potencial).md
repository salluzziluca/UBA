---
dg-publish: true
---
 Sea $\vec F$ una funcion vectorial en H se dice que $\vec F$ es un campo deq gradientes en H si existe una funcion escalar $\phi$ diferenciable en H tal que
$$\vec F = \triangledown \phi$$ En todos los puntos de H. 
Tambien se dice que la funcion $\phi$ es el potencial del campo $\vec F$ 

Ej: ![[Pasted image 20220120111806.png]]

## Independencia del camino en intregral de línea de campo vectorial
Si $\vec F$ es un campo continuo en H abierto y conexo tal que $\vec F = \triangledown \phi$ entonces en todo punto de H la circulacion de $\vec F$ desde $\vec A$ hasta $\vec B$ a lo largo de cualquier curva suave a trozos no depende de la curva que se utilice y, además
$$\int_{C_{AB}}\vec F d \vec s = \phi(\vec B)- \phi(\vec A)$$
Si el campo es conservativo, lo mismo: $$\int_{C_{AB}}\vec F d \vec s = \phi(\vec B)- \phi(\vec A)$$
Entonces:
- Si la curva es cerrada
$$\oint_C \vec F d\vec s = \phi(\vec B)- \phi(\vec A)=\phi(\vec A) -\phi(\vec A) = 0 $$
- Si  $\phi(\vec B)= \phi(\vec A)$
$$\int_{C_{AB}}\vec F d \vec s = \phi(\vec B)- \phi(\vec A)= 0$$
![[Pasted image 20220120113511.png]]

#### Campos conservativos
![[Pasted image 20220120113841.png]]

## Condición necesaria para que un campo sea de gradientes
- Es necesario que la matriz jacobiana de $\vec F$  sea continua y simetrica, más ==no es suficiente== o, dicho de otro modo, que las derivadas cruzadas sean iguales.
	-demostracion en R²: ![[Pasted image 20220120120052.png]]
	- demostración en R³: ![[Pasted image 20220120120148.png]]
- Es tambien necesario que el conjunto H sea abierto y [[1.8 Topología#Simplemente Conexo|simplemente conexo]] 

## Paso a paso
1. Fijarse que $\vec F$ sea conservativa (chequear que P'y y Q'x sean iguales)
2. Integrar P con respecto a x, nos queda la funcion dependiente de y h(y). Obtenemos $\phi$
3. derivar en funcion de y a $\phi$
4. igualar $\phi'y$ a Q para obtener el valor de h(y)
5. Luego reemplazar h(y) en $\phi$

## Definiciones
Equipotencial: de igual potencia (similar a los conjuntos de nivel)