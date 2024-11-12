---
dg-publish: true
---
# Corte de Control
Es una serie de whiles que corre segun uno de los campos de un csv, ese campo tiene que estar ordenada.
ej: mientras el campo tenga la misma fecha---> hago algo, cuando cambia, hago otra cosa.
![[Pasted image 20211116193610.png]]
## Pasos
1) Abrimos el archivo
2) Separamos los diferentes campos 
```py
def leer(archivo):
	linea = ar_ventas.readline() 
	if linea:
		devolver = linea.rstrip("\n").split(",")
	else:
		devolver = "","","0","0" 
	return devolver

```
3) y los igualamos a variables
 ```py  
 campo1, campo2, campo3, campo4 = leer(ventas)
 campo2 = int(campo2)
 campo3 = float(campo3)
 cantidad = importe = 0
 ```
4) finalmente, evaluamos por campos.
 ```py
 while cod_suc:
	cantidad += campo3
	importe += campo4
	campo1, campo2, campo3, campo4 = leer(ventas)
	campo3 = float(campo3)
 
 ```
5) (opcional) imprimir lo que nos quedó.`print(f'para el {campo1} la cantidad fue{cantidad} y el importe {importe}`
ej:  Mientras el archivo no termine, mientras el DNI no termine, mientras el DNI no termine y el DNI no cambie... Sumame toda la plata del dia

ejercicio; ![[Pasted image 20211116193906.png]]