import numpy as np

z = np.random.randint(low=0, high=2, size=(32, 1))
print(z, '\n')

x = np.random.randn(32, 2) + 3
x = x * (z+1)
print(type(x))
print(x, '\n')

