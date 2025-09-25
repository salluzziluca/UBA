---
Dia: 2025-09-18
dg-publish: true
---
Una ip e s192.168.1.0
los primeros 3 numeros (192.168.1), son la red, el otro es el host. bajo una misma IP (un [[router]] de una cas apor ejemplo, cada computadora va dar un host)



hay 3 grupos de IP

Estos se identifican con mascaras que tienen 11111 en la parte de red y 00000 en la parte de host. Uno cuenta la cantidad de numeros y asi indica cual es largo en bytes de la red

| Red    | Host   | Identificacion (como empieza) | Clase | Mascara |
| ------ | ------ | ----------------------------- | ----- | ------- |
| 1 Byte | 3 Byte | 0                             | A     | /8      |
| 2 Byte | 2 byte | 10                            | B     | /16     |
| 3 Byte | 1 Byte | 110                           | C     | /24     |


>[!example] 157.92.0.0./16 es una IP tipo B que pertenece a la facultad de ingeneria. En este caso no se indica ningun host.




| Red             | Host               | Tipo                            |     |
| --------------- | ------------------ | ------------------------------- | --- |
| 111111....11111 | 000000....00000    | Todas las redes                 |     |
| 111111....11111 | 111111....11111    | Todas las redes todos los hosts |     |
| 00000....0000   | 111111....11111    | Todos los hosts de esta red     |     |
| 00000...000000  | 00000000....000000 | Este host en esta red           |     |
Direcciones reservadas

`127.0.0.1` localhost
10.0.0
faltan.....


En el caso de IPs muy parecidas en las tablas de routeo se las pasa a binario y se mira cual coincide mas 

192.168.1.0/24
192.168.0.0/24

paso a binario la oarte que me importa

192.168.000000001.00000000
192.168.0000000.0000000

>[!important] Si difieren en el ultimo bit, tienen la misma mascara Y SALEN POR LA MISMA INTERFAZ son contiguas
>