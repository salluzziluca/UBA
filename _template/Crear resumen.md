---
dg-publish: true
---
<%*
	let template = await tp.file.find_tfile("Resumen - Template");
	let libro = await tp.system.prompt("Nombre del libro: ");
	let capitulo = await tp.system.prompt("Nombre del capitulo:");
	let titulo = libro + " - " + capitulo;
	let carpeta = await this.app.vault.getAbstractFileByPath("referencias");

	tp.file.create_new(template, titulo, true, carpeta);
_%>