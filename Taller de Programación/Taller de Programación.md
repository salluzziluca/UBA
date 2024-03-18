# Ownership 
Cada valor en rust tiene una variable que es su dueña. Un dueño a la vez. Cuando la variable dueño sale de scope, se libera la memoria asignada al valor. El dueño determina el lifetime 