> Es un TDA que agrupa elementos. Sin restricciones

Cada elemento tiene un sucesor y un predecesor

- Crear (create)
- Insertar (insertAt)
- Vacía (isEmpty)
- Destruir (destroy)
- Eliminar (deleteAt)
- Ver elemento (ﬁnd)

## Tipos de listas
### Simplemente enlazada
- Cada elemento apunta al sucesor
- Cada uno con referencia al nodo siguiente
- Lista mantiene referencia al primer nodo

#### ¿Cuándo reservo / libero memoria?
- Reservo memoria para cada nodo
- Libero memoria para cada nodo
#### Ventaja:
- Memoria no debe ser contigua
Para insertar creo el nodo y lo apunto a un elemento posterior, despues apunto otro al anterior
### Doblemente enlazada