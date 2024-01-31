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