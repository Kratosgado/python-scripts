from matplotlib import pyplot as plt
import numpy as np

# Assuming initialization of necessary variables
num_nodes = 45  # Number of nodes
D = 0.9  # Diffusion coefficient, example value
F = 2.0  # Convection coefficient, example value
p = 1.0  # Property related to accumulation term, example value
dx = 1.0 / (num_nodes - 1)  # Spatial step, example calculation
dt = 0.01  # Time step, example value
tolerance = 1e-9  # Tolerance for convergence

u = 2.0  # velocity
G = 0.03  # diffusion coefficient
L = 1.5  # length of the domain
a = -200  # source distribution parameter
b = 100  # source distribution parameter
x1 = 0.6  # source distribution parameter
x2 = 0.2  # source distribution parameter
delta_x = L / (num_nodes - 1)  # Grid spacing
num_terms = 45  # Number of terms in the Fourier series



# Initial field values
QW = 1
QE = 1
QA = 0
Qww = 1
QP0 = 0

# Initialize arrays
QP_NEW = np.zeros(num_nodes)
QP = np.zeros(num_nodes)  # Previous time step values
SU = np.zeros(num_nodes)  # Source term array

converge_counter = 0

for t in np.arange(0.01, 100, dt):  # Iterate for convergence
    ap0 = (p * dx) / dt
    for n in range(num_nodes):
        if n == 0:  # First node
            ae = D + (D / 3)
            aw = 0
            sp = -(((8/3.0) * D) + F)
            SU[n] = ((8/3.0) * D + F) * QA + (1 / 8.0) * F * (QP[n] - 3 * QE)
        elif n == 1:  # Second node
            aw = D
            ae = D + F
            sp = 0
            SU[n] = (1 / 8.0) * F * (3 * QP[n] - QW) + (1 / 8.0) * F * (QW + 2 * QP[n] - 3 * QE)
        elif n == num_nodes - 1:  # Last node
            aw = D + F
            ae = 0
            sp = 0
            SU[n] = (1/8.0) * F * (3 * QP[n] - 2 * QW - Qww)
        else:  # Interior nodes
            aw = D
            ae = D + F
            sp = 0
            SU[n] = (1 / 8.0) * F * (3 * QP[n] - 2 * QW - Qww) + (1 / 8.0) * F * (QW + 2 * QP[n] - 3 * QE)
        ap = aw + ae + ap0 - sp
        QP_NEW[n] = (aw * QW + ae * QE + ap0 * QP[n] + SU[n]) / ap

    # Check convergence
    max_diff = np.max(np.abs(QP_NEW - QP))
    if max_diff < tolerance:
        print("Converged at iteration:", t)
        break
    QP = QP_NEW.copy()

# Print the converged values
print("Converged values:", QP)


# Function to compute coefficients C1 and C2
def compute_C1_C2():
    P = p * u / G
    sum_terms = 0
    for n in range(1, num_terms + 1):
        sum_terms += np.cos(n * np.pi) / (n ** 2 * np.pi ** 2) * np.exp(-n ** 2 * np.pi ** 2 * P * L / G)
    C2 = a / (P ** 2) + sum_terms
    C1 = -C2
    return C1, C2


# Function to compute coefficients an
def compute_an():
    an = np.zeros(num_terms)
    for n in range(1, num_terms + 1):
        term1 = n ** 2 * (2 * np.pi * L) ** 2
        term2 = a * (x1 + x2) / 2 + b * np.cos(n * np.pi * (x1 + x2) / L)
        term3 = a * x1 * x2 + b * np.cos(n * np.pi * (x1 + x2) / L) * (x1 + x2)
        term4 = b * np.cos(n * np.pi * (x1 + x2) / L) * (x1 * x2)
        an[n - 1] = term1 / (424 * G * term2) * (term3 + term4)
    return an


# Function to compute transient temperature field
def compute_transient_temperature_field(time_steps, n=45):
    C1, C2 = compute_C1_C2()
    an = compute_an()

    # Initialize temperature field
    phi_transient = np.zeros(n)

    # Time-stepping loop
    for _ in range(time_steps):
        phi_transient_new = np.zeros(n)
        for x_index in range(num_nodes):
            x = x_index * delta_x
            term_sum = 0
            for n in range(1, num_terms + 1):
                term_sum += an[n - 1] * np.sin(n * np.pi * x / L)
            phi_transient_new[x_index] = C1 + C2 * np.exp(-p * u * x / G) + term_sum
        phi_transient = phi_transient_new

    return phi_transient

# Example usage
time_steps = 1000  # Define the number of time steps
phi_transient = compute_transient_temperature_field(time_steps)
print(phi_transient)

x = np.linspace(0, L, num_nodes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, QP, label='Numerical Solution', marker='o', linestyle='-', color='blue', markersize=4)
plt.plot(x, phi_transient, label='Analytical Solution', marker='x', linestyle='--', color='red')
plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('Comparison of Numerical and Analytical Solutions')
plt.legend()
plt.grid(True)
plt.show()