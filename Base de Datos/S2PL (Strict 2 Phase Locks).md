---
aliases:
  - S2PL
  - 2PL estricto
---
Una [[transacción]] no puede adquirir un lock luego de haber liberado un lock que había adquirido, y además los locks de escritura sólo pueden ser liberados después de haber commiteado la [[transacción]].