---
Dia: 2025-03-15
dg-publish: true
aliases:
  - User Story Map
  - user story map
  - User story map
  - user story mapping
  - users story map
  - user stories map
  - user storie maps
---
## Flat User Story Backlog dont work
Se hace un gran laburo para entender lo que el cliente quiere. Al final todo eso que aprendemos queda tirado a la basura porque lo minimizamos para quedarnos solo con la punta del iceberg que son las user stories

>[!quote] “We spend lots of time working with our customers. We work hard to understand their goals, their users, and the major parts of the system we could build. Then we finally get down to the details – the pieces of functionality we’d like to build. In my head a see a tree where the trunk is built from the goals or desired benefits that drive the system; big branches are users; the small branches and twigs are the capabilities they need; then finally the leaves are the user stories small enough to place into development iterations.”

>[!danger] 
>That’s what a flat backlog is to me. A bag of context-free mulch.
I need that context in order for me to really tell a story about the system.

Es muy facil perderse y nunca lograr ver la big picture. 


## Story Map 
![[Pasted image 20250315185429.png]]
![[Pasted image 20250315194733.png]]
Arriba de todo estan las "big stories", llamadas actividades o [[Actiivity|activities]]. Una [[Actiivity|actividad]] es parte en diferentes stories. Si tengo por ejemplo la [[Actiivity|actividad]]: "managing email". Otras stories podrian ser: "send message", "read message", "delete message", "mark message as smap." Estas se denominan [[Task|tasks]].

>[!important] I simply arrange the small things under the big things in a bit of a grid form.
> when arranging stories in the map, if a person using the system typically does one thing after another, then I’ll put the early thing on the left, and the later thing on the right.


>[!info] When teaching this, people often tell me “the users can perform these in any order. What order should I put them in?” I’ll ask them to “explain to me what the system does at a high level – just tell me the [[Actiivity|activities]].” They then recite them to me. “That’s the order” I say. In fact, the order you’d explain the behavior of the system in is the correct order. We’re building a map that lets us tell a really big story about the system. Build the map in a way that helps you tell the story.


Jeff Patton recomienda dejar de usar al palabra Epics para las [[Actiivity|activities]] porque la gente tiene a descartar las epicas una vez que las diviide en user stories. Y en eso se pierde contexto. Buscamos lo contrario.

Ahora que lo tenemos armado es muy facil entender lo grande Y lo chico.

La fila de Actividades vendria a ser como la columna vertebral de nuestro software. No se prioriza eso (seria como priorizar hacer el motor, las ruedas o el chasis de un auto) se priorizan sus subtareas (quiero ruedas de caucho de 18 o 19 pulgadas?, quiero un chasis modular o fijo?). las [[Task|tasks]] nos permiten llegar al [[Minium Viable Product|MVP]], las [[Actiivity|activities]] SON el producto.

>[!note]  prioritize their characteristics that matters



lo unico malo es que se complica agregar [[Feature|features]]. Para esos casos se puede directamente armar un nuevo map chikito solo con esa [[feature]] y listo.