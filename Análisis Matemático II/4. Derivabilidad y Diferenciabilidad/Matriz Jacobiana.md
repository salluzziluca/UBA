---
dg-publish: true
---
# Matriz Jacobiana
Si la funcion es de [[3.1 Función#Funcion de campo vectorial|campo vectorial]], es decir, que su dominio tiene más de una variable, podemos tomar cada una de esas como un [[3.1 Función#Funcion de campo escalar|campo escalar]] y, haciendo el gradiente de c/u de ellas, armar una matriz jacobiana.
> Sea $f:D⊂R^n→R^m$, \vec f tiene m campos escalares, los cuales, a su vez, si están definidas admiten n derivadas parciales, entonces la matriz Jacobiana o matriz derivada será una matriz de m x n definida por:
> ![[Pasted image 20211010102935.png]]

### notas
- Cada fila es el gradiente de cada campo

- Cada columna es la derivada con respecto a cada variable

- Si esta matriz es continua, entonces decimos que $\vec f∈C^1$--> sus primeras derivadas parciales son continuas
- La continuidad se evalua antes de tomarla en un punto

ej: ![[Pasted image 20211010103429.png]]