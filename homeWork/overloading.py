# Overloading

from multipledispatch import dispatch


@dispatch(str, str)
def summary(first, second):
    result = first + second
    print(result)


@dispatch(int, int, int)
def summary(first, second, third):  
    result = first + second + third
    print(result)


@dispatch(float, float, float)
def summary(first, second, third):
    result = first + second + third
    print(result)


summary("Papaya ", "Orange")
summary(10, 333, 212)
summary(42.32, 23.14, 22.43)
