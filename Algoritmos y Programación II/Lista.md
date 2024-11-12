---
dg-publish: true
---
# Lista
> Es un TDA que agrupa elementos. Sin restricciones

Cada elemento tiene un sucesor y un predecesor

- Crear (create)
- Insertar (insertAt)
- Vacía (isEmpty)
- Destruir (destroy)
- Eliminar (deleteAt)
- Ver elemento (ﬁnd)

## Tipos de listas
### Lista de nodos simplemente enlazada
- Cada elemento apunta al sucesor
- Cada uno con referencia al nodo siguiente
- Lista mantiene referencia al primer nodo y al ultimo, depende de implentacion.

#### ¿Cuándo reservo / libero memoria?
- Reservo memoria para cada nodo
- Libero memoria para cada nodo
#### Ventaja:
- Memoria no debe ser contigua

##### Insertar
Para insertar creo el nodo y lo apunto a un elemento posterior, despues apunto otro al anterior
![[Pasted image 20220412204311.png]]
O usamos un aux

##### Eliminar
![[Pasted image 20220412204449.png]]
### Doblemente enlazada
Tiene una referencia al predecesor y al sucesor
##### Insertar
![[Pasted image 20220412210657.png]]

##### Borrar
![[Pasted image 20220412210712.png]]

### Lista circular
![[Pasted image 20220412210729.png]]

Cuando la lisa tiene un solo elemento, este apunta a si mismo
![[Pasted image 20220412210758.png]]

[[informe_tda1]]