import math as np

def f(x):
    return (x/3)**2 - np.sin(x) - 3
def g(x):
    return (2/9)*x - np.cos(x)

x=np.zeros(20)
x[0]=10

for n in range(20):
    x[n+1]=x[n]-f(x[n])/g(x[n])
    print(x[n],'\t',f(x[n]))
