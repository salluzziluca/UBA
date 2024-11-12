---
dg-publish: true
---
![[Pasted image 20221006160242.png]]
---
# Patrones de Creación
# 1. Abstract Factory
> Proporciona una interfaz para crear familias de objetos relacionados o que dependen entre sí, sin especificar sus clases concretas

Este patrón se usa cuando tenemos varias clases diferentes, pero relacionadas que pueden tener 2 o más variantes de ellas mismas. Para esto abstraemos esas clases utilizando interfaces y luego abstraemos una fábrica que devuelve esas interfaces. De esa forma, podemos crear fábricas que devuelvan una variante concreta de esas clases.
![[Pasted image 20221016172250.png]]
Un ejemplo concreto seria con botones de una web page. tenemos el boton de inicio y el de busqueda y necesitamos que sean de x forma y color para windows y de x forma y color para mac.

# 2. Builder
> Separa la construcción de un objeto complejo de su representación, de forma que el mismo proceso de construcción pueda crear diferentes representaciones.

En vez de tener un constructor que sea `Casa(true, true, false, true, true, true)`. Utilizamos una interfaz builder, la cual tiene diferentes parámetros correspondientes a las diferentes características de la clase que estemos construyendo. 
```
car.setSeat(int)
car.serEngine(Engine)
```
Adicionalmente, podemos tener un director el cual se encarga de gestionar las construcciones y nos puede ayudar a construir versiones ya definidas de la clase. 
![[Pasted image 20221016175712.png]]Ejemplo de un director concreto
![[example-en 1.png]]
# 3. Factory Method
> Define una interfaz para crear un objeto, pero deja que sean las subclases quienes decidan qué clase instanciar. Permite que una clase delegue en sus subclases la creación de objetos.

Es util cuando tenemos dos clases que hacen lo mismo con sus variaciones en comportamientos internos (Entrega de pedidos en bici, en moto y en helicóptero). De esa forma, mientras ambos productos cumplan con la interfaz correspondiente, la clase `Creador` puede crearlos a cualquiera de los dos. No tenes atado todo a una clase particular y toda al logica que decide cual de las variantes del objeto elegir está dentro del creador.

![[Pasted image 20221016181646.png]]

# Prototype 
>Especifica los tipos de objetos a crear por medio de una instancia prototípica, y crea nuevos objetos copiando de este prototipo.

Todo aquel objeto que pueda ser clonado implementa la interfaz prototype, y ahi se especifica su clonacion. Esto permite acceder a los campos privados tambien y realizar una clonacion exitosa

![[Pasted image 20221016183403.png]]

# Singleton
>Garantiza que una clase sólo tenga una instancia, y proporciona un punto de acceso global a ella.

Se trata de reutilizar la misma instancia cada vez que se la llama
![[Pasted image 20221017195433.png]]

# Patrones Estructurales
# Adapter
>Convierte la interfaz de una clase en otra distinta que es la que esperan los clientes. Permite que cooperen clases que de otra manera no podrían por tener interfaces incompatibles.

Es un PUTISIMO ADAPTADOR, no hay mas magia. Clase 1 habla español Clase 2 habla ingles el adapter adapta de español a ingles, LISTOOO.
![[Pasted image 20221017195645.png]]

# Bridge
>Desacopla una abstracción de su implementación, de manera que ambas puedan variar de forma independiente.

Permite dividir una clase grande en dos partes de la misma (abstracción e implementación), para que puedan laburar una independientemente de la otra.
La abstracción delega a la implementación, siempre.
Este patron permite escalar ambas partes tranquilamente sin tener que laburar de manera monolitica.
![[Pasted image 20221017200342.png]]
# Composite
>Combina objetos en estructuras de árbol para representar jerarquías de parte-todo. Permite que los clientes traten de manera uniforme a los objetos individuales y a los compuestos.

==Solo tiene sentido si el modelo central del programa puede representarse en forma de [[Arboles|arbol]]== 
Si vos necesitas ejecutar una accion que involucre la totalidad de varios elementos que esten nesteados, simplemente se lo pedis al primero y haces que este se lo pida a sus hijos, y estos a sus hijos, y asi [[Algoritmos Recursivos|recursivamente]]
![[Pasted image 20221017201559.png]]
El Composite siempre delega el trabajo a sus componentes hijos.

# Decorador
>Añade dinámicamente nuevas responsabilidades a un objeto, proporcionando una alternativa flexible a la herencia para extender la funcionalidad.

Es una alternativa a la herencia que permite agregarle funcionalidades a una clase en tiempo de ejecución. A la hora decorar la clase, simplemente le pasamos la clase anterior como parametro al constructor de la clase decorada.
	![[Pasted image 20221017201852.png]]
# Façade
>Proporciona una interfaz unificada para un conjunto de interfaces de un subsistema. Define una interfaz de alto nivel que hace que el subsistema sea más fácil de usar.

![[Pasted image 20221017202900.png]]
ejemplo:![[Pasted image 20221017203020.png]]
# Flyweight
>Usa el compartimiento para permitir un gran número de objetos de grano fino de forma eficiente.

