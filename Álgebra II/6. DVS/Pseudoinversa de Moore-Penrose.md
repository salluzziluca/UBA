---
dg-publish: true
---
rg(A)=k
Si $A = U_k D_k V_k^T$ se define como pseudoinversa de A
$A^+ = V_k D_k^{-1} U_k^T$
$A^+A = V_k D_k^{-1} U_k^T U_k D_k^{1} V_k^T = V_k D_k^{-1} I D_k^{1} V_k^T = V_k V_k^t = Pfil(a)$
tanto $U_k^t U_k$, como $D_k^{-1} D_k^1$  dan la identidad 
$AA^+ =U_k U_k^t = Pcol(A)$
$AA^+A= A$ 

Si $A \in R^{m \times n}$ y $rg(A)=n$
$\exists$ A^# $= (A^T A)^-1 A^T$
$A^+ \exists \forall A \in R^{m \times n}$. Si rg(A) = n -> A^+=A^#

![[Pasted image 20221201223839.png]]
![[Pasted image 20221201223849.png]]
![[Pasted image 20221201223920.png]]
