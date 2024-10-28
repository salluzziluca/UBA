---
Dia: 2024-10-28
aliases:
---
![[Pasted image 20241028180149.png]]
3a. Termina justo antes de la 18. Subo de la 17 hasta la 1, me encuentro con el START T3 y el START CKPT (T1, T2) de la linea 7. Sus transacciones activas son T1 y T2. No encontré el checkpoint pero se que commitearon (linea 10 y 15. Como no encontre el commit de T3 (solo start y writes). Voy a tener que hacer UNDO y abort de T3 y REDO de T1 y T2.

El item A lo pongo en 50
El item B en 60
El item A en 70
el item C en 25
El item B en 80
El item D en 40
Al item C lo pongo en 35
Al item E lo pongo en 70 (undo)
Al item D lo pongo en 60 
al item F lo pongo en 50 (UNDO)

| Linea | A   | B   | C   | D   | E   | F   | G   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| 18    | 70  | 80  | 35  | 60  | 70  | 50  | -   |
| 22    |     |     |     |     |     |     |     |


3b Termina antes de la linea 22
Encuentro un END CKPT, subo hasta encontrar un START CKPT (linea 7). Se entonces que T1 y T2 terminaron (tengo que hacer REDO). Tambien se que T3 y T4 empezaron pero no commitearon, tengo que hacer UNDO y ABORT de ambas. 
El item A lo pongo en 50
El item B en 60
El item A en 70
el item C en 25
El item B en 80
El item D en 40
Al item C lo pongo en 35
Al item E lo pongo en 70 (undo)
Al item D lo pongo en 60 
al item F lo pongo en 50 (UNDO)
Al Item G lo pongo en 80 (UNDO)
La linea 20 no modifiica el valor de E porque estamos haciendo UNDO de T3 y T4

| Linea | A   | B   | C   | D   | E   | F   | G   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| 18    | 70  | 80  | 35  | 60  | 70  | 50  | -   |
| 22    | 70  | 80  | 35  | 60  | 70  | 50  | 80  |

3c termina desp