Solo se conserva dentro del objeto la parte intrínseca, la que SIEMPRE va a estar junto al objeto no matter what. El resto de variables del objeto que puedan mutar o demanden cómputo se extraen a una nueva clase que se encarga de procesarlo. De esa forma no se gastan recursos en cosas que nunca van a cambiar.
![[Pasted image 20221017203428.png]]

# Proxy 
>Proporciona un sustituto o representante de otro objeto para controlar el acceso a este

En vez de que el cliente se comunique directamente con el objeto, se comunica con el proxy y este con el objeto original. 
![[Pasted image 20221017204232.png]]
# Patrones de Comportamiento
# Chain of Responsibilty
>Evita acoplar el emisor de una petición a su receptor, al dar a más de un objeto la posibilidad de responder a la petición. Crea una cadena con los objetos receptores y pasa la petición a través de la cadena hasta que ésta sea tratada por algún objeto.

![[Pasted image 20221017204825.png]]
![[Pasted image 20221017205016.png]]

# Command
>Encapsula una petición en un objeto, permitiendo así parametrizar a los clientes con distintas peticiones, encolar o llevar un registro de las peticiones y poder deshacer las operaciones.

El invoker handelea las peticiones y las manda mediante un comando, el cual lo ejecuta en el reciever adecuado.

![[Pasted image 20221017205145.png]]


# Interpreter
>Dado un lenguaje, define una representación de su gramática junto con un intérprete que usa dicha representación para interpretar sentencias del lenguaje.

Esto es literalmente los regex, pero literalmente. Cuando dice lenguaje se refiere a posta un lenguaje humano![[Pasted image 20221019174953.png]]
# Iterator
>Proporciona un modo de acceder secuencialmente a los elementos de un objeto agregado sin exponer su representación interna.

![[Pasted image 20221017211306.png]]

# Mediador
>Define un objeto que encapsula cómo interactúan un conjunto de objetos. Promueve un bajo acoplamiento al evitar que los objetos se refieran unos a otros explícitamente, y permite variar la interacción entre ellos de forma independiente.

Es como una torre de control o un organizador para el resto del sistema.
![[Pasted image 20221017211533.png]]

# Memento
>Representa y externaliza el estado interno de un objeto sin violar la encapsulación, de forma que este puede volver a dicho estado más tarde.

Literalmente git

![[Pasted image 20221017211845.png]]

# Observer
>Define una dependencia de uno-a-muchos entre objetos, de forma que 
>cuando un objeto cambie de estado se notifica y se actualizan automáticamente todos los objetos que dependen de él

el publisher se guarda un array de subscribers (objetos que quieren ser notificados cuando cambie). Cuando haya un nuevo evento, el publisher llama notify subscribers con toda la lista de subscribers.
![[Pasted image 20221017212219.png]]

# State
> Permite que un objeto modifique su comportamiento cada vez que cambie su estado interno. Parecerá que cambia la clase del objeto.

Para una clase con muchos comportamientos posibles, almacenamos cada uno de esos subcomportamientos en otras clases. Luego el contexto se encarga de cambiar de estado y de ejecutar esos comportamientos
![[Pasted image 20221017212726.png]]

# Strategy
>Define una familia de algoritmos, encapsula cada uno de ellos y los hace intercambiables. Permite que un algoritmo varíe independientemente de los clientes que lo usan.

cuando una clase hace algo especifico en diferentes formas podes agrupar esas formas en estrategias, y modularizarlas en clases concretas. Luego, el contexto setea esas estrategias y las ejecuta.
![[Pasted image 20221017213114.png]]
# Template Method
>Define en una operación el esqueleto de un algoritmo, delegando en las subclases algunos de sus pasos. Permite que las subclases redefinan ciertos pasos del algoritmo sin cambiar su estructura 

Primero modularizas los metodos de una clase y luego te fijas cuales comparte con sus clases allegadas, de esta forma podes compartir codigo up to a point
![[Pasted image 20221017213454.png]]

# Vistor
>Representa una operación sobre los elementos de una estructura de objetos. Permite definir una nueva operación sin cambiar las clases de los elementos sobre los que opera

En vez de que cada clase ejecute el metodo en cuestion, creas una clase visitante que pase por cada una de las clases involucradas y ejecute ese metodo. asi no alteramos el comportamiento original de las clases
![[Pasted image 20221017213802.png]]

![[Pasted image 20221018120141.png]]![[Pasted image 20221020113528.png]]
![[Pasted image 20221018120308.png]]
# Asociación
La clase A “tiene” a la clase B como parámetro.

# Inheritance
Tiene que haber un extends, la clase B hereda las características de la clase A.

# Realización/Implementación
La clase A implementa una interfaz o clase abstracta

# Dependencia
Es más débil que la asociación, no están tan acopladas las clases, ya que el objeto A no tiene al objeto B como atributo. Sea que lo utiliza por haberlo recibido por parámetro o por haberlo creado

# Agregación
son independientes, pero conviven juntos, en este caso ambos interaccionan y se mandan mensajes.

# Composición
Un objeto compone a otro y tienen el mismo ciclo de vida. Usualmente, solo el objeto compuesto se comunica con el que compone
