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

## NS: Número de usuarios en el sistema

Número promedio de usuarios (en cola + en servicio):

$$
N_s = \frac{\rho \left(1 - (K+1)\rho^K + K\rho^{K+1}\right)}{(1 - \rho)(1 - \rho^{K+1})}
$$

---

## TS: Tiempo en el sistema

Tiempo promedio que un usuario pasa en el sistema (espera + servicio):

$$
T_s = \frac{N_s}{\lambda \cdot (1 - P_K)}
$$

---

## Nw: Número de usuarios en cola

Número promedio de usuarios esperando su turno en la cola:

$$
N_w = N_s - (1 - P_0)
$$

donde 

$$
P_0 = \frac{1-\rho}{1-\rho^{K+1}}
$$

es la probabilidad de que el sistema esté vacío.

---

## Tw: Tiempo en cola

Tiempo promedio que un usuario pasa esperando en la cola:

$$
T_w = \frac{N_w}{\lambda \cdot (1 - P_K)}
$$

---

### Notas:
$$
\(P_K = \dfrac{(1-\rho)\rho^K}{1-\rho^{K+1}}\)
$$

es la probabilidad de que el sistema esté lleno (bloqueo).  

$$
\(\lambda \cdot (1 - P_K)\) 
$$

representa la tasa **efectiva de llegada** (solo los usuarios que logran entrar al sistema).
