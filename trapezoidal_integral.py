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

#引数のデフォルト値を設定しました。

def trapezoidal_integral(f,a=0,b=1,n=100):
    s = 0
    h = (b-a)/n

#　for文のところのインデントの数を修正しました。
    for i in range (1,n+1):
        s += h/2*(f(a+(i-1)*h)+f(a+i*h))
    return s

# 4/25 (1)の分割数を50にしました。
probrem1 = trapezoidal_integral(f,0,pi/2,50)
probrem2 = trapezoidal_integral(g,0,1,100)
probrem3 = trapezoidal_integral(h,-100,100,1000)

print((1),probrem1)
print((2),probrem2)
print((3),probrem3)