## De Programa a Proceso

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
Recibe: el archivo objeto (.i)
Devuelve: Un programa ejecutable con todas las librerias necesarias para que este corra, ordenadas de forma tal que no hay problemas con las posiciones de memoria

![[Pasted image 20240405140700.png]]

## En UNIX
Un programa en unix puee ser de "formato de indentificacion binario