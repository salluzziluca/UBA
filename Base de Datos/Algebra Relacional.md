Para interactuar con un modelo es necesario un lenguaje, hay dos tipos: Procedurales y declarativos. Casi todos son procedurales (python, c, etc). SQL es declarativo
![[Pasted image 20240903190744.png]]


## Caracteristicas del Álgebra relacional 
Propuesto por E. Codd en 1970, se lo considera parte integral del modelo relacional

![[Pasted image 20240903190930.png]]

## Operaciones Basicas 
### Selección
$$\sigma_{cond}:R\to S$$
Dad una relacion R y una condicion que se acplica a cada tupla de R. $$\sigma_{cond}(R)$$ selecciona aquellas tuplas de R para las cuales la condicion es verdera
![[Pasted image 20240903191814.png]]

### Proyección