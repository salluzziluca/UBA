---
dg-publish: true
---
<%*

	let carpeta = tp.file.folder(true);
	let materia;
	if (carpeta == "/") {
		let materiaArchivo = await preguntarMateria(dv);
		if (!materiaArchivo)
			return salir("No se ingreso una materia");
		materia = materiaArchivo.file.folder.split("/")[0];
	} else {
		materia = carpeta.split("/")[0];
	}
	
	let tema = await tp.system.prompt("Cuál va a ser el nuevo tema?");
	if (!tema) return salir("No se ingreso un tema");
	
	let pathActual = tp.file.path(true);
	let temasExistentes = dv.pages(`"${materia}" and -#materia`)
		.filter(archivo => archivo.file.path != pathActual)
		.sort(archivo => parseInt(archivo.capitulo, 10))
		.groupBy(archivo => parseInt(archivo.capitulo, 10))
		.map(grupoCapitulo => {
			let primero = grupoCapitulo.rows[0];
			let capitulo = parseInt(primero.capitulo, 10);
			let nombre = primero.file.folder.split("/")[1];
			return [nombre, capitulo];
		});

	if (temasExistentes.length == 0) {
		moverArchivo(tema, materia);
		crearFrontmatter(1, materia);
	} else {
		let opciones = temasExistentes.map(([nombre, capitulo]) => {
			return `Después de ${nombre}, con el capitulo: ${capitulo + 1}`;
		}).values;
		let [primerNombre, primerCapitulo] = temasExistentes[0];
		opciones.splice(0, 0, `Antes de ${primerNombre}, con el capitulo: ${primerCapitulo}`);
		
		let resultados = temasExistentes.map(([_, capitulo]) => capitulo + 1).values;
		resultados.splice(0, 0, primerCapitulo);

		let capitulo = await tp.system.suggester(opciones, resultados, false, "Donde se ubica el nuevo tema?");
		if (!capitulo)
			return salir("No se ingreso la ubicación del tema");

		let tArchivos = dv.pages(`"${materia}" and -#materia`)
			.filter(archivo => {
				if (archivo.file.path == pathActual)
					return false;
				return archivo.capitulo >= capitulo;
			})
			.map(archivo => tp.file.find_tfile(archivo.file.path))
			.values;

		for (let tArchivo of tArchivos) {
			await app.fileManager.processFrontMatter(tArchivo, (frontmatter) => {
				frontmatter["capitulo"] = frontmatter["capitulo"] + 1; 
			});
		}

		moverArchivo(tema, materia);
		crearFrontmatter(capitulo, materia);
	}

	async function preguntarMateria(dv) {
		let materias = dv.pages("#materia");
		return tp.system.suggester(
			materia => materia.file.name, 
			materias, 
			false, 
			"En que materia estaría este archivo?");
	}

	async function moverArchivo(tema, materia) {
		try {
			await this.app.vault.createFolder(`${materia}/${tema}`);
		} catch {}

		let tempCreado = false;
		let contador = 0;
		let nombre = "temp";
		while (!tempCreado) {
			try {
				await tp.file.move(`${materia}/${tema}/${nombre}`);
				tempCreado = true;
			} catch {}	
			contador++;	
			nombre = `temp (${contador})`;
		}
	}

	function crearFrontmatter(capitulo, materia) {
		tR += "---\n";
		
		let dia = tp.file.creation_date("YYYY-MM-DD");
		tR += `dia: ${dia}\n`;
		tR += `materia: ${materia}\n`;
		tR += `capitulo: ${capitulo}\n`
		
		tR += "---\n";
		
		tR += "### Definición\n---";
	}

	async function salir(mensaje) {
		let archivoActivo = app.workspace.getActiveFile();
		new Notice(mensaje);
		await app.vault.trash(archivoActivo, true);
	}
%>
<% tp.file.cursor() %>