<---
dia: 2024-01-23
referencia: 


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
dia: 2024-03-20
referencia: [
	asdas,
]
---
### Definición
---
<% tp.file.cursor() %>
