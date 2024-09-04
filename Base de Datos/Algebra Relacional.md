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

Dada una relacion y una lista de atributos L, devuelve una relacion cuyas tuplas respresentan los posibles valores de los atributos de L en R
![[Pasted image 20240903192542.png]]

Siempr remueve tuplas duplicadas

### asignacion
![[Pasted image 20240903193206.png]]
guardo en variables

### Redenominacion
Permite modficar los nombres de los atributos de una relacion o el nombre de la relacion misma
![[Pasted image 20240903193811.png]]


### Union e intersección 
ver [[1.9 Nomenclatura]]


### diferencia 
dada dos relaciones R y S conserva solo aquellas tuplas de R que no pertenecen a S

### Producto cartesiano
![[Pasted image 20240903194817.png]]


HAce un todos con todos



## Operaciones adicionales
### Proyeccion generalizada
me permite no solo utilizar nombres de columnas sino utilizar funciones u operaciones 

### Agregacion 
Me permite resolver consultas que tengan que ver con varias filas al mismo tiempoej: cuantos goles metio un pais?? Necesito todas las tuplas de los goles de francia. Promedio tambien

### Junta externa 
![[Pasted image 20240903211843.png]]
