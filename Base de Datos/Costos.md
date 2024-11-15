---
Dia: 2024-11-12
dg-publish: true
---
Viva moreno carajo, hay que hacer costos 

![[Pasted image 20241115185216.png]]

1. Parser y Translator
	Rechazar consulta inválida
2. Optimizador
	Conversión a expresión de A.R.
	Expresión equivalente de A.R.
	Estrategia para cada operador
3. Evaluación del plan de ejecución
	Devolver el resultado en base a los datos


Mediante heurísticas la expresión se convierte en una expresión equivalente, obteniéndose un plan de consulta ● En base a datos sobre los datos de la base (metadatos) que se encuentran en el catálogo, se elige cómo resolver cada operador de álgebra relacional, obteniéndose el plan de ejecución


### Tipos de costos 

- Costo de acceso a disco (lectura o escritura)
- Costo de procesamiento 
- Costo de uso de memoria
- Costo de uso de redes
En este tipo de otpimizaciones ya no corren por parte del usuario. Sin internas de la bdd y es dificil tener ingerencia en ellos

## Reglas de equivalencia 

Buscamos consultas equivalentes y nos fijamos cual es mas optima 

![[Pasted image 20241115185750.png]]
![[Pasted image 20241115185836.png]]
Hacer una junta es equivalente a realizar el producto
cartesiano entre las tablas y luego revisar la condición de junta
con una selección
$σc( R X S ) = R ⨝c S$


Distribución de la selección en la junta $σc( R ∗ S ) = σcR( R ) ∗ σcS( S )$ ○ Si la condición c puede escribirse como cR∧cS donde cR y cS involucran atributos sólo de R y S respectivamente