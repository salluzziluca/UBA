---
Dia: 2025-10-14
dg-publish: true
---
## **Flashcards de: Resolución Recuperatorio Parcial 23-11-2023**

**Pregunta** ¿Cómo se interpreta un coeficiente de correlación de Pearson (r) y qué relación tiene con los gráficos de dispersión? ? **Respuesta** El coeficiente **r** mide la fuerza y la dirección de una relación lineal entre dos variables.

- **r cercano a 1** (ej: 0.80) indica una asociación lineal positiva fuerte (a medida que una variable aumenta, la otra también).
    
- **r cercano a -1** (ej: -0.86) indica una asociación lineal negativa fuerte (a medida que una variable aumenta, la otra disminuye).
    
- **r cercano a 0** (ej: 0.35) indica una asociación lineal débil o nula.
    

---

**Pregunta** ¿Qué es y para qué se utiliza el método _Early Stopping_ en Redes Neuronales? ? **Respuesta** Es una técnica de **regularización** que consiste en detener el entrenamiento de la red cuando el error sobre el conjunto de validación comienza a aumentar. Su objetivo principal es **evitar el overfitting** (sobreajuste) y mejorar la capacidad de generalización del modelo.

---

**Pregunta** ¿Qué es el Error de Sesgo (Bias) y cómo se relaciona con la complejidad de un modelo? ? **Respuesta** El **Bias (Sesgo)** se refiere a los errores que surgen de suposiciones incorrectas en el modelo de aprendizaje. Un **alto sesgo** puede hacer que el algoritmo no capture las relaciones relevantes entre las características y las salidas (underfitting). Generalmente, los modelos **menos complejos** tienen un mayor sesgo.

---

**Pregunta** ¿Qué es el _Overfitting_ (sobreajuste) y cómo se relaciona con la complejidad de un modelo? ? **Respuesta** El **Overfitting** ocurre cuando un modelo aprende el detalle y el ruido de los datos de entrenamiento a tal punto que impacta negativamente su rendimiento con datos nuevos. Está asociado a una **alta varianza**. Generalmente, los modelos **más complejos** son más propensos al overfitting.

---

**Pregunta** Dada una matriz de confusión, ¿cómo se calcula la métrica **Accuracy**? ? **Respuesta** El **Accuracy** (Exactitud) se calcula dividiendo la suma de las predicciones correctas (Verdaderos Positivos + Verdaderos Negativos) por el total de predicciones.

**Fórmula:** Accuracy = (TP+TN)/(TP+TN+FP+FN)

---

**Pregunta** Dada una matriz de confusión, ¿cómo se calculan las métricas **Precision** y **Recall** para la clase positiva (Clase 1)? ? **Respuesta**

- **Precision (Precisión):** Mide la proporción de identificaciones positivas que fueron realmente correctas.
    
    **Fórmula:** Precision=TP/(TP+FP)
    
- **Recall (Sensibilidad):** Mide la proporción de positivos reales que fueron identificados correctamente.
    
    **Fórmula:** Recall=TP/(TP+FN)
    

---

**Pregunta** ¿Cómo se calcula el **F1-Score**? ? **Respuesta** El **F1-Score** es la media armónica de Precision y Recall, proporcionando un balance entre ambas métricas.

**Fórmula:** F1Score=2∗(Precision∗Recall)/(Precision+Recall)

---

## **Flashcards de: Resolución Parcial 26-10-2023**

**Pregunta** ¿Qué es el _Underfitting_ y cómo se puede detectar y solucionar? ? **Respuesta** El **Underfitting** (subajuste) ocurre cuando un modelo es demasiado simple y no logra capturar la estructura subyacente de los datos. Se detecta cuando los errores de entrenamiento y validación son **altos y similares**. Se puede solucionar usando modelos más complejos, añadiendo más características o reduciendo la regularización.

---

**Pregunta** ¿Qué son los _outliers_ y cuál es la diferencia entre univariados y multivariados? ? **Respuesta** Los **outliers** son observaciones que se desvían significativamente del resto de los datos.

- **Univariados:** Son valores atípicos en una sola variable (ej: una persona de 45 años en un dataset de niños en edad escolar). Se detectan con métodos como IQR o Z-score.
    
