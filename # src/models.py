# src/models.py

class QuantumState:
    def __init__(self, state_vector):
        self.state_vector = state_vector

    def evolve(self, hamiltonian):
        return self.state_vector
