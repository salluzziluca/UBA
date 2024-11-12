---
dg-publish: true
---
>Ir de codigo fuente a codigo assembler

## frontend

### Analisis léxico 
Analizar las palabras y ver si pertenecen al lenguaje o no (las agrega a la tabla de simbolos)simbolos

### Analisis sintáctico
analiza la estructura de la cadena de palabras

### analisis semántico
Asociar a cada variable: tipo, ambito, congruencias

## Backend
### mapeo de acciones

#### Operaciones ariméticas/lógicas

#### Estructuras decontrol de flujo del programa

#### Donde almacenar RAM
Las variables estaticas (globales) permanecen a lo largo del tiempo de ejecución de la app-> se guarda en posición de memoria conocida e tiempo de compilación

Las variales locales se guardan en el stack y desaparecen cuando termina el procedimiento que las llama 

### generacion de codigo

lo pasa a assembler