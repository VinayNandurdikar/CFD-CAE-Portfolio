# ============================================================================
# 1D Steady-State Heat Conduction using Finite Difference Method
#
# Governing Equation:
#     d2T/dx2 = 0
#
# Boundary Conditions:
#     T(0) = 0
#     T(L) = 1
#
# Numerical Method:
#     Jacobi iterative method
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Problem Parameters
# ----------------------------------------------------------------------------
N = 11          # Number of grid points
L = 1.0         # Domain length

# Grid spacing
h = np.float64(L / (N - 1))

# Iteration counter
iterations = 0

# ----------------------------------------------------------------------------
# Initializing Temperature Field
# ----------------------------------------------------------------------------
T = np.zeros(N)
T[N - 1] = 1.0          # Right boundary condition

# Iterated temperature field
T_new = np.zeros(N)
T_new[N - 1] = 1.0

# ----------------------------------------------------------------------------
# Convergence Parameters
# ----------------------------------------------------------------------------
epsilon = 1.0e-8        # Convergence tolerance
numerical_error = 1.0

# ----------------------------------------------------------------------------
# Jacobi Iterative Solver
# ----------------------------------------------------------------------------
while numerical_error > epsilon:

    # Update all interior points
    for i in range(1, N - 1):
        T_new[i] = 0.5 * (T[i - 1] + T[i + 1])

    # Recalculate numerical error
    numerical_error = 0.0
    for i in range(1, N - 1):
        numerical_error += abs(T[i] - T_new[i])

    # Update iteration counter
    iterations += 1

    # Copy new solution into old solution
    T = T_new.copy()

# ----------------------------------------------------------------------------
# Print Results
# ----------------------------------------------------------------------------
print("Converged successfully.")
print(f"Number of iterations: {iterations}")
print(f"Final numerical error: {numerical_error:.3e}")
print("Temperature distribution:")
print(T)

# ----------------------------------------------------------------------------
# Create Position Vector
# ----------------------------------------------------------------------------
x_dom = np.arange(N) * h

# Analytical solution
T_exact = x_dom

# ----------------------------------------------------------------------------
# Plot Results
# ----------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(
    x_dom,
    T,
    'gx--',
    linewidth=2,
    markersize=10,
    label='Numerical Solution'
)
plt.plot(
    x_dom,
    T_exact,
    'k-',
    linewidth=2,
    label='Analytical Solution'
)

plt.grid(True, color='k', alpha=0.2)
plt.xlabel("Position x", fontsize=14)
plt.ylabel("Temperature T", fontsize=14)
plt.title("1D Steady-State Heat Conduction")
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig("temperature_distribution.png", dpi=300)

# Show plot
plt.show()
