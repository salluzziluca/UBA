Similar a [[Archivos]], la funcion para abrir archivos es
`fopen(archivo, modo)`
y para cerrarlos
`fclose(archivo)`
con 
`fgets(archivo, bytes, archivo)`
leemos lineas hasta que llega al limite de bytes o a un /n
![[Pasted image 20220322205146.png]]
En este caso el programa siempre que encuentre una linea va a leerla hasta un /n o a hasta 200 bytes y la va a imprimir por pantalla