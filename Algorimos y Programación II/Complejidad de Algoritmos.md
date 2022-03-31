# Complejidad de Algoritmos
La complejidad se mira comparandolos en base a otros.

## Comparación por tiempo
Hay que probarlos en las mismas condiciones porque hay muchos factores externos. Es muy complicado encontrar dos maquinas iguales.

## Comparación por modelo matemático
- No medimos tiempo, solo unidades abstractas
- Utilizamos una estimación que ==solo sirve para comparar==
- Hay veces que nos sirve algo que tarde mucho y use electricidad y otras algo que tarde poco y use wifi. 
![[Pasted image 20220331185258.png]]

![[Pasted image 20220331185438.png]]

## Notación "BIG O"
- Va a mostrar como se comporta el algoritmo dado el tamaño del problema (no es lo mismo ordenar 3 numeros que 30000
- Big O= cota superior
- BIG $\Omega$ = cota inferior
- BIG $\Theta$ = cota superior e inferior

![[Pasted image 20220331190733.png]]
>Nuestro algoritmo (T(n)) es BIG O de f(n).

A BIG O le sirve si de un punto en adelante la funcion es siempre la cota superior a T(n)