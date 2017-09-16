import numpy as np

x = np.array([
    [1, 2],
    [3, 4]
], dtype=np.float64)

y = np.array([
    [5, 6],
    [7, 8]
], dtype=np.float64)

# output is the same
print(x + y)
print(np.add(x, y))
print()

# output is the same
print(x - y)
print(np.subtract(x, y))
print()

# output is the same
print(x * y)
print(np.multiply(x, y))
print()

# output is the same
print(x / y)
print(np.divide(x, y))
print()

print(np.sqrt(x))
print()

print(x * x)
print()


# use dot function
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))
print()

print(x.dot(v))
print(np.dot(x, v))
print()

print(x.dot(y))
print(np.dot(x, y))
print()

# use function sum
x = np.array([
    [1, 2],
    [3, 4]
])

print(np.sum(x))
print(np.sum(x, axis=0))    # compute sum of column
print(np.sum(x, axis=1))    # compute sum of row
print()

# Transposing matrix
x = np.array([
    [1, 2],
    [3, 4]
])

y = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(x)
print(x.T)
print()

print(y)
print(y.T)
print()