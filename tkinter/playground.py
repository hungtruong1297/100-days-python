from unicodedata import name


def add(*args):
    sum = 0
    for _ in args:
        sum = sum + _
    return sum

def calculate(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

class Car:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.model = kwargs.get('model')

my_car = Car(name='hehe')

print(my_car.model)

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)


def test(*args):
    print(args)
 
test(1,2,3,5)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)