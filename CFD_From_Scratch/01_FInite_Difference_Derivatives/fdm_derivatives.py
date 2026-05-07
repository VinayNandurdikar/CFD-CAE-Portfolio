
import numpy as np

# Polynomial definition
# f(x) = -4x^3 + 7x^2 - 3x + 9

poly_p = np.array([-4, 7, -3, 9])

# Analytical derivative using NumPy
p_der = np.polyder(poly_p)

# Evaluate exact derivative at x = 0
x_0 = 0.0
exact_derivative = np.polyval(p_der, x_0)

# Step size
h = 0.25

# Forward Difference
forward_difference = (
    np.polyval(poly_p, x_0 + h) -
    np.polyval(poly_p, x_0)
) / h

# Backward Difference
backward_difference = (
    np.polyval(poly_p, x_0) -
    np.polyval(poly_p, x_0 - h)
) / h

# Central Difference
central_difference = (
    np.polyval(poly_p, x_0 + h) -
    np.polyval(poly_p, x_0 - h)
) / (2 * h)

# Results
print("Exact Derivative       :", exact_derivative)
print("Forward Difference     :", forward_difference)
print("Backward Difference    :", backward_difference)
print("Central Difference     :", central_difference)