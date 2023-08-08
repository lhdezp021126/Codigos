
from Decorrator import decorator;
l=[ i for i in range(1,100) if i%2==0];

print(l);

map={key:value for key,value in enumerate(l)};


@decorator
def print2():
    print(map);

print2();