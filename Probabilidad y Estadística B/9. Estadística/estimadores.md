# ✅ Pasos para obtener estimadores por máxima verosimilitud (MLE)

## 1. Definí la función de densidad o probabilidad

Sea $f_\theta(x)$ la densidad (para variables continuas) o función de probabilidad (para discretas), donde $\theta$ es el parámetro o conjunto de parámetros a estimar.

**Ejemplo (Weibull con $k = 2$):**

$$
f_\alpha(x) = \frac{2x}{\alpha^2} e^{-(x/\alpha)^2}
$$

---

## 2. Escribí la función de verosimilitud $L(\theta)$

Para una muestra i.i.d. $x_1, x_2, \ldots, x_n$, la verosimilitud es:

$$
L(\theta) = \prod_{i=1}^n f_\theta(x_i)
$$

---

## 3. Calculá el logaritmo de la verosimilitud $\log L(\theta)$

Transformamos la verosimilitud para facilitar el cálculo:

$$
\log L(\theta) = \sum_{i=1}^n \log f_\theta(x_i)
$$

---

## 4. Derivá respecto del parámetro $\theta$

Calculamos:

$$
\frac{d}{d\theta} \log L(\theta)
$$

Esto se llama **ecuación de verosimilitud**.

---

## 5. Igualá la derivada a cero y resolvé para $\theta$

$$
\frac{d}{d\theta} \log L(\theta) = 0 \quad \Rightarrow \quad \hat{\theta}
$$

Eso te da el **estimador máximo verosímil**.

---

## 6. Verificá que sea un máximo (opcional pero recomendable)

Podés:

- Verificar que la segunda derivada sea negativa:
  $$
  \frac{d^2}{d\theta^2} \log L(\theta) < 0
  $$

- Ver que $\log L(\theta)$ tenga forma de máximo (cóncava).

---

## ✳️ Ejemplo aplicado: Weibull(2, $\alpha$)

1. Densidad:
   $$
   f_\alpha(x) = \frac{2x}{\alpha^2} e^{-(x/\alpha)^2}
   $$

2. Verosimilitud:
   $$
   L(\alpha) = \prod_{i=1}^n \frac{2x_i}{\alpha^2} e^{-(x_i/\alpha)^2}
   $$

3. Log-verosimilitud:
   $$
   \log L(\alpha) = C - 2n \log \alpha - \sum_{i=1}^n \left(\frac{x_i^2}{\alpha^2} \right)
   $$

4. Derivada:
   $$
   \frac{d}{d\alpha} \log L(\alpha) = -\frac{2n}{\alpha} + \frac{2}{\alpha^3} \sum x_i^2
   $$

5. Igualamos a cero y despejamos:
   $$
   \hat{\alpha} = \sqrt{\frac{1}{n} \sum x_i^2}
   $$

---

## 🔁 Este procedimiento es general

Sirve también para:

- Normal ($\mu$, $\sigma^2$)
- Exponencial ($\lambda$)
- Bernoulli ($p$)
- Binomial ($p$, con $n$ conocido)
- Poisson ($\lambda$)
- Uniforme
- Pareto, Gamma, etc.
