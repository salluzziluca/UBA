---
Dia: 2025-10-04
dg-publish: true
---
Es un modelo basado en el pasaje de mensajes. El actor es la entidad principal del modelo. Son
livianos, se pueden crear miles (en lugar de threads). Encapsulan comportamiento y estado. El actor
supervisor puede crear otros actores hijo.

Compuesto por:
• Dirección: adonde enviarle mensajes. Es como su “nombre” o ID
• Casilla de correo (mailbox): un FIFO de los últimos mensajes recibidos.
Se encolan los mensajes que se reciben; entonces cada actor va a estar procesando de su mailbox
cada mensaje de forma secuencial. De esta manera evitan las secciones críticas. Hay memoria
local para cada actor que se va a mutar a partir del procesamiento secuencial de cada mensaje.
• cuando ejecuto el channel, le tengo que asignar un tipo.
Aca no le asigno pues lo infiere de la primera vez que
utilizo el extremo de transmisión → me impide utilizar
ese canal para otro tipo de dato
• val alojada en el heap, se envía el string a través de tx.
• rx recibe el elemento a través del result. Se transfirió el
ownership, ahora el receive es dueño de ese string
38
Son aislados de otros actores: no comparten memoria. Además, su estado privado solo puede
cambiarse a partir de procesar mensajes. Pueden manejar un mensaje por vez.
Su estado interno es un mutex implícito. como solo pueden procesar un mensaje por vez, mientras
el actor maneja ese mensaje no puede procesarse otro al mismo tiempo, y por ende no voy a poder
tener dos cosas intentando de mutar el estado interno del actor al mismo tiempo.
Los actores se comunican entre ellos solamente usando mensajes, que son procesados por los
actores de forma asincrónica. Los mensajes son estructuras simples inmutables. No hay
condiciones de carrera entre los datos, no hay que poner locks entre los datos; una vez que el
emisor tiene el mensaje que le va a enviar, el receptor no lo puede modificar, el mensaje es fijo,
entonces no hay peligro de estar sobreescribiendo los datos.
Los actores pueden crear otros actores. Estos nuevos actores serán actores hijos y el actual que
los crea es un actor supervisor. No comparte memoria con otros actores.
Actores en Rust (usando Actix, un framework de actores)
Usa tokio (runtime asincrónico) y futures (operaciones async y await).
Tiene un Arbiter. Un arbiter es básicamente un hilo del SO que: corre un event loop interno, aloja
uno o más actores (son livianos) y administra tareas asincrónicas como futures, timers y el envío de
mensajes entre actores. Posee un handler que se usa para enviar mensajes al actor.
Se ejecutan en un contexto de ejecución Context<A>. Cada actor tiene su propio Context<A> donde:
• Se gestiona su casilla de mensajes.
• Se ejecuta su lógica.
• Puede detenerse o reiniciarse.
Para crear un actor:
1. Crear una estructura (struct) para representar al actor.
2. Implementar el trait Actor para esa estructura.
3. Definir un tipo de mensaje (implementando el trait Message).
4. Implementar un handler para ese mensaje usando el trait Handler<M>.
5. Spawnear el actor con .start(), que lo ejecuta dentro de un Arbiter.