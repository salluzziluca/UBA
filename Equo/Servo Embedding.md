---
Dia: 2025-02-03
dg-publish: true
---

[minibrowser](https://github.com/servo/servo/issues/30049)

[Servo embedding, create minibrowser](https://github.com/servo/servo/issues/29930)


- Esto es dificil, voy a putear. Hay approachs similares pero yo voy a estar haciendo algo completamente nuevo.
- suponiendoq ue tienene una api de embebido, en teoria lo podemos embeber en una app rust
- si nosotros despues nosotros creamos una dinamic library (DCO o dll de windows), rust te permite armar liberiras con el standar de C. Eso nos permitira cargarlo en cualquier lenguaje. 
- Complejidades: en chromium (cef) hay dos modos de funcionar. Uno es con buffer de memoria: pido un buffer, escribo los pixeles y vos despues hace lo que quieras con eso. Dame una ventana nativa del SO y yo me encargo de manejarla. De esta forma, todos los eventos de teclado y mouse los gestiona el mouse.
Parece que servo solo maneja lo 2do, en ese caso es una paja porque nosotros tenemos que avisarle todas las cosas a servo para que servo lo cambie. 

habria que ver entonces como atar los dos mundo

entender que cada ventana de java es una GTK. Asi que si tener algo que reciba una gtk, ya estamos
dont loose track of the windowed mode