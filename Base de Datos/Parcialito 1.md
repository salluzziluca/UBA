![[Pasted image 20240905161652.png]]


| Relación      | Clave Primaria | Claves Candidatas | Claves Foraneas |
| ------------- | -------------- | ----------------- | --------------- |
| H(H1, H2, F1) | {H1}           | {H1}              | {F1}            |
| F(F1, F2)     | {F1}           | {F1}              | -               |
| A(A1)         | {A1}           | {A1}              | -               |
| B(B1, A1)     | {B1, A1}       | {B1, A1}          | {A1}            |
| D(B1, H1)     |                |                   |                 |

