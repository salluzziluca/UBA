---
dg-publish: true
---
1. Crea y asigna una nueva entrada en la **Process Table** para el nuevo proceso.
2. Asigna un número de ID **único** al proceso hijo.
3. Crea una copia lógica del contexto del proceso padre, algunas de esas partes pueden ser compartidas como la sección **text**
4. Realiza ciertas operaciones de I/O.
5. Devuelve el número de ID del hijo al proceso **padre** [^3], y un 0 al proceso hijo

Por dentro, lo que hace es esto: 
- chequear que haya **recursos** en el kernel;
- obtener una entrada libre de la **Process Table**, como un PID único;
- chequear que el usuario no esté ejecutando demasiados procesos;
- macar al proceso hijo en estado “siendo creado”;
- copiar los datos de la entrada en la **Process Table** del padre a la del **hijo**;
- incrementar el contador del current directoty inode;
- incrementar el contador de archivos abiertos en la **File Table**;
- hacer una copia del **contexto** del **padre** en memoria;
- crear un contexto a nivel sistema falso para el **hijo**;
    - el contexto falso contiene datos para que el hijo se reconozca a sí mismo
    - y para que tenga un punto de inicio cuando el planificador lo haga ejecutarse;