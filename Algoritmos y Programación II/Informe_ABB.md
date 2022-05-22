    
![](https://i.imgur.com/P0aqOMI.jpg)

# **TDA N°2 — Árbol Binario de Búsqueda (ABB)** 
---
##### [7541/9515] Algoritmos y Programación II
---
###### Primer cuatrimestre de 2022
---

|  Alumno: | Salluzzi, Luca |
| ----------- | ----------- |
| Número de padrón: | 108088 |
| Email: | lsalluzzi@fi.uba.ar |


## 1. Introducción
En este trabajo se buscaba afianzar los conceptos teórico-prácticos del TDA Árbol, particularmente del Árbol Binario de Búsqueda. Para esto se nos pidió implementar uno con nodos simplemente enlazados, otorgándonos un .h y un .c con todas las primitivas necesarias y dejando a nuestro criterio la creación de funciones privadas.

## 2. Teoría

### Árboles
Un árbol puede ser definido de varias formas, la forma más sencilla es de manera recursiva, como un conjunto de nodos enlazados. Lo conforma entonces un nodo particular, el nodo raíz (el cual se distingue del resto por no tener padre) y una cantidad n de nodos hijos. Asimismo, estos nodos hijos serán, a su vez, nodos raíces de sus propios sub-árboles. El nodo raíz de cada sub-árbol es entonces hijo del nodo raíz principal del árbol. 

#### Árbol Binario
Un árbol binario es un tipo de dato abstracto árbol que puede tener, entonces, de cero a dos hijos por nodo, denominados izquierdo y derecho para una mayor comprensión por parte del usuario o desarrollador.
##### Árbol binario de búsqueda
El árbol binario no tiene mucha utilidad per se, ya que no se establece ninguna regla para la inserción de elementos. Es por esto que en el árbol binario de búsqueda se establece un contrato de comparación en el que los elemento mayores al nodo van en su nodo derecho y los menores en el nodo izquierdo. Teniendo siempre un solo valor por nodo. 
Entonces, en un árbol binario:
- Si existe nodo izquierdo, va a ser siempre menor en valor a su nodo padre.
- Si existe nodo derecho, va a ser siempre mayor en valor a su nodo padre.
- Los sub-árboles serán también árboles binarios de búsqueda.

### Primitivas y Complejidades Algorítmicas
Para todo tipo de árbol, las primitivas son:
- crear 
- destruir
- vacío
- insertar
- eliminar 
- buscar 
- recorrer
Crear, justamente, crea el árbol, lo genera y lo inicializa, según el criterio acordado o la implementación que se desee. En la mayoría de los casos esto significa crear la estructura con nodo raíz con elemento vacío e hijos también vacíos. 
Destruir, borra el árbol, dependiendo del tipo de lenguaje que estemos usando para la implementación, esto puede significar liberar la memoria asignada. Para lo cual es necesario hacerlo en un orden preciso, evitando dejar nodos huérfanos.
Vacío corrobora que el árbol no tenga elementos, esto también se puede pensar como que el tamaño actual del árbol sea cero, pero como siempre, depende de la implementación (ya que puede no tener un contador de tamaño).
Insertar agrega elementos al árbol, dependiendo del contratro/criterio, se agregaran de diferentes formas, cambia segun el tipo de árbol. Tambien, 
Eliminar es opuesta a agregar, ya que borra elementos del arbol
## 3. Detalles de implementación


### Lectura de Archivos


#### Lectura de lineas

##### Excepciones


 ##### Corroboración


### Creación del vector de nombres de objetos e impresion por pantalla.


### Validacion  e impresion de interacciones


### Liberación de memoria


## 4. Detalles de Funciones en particular

1. `agregar_objeto_a_vector`

  
2. `sala_destruir()`



## 5. Diagramas





1. Diagrama1

    ![[WhatsApp Image 2022-04-10 at 11.54.57 PM.jpeg]]



2. ![[WhatsApp Image 2022-04-10 at 11.54.56 PM.jpeg]]


