>[!info] Es una técnica de diseño (matemática) que permite resolver problemas de optimización de un sistema de ecuaciones lineal en varias variables. 
Es decir: 
cte0 * x0 + … + cten xn  >= cte
Y luego maximizar/minimizar una fórmula en particular. 
EVITAR x0x1 <= 10
Se usa principalmente en investigación operativa para maximizar ganancias o minimizar costos (y determinar márgenes de mejora, etc..). 


## Componentes de programación lineal 

1. Variables (primero vemos continuas, pero pueden ser enteras)
2. Ecuaciones e inecuaciones lineales que definen restricciones sobre dichas variables: 
3. Buscamos maximizar o minimizar una función objetivo: 
4. Luego aplicamos un algoritmo que resuelva el modelo lineal (Simplex)


## Ej:1 
Tenemos una empresa TeoAlgoSoft que vende 2 comestibles por kilo: x e y. Por cuestiones normativas (Argentina, no lo entenderías) no podemos vender y en más kilos que el triple de x. Al mismo tiempo, la cantidad de x con el doble de y no puede exceder los 14 kgr. ¿Por qué? Vos seguime el ejemplo. Luego, la cantidad de kilos que exceda x a y no puede ser mayor a 2kgr. La ganancia del día puede verse por $5/kgr del producto x + $3/kgr del producto y.
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUck-wPwNYGCu3deIDT26Goo2lwRZFSJvZ6jc1P2gCSEjvAJrgmNzVAKshPv0wmxdtSZeoF5rl9lSuvvmTjyB7c8kBXnhADw2bHHRUxNMtseyInKmhNrXu9kYui7vVu0CajJaNDGwnDYs9HvgsGIWI7LOVt5QfmM=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUevlthWJNdg5IxMPUhr3qTQOlV3eoRoYMhpfZfUdNGRwh731JalF5OzI4t67pNri2Hdx5e1RLFRMNE-0jJmhpFGBTHj_5Q_mCDOqEEVzo-ul4Iu1iUV7CGVuUT1ZPFZtolyqsY89EUo0hoUjVSMZIHeqzY9qMvW=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeqomODPebTEOzjt1wXE545tvPjPi1vVTkfOHFCLoCA3txOKBtUxwXl2FD_tOq7PS-2nvg1sOwGetz_8GPNI6Plj23vPtS1a-BJU-JK5q82rQbVr4-Y80Z9JQ8nA7ELVjZjLe_swScVQCXn1R74QgCoobZZKvby=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdSf8CgUultrvezmfoZvFP6_fV1he7xyJSnCHKCVpzgdow1i1yPHm9ISHKpVMc3JWe_DHh57JF2WjHPFi1ASM-6np7rQVF5qeBQAhxmzeG8kLfcugpbaf16Ox1U1mLa1EqMH7Tyke9ghGaBvC8BIpdei0Rb2e8=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUd3ugMXFzlNrESSBxEIebcD2b_vBez8Tdt6yOcrH7hrHz1IjelawM-fyK9xNfMzKb1QQjXUtsSTi4RsA_q-vUBW_vC_Ol8PN7_L-MSn3CXhGcDqpfB5-1DDBIzMoB4QxN97MOhh6XaGimHNQ_W4IxL2s9cV2XQV=s2048?key=bB6JHxg9eZbeHq3LLKC6wA)**


## EJ2

Nuestra empresa cereales tiene que cumplir con un pedido de al menos 100 kgr del producto estrella de la empresa para el final de la semana, para ser vendido en diferentes supermercados. Para elaborar el producto necesita de amaranto y frutos secos (misma cantidad de cada uno). Para esto contamos con dos proveedores: 

- Valle Patagua: nos vende a $1 el kilo de amaranto (máximo 40kgr)
    
- Salud Sustentable: nos vende cajas de 2 kgr de amaranto y 5 kgr de frutos rojos por $6 (máximo 30 cajas
    

**