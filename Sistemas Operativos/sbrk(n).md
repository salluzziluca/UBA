---
dg-publish: true
---
![[Pasted image 20240405173026.png]]Un proceso puede reservar memoria para sí mismo incrementando el tamaño del heap, recordar que el limite actual del heap se denomina _break_. Para reservar memoria, un programa en C normalmente utiliza la familia de funciones _malloc()_ (man 3 malloc). Esta función está basada en la system call **brk()**.

Redimensionar el heap (reservando o liberando memoria) es tan simple como pedirle al kerner que ajuste su idea de **donde** el break del proceso está.

Inicialmente el _break*_ del programa está ubicado justo en el final de datos no inicializados. Despues que brk() se ejecuta, el _break_ es incrementado, el proceso puede acceder a cualquier memoria en la nueva área reservada, pero no accede directamente a la memoria física. Esto se realiza automáticamente por el kernel en el primer intento del proceso en acceder al área reservada.