- **Multivariados:** Son combinaciones atípicas de valores en un espacio n-dimensional (ej: una manzana de color naranja). Se detectan con algoritmos como Isolation Forest, LOF o Clustering.
    

---

**Pregunta** ¿Cuáles son las diferencias clave entre los métodos de ensamble _Bagging_ y _Boosting_? ? **Respuesta**

- **Bagging:** Entrena modelos **en paralelo** sobre diferentes muestras de datos (bootstrap). Su objetivo es **reducir la varianza**. Ejemplo: Random Forest.
    
- **Boosting:** Entrena modelos **secuencialmente**, donde cada nuevo modelo se enfoca en corregir los errores de los anteriores. Su objetivo es mejorar la precisión general.
    

---

**Pregunta** ¿Cuál es la diferencia entre los ensambles de tipo _Voting_ y _Stacking_? ? **Respuesta** Ambos combinan las predicciones de diferentes modelos.

- **Voting:** La predicción final se decide por votación (mayoritaria o ponderada) de los modelos base.
    
- **Stacking:** Utiliza un **"metamodelo"** que aprende a realizar la predicción final a partir de las predicciones de los modelos base.
    

---

**Pregunta** ¿Cuál es la diferencia entre Clasificación, Regresión y Agrupamiento (Clustering)? ? **Respuesta**

- **Clasificación (Supervisado):** Predice una etiqueta o **categoría discreta** de un conjunto conocido (ej: sano/enfermo).
    
- **Regresión (Supervisado):** Predice un **valor numérico continuo** (ej: precio de una propiedad).
    
- **Agrupamiento (No Supervisado):** Agrupa los datos en conjuntos distinguibles basándose en su similitud, sin conocer las etiquetas previamente (ej: segmentación de clientes).
    

---

**Pregunta** ¿Para qué se utiliza un gráfico _Scree Plot_ al aplicar PCA (Análisis de Componentes Principales)? ? **Respuesta** Se utiliza para **seleccionar el número óptimo de componentes principales**. Se busca un "codo" (elbow) en el gráfico, que representa el punto donde añadir más componentes ya no aporta una cantidad significativa de varianza explicada.

---

**Pregunta** ¿Qué técnica de reducción de dimensionalidad usarías si sospechas que los datos se distribuyen en una variedad (_manifold_) y quieres preservar la geometría intrínseca? ? **Respuesta** Usaría **ISOMAP**. Esta técnica se enfoca en preservar las distancias geodésicas (el camino más corto sobre la variedad) entre las observaciones.

---

**Pregunta** ¿Qué técnica de reducción de dimensionalidad es adecuada si el objetivo principal es conservar los clústeres existentes en los datos? ? **Respuesta**

**t-SNE** (t-distributed Stochastic Neighbor Embedding) es una excelente opción, ya que está diseñada para preservar las estructuras locales y los clústeres de los datos en una proyección de baja dimensión.

---

**Pregunta** ¿Para qué se utiliza la técnica de **poda** (_pruning_) en un árbol de decisión como C4.5? ? **Respuesta** Se utiliza **después del entrenamiento** para **controlar el overfitting**. Consiste en eliminar nodos o ramas del árbol para mejorar su capacidad de generalización.

---

**Pregunta** ¿Cómo maneja un árbol de decisión los atributos de entrada numéricos y continuos? ? **Respuesta** Sí puede manejarlos. Para un atributo numérico, el algoritmo busca el mejor **umbral (C)** que divida los datos en dos grupos (A<C y A≥C), de manera que se maximice la ganancia de información o se reduzca la impureza.

---

**Pregunta** ¿Para qué se usa la **impureza de Gini** y qué significa que un nodo sea "puro"? ? **Respuesta** La **impureza de Gini** es una métrica utilizada para decidir cuál es el mejor atributo para dividir un nodo en un árbol de decisión.

- Un **nodo puro** es aquel que contiene instancias de una sola clase (impureza = 0).
    
- Un **nodo impuro** contiene una mezcla de instancias de diferentes clases.
    

---

**Pregunta** ¿Cuál es la diferencia conceptual entre las métricas **Precision** y **Recall**? ? **Respuesta**

