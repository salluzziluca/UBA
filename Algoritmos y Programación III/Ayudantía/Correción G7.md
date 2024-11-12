---
dg-publish: true
---
Criterios etapa 3:  

- Ejecutar la aplicación. Verificar que se pueda jugar una partida de inicio a fin, de al menos uno de los dos solitarios.
- Para encontrar bugs: Ponerse el sombrero de "tester" e intentar "romper" el juego. Hacer movimientos inválidos, hacer clicks en lugares inesperados, mover y redimensionar la ventana, etc.
- Si hay bugs que impiden llegar al fin del juego, es reentrega.
- Si hay bugs que no impiden la finalización, marcarlos pero no es necesariamente para reentrega.
- Revisar que funcione la persistencia. Que el archivo se almacene en una ruta relativa y que la extensión sea correcta (ej: que no le pongan `.txt` si es un archivo binario).
- Revisar el código y como siempre, verificar que usen bien los conceptos de OO, que no violen demasiados principios, etc.

- Revisar particularmente el uso de excepciones. Es muy común que hagan cosas como `catch (e) { System.out.println(e); }` o `catch (e) { throw e; }` lo cual no tiene sentido.

- NO evaluamos nada con respecto a la "belleza visual" o la usabilidad (a menos que sea realmente inusable o muy difícil de jugar).
- Esta etapa va con nota numérica, entre 4 y 10, dependiendo de la cantidad de bugs (no críticos) y la elegancia del código.
- Una vez que aprueban, pueden reentregar una vez para subir la nota (siempre antes de la fecha límite de aprobación).
- Antes de poner la nota, revisar los autores de los commits. Si los integrantes del grupo commitearon más o menos balanceado es la misma nota para ambos. Si casi todos los commits son de un solo integrante es sospechoso. Para revisar los autores de los commits: `git shortlog -s -n --all --no-merges`



Hacer que cuando saco la carta dada vuelta de la pila la pongo en el solitario, automaticamente se de vuelta la siguiente