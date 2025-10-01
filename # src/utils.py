# src/utils.py

def calculate_thrust(epsilon, omega, V, c, gradient):
    return (epsilon * omega**3 * V / c**2) * (gradient**2)

def p_adic_quantization(data):
    # Example function for p-adic quantization
    return data
