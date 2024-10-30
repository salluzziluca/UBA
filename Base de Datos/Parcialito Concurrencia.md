---
Dia: 2024-10-28
aliases:
---

## 1
![[Pasted image 20241029102903.png]]
![[grafo precedencia 1.a]]
T1 lee A y luego T2 lo escribe RW
WR: T1 escribe en A y luego T2 lee
WW: T1 escribe en A y luego T2 vuelve a escribir 
RW: T3 lee B, luego T1 lo escribe 
WR: T3 escribe en B, luego T1 lee
WW: T3 escribe en B, luego T1 vuelve a escribir.
RW: T2 lee C, luego T3 lo escribe 
WR: T2 escribe en C, luego T3 lee
WW: T2 escribe en C, luego T3 vuelve a escribir.

Hay un ciclo por lo cual no es serializable. 
b.
![[Pasted image 20241029104808.png]]
![[grafo precedencias 1b]]

RW: T1 lee X, luego T2 escribe X
WR: T1 escribe X, luego T2 lee
WW: T1 escribe X, luego T2 lee X

WR: T4 escribe Z, T1 lee
WR: T4 escribe Z, T3 lee 
RW: T4 lee Z, luego T1 Escribe
RW: T4 lee, luego T3 escribe
WW: T4 escribe Z, luego T1 y T3 escriben 
RW: T1 lee Z, luego T3 escribe
RW: T3 lee z, luego T1 escribe 
WW T1 y T3 escriben Z
Hay ciclo por lo cual no es serializable

c.
![[Pasted image 20241029110756.png]]
![[grafo precedencias 1c]]
RT1(A), WT4(A)
RT1(A), WT2(A)
WT1(A), RT4(A) 
WT1(A), WT4(A) 
WT1(A), RT2(A) 
WT1(A), WT2(A) 
RT4(A), WT2(A) 
WT4(A), RT2(A) 
WT4(A), WT2(A) 
RT2(B), WT4(B)
WT2(B), RT4(B)
WT2(B), WT4(B) 
RT3(C), WT1(C) 
WT3(C), RT1(C) 
WT3(C), WT1(C)
Hay un ciclo por lo cual no es serializable

# 2
![[Pasted image 20241029112452.png]]

Aclaro que estoy usando 2PL basico
```java
bT1
bT2
LockT1(D)
RT1(D)
WT1(D)
LOCKT1(B)
// aca empieza la fase de unlock
UNLOCKT1(D)
RT1(B)
WT1(B)
UNLOCKT1(B)
LockT2(A)
RT2(A)
WT2(A)
UNLOCKT2(A)



LOCKT2(D)
RT2(D)
WT2(D)
UNLOCKT2(D)
CT1
CT2

bT3
LOCKT3(A)
RT3(A)
WT3(A)
LOCK3T(B)
//aca empieza la fase de unlock
UNLOCKT3(A)
RT3(B)
WRT(B)
UNLOCK3T(B)
cT3
```
Recuperabilidad: 
Definición: Un solapamiento es recuperable si y sólo si ninguna [[transacción]] T realiza el commit hasta tanto todas las [[Transacción|transacciones]] que escribieron datos antes de que T los leyera hayan commiteado.
Analizemos transaccion a transacción 
T1: lee D y B, esos datos no son modificados por nadie antes que T1 los lea asi que no hay problema alguno. 
T2: lee A y D. A no es modificado por nadie y D es modificado anteriormente por T1. Pero como el commit de T1 se da antes que el commit de T2 y "Un solapamiento es recuperable si y sólo si ninguna [[transacción]] T realiza el commit hasta tanto todas las [[Transacción|transacciones]] que escribieron datos antes de que T los leyera hayan commiteado.", es recuperable.
T3: finalmente, T3 commitea a lo ultimo, por lo que no realiza su commit antes de que todas las transacciones que escribieron datos antes de que T los leyera (t1 por B y t2 por A) hayan commiteado.
Este solapamiento es recupr
# 3

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

| Linea | A   | B   | C   | D   | E   | F   | G             |
| ----- | --- | --- | --- | --- | --- | --- | ------------- |
| 18    | 70  | 80  | 35  | 60  | 70  | 50  | valor inicial |
| 22    |     |     |     |     |     |     |               |


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

3c. Termina despues de la linea 22.  Es decir, esta es la ultima que se guarda en el log. En este caso sasbemos que t1 y t2 commitearon (porque su checkpoint terminó) y sabemos que T3 y T4 no llegaron a commitear. Por lo que hariamos UNDO de T3 y T4 y REDO de T1 y T2
El item A lo pongo en 50
El item B en 60
El item A en 70
el item C en 25
El item B en 80
El item D en 40
Al item C lo pongo en 35
Al item E lo pongo en 70
Al item D lo pongo en 60 
al item F lo pongo en 50
Al Item G lo pongo en 80
A E lo dejo en 70 
A G lo dejo en 80

| Linea | A   | B   | C   | D   | E   | F   | G   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| 18    | 70  | 80  | 35  | 60  | 70  | 50  | -   |
| 22    | 70  | 80  | 35  | 60  | 70  | 50  | 80  |
| 24    | 70  | 60  | 35  | 60  | 70  | 50  | 80  |
