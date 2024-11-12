---
dg-publish: true
---
# Ownership 
Cada valor en rust tiene una variable que es su dueña. Un dueño a la vez. Cuando la variable dueño sale de scope, se libera la memoria asignada al valor. El dueño determina el lifetime. Un valor puede ser dueño de otros valores
O bien permito que una variable s epueda ver desde diferentes scopes o bien permito que se pueda mutar, ambas a la vez no
![[Pasted image 20240318184140.png]]

###### Box
Un `Box<T>`es un punteo a un valor de tipo T almacenado en el heap. `Box::new(v)`asigna espacio en el heap, mueve v a ese espacio y retorna un box que apunta a ese espacio. Box es udeño del esapcio al que apunta

Point es un Box, label un vector normal
![[Pasted image 20240318185136.png]]

Se pueden mover valores de un dueño a otro, se pueden tambien dar referencias (con lifetimes limitados). Cuando se le asignan valores, se les pasa una funcion o se retorna de una función no se copia el valor sino que se mueven los valores. 
El origen cede su pertenencia del valor al destinatario, el destinatario ahora controla el lifetime
```rust
let x = String::from("hello");
let y = x; // x is moved to y
```

```rust
fn take_ownership(s: String) { /* ... */ }

let x = String::from("hello");
take_ownership(x); // x is moved into the function
```

```rust 
fn give_ownership() -> String {
    let s = String::from("hello");
    s // s is moved out of the function
}
```

Si hago `derive[copy]`, se pasaran copias de los valores en vez de moverlos (mover es copiar y borrar la referencia). No se puede hacer copy de todos los valores, tienen que tener tamaño conocido. Un struct o enum puede ser copy si todos sus campos son copy.

### Referencias
Hay dos tipos:
1. Referencias compartidas: no modifican, solo lectura pero se pueden tener tantas como se desee
2. Referencias mutables: permiten cambiar el valor pero se puede tener solo una
[[Taller de Programación/Concurrencia]]
[[Sockets]]