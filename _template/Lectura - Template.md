---
dg-publish: true
---
dia: 2024-01-23


---
### Definición
---
<% tp.file.cursor() %>
%* 
	let titulo = tp.file.title;
	if (titulo.startsWith("Untitle")) {
		titulo = await tp.system.prompt("Titulo de la lectura:");
		await tp.file.rename(titulo);
	}
	tR += "---";
%>
dia: 2024-01-23

---
### Definición
---
<% tp.file.cursor() %>
