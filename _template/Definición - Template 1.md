---
dg-publish: true
---
<%* 
	let titulo = tp.file.title;
	if (titulo.startsWith("Untitle")) {
		titulo = await tp.system.prompt("Nombre:");
		await tp.file.rename(titulo);
	}
	tR += "---";
%>
dia: <% tp.file.creation_date("YYYY-MM-DD") %>
<%*
	let carpeta = tp.file.folder(true);
	let materia = carpeta.split("/")[0];
	tR += "materia: " + materia;
%>
<%* 
	let capitulo = await tp.system.prompt("Capitulo: ");
	tR += "capitulo: " + capitulo;
%>
<%* tR += "---"; %>
### Definición
---
<% tp.file.cursor() %>