---
Dia: 2025-09-22
dg-publish: true
---
>[!example] Herramientas de sincronización que permite a los hilos tener exclusión mutua y la posibilidad de esperar (block) por que una condición se vuelva falsa. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple

Un monitor consta de:
- Nombre
- Variables internas
- Procedimientos del monitor: rutinas que acceden directamente a las variables internas
- Una interfaz pública para que los procesos puedan acceder a las variables internas
- Inicialización de las variables internas
- Un conjunto de condition variables que incorporan sincronismo al monitor

Los procesos pueden tomar distintos estados:
- Esperando para entrar al monitor
- Ejecutando el monitor (sólo un proceso a la vez - exclusión mutua)
- Bloqueado en FIFO de variable de condición
- Recién liberado de la wait condition
- Recién completó una operación signalC


| Semaforo                                                                        | Monitor                                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| wait puede o no bloquear                                                        | waitC siempre bloquea                                                                       |
| signal siempre tiene efecto                                                     | signalC no tiene efecto si la                                                               |
| signal desbloquea un proceso arbritrario                                        | signalC desbloquea el proceso del tope de la cola                                           |
| un proceso desbloqueado con signal, puede continuar la ejecución inmediatamente | un proceso desbloqueado con signalC debe esperar que el proceso señalizador deje el monitor |

## Concurrencia en Java - Hilos y Sincronización

#### 1. Creación de Hilos

###### Formas de crear hilos en Java

Existen **dos formas principales** para crear hilos:

1. **Heredando de la clase `Thread`**
2. **Implementando la interfaz `Runnable`**

###### ¿Cuándo usar cada una?

- Es una **decisión de diseño** que depende de la estructura de clases de la aplicación
- Al implementar `Runnable` se puede **extender otra clase** (ventaja importante dado que Java no permite herencia múltiple)

###### Ejemplo 1: Heredando de Thread

```java
public class HiloThread extends Thread {
    public void run() {
        System.out.println("Hola, soy el hilo " + 
            Thread.currentThread().getId() + " y heredo de Thread");
        System.out.println("Termine");
    }
}
```

###### Ejemplo 2: Implementando Runnable

```java
public class HiloRunnable implements Runnable {
    public void run() {
        System.out.println("Hola, soy el hilo " + 
            Thread.currentThread().getId() + " e implemento Runnable");
        System.out.println("Termine");
    }
}
```

###### Programa principal - Uso de ambos enfoques

```java
public class Ejemplo1 {
    public static void main(String[] args) {
        HiloThread hilo1 = new HiloThread();
        Thread hilo2 = new Thread(new HiloRunnable());
        
        hilo1.start();
        hilo2.start();
    }
}
```

#### 2. Secciones Críticas

###### Bloques synchronized

- **Mecanismo propio de Java** para controlar el acceso concurrente
- Tiene **dos partes**:
    - Un objeto que servirá como **lock**
    - Un bloque de código a ejecutar de forma **atómica**

###### ¿Cómo funciona?

- Cada objeto tiene un **lock o monitor**
- **Sólo un hilo a la vez** puede tomar el lock
- El lock es **reentrante** (el mismo hilo puede adquirirlo múltiples veces)

###### Métodos synchronized

Cuando un bloque de código es un método completo, se puede declarar como `synchronized`.

###### Ejemplo: Bloque synchronized

```java
public void incrementar(int cantidad) {
    synchronized (this) {
        this.valor += cantidad;
        System.out.println("Contador: valor actual = " + this.valor);
    }
}
```

###### Ejemplo: Método synchronized

```java
public synchronized void incrementar(int cantidad) {
    this.valor += cantidad;
    System.out.println("Contador: valor actual = " + this.valor);
}
```

###### Synchronized en métodos estáticos

######## Bloque synchronized en método estático

```java
public static void escribirMensaje(String mensaje) {
    synchronized (Contador.class) {
        System.out.println("Mensaje del contador");
    }
}
```

######## Método estático synchronized

```java
public static synchronized void escribirMensaje(String mensaje) {
    System.out.println("Mensaje del contador");
}
```

#### 3. Exclusión Mutua

###### Regla importante

Los hilos participantes deben **sincronizarse con el mismo objeto** para lograr exclusión mutua.

###### ✅ Ejemplo correcto - CON exclusión mutua

```java
public static void main(String[] args) {
    Contador contador = new Contador(); // MISMO objeto
    Thread hilo1 = new Thread(new Hilo(contador));
    Thread hilo2 = new Thread(new Hilo(contador));
    
    hilo1.start();
    hilo2.start();
}
```

###### ❌ Ejemplo incorrecto - SIN exclusión mutua

```java
public static void main(String[] args) {
    Contador contador1 = new Contador(); // Objetos DIFERENTES
    Contador contador2 = new Contador();
    Thread hilo1 = new Thread(new Hilo(contador1));
    Thread hilo2 = new Thread(new Hilo(contador2));
    
    hilo1.start();
    hilo2.start();
}
```

#### 4. Señalización de Hilos

###### Prerequisito

Se debe **tener el monitor adquirido** para poder llamar a los métodos de señalización.

###### Métodos principales

- **`wait()`**: Libera el monitor adquirido y suspende el hilo hasta que otro hilo llame a `notify()` o `notifyAll()`
- **`notify()`**: Despierta alguno de los hilos que espera por el monitor
- **`notifyAll()`**: Despierta todos los hilos que esperan por el monitor

###### Ejemplo: Buffer con sincronismo

```java
public class Buffer {
    private int valor = 0;
    
    public synchronized int getValor() {
        try {
            wait(); // Espera hasta que se notifique
        } catch (InterruptedException e) {}
        return valor;
    }
    
    public synchronized void setValor(int valor) {
        this.valor = valor;
        notifyAll(); // Despierta a todos los hilos esperando
    }
}
```

#### 5. Variables Volatile

###### Problema del cache

- Los hilos guardan los valores de las variables compartidas en sus **caches**
- Esto puede causar que los hilos vean valores desactualizados

###### Solución: volatile

- La palabra clave `volatile` indica al compilador que el valor de la variable **no debe cachearse**
- Debe leerse **siempre de la memoria principal**
- De este modo, los hilos verán siempre el **valor más actualizado** de la variable

###### Importante

- La declaración de una variable como `volatile` **no realiza ningún lockeo** en dicha variable
- Solo garantiza visibilidad, no atomicidad
