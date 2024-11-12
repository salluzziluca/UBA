---
dg-publish: true
---
# Apareo
Tenemos dos o mas archivos de los cuales UNO es más importante. Lo que se hace es actualizar ese primer archivo con lo que tengamos en el resto.

Primero comparamos la primera fila de ambos archivos, comparando entre los dos campos ordenados de ambos archivos. Si el archivo2 tiene un campos mayor al del 1, se suma automaticamente el menor(archivo1), ya que sabemos que nunca va a volver a aparecer en al archivo2. Si al llegar al segundo del archivo1 nos encotraramos con el mismo campo, seguiriamo sumando. asi hasta dar con alguno distinto. ==al llegar a un campo distinto, cargamos la acumulacion a un archivo nuevo y seguimos==. Comparamos ambos campos y nos quedamos con el menor. Asi hasta terminar el archivo. 

![[Apareo.mp4]]
Ver apareo_ejeplo.py en vsc