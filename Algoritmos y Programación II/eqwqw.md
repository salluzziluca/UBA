El metodo de ordenamiento heapsort crea un heap (un tipo de arbol binario) a partir del conjunto de datos otorgado para 
despues vaciarlo, obteniendo asi un vector con los elementos ordenados. 
En el heap siempre se inserta desde el ultimo lugar (siendo este la ultima posicion de la ultima fila, yendo de izquierda 
a derecha) y se quita desde la raiz. 
Utilizando un heap maximal (ya que lo que queremos es un vector ordenado de mayor a menor) tenemos:

1) inserto el 9 en la ultima posicion, como no hay mas elementos, queda la raiz
            9           
            
            
2) inserto el 8 en la ultima posicion

            9
        8
        
    comparo el 8 con el 9, como el 9 es mayor, este debe ir mas arriba, no se modifica ninguna posición
    
    
3) inserto el 7 en la ultima posicion
            9
        8       7
    comparo el 7 con el 9, como el 9 es mayor, este debe ir mas arriba, no se modifica ninguna posición

4) Inserto el 6 en la ultima posición

            9
        8       7
    6

    comparo el 6 con el 8, como el 8 es mayor, este debe ir mas arriba, no se modifica ninguna posición

5) inserto el 5 en la ultima posicion

                9
        8               7
    6       5
    
    comparo el 5 con el 8, como el 8 es mayor, este debe ir mas arriba, no se modifica ninguna posición.

    Una vez hecho esto, no queda mas que quitar uno a uno los elementos desde la raiz e ir
    agregandolos ordenadamente a un vector

6) quito el 9 y reemplazo con el ultimo elemento del heap

            5
        8       7       vector = [9]
    6
    
    Hago sift down para que los elementos "mas pesados" salgan a flote y asi quede ubicado como nueva raiz el elemento
    mas grande del heap actual


        8
    5       7
6

        8
    6       7
5

7) repito paso 6 pero con el 8 como raiz

        5
    6       7           vector = [9, 8]
    
    sift down del 5
    
        7
    6       5
    
8) repito paso 6 pero con el 7 como raiz

        5
    6                   vector = [9, 8, 7]
    
    sift down del 5
    
        6
    5
    
9) repito paso 6 con 6 como raiz

        5               vector = [9, 8, 7, 6]
        
10) repito paso 6 con el 5 como raiz

    vector = [9, 8, 7, 6, 5]- 
    
    Se finalizó el heap sort, el vector se encuentra comprobablemente ordenado. 
    
