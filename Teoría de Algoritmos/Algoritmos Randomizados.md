---
Dia: 2024-11-17
dg-publish: true
---
El mundo es aleatorio!!!

Le permitiremos al algoritmo tomar deciisiones al azar independientemente de los valores de entrada. Esto es un factor completamente interno del algoritmo. 

Un algoritmo deterministico eficiente que alcula ra respuesta correcta puede verse como un caso particular de un algoritmo randomizado qeu da la respuesta correcto con alta probabilidad. 
O tambien puede verse como un algoritmo randomizaco que da siempre la respuesta correcta con una expectativa de complejidad temporal eficiente. 

Un algoritmo randomizado puede resolver un problema que quizas uno deterministico no puede. Son conceptualmente mas sencillos de entender e implementar. 

No requieren mantener estado interno o memoria del pasado. 

En sistemas distribuidos permite quebrar la simetria. 


## Problema de encontrar la media 
La mediana es el valor medio 
2 5 7 1 3. 1 2 3 5 7 la mediana seria 3. 
Ordenando es muy facil, O(n logn) para ordernar y O(1) para acceder a la posicion k. K=  (n+1)/2 si es impiar k = n/2 si es par 


## Problema de la Seleccion
Quiero encontrar el valor k de una array ordenado.
Si me piden el primero o el ultimo calculo directo max o min en 