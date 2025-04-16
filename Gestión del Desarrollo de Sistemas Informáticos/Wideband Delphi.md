---
Dia: 2025-04-16
dg-publish: true
---
 El metodo Delphi esta pensando para armar estimaciones grupales, en conjunto. Evitando que un "crack" de la estimacion, piense todo.

1. The starting point for a Delphi session could be a specification of the problem being estimated or an initial high-level task list or project schedule. The outputs are a detailed project task list; a list of associated quality, process-related and overhead tasks; estimation assumptions; and a set of task and overall project estimates, one from each participant
![[Pasted image 20250416110814.png]]
## Planning 
Hay que empezar definiendo el problema y su scope. Vamos dividiendo los problemas mas grandes en "manageable portions" que se puedan estimar de forma mas accurately.  Se pueden incluso divir en equipos 
>The person who initiated the estimation activity assembles a problem specification that will give the participants enough information to produce credible, informed estimates

Se contara con un moderador, que coordinara la actividad, un PM y entre 2 y 4 estimadores. El moderador deberia saber del tema como para ser un estimator pero deberá ser imparcial, para ayudar a desempatar. 


## Kickoff
Se les explica bien a todos sobre el metodo Wideband Delphi y se les da a todos los estimadores informacion suficiente sobre el problema a atacar.

The team reviews the estimation objectives and discusses the problem and any estimation issues. The participants agree on the estimation units they will use, such as weeks, labor hours, dollars or lines of code. If the moderator concludes that all team members are sufficiently knowledgeable to contribute to the estimation activity, the group is ready to roll. Otherwise, the participants may need to be briefed more fully on the problem they’re estimating, or possibly replaced by others who can generate more accurate estimates

### Condiciones 
 • Appropriate team members have been selected.
 • The kickoff meeting has been held.
 • The participants have agreed on the estimation goal and units.
 • The project manager can participate in the session.
 • The estimators have the information they need to participate effectively

## Individual Preparation
cada uno realiza una estimacion individual, teniendo en cuenta solo lo que esa persona considera, no lo que el resto quiere escuchar. Esta estimacion no se hace sobre todo el proyecto, sino sobre las tareas necesarias para llegar a cierto milestone. 

>[!example] In addition to identifying the project tasks, separately record any tasks for related or supporting activities. In my first Wideband Delphi session, every participant forgot to list tasks dealing with quality control and assurance, configuration management and process-related activities on the first cycle. We caught this quickly and added them in for the next iteration. Be sure to include rework tasks following testing or inspection activities. Reworking to correct defects is a fact of life, so you should plan for it. If you’re estimating a schedule, also think of any overhead activities that aren’t specific to the project that you might have to build into your planning. These include meetings, vacation, training, other project assignments and myriad other things that suck time out of your day


![[Pasted image 20250416112511.png]]
• Assume one person (you) will perform all tasks.
 • Assume all tasks will be performed sequentially; don’t worry about sequencing and
 predecessor tasks at this time.
 • Assume that you can devote uninterrupted effort to each task (this may seem absurdly
 optimistic, but it simplifies the estimation process).
 • In units of calendar time, list any known waiting times you expect to encounter
 between tasks. This will help you translate effort estimates into schedule estimates
 later on.
## Estimation Meeting

El moderador junta las estimaciones individuales y las agrega al siguiente grafico
![[Pasted image 20250416112832.png]]
Cada uno de los involucrados puede ver en que parte del espectro cae su estimacion. **Es todo anonimo**.

El moderador leer su task list sin revelar cual fue su estimativo (de horas, en este caso). Se combina con el resto de subtasks de cada uno, verbalmente, para llegar a una lista mas completa que la que una sola persona podria hacer.

En este momento tambien se discute acerca de asumpciones  y preguntas.


After this initial discussion, all participants modify their estimates concurrently (and silently) in the meeting room. They might revise their task lists based on the information shared during the discussion, and they’ll adjust individual task estimates based on their new understanding of the task scope or changed assumptions.

Se vuelven a recolectar las asumpciones y se vuelven a plotear anonimamente en el chart. Esto se repite hasta que 

• you have completed four rounds;
 • the estimates have converged to an acceptably narrow range (defined in advance);
 • the allotted estimation meeting time (typically two hours) is over; or
 • all participants are unwilling to alter their latest estimates
Los tiempos deberan ser de 15/20 minutos nomas, para que no se complique el tema y se vuelva lento e insoportable.

## Assembling Tasks
>[!important] The merging process involves removing duplicate tasks and reaching some reasonable resolution of different estimates for individual tasks. “Reasonable” doesn’t mean replacing the team’s estimates with values the project manager prefers. Large estimate differences for apparently similar tasks might indicate that estimators interpreted that task in different ways. For example, two people might both have a task called “implement a class.” However, one estimator might have included unit testing and code review in the task, while the other meant just the coding effort. All estimators should define their tasks clearly to minimize confusion during this merging step. The merging step should retain the estimate range for each task, but if one estimator’s task estimate was wildly different from that of the other estimators, understand it and then perhaps discard or modify it.

## Review Results

The project manager provides the other estimators with the overall task list, individual estimates, cumulative estimates, assumption list, and any other information. Bring the team back together for a 30- to 60-minute review meeting to bring closure to the estimation activity. This meeting also provides an opportunity for the team to contemplate this execution of the Wideband Delphi process and suggest ways it can be improved for future applications.

The participants should make sure the final task list is as complete as possible. Se pueden agregar nuevas tareas si surgen.

## Completing the Estimation 
Se termina cuando: 
- The overall task list has been assembled
- You have a summarized list of estimating assumptions
- The estimators have reached consensus on how their individual estimates were synthesized into a single set with an acceptable range



Estimates are predictions of the future, and the range reflects the inherent uncertainty of gazing into the crystal ball. You might present three numbers: the average of the estimates as the planned case, the minimum value as the best case and the maximum as the worst case. Or you could present the average value as the nominal expected outcome, plus the maximum-minus-the-average value, and minus the average-minus-the-minimum value