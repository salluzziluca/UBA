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


# ensamblador
Su laburo es mucho más sencilo que el del compilador, es menos Complejos


Proceso de ensamblado en 2 pasadas:
1. Detecta identificadores y les asigna una posicion de memoria. Crea la tabla de simbolos
2. Cada instruccion es convertida a codigo de maquina. Cada identificador es reemplazado por su ubicacion en memoria (usando la tabla de simbolos). Cada linea es procesada completamente antes de avanzar a la sig.  Genera el codigo obj y el listado

![[Pasted image 20231113170640.png]]

# Linker
## Relocalizacion
Si yo tengo más de un modulo (ej main y pepe), aunque ambos digan `org 2048` el assembler, mediante el linker, va a desplazar a pepe, a relocalizarlo, a otra direccion de memoria, generando una tabla de valores de 2048+n 
de esa forma crea el paquete con todo ordenado sin que se pise

# Linking loader
Cuando llega la hora de cargar al programa, si el sistema tiene multitasking el compilador tiene que ver donde hay espacio libre, dificilmente empiece en el 2048, asi que tiene que volver a relocalizar todas las etiquetas