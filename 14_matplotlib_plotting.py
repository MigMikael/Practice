import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5 * np.pi, 0.1)
y = np.sin(x)
print(x)
print()
print(y)

# plot the points using matplotlib
# plt.plot(x, y)
# plt.show()

# plot multiple lines at once

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
#plt.legend(['Sine', 'Cosine'])
plt.show()