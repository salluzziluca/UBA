---
Dia: 2025-07-09
dg-publish: true
---
## ✅ **Pasos para obtener estimadores por máxima verosimilitud (MLE)**

### **1. Definí la función de densidad o probabilidad**

Sea $fθ(x)f_\theta(x)fθ​(x)$ la densidad (para variables continuas) o función de probabilidad (para discretas), donde θ\thetaθ es el parámetro o conjunto de parámetros a estimar.

Ejemplo:

$$fα(x)=2xα2e−(x/α)2(Weibull con k=2)f_\alpha(x) = \frac{2x}{\alpha^2} e^{-(x/\alpha)^2} \quad \text{(Weibull \ con \( k = 2 \))}f\alpha(x)=\alpha22x​e−(x/α)2(Weibull con k=2)$$

---

### **2. Escribí la función de verosimilitud L(θ)L(\theta)L(θ)**

Para una muestra i.i.d. x1,x2,…,xnx_1, x_2, \ldots, x_nx1​,x2​,…,xn​, la verosimilitud es:

L(θ)=∏i=1nfθ(xi)L(\theta) = \prod_{i=1}^n f_\theta(x_i)L(θ)=i=1∏n​fθ​(xi​)

---

### **3. Calculá el logaritmo de la verosimilitud log⁡L(θ)\log L(\theta)logL(θ)**

Es más fácil trabajar con el logaritmo por simplificación de productos en sumas:

log⁡L(θ)=∑i=1nlog⁡fθ(xi)\log L(\theta) = \sum_{i=1}^n \log f_\theta(x_i)logL(θ)=i=1∑n​logfθ​(xi​)

---

### **4. Derivá respecto del parámetro θ\thetaθ**

ddθlog⁡L(θ)\frac{d}{d\theta} \log L(\theta)dθd​logL(θ)

Esto se llama **ecuación de verosimilitud**.

---

### **5. Igualá la derivada a cero y resolvé para θ\thetaθ**

ddθlog⁡L(θ)=0⇒θ^\frac{d}{d\theta} \log L(\theta) = 0 \Rightarrow \hat{\theta}dθd​logL(θ)=0⇒θ^

Esto te da el estimador máximo verosímil.

---

### **6. Verificá que es un máximo (opcional pero recomendable)**

Podés:

- Verificar que la segunda derivada es negativa (criterio de segunda derivada), o
    
- Ver que log⁡L(θ)\log L(\theta)logL(θ) tiene forma de máximo.
    

---

### ✳️ Ejemplo aplicado: Weibull(2, α\alphaα)

1. fα(x)=2xα2e−(x/α)2f_\alpha(x) = \frac{2x}{\alpha^2} e^{-(x/\alpha)^2}fα​(x)=α22x​e−(x/α)2
    
2. L(α)=∏i=1n2xiα2e−(xi/α)2L(\alpha) = \prod_{i=1}^n \frac{2x_i}{\alpha^2} e^{-(x_i/\alpha)^2}L(α)=∏i=1n​α22xi​​e−(xi​/α)2
    
3. log⁡L(α)=C−2nlog⁡α−∑i=1n(xi2α2)\log L(\alpha) = C - 2n \log \alpha - \sum_{i=1}^n \left(\frac{x_i^2}{\alpha^2} \right)logL(α)=C−2nlogα−∑i=1n​(α2xi2​​)
    
4. Derivá:
    
    ddαlog⁡L(α)=−2nα+2α3∑xi2\frac{d}{d\alpha} \log L(\alpha) = -\frac{2n}{\alpha} + \frac{2}{\alpha^3} \sum x_i^2dαd​logL(α)=−α2n​+α32​∑xi2​
5. Igualá a cero y despejá:
    
    α^=1n∑xi2\hat{\alpha} = \sqrt{\frac{1}{n} \sum x_i^2}α^=n1​∑xi2​​

---

### 🔁 Este proceso es general

Se puede aplicar a:

- Normal (μ\muμ, σ2\sigma^2σ2)
    
- Exponencial (λ\lambdaλ)
    
- Bernoulli (ppp)
    
- Binomial (ppp, con nnn conocido)
    
- Poisson (λ\lambdaλ)
    
- Uniforme
    
- Pareto, Gamma, etc.