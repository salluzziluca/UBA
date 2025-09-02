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