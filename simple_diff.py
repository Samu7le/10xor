# first grade derivate
# compute the derivation of sigle variable function (Calculus I) in python


# lim  (f(x) + f(h+x)) / h
# h-> inf

def f(x):
    return x

# high order function
def der(func, arg):
    h=1e-8
    return round((func(arg + h) - func(arg)) / h)

#test

res = der(f, 2)
print(res)
