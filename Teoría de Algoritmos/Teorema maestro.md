Utilizado para problemas recursivos del tipo divide y conquista
$$T(n) = aT(n/b) + f(n)$$
- n equivale al tamaño del problema. 
- a equivale a la cantidad de llamadas recursivas que realiza el algoritmo.  Debe ser natural
- b equivale a cuanto se divide el problema para resolverlo recursivamente. Debe ser real mayor a 1 y siempre constante.
- f(n) es el resto de cosas que se hacen en la funcion. 
Caso 1: Si f(n) = O(n logb a−e ), para alguna constante e > 0, entonces T(n) = Θ(n logb a )
![[Pasted image 20220525123633.png]]

