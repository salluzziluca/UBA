---
dg-publish: true
---
<%* 
	let titulo = tp.file.title;
	if (titulo.startsWith("Untitle")) {
		titulo = await tp.system.prompt("Articulo:");
		await tp.file.rename(titulo);
	}
	tR += "---";
%>
dia: <% tp.file.creation_date("YYYY-MM-DD") %>
tipo: referencia
<%* 
	let contador = 1;
	let link = await tp.system.prompt("Link: ");
	let referencias = "referencia: [\n\t" + link;
	while (link !== null && link !== "") {
		contador++;
		link = await tp.system.prompt("Link n°" + contador + ": ");
		if (link !== null && link !== "") 
		referencias += ",\n\t" + link;
	}
	tR += referencias + ",\n]";
%>
<%* 
	contador = 1;
	let autor = await tp.system.prompt("Autor: ");
	let autores = "autor: [\n\t" + autor;
	while (autor !== null && autor !== "") {
		contador++;
		autor = await tp.system.prompt("Autor n°" + contador + ": ");
		if (autor !== null && autor !== "") 
			autores += ",\n\t" + autor;
	}
	tR += autores + ",\n]";
%>
<%* tR += "---"; %>
### Definición
---
<% tp.file.cursor() %>
