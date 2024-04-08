I Permiten la comunicación entre dos procesos diferentes I En la misma máquina I En dos máquinas diferentes I Se usan en aplicaciones que implementan el modelo cliente - servidor: I Cliente: es activo porque inicia la interacción con el servidor I Servidor: es pasivo porque espera recibir las peticiones de los clientes}



El software de red se plantea mediante el modelo por capas, siempre se comunican los diferentes programas pura y exclusivamente en la misma capa, nunca de la capa N a la capa N-1
![[Pasted image 20240408201700.png]]

## Tipos de comunicacion
Sin conexion

Sin Conexion ACK. Por cada dato recibido 

Con conexion. Tres fases: se establece al conexion, se intercambia y se cierra, hay control de flujo y de errores. Se puede verificar que lo que enviamos