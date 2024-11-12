---
dg-publish: true
---
# Teorema del Stokes
Sea $\Gamma$ una curva, S una superficie que tiene a $\Gamma$ como borde y $\vec f$ un campo vectorial, si:
1. $\Gamma = \delta S$, simple, cerrada, suave a trozos, se recorre en sentido positivo con respecto a la orientación de S.
2. S es una superficie suave a trozos, abierta, orientable y que tiene a $\Gamma$ como borde y en cada trozo admite una parametrizacion en $C^2$.
3. $\vec f \in C^1(\Gamma \cup S)$, o en un abierto que las incluya

### las mas importantes
- C es frontera de S
- C es orientable respecto a S
- C es curva cerrada
- S orientable 
- $\vec f \in C^1$
Entonces...
$$\LARGE \oint_{\Gamma^+} \vec f .d\vec s=\int \int_S rot(\vec f) .\hat n ds$$
La circulacion de $\vec f$ a lo largo de $\Gamma$ es igual al flujo del [[Rotor|rotor]] de $\vec f$ a través de S.
La direccion se puede obtener mediante la regla de la mano derecha. Si $\hat n$ es el pulgar, el sentido en el que gira la mano es el sentido de orientacion 

![[Pasted image 20220126125253.png]]

Ver [[Teorema de Stokes]]