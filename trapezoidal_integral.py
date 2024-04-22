import math
from math import sin,pi
#(1)
def f(x):
    return sin(x)

#(2)
def g(x):
    return 4/(1+x**2)

#(3)
def h(x):
    return math.pi**(0.5)*math.exp(-x**2)

def trapezoidal_integral(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range (1,n+1):
        s += h/2*(f(a+(i-1)*h)+f(a+i*h))
        return s
    
probrem1 = trapezoidal_integral(f,0,2,100)
probrem2 = trapezoidal_integral(g,0,1,100)
probrem3 = trapezoidal_integral(h,-100,100,1000)

print((1),probrem1)
print((2),probrem2)
print((3),probrem3)