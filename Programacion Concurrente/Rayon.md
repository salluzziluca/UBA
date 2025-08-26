---
Dia: 2025-08-26
dg-publish: true
---
Rayon es una biblioteca muy popular, creada por Niko Matsakis,
implementa el modelo fork join de 2 formas.
I Realizar dos tareas en paralelo:
`let (v1, v2) = rayon::join(fn1, fn2);`
invoca a fn1 y fn2 y retorna una tupla con ambos resultados.
I Realizar N tareas en paralelo:
```rust

giant_vector.par_iter().for_each(|value| {
	do_thing_with_value(value);
});
```

El método .par_iter() crear un iterador ParallelIterator similar
a los iteradores de Rust. Rayon maneja los threads y ditribuye
el trabajo.

![[Pasted image 20250826205219.png]]

Desde afuera, Rayon parece crear una tarea por elemento del
vector.
Internamente, crea un worker thread por núcleo de CPU.
Implementa: Work stealing.
Los métodos .reduce() y .reduce_with() se usan para combinar
los resultados.
```rust
use rayon::prelude::*;

let s = ['a', 'b', 'c', 'd', 'e']
    .par_iter()
    .map(|c: &char| format!("{}", c))
    .reduce(
        || String::new(),
        |mut a: String, b: String| {
            a.push_str(&b);
            a
        },
    );

assert_eq!(s, "abcde");

```
