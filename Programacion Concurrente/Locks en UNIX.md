---
Dia: 2025-09-09
dg-publish: true
---

## Introducción
- Mecanismo de sincronismo de acceso a un archivo.
- También se pueden usar para sincronizar acceso a otros recursos.
- En Unix son *advisory* (los procesos pueden ignorarlos).
- Tipos:
  - **Read [[Locks|lock]] (shared lock)**: varios procesos pueden tenerlo a la vez.
  - **Write [[Locks|lock]] (exclusive lock)**: un solo proceso puede tenerlo.

### Condiciones para obtener [[Locks|locks]]
- Para tomar un **read [[Locks|lock]]** → esperar a que se liberen todos los *exclusive [[Locks|locks]]*.
- Para tomar un **write [[Locks|lock]]** → esperar a que se liberen todos los [[Locks|locks]] (de cualquier tipo).

## Establecimiento de un [[Locks|lock]]
1. Abrir el archivo a bloquear.
2. Aplicar el [[Locks|lock]]:
   - Mediante **`fcntl()`**:
     - Completar `struct flock`.
     - Usar `fcntl()`.
   - Mediante **`flock()`**.
   - Mediante **`lockf()`** (interfaz construida sobre `fcntl()`).

Los [[Locks]] en Unix se integran con la gestión de la [[Sección Crítica]].
