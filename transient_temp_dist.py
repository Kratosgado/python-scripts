import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.5  # Domain length (m)
u = 2.0  # Velocity (m/s)
rho = 1.0  # Density (kg/m^3)
Gamma = 0.03  # Diffusion coefficient (kg/m.s)
a = -200  # Source distribution parameter
b = 100  # Source distribution parameter
x1 = 0.6  # Source distribution parameter
x2 = 0.2  # Source distribution parameter
F = rho * u  # Convective flux
D = 0.9  # Diffusion coefficient

# Grid
N = 45  # Number of grid points
dx = L / (N - 1)
x = np.linspace(0, L, N)

# Initial condition
phi = np.zeros(N)

# Time parameters
dt = 0.01  # Time step
t_final = 100  # Final time
t = 0  # Current time

# Analytical steady-state solution
def analytical_solution(x):
    return (a / Gamma) * (x - x1) * (x2 - x) / (x2 - x1) + b * (x - x1) + a * (x2 - x) + 0.5 * F * (x ** 2) - F * L * x

# Lists to store results for plotting
numerical_solution = []
analytical_solution_values = []

# Implicit method for time integration
while t < t_final:
    # Construct tri-diagonal coefficient matrix
    A = np.zeros((N, N))
    for i in range(1, N - 1):
        F_w = max(0, min(1, F * dt / dx))  # Upwind coefficient
        F_e = max(0, min(1, -F * dt / dx))  # Upwind coefficient
        D_w = max(0, min(1, D * dt / dx ** 2))  # Diffusion coefficient
        D_e = max(0, min(1, D * dt / dx ** 2))  # Diffusion coefficient
        
        # Hayase et al. variant of the QUICK scheme
        a_w = 0.5 + F_w - 2 * D_w
        a_e = 0.5 - F_e - 2 * D_e
        a_p = a_w + a_e + F_w - F_e + 2 * (D_w + D_e)
        
        A[i, i - 1] = -a_w
        A[i, i] = a_p
        A[i, i + 1] = -a_e
    
    # Boundary conditions
    A[0, 0] = 1
    A[0, 1] = 0
    A[-1, -1] = 1
    A[-1, -2] = 0
    
    # Source term
    b = np.zeros(N)
    for i in range(N):
        if x[i] >= x1 and x[i] <= x2:
            b[i] = (a * (x[i] - x1) + b * (x2 - x[i])) / (x2 - x1)
    
    # Solve the system of equations using TDMA
    phi_new = np.linalg.solve(A, phi + b * dt)
    
    # Update phi for the next time step
    phi = phi_new.copy()
    t += dt
    
    numerical_solution.append(phi.copy())
    analytical_solution_values.append(analytical_solution(x))

    # Check for convergence (e.g., max change in phi)
    max_change = np.max(np.abs(phi_new - phi))
    if max_change < 1e-6:
        break

    
    # Update phi for the next time step
    phi = phi_new.copy()
    t += dt
    
    numerical_solution.append(phi.copy())
    analytical_solution_values.append(analytical_solution(x))

# Convert lists to arrays for easier plotting
numerical_solution = np.array(numerical_solution)
analytical_solution_values = np.array(analytical_solution_values)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, numerical_solution[-1], label='Numerical Solution (Final Time)')
plt.plot(x, analytical_solution_values[-1], label='Analytical Solution (Steady State)')
plt.title('Transient Temperature Distribution')
plt.xlabel('Position (m)')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
