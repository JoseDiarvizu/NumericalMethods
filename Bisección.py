import math
from sympy import*
import sympy as sp

def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res

def Bi(a, b,f,tol):
    if (fx(f,a) * fx(f,b) >= 0):
        return "Revise su intervalo"

    c = a
    while ((b - a) >= tol):
        c = (a + b) / 2
        if (fx(f,c) == 0.0):
            break
        if (fx(f,c) * fx(f,a) < 0):
            b = c
        else:
            a = c

    return c