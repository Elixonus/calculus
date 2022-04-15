from math import sin
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = np.sin(x)
y_derivative = np.cos(x)
# integral of y(x) is -cos(x)
y_integral = -np.cos(x)


number_steps = 100
y_integral_euler = np.empty(100)
last = 0
for n in range(number_steps):
    y_integral_euler[n] = last
    last += 0.01 * y[n]

fig, ax = plt.subplots()
ax.plot(x, y_integral_euler)
ax.plot(x, y_integral)
plt.show()