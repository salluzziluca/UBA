# Ownership 
Cada valor en rust tiene una variable que es su dueña. Un dueño a la vez. Cuando la variable dueño sale de scope, se libera la memoria asignada al valor. El dueño determina el lifetime. Un valor puede ser dueño de otros valores
O bien permito que una variable s epueda ver desde diferentes scopes o bien permito que se pueda mutar, ambas a la vez no
![[Pasted image 20240318184140.png]]

###### Box
Un `Box<T>`es un punteo a un valor de tipo T almacenado en el heap. `Box::new(v)`asigna espacio en el heap, mueve v a ese espacio y retorna un box que apunta a ese espacio. Box es udeño del esapcio al que apunta

Point es un Box, label un vector normal
![[Pasted image 20240318185136.png]]

Se pueden mover valores de un dueño a otro, se pueden tambien dar referencias (con lifetimes limitados). Cuando se le asignan valores, se les pasa una funcion o se retorna de una funcion no se copia el valor sino que se mueven los valores. 
El origen cede su perte