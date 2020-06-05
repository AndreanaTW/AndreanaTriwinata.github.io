import math

def f(x):
    function = (x*x*x) - (2*x) - 1
    return function

def derivative(x): 
    h = 0.000001
    derivative = (f(x + h) - f(x)) / h
    return derivative
 
def newton_raphson(x):
    return (x - (f(x) / derivative(x)))
 



def iterate(p, n):
    x = p
    for i in range(n):
        x = newton_raphson(x)
        print( x)         
    return ("")
       

print(iterate(1, 10))
