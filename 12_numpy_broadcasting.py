# For example, suppose that we want to add a constant vector to each row of a matrix.
# We could do it like this

import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

v = np.array([1, 0, 1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)
print()

vv = np.tile(v, (4, 1))     # Stack 4 copies of v on top of each other
print(vv)
print()

'''
vvv = np.tile(v, (4, 2))    #
print(vvv)
print()

vvvv = np.tile(v, (4, 3))    #
print(vvvv)
print()
'''

y = x + vv
print(y)
print()


# some applications of broadcasting
v = np.array([1, 2, 3])
w = np.array([4, 5])

print(np.reshape(v, (3, 1)) * w)