---
Dia: 2025-09-02
dg-publish: true
---
Se usan tareas asincronicas para intecalarlas en un unico thread o en una pool de threads. Estas son mucho mas livianas que los threados. 

Es mas rapida la creacion y el [[Memoria#Virtualización de Memoria|context switch]], tenemos un menor overhead de memoria. 

El [[Scheduling|scheduler]] no controla todo, sino que hay una capa intermedia propia de nuestro programa, es mucho ams eficiente.

version sync
```rust 

use std::{net, thread};

let listener = net::TcpListener::bind(address)?;
for socket_result in listener.incoming() {
    let socket = socket_result?;
    let groups = chat_group_table.clone();

    thread::spawn(|| {
        log_error(serve(socket, groups));
    });
}

```

version async

```rust 

use async_std::{net, task};
use futures::stream::StreamExt; // Necesario para `.next()`

let listener = net::TcpListener::bind(address).await?;
let mut new_connections = listener.incoming();

while let Some(socket_result) = new_connections.next().await {
    let socket = socket_result?;
    let groups = chat_group_table.clone();

    task::spawn(async move {
        log_error(serve(socket, groups).await);
    });
}
```

## Future, polls y executor

Un `Future` en Rust **no ejecuta nada por sí mismo**.  
El `executor` (Tokio, async-std, etc.) es el que lo “golpea” llamando a `poll` repetidamente hasta que el Future diga:

- `Poll::Ready(valor)` → “Ya terminé, acá está el resultado”.
- `Poll::Pending` → “Todavía no terminé, volvé a llamarme más tarde”.

- Llamás una función `async`, obtenés un `Future`.
- El executor (tokio, async-std) mete ese `Future` en una cola de tareas.
- Llama a `poll()` →
    - Si está listo (`Ready`), devuelve el valor.
    - Si no (`Pending`), lo saca de la cola y espera que alguien llame a `wake()` cuando haya progreso (ej. kernel dice "hay datos en el socket").
- Cuando se despierta, el executor vuelve a llamar `poll()`.
- Repite hasta que salga `Ready`.

>[!important]  El `poll` **no bloquea nunca**. Si el future está esperando I/O, dice “Pending” y le da al executor un `Waker` para que lo despierte cuando haya datos.