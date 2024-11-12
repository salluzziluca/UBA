---
dg-publish: true
---
I Permiten la comunicación entre dos procesos diferentes I En la misma máquina I En dos máquinas diferentes I Se usan en aplicaciones que implementan el modelo cliente - servidor: I Cliente: es activo porque inicia la interacción con el servidor I Servidor: es pasivo porque espera recibir las peticiones de los clientes}



El software de red se plantea mediante el modelo por capas, siempre se comunican los diferentes programas pura y exclusivamente en la misma capa, nunca de la capa N a la capa N-1
![[Pasted image 20240408201700.png]]

## Tipos de comunicacion
Sin conexion: Los datos se envían al receptor y no hay control de fujo ni de errores.
Sin Conexion ACK. Por cada dato recibido se envia un ACK, para que el emisor sepa que llego todo correctamente

Con conexion. Tres fases: se establece al conexion, se intercambia y se cierra, hay control de flujo y de errores. Se puede verificar que lo que enviamos. Junto con el ACK el receptor puede pedir que se envie algun dato faltante, llegado el caso



## Tipos de Socket
Stream Sockets: Usan el protocolo TPC: entreg garantrizada en flujo de bytes
Datagram Socket: Usan el UDP: Sin conexion 
Raw Socket: permiten a las apps enviar paquetes IP
Sequenced Packet Sockets: silimilares al stream, preservan los delimitariode de registro. Utulizan el protocolo SPP

```rust 
pub fn bind<A: ToSocketAddrs>(addr: A) -> Result<TcpListener>
let listener = TcpListener::bind("127.0.0.1:80")?;
```
El listener se va aquedar escuchando conexiones entrantes en esa direccion


## Servidor

Obtener conexiones: 
```rust 
pub fn incoming(&self) -> Incoming<'_> 
for stream in listener.incoming() { let stream = stream.unwrap(); 
println!("Conexion establecida!");
```
Cada stram representa una conexion abierta entre cliente y server. La iteracion es sobre "intentos de conexion" y puede devolver error


Forma 2: 
EL método accept obtiene una conexión establecida de un listener.
```rust 
pub fn accept(&self) -> Result<(TcpStream, SocketAddr)> //El hilo se bloquea hasta que haya una conexión establecida. 
match listener.accept() { 
Ok((_socket, addr)) => println!("nuevo cliente: {:?}", addr),
Err(e) => println!("error: {:?}", e), 
}
```

Leer datos del socket: `read`

```rust 
fn read(&muy self, buf: &mut [u8])-> Result<usize>
// por ej
let mut buffer = [0; 1024];
stream.red(&mut buffer).unwrap();
```


## Cliente
El cliente debe establecer conexion con el server 
```rust
// a traves de una IP
use std::net::{IpAddr, Ipv4Addr, SocketAddr}; 
let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080)

//a traves de un nombre
fn to_socket_addrs(&self) -> Result<Self::Iter>


let mut addrs_iter = "localhost:443".to_socket_addrs().unwrap(); //devuelve un iterador de direcciones
```



El cierre de la conexion TCP puede ser realizado de forma individual. La conexion establecida con Tcp 