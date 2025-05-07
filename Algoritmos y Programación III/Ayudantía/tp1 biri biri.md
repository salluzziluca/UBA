
- [x]   ievisar que el juego sea jugable, con el mouse y con el teclado. Que al finalizar el juego se pueda jugar de nuevo.
- [x] Verificar que el diagrama de clases sea correcto.
- [x] Se espera que el código sea razonablemente elegante y legible, y que usen correctamente el paradigma de objetos.
    - [x] Verificar que usen polimorfismo correctamente para los diferentes tipos de robots.
- [x] Deben estar bien separadas la vista de la lógica. En las clases del modelo no debe haber ninguna dependencia (directa o indirecta) a javafx.
    - [x] No es obligatorio que hagan MVC, pero si decidieron hacerlo, revisar que el controlador también esté bien separado de las vista y el modelo. Que no haya responsabilidades mezcladas.
- [x] Al marcar algo para corregir en el código es preferible indicar cuál es el principio que se viola y por qué.
- [x] No evaluamos nada con respecto a la "belleza visual" o la usabilidad (a menos que sea realmente inusable).
- [x] Prohibido:
    - [ ] Variables globales / static (sí se permite `static final` para constantes)
    - [ ] Clases o métodos demasiado largos, código spaghetti
    - [ ] `instanceof` (en el 99% de los casos viola OCP o TDA)
- [ ] En caso de que la entrega no cumpla alguno de los requisitos mínimos, pedir reentrega.
    - [ ] En caso de pedir reentrega, especificar los requisitos mínimos para aprobar.
- [ ] En caso de estar aprobado, la corrección lleva nota.
    - [ ] Si cumple los requisitos mínimos, a partir de ahí es una nota entre 4 y 10 dependiendo de cuán elegante sea el código.
- [ ] Antes de poner la nota, revisar los autores de los commits. Si los integrantes del grupo commitearon más o menos balanceado es la misma nota para ambos. Si casi todos los commits son de un solo integrante es sospechoso. En ese caso preguntarle a los integrantes qué onda.

Para revisar los autores de los commits: `git shortlog - [ ]s - [ ]n - [ ]- [ ]all - [ ]- [ ]no- [ ]merges`  

- [ ] Solo hay 2 instancias de corrección, con las fechas límite especificadas en el calendario. Si no entregaron en la primera fecha, pierden una instancia de corrección. Si el TP no está aprobado en la 2da instancia, pierden la materia.



### bugs
Cuando los robots mueren justo en el mismo cuadroo que el jugador, el jugador sigue Vivo
las lineas del tablero se mueven raro