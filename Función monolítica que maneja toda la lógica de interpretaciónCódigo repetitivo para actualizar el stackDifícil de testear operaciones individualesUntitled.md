---
Dia: 2025-06-23
dg-publish: true
---
- Función monolítica que maneja toda la lógica de interpretación
- Código repetitivo para actualizar el stack
- Difícil de testear operaciones individuales
# Revisión de Código - Análisis de Buenas Prácticas Clojure

## Resumen
Este análisis identifica oportunidades de mejora en el código para seguir mejor las convenciones idiomáticas de Clojure, enfocándose en legibilidad, mantenibilidad y simplicidad.






La funcion interpreter en turtle.clj es demasiado larga.
- Función monolítica que maneja toda la lógica de interpretación
- Código repetitivo para actualizar el stack
- Difícil de testear operaciones individuales
vean de separar en helpers
```clojure
(defn update-turtle-in-stack [state update-fn]
  ;; Helper para actualizar tortuga en el stack
  )

(defn execute-command [state command angle]
  ;; Delegar a funciones específicas por comando
  )
```

## 🔧 Áreas de Mejora Principales

### 1. Función `interpretar` demasiado extensa
**Ubicación:** ```38:113:src/tp2/turtle.clj```


La función `interpretar` tiene más de 75 líneas y maneja múltiples responsabilidades. Esto viola el principio de responsabilidad única y hace el código difícil de mantener y testear.

**Problema:**
- Función monolítica que maneja toda la lógica de interpretación
- Código repetitivo para actualizar el stack
- Difícil de testear operaciones individuales

**Sugerencia:** Extraer cada operación a funciones separadas:
```clojure
(defn update-turtle-in-stack [state update-fn]
  ;; Helper para actualizar tortuga en el stack
  )

(defn execute-command [state command angle]
  ;; Delegar a funciones específicas por comando
  )
```

### 2. Uso de Math/PI en lugar de funciones estándar
**Ubicación:** ```3:4:src/tp2/turtle.clj```

```clojure
(defn grados->radianes [grados]
  (* grados (/ Math/PI 180)))
```

**Problema:** Reimplementación manual de conversión de grados a radianes.

**Sugerencia:** Usar la biblioteca estándar:
```clojure
(:require [clojure.math :refer [to-radians]])
```

### 3. Complejidad innecesaria en el modelo de datos
**Ubicación:** ```35:39:src/tp2/turtle.clj```

La estructura del estado inicial es muy anidada y compleja:
```clojure
{:stack  [{:posicion    [0.0 0.0]
           :orientacion -90.0
           :pluma       {:abajo? true
                         :color  "black"
                         :ancho  1.0}}]
 :lineas []}
```

**Sugerencia:** Simplificar la estructura para mejorar legibilidad y mantenibilidad.

### 4. Recursión manual poco idiomática
**Ubicación:** ```9:15:src/tp2/lsystem.clj```

```clojure
(defn expandir [sistema iteraciones]
  (let [reglas (:reglas sistema)]
    (if (zero? iteraciones)
      (:axioma sistema)
      (aplicar-reglas
        (expandir sistema (dec iteraciones))
        reglas))))
```

**Problema:** Recursión manual cuando Clojure ofrece abstracciones más expresivas.

**Sugerencia:** Usar composición de funciones para mayor claridad:
```clojure
(defn apply-n-times [n f]
  (apply comp (repeat n f)))
```

### 5. Código repetitivo en operaciones de stack
**Ubicación:** ```48:87:src/tp2/turtle.clj```

Múltiples bloques similares para actualizar el stack:
```clojure
(let [tortuga-nueva (girar-derecha tortuga-activa angulo)
      nuevo-stack (assoc stack idx-activo tortuga-nueva)]
  (assoc estado :stack nuevo-stack))
```

**Sugerencia:** Extraer a función helper para eliminar duplicación:
```clojure
(defn update-active-turtle [state update-fn]
  ;; Abstracción para operaciones comunes del stack
  )
```

## ✅ Aspectos Positivos

### Buena modularización
- Separación clara de responsabilidades entre namespaces
- Cada módulo tiene un propósito bien definido

### Uso correcto de inmutabilidad
- Estructuras de datos inmutables
- Transformaciones que crean nuevos estados

### Manejo de errores apropiado
**Ubicación:** ```7:24:src/tp2/parser.clj```
- Validaciones con `ex-info` para errores descriptivos
- Verificación de argumentos en funciones críticas

## 📋 Recomendaciones Priorizadas

1. **Alta prioridad:** Refactorizar función `interpretar` en funciones más pequeñas
2. **Media prioridad:** Usar bibliotecas estándar para operaciones matemáticas  
3. **Media prioridad:** Simplificar modelo de datos del estado
4. **Baja prioridad:** Optimizar recursión en `expandir`

## 🎯 Beneficios Esperados

- **Mantenibilidad:** Funciones más pequeñas son más fáciles de entender y modificar
- **Testabilidad:** Operaciones separadas permiten tests unitarios más específicos
- **Legibilidad:** Código más expresivo y menos repetitivo
- **Performance:** Uso de funciones optimizadas de la biblioteca estándar