import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# Define the transfer function
num = [1]
den = [1, 1]
sys = sig.TransferFunction(num, den)

# Create the time vector
t = np.linspace(0, 10, 1000)
print("hello")

# Define the input
u = np.ones_like(t)

# Simulate the system
t, y, _ = sig.lsim(sys, u, t)

# Plot the results
plt.plot(t, u, label='Input')
plt.plot(t, y, label='Output')
plt.legend()
plt.show()
