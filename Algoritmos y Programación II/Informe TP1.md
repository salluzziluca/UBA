---
dg-publish: true
---
    
![](https://i.imgur.com/P0aqOMI.jpg)

# **Trabajo Práctico n°1 — Sala de escape Pokemon** 
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
En este TP se buscaba primero terminar de afianzar los conceptos de lecturas de archivos vistos en Algoritmos y Programacion I, tema de vital importancia para el desarrollo productivo como programadores. Asimismo y como tema central, se buscaba introducir las funcionalidades de manejo de memoria propias del lenguaje C. 

## 2. Teoría

Respuestas a las preguntas teóricas (si no las hay podes borrar esta sección!)

1. La lectura de archivos se realiza primero verificando que el archivo sea valido, luego, al leer una linea, que el string que devuelve tambien sea valido y, por ultimo,  parseando ese string y verificando que devolvio la cantidad de campos que le pedimos (lo cual indica, por como funcion sscanf, si el parseo fue hecho correctamete). Se asignan entonces los valores parseados y verificados a los campos correspondientes de los struct (en este caso).
2. La memoria dinamica la manejo mediante el uso de funciones alocadoras como `malloc` `realloc` y `calloc`. Las cuales reservan una cantidad de memoria (bytes)  que nosotros le pidamos y se la asignan a un puntero. Ese puntero (el original), se encuentra en memoria estatica en el stack, pero apunta a una direccion en el heap. 
	Mediante `malloc` nosotros podemos crear un bloque fijo de memoria. Luego, con `realloc`, lo podemos modificar, pedirle mas memoria (muy util utilizado de la mano de un for o de un while). 
	Esta memoria no la podemos dejar alocada para siempre en el heap. Cuando la dejemos de utilizar, debemos devolverla. Esto puede ocurrir cuando terminamos de ejecutar nuestro programa (panorama deseable) o cuando la ejecución de nuestro programa se corta por algun error. Es por esto que debemos estar atentos y detectar cuales son esos casos en los que debemos, junto con el retorno de un NULL, por ejemplo, devolver el bloque de memoria correspondiente. 
	Aclaración: Dentro de la memoria dinamica se pueden crear bloques de memoria que apunten a otros bloques mediante punteros, no estamos limitados a depender siempre de un puntero en el stack para un bloque en el heap. 

## 3. Detalles de implementación


Explicación de como se implemento el trabajo pedido, esta sección es para que puedas explicar de forma un poco mas detallada como se implemento o como planteaste el trabajo y los detalles al respecto. Estos detalles pueden ser alguna justificación de porque implementaste lo pedido de la forma que lo hiciste, con que linea se compilo el trabajo, como ejecutarlo, algún supuesto que hayas hecho, etc. (La idea no es que se explique utilizando código pero si lo ves necesario podes hacerlo.)

Primero que nada, el Trabajo Practico se puede implementar con las lineas `gcc escape_pokemon.c  src/*.c -std=c99 -Wall -Wconversion -Wtype-limits -g -Werror -o  escape_pokemon`. Digo puede porque los flags son completamente opcionales a la hora de correrlo. 

Dicho esto, yo tome una implementacion que buscaba modularizar correctamente sin volverse uno loco intentando hacer las cosas mas chicas de lo realmente posible. Me concentre sobre todo en (intentar) no tener ninguna funcion demasiado larga o dificil de leer. Es por esto que a veces se pueden encontrar diferentes llamados o declaraciones separados por espacios aunque la [guia de estilo](https://programmerclick.com/article/47731811610/)  no lo recomendara necesariamente.

--- 
Primero y principal: se aloca memoria para la sala y se inicializa (mediante `calloc`) todo en cero. Si bien esto es un poco redundante (es la primer linea de la funcion) es importantisimo aclararlo porque de esta estabilidad inicial dependen el resto de los procesos. Sin esa memoria "core" en el heap (porque todo despues se asigna a la sala) no hay donde luego "poner" los diferentes valores. Dicho esto...

### Lectura de Archivos
Empecé por la lectura de archivos (ya dentro de `sala_crear_desde_archivos`) mediante una funcion que abre uno pasado por parametro y verifica que no sea nulo (de lo contrario retorna -1, error) para luego leerlo linea por linea y, segun se le aclare en la firma de la funcion inicializar y "llenar" un vector dinamico de objetos o de interacciones (respectivamente). 
Me parecio una buena implementacion la modularizacion de esta funcion (`cargar_a_memoria`) ya que queda visualmente demostrado en el codigo que con ambos archivos realizamos el mismo accionar. Y que si bien luego los campos a rellenar son distinto comparten (aunque sea conceptualmente) una gran parte del proceso.

#### Lectura de lineas
En esta parte del proceso ya se pueden empezar a notar las diferencias puntuales entre objetos e interacciones, es por eso que decidi programar sus funciones por separado. La diferencia de campos era significativa y me hubiese visto envuelto en una madeja de `ifs` que iba a oscurecer mas que aclarar.  
En ambas funciones se inicializan los diferentes vectores (o caracteres) en valores basicos para evitar manejo de basura, se verifica que el string recibido no sea ni nulo ni vacio(de ser asi se libera la memoria y se retorna `NULL`) y se parsea la linea. 
En caso de error en el parseo, sscanf ==no== nos devolvera un entero con la cantidad de valores leidos que le pedimos (si tenia que "dividir" el string en 3, nos deberia devolver 3 si todo salio bien). Asi que si estas condiciones no se verifican como verdaderas, retornamos `NULL`, no sin antes liberar la memoria pedida.
Si el proceso se ejecutó correctamente, se copian los valores de las variables auxiliares a los campos definitivos de los objetos o interacciones segun corresponda. Sin embargo, en ambos casos tenemos valores que no son strings. 

##### Excepciones
- En objetos tenemos un booleano, por lo que hay que hacer una comparacion extra entre strings y ahi asignarle el valor correspondiente a su campo (ya que asignarle el string "true" o "false" sería incorrecto.)
- En interacciones tenemos un enum, el cual requiere de un switch en este caso para su correcta carga al campo.
 ---
Mientras la linea leida siga siendo valida (no sea `NULL` o `FEOF`) se seguiran cargado elementos a los vectores correspondientes. Y una vez que se llegue al final del archivo, se cierra el mismo y se retorna `0` (no  hubo error).

 ##### Corroboración
 Finalmente, el programa verifica que las cantidades de ambos vectores no sea nula. Si al menos una lo es, se destruye la sala (con todos sus componentes) y se devuelve `NULL`. De lo contrario, se devuelve una sala ya inicializada

### Creación del vector de nombres de objetos e impresion por pantalla.
Una vez que esta la sala creada y (verificada), se crea un vector dinamico que contiene solamente el nombre de los objetos ya cargados originalmente en la sala. Este vector no se encuentra dentro de sala pero está ligado a `sala->objetos`. 
A la funcion que lo crea se le pasa por parametro un puntero a la sala ya llena y otro puntero a una cantidad particular que se ha de "llenar". 
Se verifican que ninguno de los valores pasados por parametro sean nulos y se procede a alocar la memoria (si por casualidad la `*sala` recibida es nula pero la `*cantidad` recibida no, se asigna una cantidad de -1, mostrando asi que no se pudo crear el vector).
Luego de haber alocado y verificado la memoria (mismo comportamiento con cantidad si hay error), se le asignan los diferentes nombres de objetos en las posiciones del vector dinámico y si la cantidad no es nula, se le asigna el valor de `sala->cantidad_objetos` ya registrada en el `struct sala`. Se devuelve el vector con los nombres cargados
Mediante el uso de este nuevo vector, se imprimen con un simple for los nombres de los objetos disponibles en la sala


### Validacion  e impresion de interacciones
Finalmente, se verifica mediante el uso de `sala_es_interaccion_valida` (la cual recibe como string los diferentes campos posibles de una interaccion y los compara con los registros de una sala ya creada) que las interacciones pedidas sean validas o invalidas y se imprime por pantalla el nombre de la interaccion seguida de su validez. En este caso, para no crear 4 variables mas y de alguna forma floodear el main, el contenido del string que se imprimirá por pantalla se verifica directamente en el printf. 
```c
printf("examinar la habitacion: %s\n", interaccion_valida(es_examinar_habitacion_valida));
```

### Liberación de memoria
Por ultimo, se destruye la sala. Agradeciendole a nuestra computadora por toda la memoria que nos prestó (como nos enseñaron en el colegio). Primero se liberan las diferentes posiciones de los vectores de elementos, luego el priopio vector y por ultimo la estructura misma de la sala.

## 4. Detalles de Funciones en particular

1. `agregar_objeto_a_vector`

    la funcion
    ```c
    agregar_objeto_a_vector(struct objeto ***objetos, int *cantidad_objetos, struct objeto *objeto_actual)
    ```
    
	Recibe por parametro un puntero a un vector de punteros, una cantidad y un objeto que se quiere agregar a ese vector. Crea un bloque de memoria auxiliar con el tamaño del vector de punteros que se le pasa + el tamaño de un  `struct objeto*` (le suma una espacio mas al vector para el nuevo elemento). Verifica que l bloque creado no sea nulo, que la memoria estpe correctamente asignada y luego le dice a `struct objeto **objetos` que apunte al mismo lugar donde está apuntando el bloque auxiliar (esto se hace para que, si la memoria no se carga correctamente en el realloc, no se pierda lo que ya habia en el vector importante y principal.).
	Por ultimo, carga el objeto actual en la posicion correspondiente segun cantidad_objetos y suma uno a cantidad. Devuelve 0, exitoso.

2. `sala_destruir()`

	Destruye la sala creada y alocada en memoria. La destruye de a partes, primero los vectores dinamicos y luego la estructura de la sala en si. No destruye el vector `nombre_objetos` porque este depende exclusivamente de  `sala->objetos`. No retorna nada porque es un ==**procedimiento==

## 5. Diagramas


En esta sección van los diagramas que realizas para poder acompañar los detalles de implementación y de funciones que escribiste mas arriba. Trata de que sean lo mas claros posibles, podes hacer mas de un diagrama para una sola función, por ejemplo podes tener un diagrama por cada paso que realiza la función en vez de tener un solo diagrama (que a lo mejor termina siendo poco claro) con toda la información metida junta.


1. Diagrama1

    ![Diagrama1](https://i.imgur.com/KvYn8UD.png)

    Explicacion del diagrama1, en caso de ser necesaria.

2. Diagrama2

    ![Diagrama2](https://i.imgur.com/nhqXNr6.png)

    Explicacion del diagrama2, en caso de ser necesaria.