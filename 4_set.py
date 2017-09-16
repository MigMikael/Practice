# set
# A set is an unordered collection of distinct elements.
print('------------------------------------------')

animals = {'cat', 'dog'}
print("All animals : ", animals)
print('cat' in animals)
print('fish' in animals)

print()

animals.add('fish')
print("All animals : ", animals)
print('fish' in animals)
print(len(animals))

print()

print("All animals : ", animals)
animals.add('cat')
print(len(animals))
animals.remove('cat')

print(len(animals))
print("All animals : ", animals)


# loop over set
print('------------------------------------------')

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))


# set comprehensions
print('------------------------------------------')

from math import sqrt
nums = {sqrt(x) for x in range(30)}
print(nums)
print(len(nums))

nums_int = {int(sqrt(x)) for x in range(30)}
print(nums_int)
print(len(nums_int))
