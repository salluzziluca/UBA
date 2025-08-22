---
Dia: 2025-08-22
dg-publish: true
---
## Arquitecturas 

### Cliente Servidor 
Esto nos lleva a tener datacenteres enormes

### Peer to Peer (p2p)
Torrent

## Comunicación entre procesos
Cuando me quiero comunicar con alguien externamente, abro un socket. El socket nos conecta la aplicacion con [[Introduccion a la materia#Transporte !!|la capa de transporte]]. 
Esta capa nos da:
- Una transmition confiable.
- Sin duplicados, sin perdida, sin delay.
- Brinda un servicio de caudal, controlado a que velocida recibo las cosas.
- Sincronizacion (que en todos lados se vea lo mismo)
- Seguridad (privacidad, verificaicon de los extremos, integridad de los datos)