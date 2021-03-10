import math
from sympy import *
import scipy.integrate as spi
import numpy as np
def fxE(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a).evalf()
    return res

def trapecio(f, a, b, n=1000):
    h = (b-a)/float(n)
    s = 0.5*(fxE(f,a) + fxE(f,b))
    for i in range(1,n,1):
        s = s + fxE(f,a + i*h)
    return h*s


# Function for approximate integral
def simpson(f,a, b, n=100):
    h = (b - a) / n
    x = list()
    fx = list()
    i = 0
    while i <= n:
        x.append(a + i * h)
        fx.append(fxE(f,x[i]))
        i += 1

    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res


def mean(a, b):
    meanValue = (a + b) / 2
    return meanValue

def puntomedio(f,a,b,n=100):
    deltaX = (b - a) / n

    xValue = [a]
    heightValue = []

    for i in range(0, n):
        xValue.append(a + deltaX)
        deltaX = deltaX + (b - a) / n

    for i in xValue:
        heightValue.append(fxE(f,mean(i, i + (b - a) / n)))
    del heightValue[-1]

    the_sum = sum(heightValue)
    definite_integral = the_sum * ((b - a) / n)

    return definite_integral

print(simpson("(250*x/(6+x**2))*E**(-x/10)",0,30))