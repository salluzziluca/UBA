---
Dia: 2025-09-09
dg-publish: true
---
## Traits Send y Sync
- **Send**: permite transferir ownership entre threads.
  - Casi todos los tipos son Send.
  - Excepciones: `Rc<T>`.
  - Tipos compuestos formados por Send → también son Send.
- **Sync**: permite que el tipo sea referenciado desde múltiples threads.
  - Un tipo `T` es Sync si `&T` es Send.
  - Casi todos los primitivos son Sync.

## [[Locks|RwLock]]
Rust provee [[Locks|locks]] compartidos y exclusivos en el módulo `std::sync::RwLock`.
- **Shared [[Locks|lock]] (read)**: varios threads pueden leer.
- **Exclusive [[Locks|lock]] (write)**: solo un thread puede escribir.

Ejemplo:
```rust
use std::sync::RwLock;

let lock = RwLock::new(5);
