<%* 
	let titulo = tp.file.title;
	if (titulo.startsWith("Untitle")) {
		titulo = await tp.system.prompt("Titulo de la lectura:");
		await tp.file.rename(titulo);
	}
	tR += "---";
%>
dia: <% tp.file.creation_date("YYYY-MM-DD") %>
<%* 
	let link = await tp.system.prompt("Link: ");
	tR += "referencia: [\n\t" + link + ",\n]";
%>
<%* tR += "---"; %>
### Definición
---
<% tp.file.cursor() %>
