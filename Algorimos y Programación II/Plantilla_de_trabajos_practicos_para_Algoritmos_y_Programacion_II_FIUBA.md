    
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

1. respuesta1
2. respuesta2

## 3. Detalles de implementación


Explicación de como se implemento el trabajo pedido, esta sección es para que puedas explicar de forma un poco mas detallada como se implemento o como planteaste el trabajo y los detalles al respecto. Estos detalles pueden ser alguna justificación de porque implementaste lo pedido de la forma que lo hiciste, con que linea se compilo el trabajo, como ejecutarlo, algún supuesto que hayas hecho, etc. (La idea no es que se explique utilizando código pero si lo ves necesario podes hacerlo.)

Primero que nada, el Trabajo Practico se puede implementar con las lineas `gcc escape_pokemon.c  src/*.c -std=c99 -Wall -Wconversion -Wtype-limits -g -Werror -o  escape_pokemon`. Digo puede porque los flags son completamente opcionales a la hora de correrlo. 

Dicho esto, yo tome una implementacion que buscaba modularizar correctamente sin volverse uno loco intentando hacer las cosas mas chicas de lo realmente posible. Me concentre sobre todo en (intentar) no tener ninguna funcion demasiado larga o dificil de leer. Es por esto que a veces se pueden encontrar diferentes llamados o declaraciones separados por espacios aunque la [guia de estilo](https://programmerclick.com/article/47731811610/)  no lo recomendara necesariamente.

--- 
Primero y principal: se aloca memoria para la sala y se inicializa (mediante `calloc`) todo en cero. Si bien esto es un poco redundante (es la primer linea de la funcion) es importantisimo aclararlo porque de esta estabilidad inicial dependen el resto de los procesos. Sin esa memoria "core" en el heap (porque todo despues se asigna a la sala) no hay donde luego "poner" los diferentes valores. Dicho esto...

### Lectura de Archivos
Empecé por la lectura de archivos (ya dentro de `sala_crear_desde_archivos`) mediante una funcion que abre uno pasado por parametro (para luego leerlo linea por linea) y, segun se le aclare en la firma de la funcion se encarga de inicializar y "llenar" un vector dinamico de objetos o de interacciones (respectivamente). 
Me parecio una buena implementacion la modularizacion de esta funcion (`cargar_a_memoria`) ya que queda visualmente demostrado en el codigo que con ambos archivos realizamos el mismo accionar. Y que si bien luego los campos a rellenar son distinto comparten (aunque sea conceptualmente) una gran parte del proceso.

#### Lectura de lineas
En esta parte del proceso ya se pueden empezar a notar las diferencias puntuales entre objetos e interacciones, es por eso que decidi programar sus funciones por separado. La diferencia de campos era significativa y me hubiese visto envuelto en una madeja de if que iba a oscurecer mas que aclarar.  
En ambas funciones se inicializan los diferentes vectores (o caracteres) en valores basicos para evitar manejo de basura, se verifica que el string recibido no sea ni nulo ni vacio(de ser asi se libera la memoria y se retorna `NULL`) y se parsea la linea. 
En caso de error en el parseo, sscanf ==no== nos devolvera un entero con la cantidad de valores leidos que le pedimos (si tenia que "dividir" el string en 3, nos deberia devolver 3 si todo salio bien). Asi que si estas condiciones no se verifican como verdaderas, retornamos `NULL`, no sin antes liberar la memoria pedida.
Si el proceso se ejecutó correctamente, se copian los valores de las variables auxiliares a los campos definitivos de los objetos o interacciones segun corresponda. Sin embargo, en ambos casos tenemos valores que no son strings. 
##### excepciones
- En objetos tenemos un booleano, por lo que hay que hacer una comparacion extra entre strings y ahi asignarle el valor correspondiente a su campo (ya que asignarle el string "true" o "false" sería incorrecto.)
- En interacciones tenemos un enum, el cual requiere de un switch en este caso para su correcta carga al campo.
Mientras la linea leida siga siendo valida (no sea `NULL` o `FEOF`) se seguiran cargado elementos a los vectores correspondientes. Y una vez que se llegue al final del archivo, se cierra el mismo y se retorna `0` (no  hubo error)
 
1. Detalles de alguna función

    Algún detalle importante sobre alguna función. La idea no es que expliques todas las funciones, es para que expliques mas en detalle las funciones mas importantes del trabajo (como por ejemplo, como funciona el insertar en una posición especifica en una lista) y como funcionan, porque están implementadas de cierta forma, etc.

2. Detalle de otra función

    Algún detalle de otra función.

#### 4. Diagramas


En esta sección van los diagramas que realizas para poder acompañar los detalles de implementación y de funciones que escribiste mas arriba. Trata de que sean lo mas claros posibles, podes hacer mas de un diagrama para una sola función, por ejemplo podes tener un diagrama por cada paso que realiza la función en vez de tener un solo diagrama (que a lo mejor termina siendo poco claro) con toda la información metida junta.


1. Diagrama1

    ![Diagrama1](https://i.imgur.com/KvYn8UD.png)

    Explicacion del diagrama1, en caso de ser necesaria.

2. Diagrama2

    ![Diagrama2](https://i.imgur.com/nhqXNr6.png)

    Explicacion del diagrama2, en caso de ser necesaria.