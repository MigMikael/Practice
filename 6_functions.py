def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(sign(x))


# define functions to take optional keyword arguments
def hello(name, loud=False):
    if loud:
        print("HELLO, %s!" % name.upper())
    else:
        print("Hello, %s" % name)


hello('Bob')
hello('Fred', True)         # you can call function like this
hello('Mig', loud=True)     # or like this
