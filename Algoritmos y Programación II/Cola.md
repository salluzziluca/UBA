 Es una TDA ddel tipo FIFO (First In First Out) que permite encolar y desencolar datos.

![[Pasted image 20211123212205.png]]

## Operaciones o primitivas
- Crear: crea la pila
- Destruir: destruye la pila
- Encolar: agrega un elemento al final
- Desencolar: saca el elemento que esté primero.
- Primero: chequear o cambien el elemento que va primero(el proximo a salir)
- Vacío: chequea que esté vacio
- Cantidad maxima: Se fija donde esta la cantidad maxima del vector.

## Implementaciones
### Cola con vector estático
![[Pasted image 20220414175022.png]]
Para ver si puedo encolar me fijo---> si `tope=fin`
Para ver si está vacia ---> `tope=0`
Para ver si puedo desencolar ---> `tope=0` 

![[Pasted image 20220414175215.png]]
En este caso, solo podriamos encolar en la posicion 6, del 0 al 1 están inutilizables.
Si esto ocurre, podemos intentar mover todo un lugar todo para atras
![[Pasted image 20220414175540.png]]
![[Pasted image 20220414175553.png]]

Otra forma, es con una cola circular, en la que el tope siempre va a estar persiguiendo al principio
![[Pasted image 20220414175723.png]]
![[Pasted image 20220414175708.png]]
### Cola con vector dinámico

### Cola con [[Nodo Enlazado|nodos en lazados]]