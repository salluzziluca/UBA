---
dg-publish: true
---
Si sumo dos numeros con signo y quiero ver si el resultado es representable-> miro el overflow (V)
Si sumo dos enteros sin signo y quiero saber si el resultado es representable -> miro el carry


# Teoria para que alguien me tome 
> señale todas las caracteristicas del procesador ARC que se corresponden con la fiosofia RISC. Jusitfique detalladamente su respuesta: 

El procesador ARC es un procesador de arquitectura RISC. Algunas características

1. Instrucciones simples y compactas de un tamaño fijo (32 bits) lo que permite una mayor eficiencia en la ejecución y una mayor velocidad de procesamiento.
    
2. Solo las instrucciones ld y st acceden a memoria ⇒ aumento velocidad al reducir los accesos a memoria
    
3. Uso de registros: ARC utiliza una gran cantidad de registros internos para almacenar y procesar los datos, lo que aumenta la eficiencia y reduce la necesidad de acceder a la memoria.
    
4. Permite la segmentación y paralelismo lo que posibilita que varias instrucciones puedan ser procesadas al mismo tiempo
    
5. Al manejarse con Buses puede dividir el bus del sistema en
    
    1. Bus de direcciones
    2. bus de datos
    3. bus de control
    
    y aumentar la velocidad y eficiencia al momento de acceder a memoria
    

SANTO GRIAL: cada instrucción de assembler en 1 ciclo de reloj (se apunta a que se cumpla esta filosofía, pero al tener la existencia de las microinstrucciones en la vida real no pasa). Ciclo de fetch: buscar, decodificar y ejecutar





> Indique cual es la informacion que se guarda en la tabla de simbolos y luego explique con detalle todas las instancias en que esta informacion es utilizada


La tabla de símbolos en un ensamblador es una estructura de datos que almacena información sobre identificadores (típicamente etiquetas, nombres de variables y nombres de procedimientos) utilizados en el código fuente. La información almacenada en la tabla de símbolos puede incluir:

- Nombre del símbolo
- Valor o dirección de memoria asociada con el símbolo
- Tipo de símbolo (etiqueta, variable, procedimiento, etc.)
- Otros atributos relevantes, dependiendo del ensamblador

La información en la tabla de símbolos es utilizada en diferentes etapas del proceso de ensamblaje:

1. Durante la fase de preprocesamiento, se pueden utilizar identificadores en la tabla de símbolos para sustituir las macros y las directivas.
2. Durante la fase de ensamblaje, la tabla de símbolos se utiliza para resolver las referencias a identificadores en el código fuente. Por ejemplo, una referencia a una etiqueta puede ser reemplazada por la dirección de memoria asociada con esa etiqueta.
3. Durante la fase de enlazado, la tabla de símbolos se utiliza para resolver las referencias a identificadores en diferentes módulos o archivos fuente. Por ejemplo, una referencia a una variable o procedimiento en un módulo puede ser reemplazada por la dirección de memoria asociada con ese identificador en otro módulo.

En resumen, la tabla de símbolos es una herramienta esencial en el proceso de ensamblaje que permite a los ensambladores resolver las referencias a identificadores en el código fuente y generar una representación ejecutable de ese código.

## Buses 
![[Pasted image 20231130105240.png]]
la memoria nunca genera adress y la cpu no recibe
## Memoria 
registros numerados 
32 bits (2^32-1 bytes)
![[Pasted image 20240204165846.png]]
mapa de ARC:
primeras 2040: para el SO
desde 2048 hasta la pila: espacio de usuario para programas ya ensamblados
2^{31}-1: pila (stack). Aumentá hacia posiciones inferiores, coexiste con el espacio de usuario
2^{31} hasta 2^{32}-1: I/O
#### Caché
fallo en la caché: analiza el contenido en la caché, no encuentra la palabra requerida 
#### Reemplazo en caché
[[7.0 Memoria#Associative Map Caché|LFU]]: Se agrega un identificador de frecuencia, cuando se llega a fallo se quita la menos frecuente
[[7.0 Memoria#Associative Map Caché|LRU]]: idem pero con un timestamp
[[7.0 Memoria#Associative Map Caché|FIFO]]: first in first out
[[7.0 Memoria#Associative Map Caché|Aleatorio]]

#### Tipos:
Unificada: almacena tanto datos como instrucciones (+ simple, + busqueda costosa)
especializada: tiene dos partes, una para datos y otra para inst (permite + optimizacion, + compleja, busqueda - costosa)
multinivel 
Multinivel: una parte en el procesador(L1) y otra por fuera (L2). L1 mas cercana y especializada L2 lenta y unificada

#### Tipos de asignacion:
cada linea de caché tiene 3 campos asociados:
1. etiqueta (a cual bloque de mem representa)
2. validez (si el bloque pertenece al programa en ejecución)
3. suciedad (si se hizo una modificacion en el bloque)|
- asociativa: cada bloque de memoria tiene +1 linea de caché
- directa: cada bloque de memoria tiene una sola linea de caché asignada
- asociativa por conjuntos: Un conjunto es un grupo conformado por >1 linea de caché  y c/conjunto tiene asignacion directa con memoria principal. Al lado de c/linea siguenes tando los mismos 3 campos de asoigancion asociativa

# Compilacion
1 .



![[Pasted image 20240204192210.png]]