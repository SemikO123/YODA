from math import *
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    y = sin(x)
    return y
def g(x):
    y = x**4
    return y

def fi(f,x, Eps = 1e-8):
    y = (f(x+Eps)-f(x))/Eps
    
    return y

def fi2(fi,x,Eps = 1e-5):
    y = (fi(f,x+Eps)-fi(f,x))/Eps
    return y



def Graf(a=-10,b=10,step=2):
    x = np.arange(a,b+0.01,0.001)
    y = [f(i) for i in x]
    plt.plot(x,y)
    plt.grid(True)
    minY = min(y)
    maxY = max(y)
    plt.axis([a-(b-a)*0.05,b+(b-a)*0.05,
              minY-(maxY-minY)*0.05,maxY+(maxY-minY)*0.05])
    if abs(a-b)/step < 20:
        plt.xticks(np.arange(a,b+1e-9,step))
    plt.show()

x = 0.001
print(f(x))
print(fi(f,x))
print(fi2(fi,x))


Graf()
