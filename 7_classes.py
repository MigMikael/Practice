class Greeter(object):

    # constructor
    def __init__(self, name, last_name=None):
        self.name = name    # instance variable
        self.last_name = last_name

    # instance method
    def greet(self, loud=False):
        if self.last_name is not None :
            full_name = self.name + ' ' + self.last_name
        else:
            full_name = self.name

        if loud:
            print('HELLO, %s!' % full_name)
        else:
            print('Hello, %s' % full_name)


g = Greeter('Mig')
g.greet()
g.greet(True)
g.greet(loud=True)
print(type(g.last_name))

g2 = Greeter('Mig', 'Mikael')
g2.greet()
print(g2.last_name)
