import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 normally distributed values with mean=5 and std=2
data = np.random.normal(loc=5, scale=2, size=1000)

# Define the x range and function h(x) = x^3
x = np.linspace(0, 10, 400)
h = x**3

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the histogram of the data
plt.hist(data, bins=30, alpha=0.6, color='skyblue', label='Normal Distribution (μ=5, σ=2)', density=True)

# Plot the function h(x) = x^3
#plt.plot(x, h, color='darkorange', label='h(x) = x³', linewidth=2)

# Make the plot look nice
plt.title('Histogram and h(x) = x³')
plt.xlabel('x')
plt.ylabel('Density / h(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('plot_output.png')

# Show the plot
plt.show()