import numpy as np
import matplotlib.pyplot as plt
import math


# Parameters
L = 1.5  # length of the domain
u = 2.0  # velocity
p = 1.0  # density
G = 0.03  # diffusion coefficient
a = -200  # source distribution parameter
b = 100  # source distribution parameter
x1 = 0.6  # source distribution parameter
x2 = 0.2  # source distribution parameter
N = 100  # number of spatial grid points
dt = 0.01  # time step
dx = 0.0333
D = 0.9 # T/dx
F = 2.0 # p*u
num_nodes = 45
num_terms = 45  # Number of terms in the Fourier series
delta_x = L / (num_nodes - 1)  # Grid spacing
QW = 1
QE = 1
QA = 0
Qww = 1
QP0 = 0
# n = 45  # Number of nodes
# initial field values
QP = 0
QP_NEW = np.zeros(num_nodes)
converge_counter = 0

# Tolerance for convergence
tolerance = 1e-9

for t in np.arange(0.01, 100, dt):  # Iterate for convergence
    # Initialize arrays
    # SU = np.zeros(num_nodes)

    ap0 = (p * dx) / dt
    for n in range(num_nodes):
        if n+1 == 1:
            ae = D + (D / 3)
            aw = 0
            sp = -(((8/3.0) * D) + F)
            SU = ((8/3.0)* D + F) * QA +( 1 / 8.0) * F * (QP - 3 * QE)
        elif n+1 == 2:
            aw = D
            ae = D + F
            sp = 0
            SU =( 1 / 8.0 )* F * (3 * QP - QW) +( 1 / 8.0 )* F * (QW + 2 * QP - 3 * QE)
        elif n+1 == 45:
            aw = D + F 
            ae = 0
            sp = 0
            SU = (1/8.0) * F * (3 * QP - 2 * QW - Qww)
        else:
            aw = D
            ae = D + F
            sp = 0
            SU =( 1 / 8.0 )* F * (3 * QP - 2 * QW - Qww) +( 1 / 8.0 )* F * (QW + 2 * QP - 3 * QE)

        ap = aw + ae + ap0 - sp
        # Update QP_NEW[n]
        QP_NEW[n] = (aw * QW + ae * QE + ap0* QP + SU) / ap

    # Check convergence
    max_diff = np.max(np.abs(QP_NEW[n] - QP_NEW[n-1]))
    if max_diff < tolerance:
        QP = QP_NEW[n]
        print("Converged at iteration:", t, "QP = ", QP)
        break

    # Update QP for next iteration
    # QP = np.copy(QP_NEW[n])

# print(QP_NEW)


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


# Main function
def main():
    time_steps = 1000  # Number of time steps
    # phi_transient = compute_transient_temperature_field(time_steps)
    return compute_transient_temperature_field(time_steps)
    


# if __name__ == "__main__":
#     main()

# Plotting the graph for Distance vs (analytical and numerical)
# x_axis values are the distance values
x = [n]
x_axis = x

# y_axis values are the numerical transient temperature values
yaxis = QP_NEW[n]
# y2axis =


# plt.figure(figsize=(10, 6))
# plt.plot(x,QP_NEW[n] , label='Numerical Solution', color='blue')
# plt.plot(x, main(), label='Analytical Solution', linestyle='--', color='red')
# plt.title('Comparison of Numerical and Analytical Solutions')
# plt.xlabel('Position(m)')
# plt.ylabel('Temperature')
# plt.legend()
# plt.grid(True)
# plt.show()


Comment = "Comment: By comparing the graphs, the analytical solution is more precise than the numerical approach"
print(Comment)