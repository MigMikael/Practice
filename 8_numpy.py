import numpy as np

# numpy array
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)

print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b.shape)
print(b[0,0], b[0,1], b[1,0])
print()

# Numpy also provides many functions to create arrays

a = np.zeros((2,2))
print(a)
print()

b = np.ones((1,2))
print(b)
print()

c = np.full((2,2), 5)
print(c)
print()

d = np.eye(2)
print(d)
print()

e = np.random.random((2,2))
print(e)
print()