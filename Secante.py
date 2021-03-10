import math
from sympy import*

def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res

def Secante(x1, x2, E,f):
    xm = 0;
    x0 = 0;
    c = 0;
    if (fx(f,x1) * fx(f,x2) < 0):
        while True:

            x0 = ((x1 * fx(f,x2) - x2 * fx(f,x1)) /
                  (fx(f,x2) - fx(f,x1)));
            c = fx(f,x1) * fx(f,x0);
            x1 = x2;
            x2 = x0;
            if (c == 0):
                break;
            xm = ((x1 * fx(f,x2) - x2 * fx(f,x1)) /
                  (fx(f,x2) - fx(f,x1)));
            if (abs(xm - x0) < E):
                break;

        return x0

    else:
        return "Revise su intervalo"
