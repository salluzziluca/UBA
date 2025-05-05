---
dg-publish: true
---
Utiliza sistemas de ecucaciones lineales.


Es una tecnica de diseño matematica qu epermite resolver problemas de optimizacion de un sistema deecuaciones LINEAL en varias variables 


Es decir: 
cte0 * x0 + … + cten xn  >= cte
Y luego maximizar/minimizar una fórmula en particular. 
EVITAR x0x1 <= 10 (no puedo multiplicar variables)
Se usa principalmente en investigación operativa para maximizar ganancias o minimizar costos (y determinar márgenes de mejora, etc..). 


## Componentes de programación lineal 

1. Variables (primero vemos continuas, pero pueden ser enteras y, en particular, binarias)
2. Ecuaciones e inecuaciones lineales que definen restricciones sobre dichas variables: **![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfVRS__5822L9TqT6_r_x9_EATTHs61sOaOVCFMx3x3RwFss9djARjnHKIb-AGjm3NCbrJ_SD5b03QaEqSv7o8RiEwvjE3Qk3CzwfRPSOqSkeKgpSlXymUnaQRjLnwGgF0CjePzjWcMvFsDo9W_uE90mg=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**
3. Buscamos maximizar o minimizar una función objetivo: **![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfxD_3vtrfudryca4U8JLfv68knivj0EDernhQoUfls1ATsxJJyT6fFAwoo42vKDvQPQ8O6dbxI9uX1PsJNETJVB2WbWoSg1sgn61de1pzVSqVLB3oYOEybJQGcymTJB1fgrphTSmdctqDxyixKOmqRWQ=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**
4. Luego aplicamos un algoritmo que resuelva el modelo lineal (Simplex)



Las restricciones van creado un dominio de soluciones válidas. Puede haber sistemas incompatibles (x>3 x<0)

## EJ:0
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdlLd43m-zAAf0VnKoYH2LK_OqHSu6h1Zrb8grztHa8N0SCQUjYJEP4SylDjWKjDZq690-Xalmt2XTolE9Aw91lER1aLoZYjgYL2S_BhJQF5RKPwD-vKb3aBcl3etEw_BGh1tcCxk9CCq3C7ic9EGsHbQ=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**

Buscamos maximizar x1+x2

Si graficamos nos queda el dominio
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdX42rdtvNNnEpJ5lTfVuhnfa4DqPuPYLBaN4Wz9JC_cQV2MI66gnoWJlm5SVHdSdtnzdRB_l63v0acas6ZyiXw6bsDWH61EkACJEG9LUq6CkP7PSpyvXwfhYBVd_zON6Q2_KR1J3zwhIUiX4ZTVplsLA=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**

Si buscamos maximizar vamos peinando y mirando como se acumulan los valores
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfqsLjdaoQ69k5HokB-rcYBG1FYfHp1Zbmbl7uDjycufpo_1XyMm5x8k1HI856i86y-1TWe8bi_H29BHtAAX7murVHD1hIPHeh3k9MxUBkLlXVxDeG5OaplwqJW3e29jN3RVjqJwTQJtuK8brnzbX63Rg=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**

**

En problemas lineales continuos la solución óptima siempre va a estar en algún vértice (puede estar en otro punto, pero en un vértice va a estar sí o sí)

**

## Ej:1 
Tenemos una empresa TeoAlgoSoft que vende 2 comestibles por kilo: x e y. Por cuestiones normativas (Argentina, no lo entenderías) no podemos vender y en más kilos que el triple de x. Al mismo tiempo, la cantidad de x con el doble de y no puede exceder los 14 kgr. ¿Por qué? Vos seguime el ejemplo. Luego, la cantidad de kilos que exceda x a y no puede ser mayor a 2kgr. La ganancia del día puede verse por $5/kgr del producto x + $3/kgr del producto y.
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUck-wPwNYGCu3deIDT26Goo2lwRZFSJvZ6jc1P2gCSEjvAJrgmNzVAKshPv0wmxdtSZeoF5rl9lSuvvmTjyB7c8kBXnhADw2bHHRUxNMtseyInKmhNrXu9kYui7vVu0CajJaNDGwnDYs9HvgsGIWI7LOVt5QfmM=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUevlthWJNdg5IxMPUhr3qTQOlV3eoRoYMhpfZfUdNGRwh731JalF5OzI4t67pNri2Hdx5e1RLFRMNE-0jJmhpFGBTHj_5Q_mCDOqEEVzo-ul4Iu1iUV7CGVuUT1ZPFZtolyqsY89EUo0hoUjVSMZIHeqzY9qMvW=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeqomODPebTEOzjt1wXE545tvPjPi1vVTkfOHFCLoCA3txOKBtUxwXl2FD_tOq7PS-2nvg1sOwGetz_8GPNI6Plj23vPtS1a-BJU-JK5q82rQbVr4-Y80Z9JQ8nA7ELVjZjLe_swScVQCXn1R74QgCoobZZKvby=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdSf8CgUultrvezmfoZvFP6_fV1he7xyJSnCHKCVpzgdow1i1yPHm9ISHKpVMc3JWe_DHh57JF2WjHPFi1ASM-6np7rQVF5qeBQAhxmzeG8kLfcugpbaf16Ox1U1mLa1EqMH7Tyke9ghGaBvC8BIpdei0Rb2e8=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUd3ugMXFzlNrESSBxEIebcD2b_vBez8Tdt6yOcrH7hrHz1IjelawM-fyK9xNfMzKb1QQjXUtsSTi4RsA_q-vUBW_vC_Ol8PN7_L-MSn3CXhGcDqpfB5-1DDBIzMoB4QxN97MOhh6XaGimHNQ_W4IxL2s9cV2XQV=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**


## EJ2

Nuestra empresa cereales tiene que cumplir con un pedido de al menos 100 kgr del producto estrella de la empresa para el final de la semana, para ser vendido en diferentes supermercados. Para elaborar el producto necesita de amaranto y frutos secos (misma cantidad de cada uno). Para esto contamos con dos proveedores: 

- Valle Patagua: nos vende a $1 el kilo de amaranto (máximo 40kgr)
- Salud Sustentable: nos vende cajas de 2 kgr de amaranto y 5 kgr de frutos rojos por $6 (máximo 30 cajas

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfShqF2P_Jx-dp1f3j763GUsGIxG4-KXLBt1L1S9tdX_m2tYbo8ktZr21mm7ExSL1UD9bCdrVrLjp0ZeeLW1DmrVHl2LL4yWO7OCtddGNsZqnb0xXsUMIyLgLXWTcs61dqZWVTaH8rGR03B9bQY7LMzCfdj3Bcy=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcTkUf5PJcG92Skd5PRXXJbLgN9SukR5ZhaXq_X5kV4f161oOCYT6zFwbLd-Lowrcgqi5vDTsKvo9cFvkDyzf0bg2iDbzoTm4Iynqu3Xwga19bUKG1RYDENe1gLen75z56QAfn9b2UK7JjMiEB2IGUaMJi-qWg=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfLSK5bVpvEOMXeWlRsVDngUrPtrtf-oPGz2t0G7YW_BgV6nIfgjy-FlRCs-WKGpqtD36BwXOmVYNAa0scMjWFyft-8JKESguPIvx24lduhpF_MTLJ7xy0NOKAt-ku0reZ9n0FNCLSWI22ZDQq2VcWUGpGgd_js=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcusDC6jZcSeG16uq4VQ8BxT-lD1LnvHthxeESMCy7EXQMKLWFMgs336qIVshWeBSTpTeq6EaDk0DrOwGD8ilUeU_O4YeSaRGZofqO3CU3Vhf5hU2OxuoMV_L-5A4ecbxPAZa-IDTsZrOZyZZzPqPakBmE280k=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdD6wreJBHorq_Wr7lbj79kD-f_HrDd1WdmlFnEU30er6F-jHsQQ6tXYPtGwLySmjBJZcpIkJLLIGmWpg8EwEkC2RuLElZe4tzAQA221JGmKoqq70BVyzXVBk11bV5NuMS9Qat_ICjptUmfVbdclfqqVOxlh2DJ=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)

```python 
def ejemplo():
    problem = pulp.LpProblem("products", pulp.LpMinimize)
    vp = pulp.LpVariable("vp")
    ss = pulp.LpVariable("ss")
    problem += vp <= 40
    problem += ss <= 30
    problem += 5 * ss >= 50  # mostrar cambiando a 51
    problem += vp + 2 * ss >= 50  # mostrar cambiando a 51
    problem += 1 * vp + 6 * ss
    problem.solve()
    return pulp.value(vp), pulp.value(ss)
```


## Binarios (booleanos)
$y_{x}$ es si lanzo el producto X. 

Si se lanza el 5 0 6, lanzo el 1. 

$$\LARGE y_{1} \geq y_{5}$$
$$\LARGE y_{1} \geq y_{6}$$
Si y5 i y6 son 1(se lanzan) entonces y1 se va a tener que lanzar para cumplir ka condicion![[Pasted image 20250505195449.png]]

### And y Or
![[Pasted image 20250505195523.png]]


## Problema del cambio 

valores de entrada: 
v_i = valor de moneda de denominacion i (constante)
c: cambio al que queremos lelgar (constante)

M_i= cantidad de monedads de denominacion i que usamos para el cambio 
![[Pasted image 20241017102456.png]]

## Problema del viajante por PLE 
Agregamos virtualmente las aritas faltantes con pedo F= "infinito" (sumatoria de todas las artistas existentes +1)
Construimos nuestras variables $Y_{i,j}= 1$ si usamos la arista i->j (0 sino)
$\sum_{j} Y_{i,j}=1$ de todos salgo una sola vez $\sum_{i} Y_{i,j} = 1$ a todos entro una sola vez. De todos entro y salgo una sola vez, genera un ciclo 
![[Pasted image 20241017103218.png]]
el tema es que puede generar subciclos cuando necesito uno solo
agrego una restriccion de secuencia. p_i = numero de secuencia en la cual visito a la ciudad i 
$p_i-p_j + nY_{i,j} \leq n-1$



## Simplex 
AL ser un problema lineal, los optimos van a estar si o si en vertices 
Es greedy, busca optimos locales esperando que sean optiomos generales tmb 
Complejidad = O(cant_vertices) <= O(2^n)
caso lineal continuo: se demostro que es O(n^9)

![[Pasted image 20241017145218.png]]
de esa forma nos aseguramos de que x1 y x2 pueden valer 0 


otro caso![[Pasted image 20241017145620.png]]


![[Pasted image 20241017145654.png]]
siendo C la zmax

![[Pasted image 20241017145806.png]]
![[Pasted image 20241017145959.png]]![[Pasted image 20241017150336.png]]![[Pasted image 20241017150350.png]]


## Branch and Bounds 
Es como [[Backtracking]], aplicando branching para ver diferentes alternativas, con bounds (restricciones) como podas

1. Buscamos solución relajada (no consideramos variables enteras)
2. Sobre la solución relajada, para variables enteras, vemos una variable y volvemos a resolver agregando una restricción: X <= [a] , y otra vez con X >= [a] + 1, y además vemos que valga eso. Ramificamos y resolvemos.
3. Seguir aplicando 2 hasta que todas las variables que deban ser enteras, sean enteras. Vamos quedándonos con la mejor solución cada vez que volvemos. 


![[Pasted image 20241017151109.png]]![[Pasted image 20241017151115.png]]