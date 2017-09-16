# Lists
# A list is the Python equivalent of an array, but is resizeable and can contain elements of different types

print('------------------------------------------')
xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])

xs[2] = 'fool'
print(xs)
xs.append('lish')
print(xs)

x = xs.pop()
print(x)
print(xs)


# Slicing
print('------------------------------------------')

nums = list(range(5))
print(nums)             # [0, 1, 2, 3, 4]
print(nums[2:4])        # [2, 3]
print(nums[2:])         # [2, 3, 4]
print(nums[:2])         # [0, 1]
print(nums[:])          # [0, 1, 2, 3, 4]
print(nums[:-1])        # [0, 1, 2, 3]
nums[2:4] = [8,9]
print(nums)             # [0, 1, 8, 9, 4]


# Loops
print('------------------------------------------')

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))


# List comprehensions
print('------------------------------------------')

nums = [0, 1, 2, 3, 4]
squares = []
for n in nums:
    squares.append(n ** 2)
print(squares)

nums = [0, 1, 2, 3, 4]
squares = [x ** 3 for x in nums]
print(squares)

nums = [0, 1, 2, 3, 4]
squares = [x ** 3 for x in nums if x % 2 == 0]
print(squares)
