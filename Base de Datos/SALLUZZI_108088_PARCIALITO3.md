![[Pasted image 20241003150217.png]]

# 1.
F={AD->G, B->H, BD->E, HG->D, CDE->A, GDE->C}
## Paso2: Atributos Independientes
En este caso, B es independiente porque no depende de ningun otro atributo. Solo se encuentra en el lado izquierdo. Para poder sacarlo de F, sabemos que B-> y que BD->E. Por lo que HD->E
F={AD->G, HD->E, HG->D, CDE->A, GDE->C}
## Paso3: Atributos equivalentes 
No hay atributos equivalentes 

## Paso4: Busco K
K = {H}. H no es clave porque con H puedo llegar solamente a H.
$H^+ ={H}$
## Paso5: 
{A, C, D, E, G}
Combino todos esos con H secuencialmente.
$(HA)^+=\{HA\}$
$(HC)^+=\{HC\}$
$(HD)^+=\{HD, E\}$
$(HG)^+=\{HG, D, E, C, A, G\}$
Con HG llego a D, luego con HD lleg o a E. Con GDE llego a C y con CDE llego a A. Finalmente, con AD tambien llego a G

#### Segundo ciclo, sin usar G: o sea, uso AC AD AE CD CE DE
$(HAC)^+=\{HAC\}$
$(HAD)^+=\{HAD, G, D, E, C, A\}$
$(HAE)^+=\{HAE\}$
$(HCD)^+=\{HCD, E, A, G\}$
$(HCE)^+=\{HCE\}$
$(HDE)^+=\{HDE\}$

#### Tercer ciclo, sin usar G: O sea uso ACD, ACE, DEA, DEC
$(HACD)^+=\{HACD\}$ Es redundante con HAD
$(HACE)^+=\{HACE\}$
$(HDEA)^+=\{HDEA\}$ es redundante con HAD
$(HDEC)^+=\{HDEC\}$ es redundante con HCD

## Paso 6:
Agrego la independencia
$$HGB, HADB, HCDB $$

==RTA: HGB, HADB, HCDB== 

# 2

{AG → B, D → H, EC → A, HE → D}
R1(E, C, A)
R2(B, C, D, E, G, H)
Obtener los conjuntos minimales F1 y F2 de dependencias funcionales y los conjuntos CC1 y CC2
### R1
El conjunto minimal $F{1min}$ es $F{1min}= \{EC\to A\}$
CC = EC
Forma normal de R1:
Es 2FN porque A es no primo y tiene dependencia funcional completa (solamente puedo llegar a A mediante AC)
Es 3FN porque no existen dependencias transitivas CK(clave candidata)->Y de atributos no primos. A es el unico atributo no primo y depende pura y exclusivamente de EC.
Es FNBC porque para toda dependencia funcional no trivial X->Y, x es superclave
### R2
R2(B, C, D, E, G, H)
F2: HE->D, D->H, ECG->B


No hay equivalentes
implicantes Ai: CEG
Pruebo todas las opciones 
CEGB no es clave
$CEGD^+=${B, D, H, C, E, G} es clave

$CEGH^+=${C, E , G, H, D, B} es clave

Me fijo si esta en 2FN. B no es primo y solo puedo llegar a el mediante ECG. 


# 3.
Precio, MaterialChasis->Version