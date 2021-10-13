# Diferenciabilidad
## Diferenciabilidad en funciones escalares
![[Pasted image 20211010222400.png]]

De ahi sacamos que la recta tangente es: $y = f(x_0)+f'(x_0)(x-x_0)$ (mirar [[Ecuacíon de la Recta Tangente]]) y que la funcion se puede expresar como $f(x)= f(x_0)+f'(x_0)(x-x_0)+E(h)$, por lo que $E(h)=f(x)-f(x_0 )-f'(x_0 )h$ y el error relativo $E(h)/h=e_r (h)=   \frac {(f(x_0+h)-f(x_0 ))}{h}-f'(x_0 )$
Y, por ultimo:
>   $\lim_{h\to 0} e_r (h)=\lim_{h\to 0} \frac {   f(x_0+h)-f(x_0 )}{h} - f'(x_0)=0$
Cuando h tiende a cero el error realtivo tambien tiende a cero, el error es infimo tomando el valor de la recta tangente cuanto estas cerca del punto. Si esto ocurre, si la recta tangente nos sirve para aproximarnos tan bien a el valor de la función original, decimos que la función es diferenciable. ==Una función escalar es diferenciable cuando la recta tangente es una muy buen aproximación de la funcion alrededor del punto donde la calculaste.==
Otra forma de verlo es: Si el límite de $x$tendiendo a $x_0$de la division de la funcion menos el valor de la recta tangente sobre lo que te alejaste de ese punto y te da cero, la función es diferenciable.
(recordando que $h = x-x_0$)
![[Pasted image 20211010224300.png]]

## Diferenciabilidad en campos escalares
Igual que en la función escalar, reemplazamos x por (x,y) o (x, y, z), segun corresponda, en vez de derivada tenemos gradiente y el divisor es la norma de un vector en lugar de un valor absoluto.
F es diferenciable en el entorno de $X_0$ si:
![[Pasted image 20211010224831.png]]
Ademas, va admitir un plano tangente en R3 o  R4

ej: 
![[Pasted image 20211010230712.png]]
![[Pasted image 20211010230721.png]]
![[Pasted image 20211010230732.png]]
![[Pasted image 20211010230745.png]]