---
Dia: 2025-09-22
dg-publish: true
---
## Semaforos
Tipo de dato compuesto por dos campos:
- unit `V`
- un set de procesos llamado `L`

Se inicializa con un  `k` mayor a 0 y con el conjunto vacio. 

Se definen dos operaciones atomicas
`wait(S)` y `signal(S)`

Si `V` mayor a 0, recurso disponible 
Si `V` menor a 0, recurso no disponible

El valor del semafoto representa la cantidad de recursos disponibles. Si V vale 0 o 1, es un semaforo binario, tambien conocido como `MUTEX`
`wait(S)` resta 1 al contador y `signal(S)`suma 1 al contador


```go
func wait(S){
	if S.V > 0
		S.V := S.V - 1
	else
		S.L add p
		p.state := blocked
}

func signal(S){
	if S.L is empty
		S.V := S.V + 1
	else
		sea q un elemento arbitrario del conjunto S.L
		S.L remove q
		q.state := ready
}

func signalBinario(S){
	if S.V = 1
		// undefined
	else if S.L is empty
		S.V := 1
	else
		sea q un elemento arbitrario del conjunto S . L
		S.L remove q
		q.state := ready
}
```


Tipos de semáforos
I System V
I POSIX
Un semáforo System V está compuesto por:
I El valor del semáforo
I El process id del último proceso que utilizó el semáforo
I La cantidad de procesos esperando por el semáforo
I La cantidad de procesos que está esperando que el semáforo
sea cero



## Barreras en rust 
Tipo de dato usado para **sincronizar múltiples threads** en un punto de ejecución común.  
Se asegura que **ningún thread continúe más allá de la barrera hasta que todos hayan llegado**.

Se inicializa con un entero `n > 0` que representa la **cantidad de threads participantes**.  

Cuando un thread llama a `wait()`, queda bloqueado hasta que **los `n` threads hayan llegado**.  
En ese momento, **todos se liberan a la vez** y la barrera puede volver a usarse (es *reusable*).

En Rust, se implementa con la estructura `std::sync::Barrier`.

---

### Operaciones atómicas
- `Barrier::new(n)`  
  Crea una barrera para `n` threads.
- `wait()`  
  El thread llama a este método y:
  - Si todavía no llegaron todos los `n` threads, queda **bloqueado**.  
  - Cuando llega el último thread, **todos se desbloquean simultáneamente**.

---

### Representación conceptual
Una barrera puede verse como:
- `N`: número fijo de threads requeridos.  
- `C`: contador de threads que llegaron.  
- `L`: conjunto de threads esperando.

Inicialización:
- `C := 0`
- `L := { }`

```go
struct Barrier {
    N: usize,   // cantidad de threads que deben sincronizar
    C: usize,   // contador de threads que llegaron
    L: set<Thread> // threads esperando
}


func wait(B){
    B.C := B.C + 1
    if B.C < B.N
        B.L add p
        p.state := blocked
    else
        // Último thread en llegar
        B.C := 0
        para cada q en B.L
            q.state := ready
        B.L := {}
}

```

```rust
use std::sync::{Arc, Barrier};
use std::thread;

fn main() {
    let n = 5;
    let barrier = Arc::new(Barrier::new(n));
    
    for i in 0..n {
        let c = barrier.clone();
        thread::spawn(move || {
            println!("Thread {} listo", i);
            c.wait(); // todos esperan aquí
            println!("Thread {} continúa", i);
        });
    }
}

```
Diferencias con semaforos
- **Semáforo:** controla acceso a recursos (permite o bloquea según disponibilidad).
    
- **Barrera:** fuerza sincronización en un punto común (todos esperan a todos).

## Producto Consumidor