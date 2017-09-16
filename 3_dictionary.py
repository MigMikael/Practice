# dictionaries
# A dictionary stores (key, value) pairs, similar to a Map in Java or an object in Javascript.

print('------------------------------------------')

d = {
    'cat': 'cute',
    'dog': 'furry'
}

print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])

print()

print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
del d['fish']
print(d.get('fish', 'N/A'))


# loop to dictionaries
print('------------------------------------------')

d = {
    'person': 2,
    'cat': 4,
    'spider': 8
}

for animal in d:
    legs = d[animal]
    print('A %s has %d legs.' % (animal, legs))

print()

for animal, legs in d.items():
    print('A %s has %d legs.' % (animal, legs))


# Dictionary comprehensions
print('------------------------------------------')

nums = [0, 1, 2, 3, 4]
num_to_square = {x: x**2 for x in nums}
print(num_to_square)

even_num_to_square = {x: x**2 for x in nums if x % 2 == 0}
print(even_num_to_square)