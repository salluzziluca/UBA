Castear es convertir un tipo de dato en otro tipo de dato ej: char a int.
![[Pasted image 20220329191052.png]]
Tenemos dos tipos de casteo

## Casteo implicito 
> Dejamos que el compilador castee por su cuenta. Le hacemos que analice un tipo de dato como otro, se ve forzado a tomarlo asi. 

```c
int numero = 12345;
char caracter = numero;
short cortito = numero;
```

## Casteo explicito
>Convertimos un tipo de dato a otro manualmente, nos hacemos cargo.
```c
int numero = 12;
char nombre=(char)12345
long largooo = (long)nombre
```


![[Pasted image 20220329191833.png]]