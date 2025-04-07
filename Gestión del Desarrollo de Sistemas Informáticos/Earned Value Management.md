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
 - Alcance: se recomienda descomponer el trabajo por realizar siguiendo lineamiento y practicas de 