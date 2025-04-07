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
a) **Curva de código completo**: muestra cuándo el equipo de desarrollo entrega código nuevo al equipo de control de calidad. Ese código aún no está probado ni estabilizado. Se debe tener especial cuidado con las conclusiones que se obtengan con esta curva ya que no está basada en evidencia física validada y suele ocultar el síndrome del 90%.
b) **Curva de funcionalidad aprobada por usuario**: marca la funcionalidad que además de estar completa ha sido validada por el usuario final. Indica el avance más seguro ya que posee una aprobación de usuario. A diferencia de la funcionalidad completa, es imposible lograr avance semanal con esta curva, pero debería aumentar escalonadamente cada vez que el proyecto realice una entrega al usuario. Es muy útil graficarla, especialmente si trabajamos con un esquema de entregas incrementales al usuario 
c) **Productividad**: se obtiene dividiendo los PFC reales sobre la unidad de tiempo. En la figura anterior, la productividad es 3 PFC x Sem (15 PFC reales / 5 semanas reales). Esto nos permitiría hacer la siguiente extrapolación lineal: necesitaré 13,33 semanas para obtener los 40 PFC restantes (40/3). Puede servir para predecir el futuro (figura 3).

### Consideraciones 
Consideraciones sobre este indicador
a) Validez: este indicador sólo es valido en etapa de construcción. No se utiliza en el período final de
estabilización ya que durante ese período la funcionalidad real es similar a la planificada.
b) Proceso: este indicador no generará avance si el equipo no se focaliza en cerrar temas. El indicador es binario, la funcionalidad está completa o no está.
c) Síndrome del 0%: si se considera completa a una funcionalidad cuándo no tiene ningún defecto, evitaremos el síndrome del 90%, pero caeremos en el síndrome del 0%, es decir, no registraremos avance porque siempre habrá algún defecto pendiente. Es por eso que una funcionalidad está completa cuando no posee defectos críticos, pero sí tiene defectos pendientes.

d) Funcionalidad = código: es su forma más pura, este indicador sólo considera funcionalidad al producto final para el usuario. Una especificación no es producto final. Sin embargo, en algunos proyectos en donde hay una marcada etapa de análisis al principio y un equipo de control de calidad que verifica el análisis, puede considerarse funcionalidad a la especificación para poder utilizar este indicador como una herramienta de control.


## Estados intermedios 
Como vimos hasta ahora, el indicador de funcionalidad completa divide al producto en dos estados:funcionalidad completa o no completa. Algunas veces necesitamos utilizar estados intermedios.
![[Pasted image 20250407163642.png]]
lit lo que yo hago en [[Kanban]]

Esto permite diferentes y nuevos analisis

## Medir defectos 
Midiendo la cantidad de defenctos que ocurren y cuantos se resuelven por dia tambien tenemos la velocidad de correccion y el tiempo estimado para estabilizar el producto 
![[Pasted image 20250407164305.png]]


### Consideraciones sobre este indicador
a) Validez: este indicador es válido durante todo el proyecto cuando hay prueba en paralelo al desarrollo. Si sólo
hay prueba al final, el indicador es muy útil durante la etapa de prueba final y estabilización.
b) Proceso: el indicador es muy útil para detectar el síndrome del 90 %, por ejemplo cuando avanza el código completo, pero la funcionalidad posee gran cantidad de defectos pendientes. Asimismo ayuda a detectar si se está aplicando en forma correcta el proceso de desarrollo y prueba en paralelo. En el ejemplo (figura 7) el proceso se está aplicando adecuadamente.


## Indicador de cobertura de prueba 
- Planificados: cantidad de casos a ejecutar 
- Disponibles: lo que realmente puedo ejecutar teniendo en cuenta lo que el equipo de desarrollo entregó al equipo de prueba.
- Ejecutados: lo que el equipo de prueba pudo ejecutar.
- Ejecutados OK: casos ejecutados sin errores. Es otra forma de ver avance del proyecto.
![[Pasted image 20250407164516.png]]

Este indicador puede ser utilizado para tener otra forma de validar avance del proyecto. El avance está dado por
los casos de prueba que han sido ejecutados sin problemas.

## Earned Value (cuanto costará)
![[Pasted image 20250407164601.png]]
### Consideraciones 
Consideraciones sobre este indicador
- Alcance: es necesario separar los costos que no están asociados directamente a la construcción de software. Por ejemplo, la adquisición de un equipo, la planificación inicial, el despliegue, etc. Otros costos, como la administración del proyecto, podrían distribuirse dentro de los PFC.
- Validez: al igual que el indicador de Funcionalidad Completa, sólo aplica a la construcción, no a la estabilización.
 - Margen de error: existe cierto margen de error aceptable con el objetivo de no aumentar la cargaadministrativa debido a:
 - Los pesos generan información inexacta
 - El Actual está insumido en funcionalidades que aún no están completas
- Los costos indirectos que se distribuyen en los PFC pueden generar margen de error.