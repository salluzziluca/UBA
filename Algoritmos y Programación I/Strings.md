---
dg-publish: true
---
# Strings
Inmutables, una vez creados cagaste bro no los podes cambiar

```py
palabra = 'Mascarpone'
palabra[0] = 'M'
palabra[-1] = 'e'
palabra[0:4]='Masc'
palabra[:4] = 'Masc'
palabra[-4:-1] = 'pon'
palabra[2:8:2]= 'sap'
palabra.upper() = 'MASCARPONE'
palabra.count('a')= 2 #La cantidad de veces que aparece a
palabra.index('c') = 3 #donde aparece 'c' por primera vez
palabra.find('carp')= 3 #donde empieza el sub-string carp
palabra.isalpha() = True #devuelve true si la cadena esta formada solo por letras
palabra.isdigit() = False #devuelve true si la cadena esta formada solo por numeros
palabra.isalnum() = False #devuelve true si la cadena esta formada solo por numeros y letras
caracter.isupper() 
```