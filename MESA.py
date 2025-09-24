# mm1k_mesa.py
import random
import math
from mesa import Model
from mesa.time import BaseScheduler
from mesa.datacollection import DataCollector

class MM1KModel(Model):
    def __init__(self, arrival_rate, service_rate, K, max_time=1000.0):
        super().__init__()
        self.lambda_rate = arrival_rate  # λ
        self.mu = service_rate           # μ
        self.K = K                       # Capacidad máxima del sistema
        self.max_time = max_time

        # Estado del sistema
        self.now = 0.0
        self.num_in_system = 0
        self.num_in_queue = 0
        self.server_busy = False

        # Estadísticas
        self.total_arrivals = 0
        self.total_served = 0
        self.total_blocked = 0
        self.area_num_in_system = 0.0
        self.area_num_in_queue = 0.0
        self.last_event_time = 0.0
        self.wait_times = []

        # Eventos futuros
        self.next_arrival = self.now + random.expovariate(self.lambda_rate)
        self.next_departure = math.inf  # no hay salida hasta que alguien entre

        self.running = True

    def step(self):
        """Un paso de simulación: avanza hasta el próximo evento."""
        if self.now >= self.max_time:
            self.running = False
            return

        # Determinar qué ocurre primero: llegada o salida
        if self.next_arrival < self.next_departure:
            next_event_time = self.next_arrival
            event = "arrival"
        else:
            next_event_time = self.next_departure
            event = "departure"

        # Actualizar área para métricas de tiempo promedio
        dt = next_event_time - self.last_event_time
        self.area_num_in_system += self.num_in_system * dt
        self.area_num_in_queue += self.num_in_queue * dt
        self.last_event_time = next_event_time
        self.now = next_event_time

        if event == "arrival":
            self.handle_arrival()
        else:
            self.handle_departure()

    def handle_arrival(self):
        if self.num_in_system < self.K:  # hay espacio en el sistema
            self.num_in_system += 1
            self.total_arrivals += 1

            if self.server_busy:
                self.num_in_queue += 1
            else:
                self.server_busy = True
                self.next_departure = self.now + random.expovariate(self.mu)
        else:
            # Sistema lleno -> bloqueo
            self.total_blocked += 1

        # Programar la próxima llegada
        self.next_arrival = self.now + random.expovariate(self.lambda_rate)

    def handle_departure(self):
        self.num_in_system -= 1
        self.total_served += 1

        if self.num_in_queue > 0:
            self.num_in_queue -= 1
            self.next_departure = self.now + random.expovariate(self.mu)
        else:
            self.server_busy = False
            self.next_departure = math.inf

    def run_model(self):
        while self.running:
            self.step()

    def results(self):
        lambda_eff = self.total_arrivals / self.now  # tasa de llegada efectiva
        Ns = self.area_num_in_system / self.now
        Nw = self.area_num_in_queue / self.now
        Ts = Ns / lambda_eff if lambda_eff > 0 else 0
        Tw = Nw / lambda_eff if lambda_eff > 0 else 0
        rho = Ns / self.K if self.K > 0 else 0

        return {
            "Tiempo final": round(self.now, 3),
            "λ efectivo": round(lambda_eff, 4),
            "ρ (utilización)": round(rho, 4),
            "Ns (en sistema)": round(Ns, 4),
            "Nw (en cola)": round(Nw, 4),
            "Ts (tiempo en sistema)": round(Ts, 4),
            "Tw (tiempo en cola)": round(Tw, 4),
            "Bloqueo (%)": round(self.total_blocked / (self.total_arrivals + self.total_blocked) * 100, 2)
        }

if __name__ == "__main__":
    casos = [
        {"nombre": "Caso 1: λ<μ (estable)", "lambda": 0.5, "mu": 1.0, "K": 10},
        {"nombre": "Caso 2: λ=μ (saturación)", "lambda": 1.0, "mu": 1.0, "K": 10},
        {"nombre": "Caso 3: λ>μ (sobrecarga)", "lambda": 1.0, "mu": 0.5, "K": 10},
    ]

    for caso in casos:
        print(f"\n--- {caso['nombre']} ---")
        model = MM1KModel(caso["lambda"], caso["mu"], caso["K"], max_time=20000)
        model.run_model()
        for k, v in model.results().items():
            print(f"{k}: {v}")