- **Precision:** De todo lo que el modelo predijo como positivo, ¿qué proporción era realmente positiva? Se enfoca en la calidad de las predicciones positivas.
    
- **Recall:** De todos los casos que eran realmente positivos, ¿qué proporción fue capaz de identificar el modelo? Se enfoca en la capacidad del modelo para encontrar todos los casos positivos.
    

---

**Pregunta** ¿Cuándo es conveniente maximizar **Precision** y cuándo **Recall**? Da un ejemplo. ? **Respuesta**

- **Maximizar Precision:** Cuando el costo de un **falso positivo** es alto. Ejemplo: En un clasificador de spam, es preferible que un email legítimo no sea marcado como spam.
    
- **Maximizar Recall:** Cuando el costo de un **falso negativo** es alto. Ejemplo: En la detección de enfermedades graves, es crucial no pasar por alto a un paciente enfermo.
    

---

**Pregunta** ¿Son Precision y Recall métricas adecuadas para un problema de **regresión**? ? **Respuesta** **No**. Estas son métricas de clasificación. Para problemas de regresión se utilizan métricas que miden el error de predicción, como **MAE** (Error Absoluto Medio), **MSE** (Error Cuadrático Medio) o **RMSE** (Raíz del Error Cuadrático Medio).

---

## **Flashcards de: Ejemplo de preguntas tipo parcial**

**Pregunta** ¿Para qué se utiliza el método _backpropagation_ en redes neuronales y qué recurso matemático emplea? ? **Respuesta** El _backpropagation_ (retropropagación) se utiliza para **entrenar la red neuronal**, ajustando los pesos de las conexiones para minimizar el error. Es un método que utiliza la **regla de la cadena** (un concepto del cálculo diferencial) para calcular el gradiente de la función de pérdida con respecto a cada peso de la red.

---

**Pregunta** En K-Fold Cross Validation (con k=5) sobre un conjunto de 240 registros de entrenamiento, ¿cuántas veces se entrena el modelo? ? **Respuesta** El modelo se entrenará **5 veces** (una vez por cada "fold" o pliegue).

---

**Pregunta** Verdadero o Falso: En K-Fold CV (k=5) con 240 registros, cada registro estará 4 veces en el conjunto de entrenamiento y 1 vez en el de validación. ? **Respuesta** **Verdadero**. El conjunto de datos se divide en 5 pliegues. En cada una de las 5 iteraciones, se utilizan 4 pliegues para entrenar y 1 pliegue para validar. Por lo tanto, cada registro forma parte del conjunto de validación una vez y del conjunto de entrenamiento cuatro veces.

---

**Pregunta** Verdadero o Falso: Un árbol ID3 usa la entropía, mientras que C4.5 usa la impureza de Gini. ? **Respuesta** **Falso**. Tanto ID3 como su sucesor C4.5 utilizan la **entropía** y la **ganancia de información** para construir el árbol. El algoritmo CART es el que utiliza la impureza de Gini.

---

**Pregunta** Verdadero o Falso: La técnica de poda se utiliza en los árboles C4.5 para evitar el _underfitting_. ? **Respuesta** **Falso**. La poda se utiliza para evitar el **overfitting**.

---

**Pregunta** Si el F1-Score en entrenamiento es 0.25 y en test es 0.4, ¿el modelo está sobreajustando? ? **Respuesta** **Falso**. Un F1-Score bajo tanto en entrenamiento como en test sugiere un problema de **underfitting** (subajuste). El modelo no está capturando bien los patrones de los datos.

---

**Pregunta** Verdadero o Falso: Una alta correlación entre dos variables implica causalidad. ? **Respuesta** **Falso**. Correlación no implica causalidad. Dos variables pueden estar altamente correlacionadas debido a una tercera variable oculta (variable de confusión) o por simple coincidencia.

---

**Pregunta** Verdadero o Falso: En un problema de regresión lineal se busca predecir un valor en un rango continuo. ? **Respuesta** **Verdadero**. El objetivo de la regresión es predecir una variable dependiente cuantitativa y continua.

Fuentes

![foto de perfil](https://lh3.googleusercontent.com/a/ACg8ocJWHTYYW3WvZ119xfT7x6hC6lzzAeRt03YRYZzUw61bTWjxbN8nSQ=s64-c)