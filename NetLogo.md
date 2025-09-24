# Comparación Teórica vs Simulación — M/M/1/K (K=10)

Estos son los **valores teóricos** calculados para tres escenarios: sistema estable, saturado y sobrecargado.

<img width="712" height="85" alt="image" src="https://github.com/user-attachments/assets/9c1ef4c7-7953-4962-a1ca-dc9775f4bc3c" />

---

## Caso 1: λ < μ (estable)

<img width="954" height="621" alt="image" src="https://github.com/user-attachments/assets/8a1c2803-2034-4120-830c-e2b3537f932a" />

**Parámetros:**
- λ = 0.5  
- μ = 1.0  
- ρ = 0.500  
- K = 10  

| **Métrica**             | **Teórico** | **Simulación (NetLogo)** | **Error Relativo (%)** |
|-----------------------|-----------|------------------------|----------------------|
| **ρ (Utilización)**   | 0.500 (50%) | 50 % | 0 % |
| **Ns (en sistema)**   | 0.9946    | ... | — |
| **Nw (en cola)**      | 0.4949    | 0.49 | 0.99 % |
| **Ts (tiempo en sistema)** | 1.9902 | 1.977 | 0.66 % |
| **Tw (tiempo en cola)** | 0.9902 | 0.978 | 1.23 % |
| **Pₖ (bloqueo)**      | 0.0005    | *No medido en NetLogo* | — |

---

## Caso 2: λ = μ (saturación)

<img width="955" height="660" alt="image" src="https://github.com/user-attachments/assets/11cec60a-176a-4891-b190-1780bd555c4a" />

**Parámetros:**
- λ = 1.0  
- μ = 1.0  
- ρ = 1.000  
- K = 10  

| **Métrica**             | **Teórico** | **Simulación (NetLogo)** | **Error Relativo (%)** |
|-----------------------|-----------|------------------------|----------------------|
| **ρ (Utilización)**   | 1.000 (100%) | 50.0 | 0 % |
| **Ns (en sistema)**   | 5.0000    | ... | — |
| **Nw (en cola)**      | 4.0909    | 0.497 | 87.85% |
| **Ts (tiempo en sistema)** | 5.5000 | 1.997 | 63.69%  |
| **Tw (tiempo en cola)** | 4.5000 | 0.994 | 77.91% |
| **Pₖ (bloqueo)**      | 0.0909    | *No medido en NetLogo* | — |

---

## Caso 3: λ > μ (sobrecarga)

<img width="956" height="631" alt="image" src="https://github.com/user-attachments/assets/d44104ee-bda5-472a-adb9-aed1c814403f" />

**Parámetros:**
- λ = 1.0  
- μ = 0.5  
- ρ = 2.000  
- K = 10  

| **Métrica**             | **Teórico** | **Simulación (NetLogo)** | **Error Relativo (%)** |
|-----------------------|-----------|------------------------|----------------------|
| **ρ (Utilización)**   | 2.000 (>100%) | 52.57 | 2528.5% |
| **Ns (en sistema)**   | 9.0054    | ... | — |
| **Nw (en cola)**      | 8.0059    | 0.583 | 92.71% |
| **Ts (tiempo en sistema)** | 18.0196 | 1.056 | 94.14% |
| **Tw (tiempo en cola)** | 16.0196 | 0.555 | 96.53% |
| **Pₖ (bloqueo)**      | 0.5002    | *No medido en NetLogo* | — |

---


**Notas:**
- Se espera que el **error relativo** sea pequeño (idealmente <10%), pero en casos de saturación o sobrecarga las colas pueden fluctuar más.
- Para reducir variabilidad:
  - Usa `max-run-time` alto (≥ 200 000 ticks).
  - Ignora los primeros `stats-reset-time` ticks (≥ 5 000).
  - Ejecuta varias corridas y promedia.
