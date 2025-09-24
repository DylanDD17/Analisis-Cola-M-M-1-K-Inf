import math

def mm1k_theory(lmbda, mu, K):
    """Calcula métricas teóricas para M/M/1/K."""
    rho = lmbda / mu
    eps = 1e-12

    # Caso K = infinito (M/M/1)
    if K is None or K == math.inf:
        if rho >= 1:
            return {"rho": rho, "P0": 0.0, "PK": 0.0,
                    "Ns": math.inf, "Nw": math.inf,
                    "lambda_eff": lmbda, "Ts": math.inf, "Tw": math.inf}
        Ns = rho / (1 - rho)
        Nw = rho**2 / (1 - rho)
        Ts = 1.0 / (mu - lmbda)
        Tw = rho / (mu - lmbda)
        return {"rho": rho, "P0": 1 - rho, "PK": 0.0,
                "Ns": Ns, "Nw": Nw, "lambda_eff": lmbda, "Ts": Ts, "Tw": Tw}

    # Caso K finito
    if abs(rho - 1.0) < 1e-10:
        P0 = 1.0 / (K + 1)
        PK = P0
        Ns = K / 2.0
        prob_busy = 1.0 - P0
        lambda_eff = lmbda * (1 - PK)
        Nw = Ns - prob_busy
        Ts = Ns / lambda_eff
        Tw = Nw / lambda_eff
        return {"rho": rho, "P0": P0, "PK": PK, "Ns": Ns,
                "Nw": Nw, "lambda_eff": lambda_eff, "Ts": Ts, "Tw": Tw}
    else:
        P0 = (1.0 - rho) / (1.0 - rho**(K+1))
        PK = P0 * rho**K
        Ns = rho * (1 - (K+1)*rho**K + K*rho**(K+1)) / ((1 - rho) * (1 - rho**(K+1)))
        prob_busy = 1.0 - P0
        Nw = Ns - prob_busy
        lambda_eff = lmbda * (1 - PK)
        Ts = Ns / lambda_eff
        Tw = Nw / lambda_eff
        return {"rho": rho, "P0": P0, "PK": PK, "Ns": Ns,
                "Nw": Nw, "lambda_eff": lambda_eff, "Ts": Ts, "Tw": Tw}

# ========================
# CASOS DE PRUEBA
# ========================
casos = [
    {"nombre": "Caso 1: λ<μ (estable)", "lambda": 2.0, "mu": 3.0, "K": 10},
    {"nombre": "Caso 2: λ=μ (saturación)", "lambda": 3.0, "mu": 3.0, "K": 10},
    {"nombre": "Caso 3: λ>μ (sobrecarga)", "lambda": 4.0, "mu": 3.0, "K": 10},
]

# Imprimir resultados
print(f"{'Caso':35s} {'ρ':>6s} {'Ns':>10s} {'Nw':>10s} {'Ts':>10s} {'Tw':>10s} {'P_K':>10s}")
print("-"*90)
for c in casos:
    r = mm1k_theory(c["lambda"], c["mu"], c["K"])
    print(f"{c['nombre']:35s} {r['rho']:6.3f} {r['Ns']:10.4f} {r['Nw']:10.4f} "
          f"{r['Ts']:10.4f} {r['Tw']:10.4f} {r['PK']:10.4f}")