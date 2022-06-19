![](https://i.imgur.com/P0aqOMI.jpg)

# **TDA N°3 —  Tabla Hash** 
---
##### [7541/9515] Algoritmos y Programación II
---
###### Primer cuatrimestre de 2023
---

|  Alumno: | Salluzzi, Luca |
| ----------- | ----------- |
| Número de padrón: | 108088 |
| Email: | lsalluzzi@fi.uba.ar |


## 1. Introducción
En este trabajo se buscaba afianzar en el alumno los conocimientos sobre tablas hash. Para esto, se le pidió implementar una tabla hash abierta con primitivas otorgadas por la cátedra.

## 2. Teoría, tipos de tablas hash

Un hash es una implementación de un TDA diccionario. Este está compuesto por una tabla en la cual se asginan elementos segun su clave. Para encontrar su posicion en la tabla, se pasa la clave por una función hash la cual devuelve un numero. Al aplicar la funcion modulo entre ese numero obtenido y la capacidad de nuestra tabla obtenemos la posicion a la que asignaremos el elemento.
Si dos elementos son asignados a la misma posición, se genera una colision, la forma de resolverla depende del tipo de hash a utilizar.

### Hash abierto
En un hash abierto, los elementos se guardan fuera de la estructura original (vease, por ejemplo, en una lista). Las colisiones se resuelven concatenando los elementos que se encuentran en la misma posición dentro de otra estructura. De esta forma, nos ahorramos el tener que reasignarlos a una nueva posición. 
El tipo de direccionamiento de este hash es cerrado, ya que siempre que la posicion que se le asigne al elemento en su primer hasheo, se mantendra siempre y no variará. 
Su complejidad en el peor caso es O(n), ya que puede terminar degenerandose a lista si no se lo rehashea al alcanzar una cantidad especifica de elementos.
Sus complejidades son:
| crear | Destruir | Agregar un elemento| Quitar un elemento| Buscar un elemento|
| ----- | -------- | ------- | ---------------- | ----------- |
| O(1)  | O(n)     | O(1)    | O(n)            | O(n)       |
A la hora de agregar, simplemente se hashea la clave para buscar la posicion y luego se carga el par <clave;valor> a la ultima posición de la lista correspondiente. Siempre el proceso es el mismo ya que, utilizando el puntero al ultimo par, no es necesario recorrer todos los elementos de la lista.
Luego, para quitar o buscar, la justificación es la misma, ya que, en el peor caso, debemos recorrer los elemenos de la lista de la posición correspondiente hasta encontrar el par buscado o el par a eliminar (pudiendose este encontrarse al final).
Finalmente, a la hora de destruir el hash, dependemos de la cantidad de elementos en el mismo, por lo que la complejidad será O(n).

### Hash cerrado
Un hash cerrado siempre guarda sus elemento dentro de su estructura original. A la hora de resolver colisiones, se buscan nuevas posiciones libres a las que asignar los elementos colisionados. DE esta forma, siempre vamos a tener un tamaño de tabla mayor o igual al numero de claves, jamas menor. Es por esta forma de reasignar colisiones que este es un hash de direccionamiento abierto.
Para buscar nuevas posiciones libres a la hora de redireccionar las colisiones, se pueden utilizar diferentes metodos:
- Probing lineal: Se trata de buscar el proximo espacio libre inmediato
- Probing cuadratico: Busca el espacio libre inmediato, de no encontrarlo, busca la proxima posicion libre tomando en cuenta estadisticamente la posicion actual y la posicion a la que se quiere llegar.
- Hash doble: aplicar por segunda vez la misma funcion hash buscando que nos devuelva una posicion no ocupada. Esto puede llevar, en hashes ya muy cargados, a volver a colisionar y tener que repetir el proceso hasta encontrar una posicion libre. 

Sus complejidades son:
| crear | Destruir | Agregar un elemento| Quitar un elemento| Buscar un elemento|
| ----- | -------- | ------- | ---------------- | ----------- |
| O(1)  | O(1)     | O(n)    | O(n)            | O(n)       |
En un hash cerrado en el peor escenario, para agregar deberiamos recorrer todo el hash. Suponiendo que la posicion dada por la función hash sea la primera y la unica posicion libre la última.
Luego, a la hora de quitar y buscar, al igual que en el hash abierto, vamos a tener que recorrer todo el hash hasta encontrarlo (tomando siempre el peor caso).
## 3. Detalles de implementación


Explicación de como se implemento el trabajo pedido, esta sección es para que puedas explicar de forma un poco mas detallada como se implemento o como planteaste el trabajo y los detalles al respecto. Estos detalles pueden ser alguna justificación de porque implementaste lo pedido de la forma que lo hiciste, con que linea se compilo el trabajo, como ejecutarlo, algún supuesto que hayas hecho, etc. (La idea no es que se explique utilizando código pero si lo ves necesario podes hacerlo.

Para mi implementacióon, decidi utilizar listas simplemente enlazadas para concatenar los elementos colisionados. De esta forma, no fue complicada la busqueda ni la eliminacion de elementos, ya que era muy similar a la de el TDA Lista entregado anteriormente. 
Como estructuras declaré un hash con un vector de listas, una cantidad maxima de elementos posibles a almacenar y una cantidad de ocupados (haciendo referencia a los elementos actuales existentes en el hash) esto me permitio tener un control mayor de la cantidad de elementos que se almacenaban en mi estructura.
Para cada lista, utilizé un puntero al primer y al ultimo elemento de estas, asi como un contador de posiciones ocupadas. Estas listas contenian como elementos los pares <clave;valor>, es decir, estructuras con un puntero a la clave y un puntero a el valor, ademas de un puntero al siguiente par.

En cuanto a la modularizacion, me decidi por "extraer" de las primitivas originales aquellas funciones o procedimientos que podian ser considerados casos bordes o especiales. En hash_insertar, por ejemplo, se llama a `sobreescribir_elemento` para, de ser necesario, actualizar en una clave ya existente el elemento por uno nuevo ingresado. No me parecio propicio, entonces, modularizar el resto de la inserccion (llenado del par y cargado de el mismo al final de la lista de la posicion correspondiente), puesto a que me parecia que esas breves lineas de codigo eran el tronco de la primitiva. Decidi tambien no utilizar hash_contiene para verificar si la sobreescripcion era necesaria ya que esto conllevaria una doble iteracion a lo largo de la lista y, por lo tanto, mayor complejidad algoritmica.

Otro ejemplo de este lineamiento en la modularización puede verse en `hash_quitar`, donde modularizo el caso de quitar un elemento en una lista de cantidad 1 y mantengo dentro de la primitiva la eliminacion en una de cantidad mayor, iterando a lo largo de los pares de la lista hasta encontrarlo y eliminarlo.

Finalmente, con respecto a mis pruebas, decidi algunas de caja blanca para poder comprobar el correcto funcionamiento de la inserccion y del rehash. Quizas vistas ahora parezcan un poco redundantes, pero teniendo en cuenta que fueron usadas en el tiempo de desarollo del TDA, fueron de mucha utiliad para comprobar minuciosamente que las funciones cumplian con su cometido.

## 5. Diagramas


En esta sección van los diagramas que realizas para poder acompañar los detalles de implementación y de funciones que escribiste mas arriba. Trata de que sean lo mas claros posibles, podes hacer mas de un diagrama para una sola función, por ejemplo podes tener un diagrama por cada paso que realiza la función en vez de tener un solo diagrama (que a lo mejor termina siendo poco claro) con toda la información metida junta.


1. Diagrama1

    ![[WhatsApp Image 2022-04-10 at 11.54.57 PM.jpeg]]

Una muestra de como se manejan el stack y el heap. Un puntero en el stack apunta a una memoria en el heap. Una variable cantidad_nombres creada en el stack tiene un puntero en el heap (creado despues) que apunta a cantidad_objetos. De esta forma se le modifica el valor a cantidad_nombres

2. ![[WhatsApp Image 2022-04-10 at 11.54.56 PM.jpeg]]


    Se tiene un archivo, de ese se lee una lina que mediante objeto_crear_desde_string se transforma luego en un struct objeto que es cargado a un vector. A ese vector se accede mediante un puntero en sala