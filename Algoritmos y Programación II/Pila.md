---
dg-publish: true
---
# Pila
> Es una estructura de datos de tipo LIFO (Last In First Out) que permite apilar (push) y desapilar (pop) datos.


![[Pasted image 20211123211035.png]]
## Operaciones o primitivas
- Crear (create): Crear la pila
- Apilar (push) (ponerle un item en la parte de arriba de la pila)
- tope (top): sumar, restar o preguntar el tope
- destruir (destroy): destruir la pila
- desapilar (pop): desapilar un elemento de arriba de la pila
- estaVacia(isEmpty): fijarse si la pila está vacia

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

#### Complejidad algorítmica
##### Vector estatico 
- Crear:
				O(1)
- Destruir 
				O(1)/O(n)
- Push
				O(n)
- Pop
				O(n)

##### Vector dinámico
- Crear:
				O(1)
- Destruir 
				O(1)/O(n)
- Push
				O(n)
- Pop
				O(n)

##### Nodos enlazados
- Crear:
				O(1)
- Destruir 
				O(1)/O(n)
- Push
				O(n)
- Pop
				O(n)


![[Pasted image 20220412192113.png]]

En el caso de push, el peor caso seria tener un elemento mas grande que el vector, por lo que hay que pedir mas memoria y mover los n elementos

<iframe src="\[https://www.notiondraw.com/\](https://www.notiondraw.com/)" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="800px" allowfullscreen></iframe> 