# Pila
> Es una estructura de datos de tipo LIFO (Last In First Out) que permite apilar (push) y desapilar (pop) datos.


![[Pasted image 20211123211035.png]]
## Operaciones
- Crear (create): Crear la pila
Apilar (push) (ponerle un item en la parte de arriba de la pila)
tope (top): sumar, restar o preguntar el tope
destruir (destroy): destruir la pila
desapilar (pop): desapilar un elemento de arriba de la pila
estáVacia(isEmpty): fijarse si la pila está vacia

## Implementaciones
### Vector estático
![[Pasted image 20220412185004.png]]
Tenemos una capacidad fija.
Para ver si puedo apilar me fijo---> si `tope==capacidad`
Para ver si está vacia ---> `tope=0`
Para ver si puedo desapilar ---> `tope=0` 

### Vector dinámico
Tenemos una capacidad dinámica. Si se nos llena, damos mas memoria. 
![[Pasted image 20220412185129.png]]

Para ver si puedo apilar me fijo---> Siempre puedo apilar, si `tope==tamanio` le damos mas memoria
Para ver si está vacia ---> `tope=0`
Para ver si puedo desapilar ---> `tope=0` 

### Algunas ideas
![[Pasted image 20220412190154.png]]