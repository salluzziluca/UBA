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


## Memoria 
### Caché
#### Reemplazo en caché
[[7.0 Memoria#Associative Map Caché|LFU]]: Se agrega un identificador de frecuencia, cuando se llega a fallo se quita la menos frecuente
[[7.0 Memoria#Associative Map Caché|LRU]]: idem pero con un timestamp
[[7.0 Memoria#Associative Map Caché|FIFO]]: first in first out
[[7.0 Memoria#Associative Map Caché|Aleatorio]]

#### Tipos:
Unificada: almacena tanto datos como instrucciones (+ sim)
especializada: tiene dos partes, una para datos y otra para inst (permite + optimizacion, + compleja)
multinivel 