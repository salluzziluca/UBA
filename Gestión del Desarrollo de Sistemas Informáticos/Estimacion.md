---
Dia: 2025-04-09
dg-publish: true
---
Estimar es dificil, no es algo que se hace una vez, ni es algo concreto ni exacto (es probabilistico). Se debe hacer a lo largo de todo el projecto. Siempre midiendo para obtener nueva informacion que me pueda ayudar a estimar mejor. Estimar mejor != que el costo sea menor

>[!quote] Estimates don’t need to be perfectly accurate as much as they need to be useful. When we have the combination of accurate estimates, good target setting, and good planning and control, we can end up with project results that are close to the “estimates.” (As you’ve guessed, the word “estimate” is in quotation marks because the project that was estimated is not the same project that was ultimately delivered.). These dynamics of changing project assumptions are a major reason that this book focuses more on the art of estimation than on the science. Accuracy of ±5% won’t do you much good if the project’s underlying assumptions change by 100%.
## Estimaciones

Estimar es el acto de anticipar cuánto va a llevar algo, generalmente en tiempo o esfuerzo. Una estimación **no es un compromiso**: es una suposición informada. 

> [!quote] Estimar es tratar de adivinar cuánto va a tomar algo sin saberlo con certeza.

Es fundamental aclarar **qué se está estimando** (¿una tarea? ¿un conjunto de tareas? ¿un producto entero?) y también en qué unidad: tiempo, esfuerzo relativo (como story points) o incluso costo monetario.
una estimacion consta de targets, commitments and control 

>[!quote] A good estimate is an estimate that provides a clear enough view of the project reality to allow the project leadership to make good decisions about how to control the project to hit its targets.
### Partes clave
#### Target
A target is a statement of a desirable business objective. Examples include the 
following:
- “We need to have Version 2.1 ready to demonstrate at a trade show in May.”
- “We need to have this release stabilized in time for the holiday sales cycle.”
- “These functions need to be completed by July 1 so that we’ll be in compliance with government regulations.”
- “We must limit the cost of the next release to $2 million, because that’s the maximum budget we have for that release.”
#### Commitment
While a target is a description of a desirable business objective, a commitment is a promise to deliver defined functionality at a specific level of quality by a certain date.
A commitment can be the same as the estimate, or it can be more aggressive or more conservative than the estimate. In other words, do not assume that the commitment has to be the same as the estimate; it doesn’t.

>[!tip] Distinguish between estimates, targets, and commitments.

### Estimación vs Planing
Estimation should be treated as an unbiased, analytical pro cess; planning should be treated as a biased, goal-seeking process.
Estimates form the foundation for the plans, but the plans don’t have to be the same as the estimates. If the estimates are dramatically different from the targets, the project plans will need to recognize that gap and account for a high level of risk. If the estimates are close to the targets, then the plans can assume less risk.

>[!tip] When you’re asked to provide an estimate, determine whether you’re supposed to be estimating or figuring out how to hit a target
### Algunas buenas prácticas:
- No comprometerse con estimaciones tempranas.
- Evitar dar estimaciones cuando el alcance no está claro.
- Ser explícito con los supuestos que se están haciendo.
- Creating a detailed schedule
- Identifying a project’s critical path
- Creating a complete work breakdown structure
- Prioritizing functionality for delivery 
- Breaking a project into iterations

> [!info] Una estimación es útil solo si es revisada y ajustada con el tiempo. Estimar una vez y no tocar más ese número es una receta para el desastre.

## Compromisos

Un compromiso sí es una promesa. Implica responsabilidad y suele tener consecuencias si no se cumple. Por eso, **un compromiso debe surgir cuando se entiende bien el trabajo** y se consideraron las dependencias, riesgos y posibles desvíos.

> [!tip] Nunca tomes una estimación como si fuera un compromiso sin revisar contexto, riesgos y supuestos.

Es válido y necesario diferenciar: _“Esto es una estimación preliminar”_ vs. _“Esto es un compromiso con fecha definida”_.

![[Conversacion]]

## Incertidumbre

La incertidumbre es inherente al desarrollo de software. Puede venir de múltiples fuentes: requisitos poco claros, dependencias externas, tecnología nueva o incluso por errores humanos.

> [!note] La incertidumbre no se elimina, se gestiona.

Mientras mas adentro estemos del proyecto, enos incertidumbre vamos a tener. Se habla de +35% al principio y entre 5 y 10 a medida que avanzamos. Depende del momento del proyecto y de la informacion disponible. 

neceistamos informacion + propuestas + costo

Algunas estrategias útiles:
- Dividir grandes problemas en partes más pequeñas.
- Planificar iterativamente y reevaluar estimaciones.
- Agregar buffers de tiempo para absorber imprevistos.
- Aceptar que no todo se puede saber de entrada.
### Probabilidad dentro de una estimacion 
No es tirar una moneda, no es que el proyecto sale o no sale. Hay chances y [[1.0 Probailididad|probabilidad]]. Se puede entender a la estimacion como una [[2.1 Definición de Variable Aleatoria|distribución]] probabilistica
![[Pasted image 20250416142712.png]]
![[Pasted image 20250416142735.png]]
![[Pasted image 20250416142754.png]]
>[!important] When you see a single-point estimate, that number’s probability is not 100%. Ask what the probability of that number is.
## Riesgos

Los riesgos son eventos que, si ocurren, afectan negativamente el proyecto. Algunos ejemplos comunes:

- Cambios de requerimientos a mitad del desarrollo.
- Fallos en servicios externos.
- Subestimación del esfuerzo necesario.
- Problemas con la disponibilidad del equipo.

> [!warning] Los riesgos no se ignoran: se documentan, se evalúan (probabilidad + impacto) y se preparan planes alternativos.

Vale la pena empezar cada proyecto haciendo una **lista de riesgos** y actualizándola a lo largo del tiempo. Esto permite reaccionar con rapidez y tomar decisiones más informadas.

## Comunicación

Una parte esencial del trabajo técnico es comunicar bien lo que se sabe y lo que no. No es un signo de debilidad decir “no lo sé todavía” o “necesito investigar más”.

> [!quote] La confianza no está en saber todo, sino en saber cuándo decir que no se sabe.

Frases útiles en este contexto:
- “Esto es una estimación, no un compromiso.”
- “Estoy suponiendo que tal cosa funciona como se espera.”
- “Si eso cambia, la estimación también cambia.”
- “Hay incertidumbre en esta parte del trabajo.”

El equipo y los stakeholders valoran más la honestidad temprana que las excusas tardías.


### Constante cambio 
![[Pasted image 20250416143214.png]]
El hecho de estimarlo yaa hace que el projecto cambie, tambine hay que tener en cuenta factores externos (se nos va a alguien, nos piden una demo antes, etc)

ver [[No Estimates]]

## Metodos y tecnicas de estimacion 
[[Wideband Delphi]]

- Juicio de expertos 
	Preguntar a los que saben, a alguien que ya haya hecho esto
- estimacion analoga 
	Busca proyectos similares en tamaño o en tiempo o cliente y encontrar una convergencia ahi de estimacion
- estimacion parametrica (estadistica)
	Vas haciendo cuentitas de una cosa a la vez.
- estimacion ascedente 
	De menos a mas.
- estimacion 3 puntos 
	$CosteEstimado= CostoOptimista +4CostoMedio + CostoPesimista)/6$

