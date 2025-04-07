---
Dia: 2025-04-06
dg-publish: true
aliases:
  - EVM,
  - Gestión del Valor Ganado
  - gestión del valor ganado
  - GVG
---
Para tomar decisiones correctas en el momento oportuno se necesita información clara, confiable y actualizada acerca del progreso del proyecto. Tambien se le debe proporcionar información concisa a los [[Stakeholder|stakeholders]]. La EVM proporcina un enfoque para medir el desempeño del proyecto a partir de compraraciones de su avance real frente al planeado, permitiendo evualuar tendencias y pronosticar

Para implementar EVM es necesario definir la Performance Measurement Baseline, PBM, que integra la descripción del trabajo a realizar (alcance), los plazos para su realización (cronograma) y el cálculo de sus costos y de los recursos requeridos para su ejecución (costo).
## 1. Introducción a la Gestión del Valor Ganado

- **Definición:**  
    La gestión del valor ganado integra alcance, tiempo y costo, proporcionando una visión consolidada del estado del proyecto mediante indicadores cuantitativos.
    
- **Objetivos:**
    
    - Medir el desempeño real frente al planificado.
        
    - Detectar desviaciones tempranas para la toma de decisiones correctivas.
        

> **Nota:**  
> La aplicación de EVM ayuda a prever problemas futuros y a gestionar de manera proactiva las desviaciones del plan.

---

## 2. Conceptos Clave y Métricas

- **Valor Planificado (PV):**  
    Representa el costo presupuestado del trabajo programado hasta la fecha.
    
- **Valor Ganado (EV):**  
    Corresponde al costo del trabajo efectivamente realizado, medido en función del presupuesto.
    
- **Costo Real (AC):**  
    Es el costo incurrido realmente en la ejecución del trabajo.
    
- **Budget at Completion (BAC) **:
	- El presupuesto total asignado
	    
- **Índices de Desempeño:**
    
    - **CPI (Cost Performance Index):** EV/AC Mide la eficiencia del costo.
        
    - **SPI (Schedule Performance Index):** EV/PV Evalúa el desempeño respecto al cronograma.
      
    - TCPI (To Complete Performance Index): (BAC-EV)/(BAC-AC)
        
- Schedule Variance (SV) EV-PV
- Cost Variance CV=EV-AC

![[Pasted image 20250406205427.png]]

## EAC  (Estimate at Completion)

El **EAC** es una proyección del costo total que se espera incurrir al finalizar el proyecto, basada en el desempeño acumulado hasta la fecha.

- **Definición:**  
  Es la estimación final del costo del proyecto, que combina el costo real incurrido (AC) con el costo futuro proyectado.

- **Fórmulas Comunes:**  
- **EAC = BAC – SV**  
  Se utiliza cuando se espera que los costos futuros difieran del presupuesto original (PMB) debido a variaciones atípicas.

- **EAC = BAC / CPI**  
  Ajusta los costos futuros de acuerdo al índice de eficiencia del rendimiento del costo (CPI) acumulado hasta la fecha.

- **EAC = BAC / (CPI * SPI)**  
  Considera tanto la eficiencia de costos (CPI) como la de cronograma (SPI) para calcular el costo final.

- **EAC = AC + Nuevo estimado para el trabajo remanente**  
  Suma el costo real incurrido (AC) y un nuevo pronóstico para completar el trabajo pendiente.


>[!important] **Dato Clave:**   La elección de la fórmula de EAC debe basarse en el contexto del proyecto y en las variaciones que se hayan observado en el desempeño.

- **Utilidad:**  
  Permite anticipar desviaciones presupuestarias y tomar decisiones correctivas para mantener el proyecto dentro del presupuesto estimado.

- **Aplicación Práctica:**  
  Una evaluación continua del EAC ayuda a los gestores de proyectos a identificar problemas de financiamiento a tiempo y a replanificar las actividades futuras para evitar sobrecostos.

---

Estimado hasta Concluir (ETC)
- **ETC = EAC – AC**  
  Representa el costo adicional que se estima se necesitará para completar el proyecto, una vez deducido el costo ya incurrido.

---

- Variación a la Conclusión (VAC)
Evalúa la diferencia entre el presupuesto inicial y el pronóstico final:
- **VAC = BAC – EAC**
- **VAC% = VAC / BAC**  
  Indica la desviación porcentual con respecto al presupuesto inicial.

---

- Índice de Rendimiento del Costo a la Conclusión (CPIAC)
- **CPIAC = BAC / EAC**  
  Este índice proyecta la eficiencia del costo al finalizar el proyecto.

---

## Enfoque Basado en Tiempo

Además del costo, se puede estimar la duración del proyecto:

### Estimado a la Conclusión Basado en Tiempo (EACt)
- **EACt** pronostica la duración final del proyecto.  
- Se recomienda obtenerlo a partir de un análisis detallado de la red del proyecto o, de manera aproximada, utilizando:
  - **EACt = Duración de la PMB / SPI**

