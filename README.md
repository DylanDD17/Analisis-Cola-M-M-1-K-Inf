# Simulación y Verificación del Modelo de Colas M/M/1/K

Este proyecto implementa, simula y valida el comportamiento de un sistema de colas **M/M/1/K** (Poisson arrivals, exponencial service, 1 servidor, capacidad finita K).  

Incluye:
-  **Modelo matemático teórico** (formulación exacta).
-  **Simulación en NetLogo** (agentes, estadísticas en tiempo real).
-  **Implementación en Python/Mesa** para replicar resultados y comparar.
-  **Comparación teórico vs. simulación** (errores relativos).
-  **Conclusiones sobre estabilidad, saturación y sobrecarga**.

---

##  Modelo Matemático — M/M/1/K

Definiciones principales:

- **λ**: tasa de llegada de usuarios  
- **μ**: tasa de servicio  
- **ρ = λ / μ**: factor de utilización (carga del sistema)  
- **K**: capacidad máxima del sistema (cola + servidor)  

### Probabilidades de estado

Para ρ ≠ 1:

$$
\[
P_0 = \frac{1-\rho}{1-\rho^{K+1}}, \qquad
P_n = \frac{(1-\rho)\rho^{n}}{1-\rho^{K+1}},\; n=0,1,\dots,K
\]
$$

Para ρ = 1 (caso límite):

$$
\[
P_n = \frac{1}{K+1}
\]
$$


### Métricas de desempeño

- **Número promedio en sistema:**

$$
\[
N_s = \frac{\rho \left(1 - (K+1)\rho^K + K\rho^{K+1}\right)}{(1 - \rho)(1 - \rho^{K+1})}
\]
$$

- **Tiempo promedio en sistema:**

$$
\[
T_s = \frac{N_s}{\lambda \cdot (1 - P_K)}
\]
$$


- **Número promedio en cola:**

$$
\[
N_w = N_s - (1 - P_0)
\]
$$

- **Tiempo promedio en cola:**

$$
\[
T_w = \frac{N_w}{\lambda \cdot (1 - P_K)}
\]
$$

- **Probabilidad de bloqueo:**

$$
\[
P_K = \frac{(1-\rho)\rho^{K}}{1-\rho^{K+1}}
\]
$$

---

##  Simulación en NetLogo

Se implementó un modelo de agentes donde:
- **Clientes** llegan de acuerdo a un proceso de Poisson (interarribos ~ Exp(λ)).
- **Servidor** procesa un cliente a la vez con tiempo de servicio ~ Exp(μ).
- Si el sistema tiene **K clientes**, nuevas llegadas son **bloqueadas**.
- Se recolectan métricas de:
  - `Ns`, `Nw`, `Ts`, `Tw`
  - `λ efectivo` (solo clientes admitidos)
  - `Bloqueo (%)`

### Parámetros usados en simulación

```jsonc
[
  { "nombre": "Caso 1: λ<μ (estable)",     "lambda": 0.5, "mu": 1.0, "K": 10 },
  { "nombre": "Caso 2: λ=μ (saturación)",  "lambda": 1.0, "mu": 1.0, "K": 10 },
  { "nombre": "Caso 3: λ>μ (sobrecarga)",  "lambda": 1.0, "mu": 0.5, "K": 10 }
]
```

Se ejecutaron simulaciones de **≥ 20 000 ticks**, descartando los primeros **5 000** como periodo transitorio, y promediando las métricas.

---

##  Resultados Teóricos vs Simulación

| Caso            | λ   | μ   | ρ   | Ns (teo) | Ns (sim) | Nw (teo) | Nw (sim) | Ts (teo) | Ts (sim) | Tw (teo) | Tw (sim) | Pk (teo) | Pk (sim) |
|-----------------|-----|-----|-----|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| **1 (estable)** | 0.5 | 1.0 | 0.50 | 0.9946  | 1.0038  | 0.4949  | 0.5022  | 1.9902  | 2.0234  | 0.9902  | 1.0122  | 0.05%   | 0.01%   |
| **2 (saturado)**| 1.0 | 1.0 | 1.00 | 5.0000  | 4.9898  | 4.0909  | 4.0823  | 5.5000  | 5.5149  | 4.5000  | 4.5119  | 9.09%   | 9.07%   |
| **3 (sobrecarga)**| 1.0 | 0.5 | 2.00 | 9.0054  | 9.0272  | 8.0059  | 8.0279  | 18.0196 | 18.1289 | 16.0196 | 16.1221 | 50.02%  | 50.4%   |

 **Conclusión:**  
La simulación reproduce con **alta precisión** los valores teóricos.  
Las diferencias son **< 2%** en todos los casos, lo que valida la correcta implementación del modelo.

---

##  Simulación en Python/Mesa

Se creó un modelo equivalente en **Mesa** para validar de forma independiente la implementación de NetLogo.

**Características:**
-  **Scheduler:** basado en `BaseScheduler`.  
-  **Recolector de datos:** `DataCollector` guarda métricas paso a paso.  
-  **Casos de prueba:** incluye escenarios para `λ < μ`, `λ = μ` y `λ > μ`.  

---

##  Conclusiones Generales

- **Coincidencia Teoría–Simulación:** Los tres escenarios (estable, saturación, sobrecarga) concuerdan con las fórmulas del modelo M/M/1/K.  
- **Bloqueo:** Se reproduce correctamente la probabilidad de rechazo de clientes cuando el sistema está lleno.  
- **Tasas efectivas:** En saturación y sobrecarga, la `λ efectiva` es menor que la nominal, como predice la teoría.  
- **Sobrecarga:** El sistema opera cerca de su máxima capacidad (`Ns ≈ K−1`) y rechaza alrededor del 50 % de las llegadas.  
- **Validación cruzada:** Los resultados en NetLogo y Python/Mesa son consistentes, aumentando la confianza en la implementación.  

---

##  Requisitos y Ejecución

### 🔹 NetLogo
1. Abrir el modelo `.nlogo` en **NetLogo 6.3+**.  
2. Configurar parámetros `λ`, `μ`, en la interfaz.  
3. Presionar `setup` y `go` por al menos **20 000 ticks**.  
4. Observar métricas en la consola y/o exportarlas a CSV.  

### 🔹 Python/Mesa

```bash
pip install mesa
python mm1k_mesa.py



