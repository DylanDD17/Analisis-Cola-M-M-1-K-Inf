# Modelo matemático M/M/1/K/∞

Para el sistema de colas **M/M/1/K/∞** se definen las siguientes variables:

- `λ` : tasa de llegada de usuarios.
- `μ` : tasa de servicio.
- `ρ = λ / μ` : factor de utilización del sistema.
- `N_s` : número promedio de usuarios en el sistema.
- `T_s` : tiempo promedio en el sistema.
- `N_w` : número promedio de usuarios en la cola.
- `T_w` : tiempo promedio de espera en la cola.

---

## Probabilidades del sistema

La probabilidad de que haya `n` usuarios en el sistema es:

\[
P_n = \frac{(1 - \rho)\rho^n}{1 - \rho^{K+1}}, \quad 0 \leq n \leq K
\]

La probabilidad de bloqueo (sistema lleno) es:

\[
P_K = \frac{(1 - \rho)\rho^K}{1 - \rho^{K+1}}
\]

---

## Número promedio de usuarios en el sistema

\[
N_s = \frac{\rho \left(1 - (K+1)\rho^K + K\rho^{K+1}\right)}{(1 - \rho)(1 - \rho^{K+1})}
\]

---

## Número promedio de usuarios en cola

\[
N_w = N_s - (1 - P_0)
\]

donde 

\[
P_0 = \frac{1 - \rho}{1 - \rho^{K+1}}
\]

es la probabilidad de que no haya usuarios en el sistema.

---

## Tiempos promedio

Aplicando la Ley de Little:

\[
T_s = \frac{N_s}{\lambda \cdot (1 - P_K)}
\]

\[
T_w = \frac{N_w}{\lambda \cdot (1 - P_K)}
\]

donde \(\lambda \cdot (1 - P_K)\) es la tasa efectiva de llegada (los usuarios que realmente ingresan al sistema).

---
