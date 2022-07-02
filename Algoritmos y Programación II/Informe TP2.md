    
![](https://i.imgur.com/P0aqOMI.jpg)

# **Trabajo Práctico n2** 


## [7541/9515] Algoritmos y Programación II


### Primer cuatrimestre de 2022

|  Alumno: | Saluuzi, Luca |
| ----------- | ----------- |
| Número de padrón: | 108088 |
| Email: | lsalluzzi@fi.uba.ar |

#### 1. Introducción
En este TP2 se nos dio mucha libertad a la hora de implementar lo pedido. De esta forma se evaluo si el alumno conocia o no los temas impartidos a lo largo del cuatrimestre y si era capaz de moverse con libertad para con ellos.
Se le pidió, entonces, reescribir el TP1 reemplazando los vectores dinamicos por otras estructuras de datos y, adicionalmente, implementar funciones nuevas que permitieran ejecutar interacciones y desarollar adecuadamente un "loop jugable".

#### Elección de TDAs
Decidí reemplazar mis vectores dinamicos con hashes. De esta forma obtenia un acceso muy directo y sencillo al dato (utilizando como clave el nombre del objeto o el string "objeto1verboobjeto2"). Para esto fue necesario eliminar ciertas partes del TDA que sobreescribian elementos con la misma clave. En vez de hacer eso, el hash actual almacena en una misma lista interacciones de igual clave y a la hora de ser llamadas pueden ser ejecutadas una atras de otra.
Luego, en cuanto a la estructura general del juego, decidi implementar un struct sala con su hash de objetos e interacciones y un struct jugador, anidado en sala. Este segundo struct contienes los objetos poseidos y los objetos conocidos por el jugador. 
Cuando el susodicho descubre un objeto, este se pas del hash de objetos de la sala al de objetos_conocidos ubicado en el jugador. Si el usuario agarra el objeto, este se mueve nuevamene de su hash de objetos conocidos a su hash de objetos poseidos.

#### Resolución de pruebas
En cuanto a las pruebas, hubo que hacer modificaciones:
Para resolver las pruebas de caja blanca del TP1, agregué (con permiso de mi correctora, o sea, vos), la estructura de la sala al entorno de pruebas mediante un .h privado. A `escape_pokemon.c` se le sigue pasando exclusivamente `sala.h`.
Otra prueba a corregir fue la que pedia todos los objetos de la sala y los comparaba con un vector. El orden en el que estos aparecen en el hash no es el mismo que el de .dat, porque el criterio de ordenamiento es otro. Para arreglar esta prueba simplemente cambie el orden del vector `esperados` (que es el que se compara con las claves del hash).

#### Detalles de la implementación
`hash_obtener_claves` Esta es una funcion que recorre todo el hash obteniendo del par clave,elemento la clave y guardandola en un vector dinamico. Me parece oportuno aclarar que no reutilicé `hash_con_cada_clave` por un tema de simplicidad a la hora de programar. Para utilizar `con_cada_clave` habria que haberle pasado como parametro un struct con un vector e informacion extra, tambien se podria haber modificado la funcion ateriormente mencionada para que reciba mas parametros la funcion booleana auxiliar. Pero me parecio mas sencilo crear una funcion desde cero que cumpliera con lo que yo estaba necesitando en ese momento. 

La mayoria de las funciones tienen un funcionamiento similar, intercambian, pasan o eliminan informacion de los 3 hashes de objetos (dos del jugador, uno de la sala).
En `ejecutar_interaccion` por ejemplo, se comprueba que los objetos esten en dentro del inventario del jugador. Se concatenan los 3 strings objeto1, verbo, objeto2 (de ser necesario este segundo objeto). Y luego se busca la interaccion dentro del hash correspondiente. Si se encuentra, se analiza que tipo de accion tiene y se la ejecuta sumando uno a la cantidad de interacciones ejecutadas. Se elimina la interaccion actual y se busca luego la proxima que cumpla con la clave correspondiete, repitiendo el proceso de analisis de tipo de accion. La funcion termina cuando no existen mas interacciones con la clave otorgada. Se devuelven, finalmente, la cantidad de interacciones ejecutadas.


1. Diagrama1

    ![Diagrama1](https://i.imgur.com/KvYn8UD.png)

    Explicacion del diagrama1, en caso de ser necesaria.

2. Diagrama2

    ![Diagrama2](https://i.imgur.com/nhqXNr6.png)

    Explicacion del diagrama2, en caso de ser necesaria.