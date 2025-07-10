---
Dia: 2025-06-19
dg-publish: true
---
### nula
LA historica. la que si no cambia nada deberia ser esa. El status quo.


# 🧪 **Resumen de Tests de Hipótesis**

## ✅ **Pasos generales para cualquier test**

1. **Plantear las hipótesis**
    
    - $H_0$: lo que se quiere contrastar (estado “por defecto”)
        
    - $H_1$: lo que se quiere probar (alternativa)
        
2. **Definir la variable de decisión (estadístico de prueba)**
    
    - Depende de lo que estés testeando: media, proporción, varianza
        
3. **Establecer la regla de decisión**
    
    - Determinar la región de rechazo de $H_0$
        
    - Se usan cuantiles: $z_{\alpha}$, $t_{\alpha}$, $\chi^2_{\alpha}$, etc.
        
    - Puede ser unilateral (>) o (<), o bilateral ($\ne$)
        
4. **Calcular el estadístico con tus datos**
    
5. **Comparar y concluir**
    
    - Si el estadístico cae en la región de rechazo, **rechazás $H_0$**
        
    - Si no, **no hay evidencia suficiente para rechazarla**
        
6. (Opcional) **Calcular errores**
    
    - Error tipo I: rechazar $H_0$ cuando es cierta ($\alpha$)
        
    - Error tipo II: no rechazar $H_0$ cuando es falsa ($\beta$)
        

---

## 🎯 **Casos típicos por tipo de variable**

### 🔸 1. **Proporción (Bernoulli, Binomial)**

- Ejemplo: una moneda, una encuesta, una campaña de imagen
    
- Variable: $X \sim \text{Ber}(p)$ o $S_n \sim \text{Bin}(n, p)$
    

**Estadístico:**

$$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}$$​​

**Cuándo usar:**

- Cuando $n$ es grande (para usar normal)
    
- Si $n$ es chico, usás binomial exacta
    

---

### 🔸 2. **Media (normal con varianza conocida o desconocida)**

#### Caso A: $\sigma$ conocida ⇒ usar **Z**

$$Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$$​​

**Ejemplo:**

- Tiempo de producción: $X \sim N(\mu, \sigma^2)$
    
- Se quiere ver si el nuevo método reduce el tiempo medio de 100 segundos.
    

---

#### Caso B: $\sigma$ desconocida ⇒ usar **T**

$$T = \frac{\bar{X} - \mu_0}{S / \sqrt{n}} \sim t_{n-1}$$​

**Ejemplo:**

- Evaluar si una muestra de sueldos tiene media mayor que cierta cantidad, pero no conocés la varianza poblacional.
    

---

### 🔸 3. **Varianza o desvío estándar ⇒ usar Chi-cuadrado**

$$χ2=(n−1)s2σ02∼χn−12\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2} \sim \chi^2_{n - 1}χ2=σ02​(n−1)s2​∼χn−12$$​

**Ejemplo:**

- Calidad de mediciones (como el pH)
    
- Querés ver si la variabilidad es menor que cierto valor.
    

---

## 🧾 Ejemplos concretos (como los que mencionaste)

|Contexto|Tipo de variable|Estadístico|Distribución|Notas|
|---|---|---|---|---|
|Moneda (cara o seca)|Proporción|$Z$|Normal|$p = 0.5$, binomial si $n$ chico|
|Imagen de una empresa (encuesta)|Proporción|$Z$|Normal|$p = 0.35$, comparar si subió|
|Tiempo para una operación industrial|Media|$Z$ o $T$|Normal o Student|Según si $\sigma$ conocida|
|Calidad de medición (pH, precisión)|Varianza|$\chi^2$|Chi-cuadrado|Compara con $\sigma_0^2$|
|Diferencia de proporciones o medias|Proporción/media|$Z$ o $T$|Normal/T|Requiere muestras independientes|

---

## 🧠 Tips finales

- **¿$\sigma$ conocida?** ⇒ $Z$
    
- **¿$\sigma$ desconocida?** ⇒ $T$
    
- **¿Querés testear la varianza?** ⇒ $\chi^2$
    
- **¿Trabajás con proporciones?** ⇒ $Z$ (si $n$ grande)
    
- **¿Comparás dos grupos?** ⇒ test de diferencia (de medias o proporciones)