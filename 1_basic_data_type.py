# int
print('------------------------------------------')
x = 3

print(type(x))
print(x)

print(x + 1)
print(x - 1)
print(x * 2)
print(x ** 2)

x += 10
print(x)

x *= 2
print(x)


# float
y = 3.0
print(type(y))
print(y)
print(y, y + 1, y * 2, y ** 2)


# booleans
print('------------------------------------------')

t = True
f = False

print(type(t))  # bool
print(t and f)  # False
print(t or f)   # True
print(not t)    # False
print(t != f)   # True


# Strings
print('------------------------------------------')

hello = 'hello'
world = 'world'
print(hello)
print(len(hello))
print(type(hello))

hw = hello + ' ' + world
print(hw)
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)

s = 'hello'
print(s.capitalize())           # Hello
print(s.upper())                # HELLO
print(s.rjust(7))               # '  hello'
print(s.center(7))              # ' hello '
print(s.center(11))             # '   hello   '
print(s.replace('l', '(ell)'))  # 'he(ell)(ell)o'
print(' world'.strip())         # world

if 3.0 == 3:
    print('equals')
