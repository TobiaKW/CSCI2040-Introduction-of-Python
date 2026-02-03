import math
from functools import reduce
def map_func1(x): return 1.5*x

def nigga(b):
    global a
    a=10
    print(a,b)


a =(1.0,2.0,3.0,4.0)
print([x*x for x in a if x*x>5])
print(reduce(lambda x,y: int(x**y), range(2,5)))
print(a)

b = ['A','B','C','D','E']
print(type(a))


dict1 = {x: y for x, y in zip(b, a)}
print(dict1)

