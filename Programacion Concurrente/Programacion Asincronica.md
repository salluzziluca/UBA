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


- Cada `Future` es como **tu ticket vibrador del bar**.
- No estás parado golpeando la puerta de la cocina (polling activo).
- El runtime te dice: “OK, ahora vos esperá tranquilo, yo te aviso cuando tu Future esté listo”.
- Cuando el SO detecta que **ya hay datos / ya terminó el timer / lo que sea**, **activa el waker** → “vibrador” → el executor lo mete de nuevo en la cola para hacer `poll()` otra vez.

```rust 
use async_std::io::prelude::*;
use async_std::net;

async fn cheapo_request(host: &str, port: u16, path: &str) -> std::io::Result<String> {
    // Conectamos al servidor
    let mut socket = net::TcpStream::connect((host, port)).await?;

    // Construimos el request HTTP básico
    let request = format!(
        "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n",
        path, host
    );

    // Enviamos el request
    socket.write_all(request.as_bytes()).await?;
    socket.shutdown(net::Shutdown::Write)?;

    // Leemos la respuesta completa
    let mut response = String::new();
    socket.read_to_string(&mut response).await?;

    Ok(response)
}

```