### Variación a la Conclusión Basada en Tiempo (VACt)
- **VACt = Duración de la PMB – EACt**
- **VACt% = VACt / Duración de la PMB**

### Índice de Rendimiento del Cronograma a la Conclusión Basado en Tiempo (SPIACt)
- **SPIACt = Duración de la PMB / EACt**

> **Dato Clave:**  
> Estos indicadores basados en el tiempo permiten pronosticar la duración final del proyecto y evaluar el desempeño del cronograma, complementando el análisis financiero.



![[Pasted image 20250406210706.png]]


## Buena implementacion de EVm
 la buena implementación de la GVG supone la integración del alcance, el cronograma y el costo en la planificación del proyecto.
 - Alcance: se recomienda descomponer el trabajo por realizar siguiendo lineamiento y practicas de EDT (estructura de desglose de trabajo)
 - Cronograma:  Se puede aplicar el EVM usando la informacion estatica de un Diagrama de Gantt
 - Recursos y Costos : Para usar la GVG se requiere que cada tarea tenga asignados los recursos necesarios con sus correspondientes tarifas. Si por alguna razón no se requiere tener un control de los recursos, podrían manejarse sólo los estimados de costos de las tareas.

## Tecnicas de Medicion de Valor Ganado
### 1. Fórmula Fija
- **Descripción:**  
  Técnica simplificada que asigna porcentajes fijos al avance de una tarea.
- **Ejemplos Comunes:**  
  - **0/100:** Se acredita el 100% solo al finalizar.
  - **50/50:** Se acredita 50% al inicio y 50% al terminar.
- **Uso:**  
  Útil para evaluaciones simples y rápidas, adaptable a otras combinaciones (30/70, 25/75, etc.).

> **Nota:**  
> Ideal para tareas con entregables bien definidos donde el avance se puede calificar de forma binaria.

---

### 2. Hitos Ponderados
- **Descripción:**  
  Se asignan valores ponderados a hitos intermedios en tareas de larga duración.
- **Uso:**  
  Recomendada cuando es difícil medir el avance parcial de manera continua, pero se pueden definir resultados parciales.

> **Consejo:**  
> Permite evaluar el progreso en etapas, facilitando el seguimiento de tareas complejas.

---

### 3. Porcentaje Completado
- **Descripción:**  
  Mide el avance parcial en función de un porcentaje completado, adaptable a diferentes contextos.
- **Modalidades:**  
  - **% de Duración Completada:**  
    Calculado como la duración real hasta la fecha dividida entre la duración total.  
    *Recomendado para tareas con desempeño lineal.*
  - **% de Trabajo Completado:**  
    Basado en la proporción de horas reales trabajadas respecto al total estimado.
  - **% de Unidades Físicas Completadas:**  
    Calculado como las unidades entregadas a la fecha en relación con las unidades totales (por ejemplo, metros cúbicos o toneladas).
  - **% Físico Completado:**  
    Evaluación basada en el avance físico observado en la fecha de corte.

> **Dato Clave:**  
> Cada modalidad se elige según la naturaleza de la tarea y la forma en que se pueda medir el progreso.

---

## 4. Esfuerzo Proporcional
- **Descripción:**  
  Se utiliza cuando el avance de una tarea está relacionado directamente con otra que ya tiene su propia medición del valor ganado.
- **Uso:**  
  Permite vincular el rendimiento entre tareas interdependientes.

---

## 5. Nivel de Esfuerzo
- **Descripción:**  
  Técnica aplicada a tareas que no generan resultados tangibles o tienen múltiples resultados difíciles de cuantificar.
- **Ejemplo:**  
  Tareas de dirección de proyectos que involucran diversas actividades semanales.

> **Recomendación:**  
> Es ideal para actividades de soporte o administrativas donde la producción tangible no es el principal indicador.

---

## 6. Análisis de Rendimiento y Pronósticos con la GVG
- **Descripción:**  
  Involucra el análisis continuo del desempeño del proyecto para determinar cómo va y cómo terminará.
- **Uso:**  
  Se actualiza en cada fecha de estado, registrando el avance y el trabajo remanente para obtener datos confiables y actualizados.

> **Dato Clave:**  
> Este análisis es esencial para identificar desviaciones y aplicar medidas correctivas a tiempo.

---

## 7. GVG y Umbrales de Calidad
- **Descripción:**  
  Establece márgenes de tolerancia (umbrales) para determinar si el desempeño está dentro de límites aceptables.
- **Zonas de Control:**  
  - **Verde:** Dentro de límites.
  - **Amarillo:** Zona de alerta.
  - **Rojo:** Problemas identificados.
  - **Azul:** Rendimiento "demasiado" bueno, lo cual también puede indicar un problema.
- **Ejemplo Práctico:**  
  Uso de semáforos de control para monitorizar el progreso del proyecto.

> **Consejo:**  
> La administración por excepción se centra en las tareas que se salen de los umbrales definidos, optimizando la gestión del proyecto.
