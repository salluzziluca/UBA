![[Pasted image 20241003150217.png]]

# 1.
F={AD->G, B->H, BD->E, HG->D, CDE->A, GDE->C}
## Paso2: Atributos Independientes
En este caso, no hay atributos independientes
## Paso3: Atributos equivalentes 
No hay atributos equivalentes 

## Paso4: Busco K
K = {B}. B no es clave porque con B puedo llegar solamente a H y a B.
$B^+ ={B}$
## Paso5: 
{A, C, D, E, G, H}
Combino todos esos con B secuencialmente.
$(BA)^+=\{BA, H\}$
$(BC)^+=\{BC, H\}$
$(BE)^+=\{BE, H\}$
$(BD)^+=\{BD, H, E\}$
$(BG)^+=\{BG, H, D, E, C,A\}$
Con HG llego a D, con BD llego a E, con GDE llego a C, con CDE llego a A.
#### Segundo ciclo, sin usar G: o sea, uso AC AD AE AH CD CE CH DE DH EH

$(BAC)^+=\{BAC, H\}$
$(BAD)^+=\{BAD,H, G, D, E, C, A\}$
$(BAE)^+=\{BAE\}$
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
Es FNBC porque para toda dependencia funcional no [[Dependencia Funcional Trivial|trivial]] X->Y, x es superclave
### R2
R2(B, C, D, E, G, H)
F2: HE->D, D->H, ECG->B


No hay equivalentes
implicantes Ai: CEG
Pruebo todas las opciones 
CEGB no es clave
$CEGD^+=${B, D, H, C, E, G} es clave

$CEGH^+=${C, E , G, H, D, B} es clave

Me fijo si no está en 2FN. B no es primo y puedo llegar tanto mediante CEGD como mediante CEGH. Depende parcialmente de ambas claves

Por ende, R2 esta solamente en 1FN


# 3.
Version-> Precio, MaterialChasis
N°Serie->Ejemplar
Ejemplar->alias, autonomia, puedeResolver, Version
fecha, DNI, N°Serie-> Venta
DNI-> Nombre

Se sabe que cada ejemplar del modelo JuanciTron2C24 se identifica con su n´umero de serie (¡un entero!), y tiene un alias, una autonom´ıa para su bater´ıa(medida en horas) y un indicador para saber si puede resolver los parcialitos de Base de Datos (no est´a a la venta para alumnos). Se registra par