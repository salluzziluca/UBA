---
Dia: 2024-11-05
dg-publish: true
---
 Es una base de datos wide row. Surgio en facebook en el 2008 y la compro APache en el 2009. La usan facebook, tuiter y netflix.

En vez de una tabal tenemos una familia de columnas
Una fila está formada por una clave compuesta. 
No es libre de esquema 
![[Pasted image 20241105200453.png]]
### Arquitectura share-nothing 
No existe un nodo padre, todos son peers. Eso la vuelve muy escalable 
Está optimizado para ofrecer una alta tasa de escrituras.
