---
Dia: 2025-08-26
dg-publish: true
---
También conocido como "Modelo Paralelismo Fork Join".

>[!info] Modelo para paralelizar computo. Nos asegura que es libre de [[Race Condition]]. Es completamente deterministico. No depende de la velocidad de los hilos

-  El computo (task) se divide en sub computos menores (subtasks). Estos se unen en un join para construir la solucion al computo inicial. Generamos un arboles de subtareas.

- Estas subtareas se pueden crear en cualquier momento de la ejecucion de la tarea 

- Estas no deben bloquearse, excepto para esperar al final a las otras que siguen corriendo.

Performance: en el caso idel t_secuencial/N_threads


Ejemplo: Programa basico secuencial 

```rust 
fn process_files(filenames: Vec<String>)
-> io::Result<()> {
	for document in filenames {
		let text = load(&document)?; // leer un archivo
		let results = process(text); // realizar el computo
		save(&document, results)?; // escribir resultados
	}
Ok(())
}
```

![[Pasted image 20250826194846.png]]