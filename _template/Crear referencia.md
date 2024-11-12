---
dg-publish: true
---
<%*
	let template = await tp.file.find_tfile("Referencia - Template");
	let titulo = await tp.system.prompt("Articulo:");
	let carpeta = await this.app.vault.getAbstractFileByPath("referencias");

	tp.file.create_new(template, titulo, true, carpeta);
_%>