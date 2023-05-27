import numpy as np
import matplotlib.pyplot as plt

# Define the parameters and boundary conditions
n_x = 10
x = [0.0] * n_x
a = [0.0] * n_x
b = [0.0] * n_x
c = [0.0] * n_x
d = [0.0] * n_x
delta_x = 1.0 / (n_x - 1.0)

for i in range(n_x):
    x[i] = delta_x * i

# Define the different values of Bi
Bi_values = [0.1, 10.0, 100.0 ]

# Loop through each value of Bi and solve for the temperature distribution
for Bi in Bi_values:
    for i in range(n_x):
        # Boundary conditions at Base
        if i == 0:
            a[i] = 0.0
            b[i] = 1.0
            c[i] = 0.0
            d[i] = 1.0
        # Convective boundary conditions at the end
        elif i == n_x-1:
            a[i] = -1.0
            b[i] = 1.0 + Bi * delta_x
            c[i] = 0.0
            d[i] = 0.0
        # Interior points
        else:
            a[i] = 2.0 * (x[i] - 1.0) - delta_x
            b[i] = -4.0 * x[i] + 4.0 - 2.0 * Bi * 100.0 * (x[i] - 1.0) * (delta_x ** 2)
            c[i] = 2.0 * x[i] - 2.0 + delta_x
            d[i] = 0.0

    # Solve the tridiagonal system of equations using Thomas algorithm:
    for i in range(1, n_x):
        b[i] = b[i] - c[i-1] * a[i] / b[i-1]
        d[i] = d[i] - d[i-1] * a[i] / b[i-1]

    Temp = [0.0] * n_xi
    Temp[n_x-1] = d[n_x-1] / b[n_x-1]
    Temp[0] = 1.0

    for i in range(n_x-2, 0, -1):
        Temp[i] = (d[i] - c[i] * Temp[i+1]) / b[i]

    # Plot the temperature distribution graph for the current value of Bi
    plt.plot(x, Temp, label=f"Bi={Bi}")

# Add labels and a legend to the graph
plt.xlabel('x')
plt.ylabel('Temperature')
plt.title(f'Temperature Distribution for Different Bi Values')
plt.legend()

# Display the graph
plt.show()
