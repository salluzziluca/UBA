# Ownership 
Cada valor en rust tiene una variable que es su dueña. Un dueño a la vez. Cuando la variable dueño sale de scope, se libera la memoria asignada al valor. El dueño determina el lifetime,
O bien permito que una variable s epueda ver desde diferentes scopes o bien permito que se pueda mutar, ambas a la vez no
![[Pasted image 20240318184140.png]]

###### Box
Un `Box<T>`es un punteo a un valor de tipo T almacenado en el heap