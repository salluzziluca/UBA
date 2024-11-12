---
dg-publish: true
---
excec() invoca otro programa, sobreponiendo el espacio de memoria del proceso con el programa ejecutable

- obtiene el inodo del programa;
- verifica si el archivo es ejecutble y si el usuario iene los permisos para ejecutarlo
- lee el header del archivo;
- copia los parámetros del exec del viejo address space al system space;
- para (cada región asociada al proceso) las des-asocia
- para (cada región especificada en el módulo ejecutable) {
     alloca espacio para las nueva región; asocia (attach) la región; carga la región en la memoria;
    }
    
- copia los parámetros del exec en la nueva región o sección stack;
- hace cierta magia;
- inicializa a modo usuario
- libera el inodo;