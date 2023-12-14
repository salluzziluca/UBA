---
cuatri: 20C1
estado: cursando
---
### Apuntes
---
```dataviewjs
	function conseguir_nombre(unidad) {
		let relative_path = unidad.rows[0].file.folder;
		let spliteado = relative_path.split("/");
		return spliteado[spliteado.length - 1];
	}

	const pagina_actual = dv.current();
	const carpeta = '"' + pagina_actual.file.folder + '"';
	const paginas = dv.pages(carpeta)
		.where(pagina => {
			if (!pagina.capitulo)
				return false;
			return pagina.file.name != pagina_actual.file.name;
		});

	let unidades = paginas.groupBy(pagina => pagina.capitulo)
		.sort(capitulo => {
			return capitulo.rows[0].capitulo;
		});
		
	for (let unidad of unidades) {		
		dv.table([conseguir_nombre(unidad)], (unidad.rows.file).map(pagina => {
			let path = pagina.path;
			let nombre = pagina.name;
			return ["[[" + path + "|" + nombre + "]]"];
		}));

		dv.el("br", "");
	}
```

<%* 
	let titulo = tp.file.title;
	if (titulo.startsWith("Untitle")) {
		titulo = await tp.system.prompt("Materia:");
		await tp.file.rename(titulo);
	}
_%>
---
<%* 
	let anio = await tp.system.suggester([
		"2020", "2021", "2022", "2023", "2024", "2025", "2026"
	], [
		"20", "21", "22", "23", "24", "25", "26"
	]);
	
	let cuatrimestre = await tp.system.suggester([
		"Primer cuatrimestre", "Segundo cuatrimestre"
	], [
		"C1", "C2"
	]);

	tR += "cuatri: " + anio + cuatrimestre;
%>
estado: <% tp.system.suggester([
	"No empezado", "Cursando", "En proceso", "Terminado",
], [
	"no-empezado", "cursando", "en-proceso", "terminado",
]) %>
---
### Apuntes
---
```dataviewjs
	function conseguir_nombre(unidad) {
		let relative_path = unidad.rows[0].file.folder;
		let spliteado = relative_path.split("/");
		return spliteado[spliteado.length - 1];
	}

	const pagina_actual = dv.current();
	const carpeta = '"' + pagina_actual.file.folder + '"';
	const paginas = dv.pages(carpeta)
		.where(pagina => {
			if (!pagina.capitulo)
				return false;
			return pagina.file.name != pagina_actual.file.name;
		});

	let unidades = paginas.groupBy(pagina => pagina.capitulo)
		.sort(capitulo => {
			return capitulo.rows[0].capitulo;
		});
		
	for (let unidad of unidades) {		
		dv.table([conseguir_nombre(unidad)], (unidad.rows.file).map(pagina => {
			let path = pagina.path;
			let nombre = pagina.name;
			return ["[[" + path + "|" + nombre + "]]"];
		}));

		dv.el("br", "");
	}
```
