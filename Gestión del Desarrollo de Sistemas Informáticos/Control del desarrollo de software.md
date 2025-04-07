---
Dia: 2025-04-07
dg-publish: true
---
Muchas veces los proyectos tienen desvios de costos, calendario o directamente no terminan. Una de las causas para esto es la falta de buenas **herramientas de control**. A pesar de tener buenas herramientas de **planificacion** (como [[Product Discovery]] o [[User Story Backlog as a Map|User Story Map]])


## Problemas clasicos 
### El síndrome del 90% 
![[Pasted image 20250407161549.png]]
el proyecto llega bien hasta el 90% y se estanca. 
Esto se da porque usamos informacion subjetiva para registrar avance. Cuando nos quermos fijar, en realidad el avance no es real. Por ahi cuando creiamos que estaba al 50%, ren realidad estaba al 20%

#### Solución
Lo primero es reunir evidencia fisica del avance, no confiar en que alguien nos dijo "avanzamos"


## Evidencias Físicas para el control de proyectos basado en control de calidad

El producto **desarrollado**... pero también **probado**... y **estabilizado** (sin defectos críticos).

Adicionalmente podremos medir no sólo la velocidad de construcción, sino también la velocidad de
corrección, obteniendo información sobre cuánto demorará la estabilización del producto.

### Grado de avancen

#### Errores comunes 
Muchas veces se mide el avance por calendario (si se dijo que tardabamos 20 dias, al dia 10 esta al 50% sin chequear)
O por codigo completo (sin chequear la estabilidad de este, puede estar "completo" pero tener muchos defectos)

#### Solución (Indicador de Funcionalidad Completa)
El indicador de Funcionalidad Completa mide avance cuando una funcionalidad está completa, pero...

*No hay avance si la funcionalidad no está completa*

*No está completa la funcionalidad si no está desarrollada, probada y estabilizada.*

1. Determinar las funcionalidades: 
	Para ello dividimos el producto a construir en partes. ¿Cuántas funcionalidades? Debemos buscar una cantidad óptima que balancee el detalle necesario para medir avance con la carga administrativa para mantener el indicador.
2. Asignar un Peso a cada funcionalidad: Story points, T-Shirt Size
3. Estimar la fecha en que la funcionalidad estará completa
4. A medida que avanza el proyecto registrar las fechas reales de funcionalidad completa
![[Pasted image 20250407162606.png]]
Tabla de datos para el indicador de funcionalidad completa

![[Pasted image 20250407162633.png]]
Indicador de funcionalidad completa

Obsérvese en el ejemplo que el eje vertical acumula los puntos de funcionalidad completa (PFC), sumando los
pesos en cada fecha. En este caso la convención es: una funcionalidad simple equivale a 1 PFC, una
funcionalidad media a 2 PFC y una funcionalidad compleja a 3 PFC.

#### Informacion adicional 
Información adicional
a) **Curva de código completo**: muestra cuándo el equipo de desarrollo entrega código nuevo al equipo de
control de calidad. Ese código aún no está probado ni estabilizado. Se debe tener especial cuidado con las
conclusiones que se obtengan con esta curva ya que no está basada en evidencia física validada y suele ocultar el
síndrome del 90%.
b) **Curva de funcionalidad aprobada por usuario**: marca la funcionalidad que además de estar completa ha
sido validada por el usuario final. Indica el avance más seguro ya que posee una aprobación de usuario. A
diferencia de la funcionalidad completa, es imposible lograr avance semanal con esta curva, pero debería
aumentar escalonadamente cada vez que el proyecto realice una entrega al usuario. Es muy útil graficarla,
especialmente si trabajamos con un esquema de entregas incrementales al usuario (Pussacq Laborde, 2003, p.
12).
c) Productividad: se obtiene dividiendo los PFC reales sobre la unidad de tiempo. En la figura anterior, la
productividad es 3 PFC x Sem (15 PFC reales / 5 semanas reales). Esto nos permitiría hacer la siguiente
extrapolación lineal: necesitaré 13,33 semanas para obtener los 40 PFC restantes (40/3). Puede servir para
predecir el futuro (figura 3).