---
dg-publish: true
---
Una vez que se edita un porograma en cualquier lang. Este se debe compilar para obtener un programa ejecutable. Compilar es considerado una actividad atómica, con varias etapas puntuales con herramientas especificas.

La fase de compilacion son 4 etapas que utilizan 4 herramientas:
1. El preprocesador
2. el compilador 
3. el [[ensamblador]]
4. el link editor o linker. Linking loader

### Procesamiento
Recibe: Un programa en C
El procesador (cpp) modifica el codigo fuente original del porgrama en C de acuerdo a las directivas que comienzan con `#`. 
Devuelve: Otro programa en C con la extension `.i`

### Compilación 
Recibe: un programa C en .i
Devuelve: Un archivo de texto .s con las instrucciones de assembly

### Ensamblaje 
Recibe: Un programa assembly en .s
Traduce el archivo a instrucciones del lenguaje de maquina empaquetandolas en un formato conocido como `relocatable object file` (.o). 
Devuelve: un .o

### LInk Editor 
![[Pasted image 20240405144211.png]]
Recibe: el archivo objeto (.i)
Devuelve: Un programa ejecutable con todas las librerias necesarias para que este corra, ordenadas de forma tal que no hay problemas con las posiciones de memoria


![[Pasted image 20240405140700.png]]

## En UNIX 
Un program es un archivo que posee toda la informacion de como construir un proceso en memoria. Este contiene 
- Formato de Identificacion Binaria: Cada archivo posee metadata describiendo el formato ejecutable. este puede ser a.out (assembler output), COFF (common object file format) o [[ELF]] (excecutable and linking format)
- Instrucciones del lenguaje de maquina
- Direccion del punto de entrada del programa (identifica la direccion con la cual la ejecucion del programa debe iniciar)
- Datos: Valores de los datos con lo scuales deben inicializar [[variables]], [[constantes]] y literales.
- Simbolos y tablas de realocacion
- bibliotecas compartidas
- informacion adicional.


---

Un programa es algo sin vida, es el SO el que toma ese puñado de bytes y lo transforma en algo util, mediante el [[kernel]]. 

El **Sistema Operativo** más precisamente el **[[Kernel]]** se encarga de:

1. Cargar instrucciones y Datos de un programa ejecutable en memoria.
    
2. Crear el Stack y el [[Heap]] 
    
3. Transferir el Control al programa
    
4. Proteger al SO y al Programa