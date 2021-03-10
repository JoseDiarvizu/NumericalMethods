from sympy import*
import math
def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res

def FP(p0, p1, TOL,f):
    i = 0
    if (fx(f,p0) * fx(f,p1)>=0):
        return "Revise su intervalo"
    pn = p1 - (fx(f,p1) * (p1 - p0)) / (fx(f,p1) - fx(f,p0))
    if (fx(f,p1) * fx(f,pn) < 0):
        p0 = pn
        p = p0
    else:
        p1 = pn
        p = p1
    pn = p1 - (fx(f,p1) * (p1 - p0)) / (fx(f,p1) - fx(f,p0))
    while ((abs(pn - p) / abs(pn)) > TOL and i < 10):
        print("pn: ",pn," p1: ",p0," p2: ",p1, " Error: ", abs(pn - p) / abs(pn))
        if (fx(f,p1) * fx(f,pn) < 0):
            p0 = pn
            p = p0
        else:
            p1 = pn
            p = p1
        pn = p1 - (fx(f,p1) * (p1 - p0)) / (fx(f,p1) - fx(f,p0))
        i += 1
    print("pn: ", pn, " p1: ", p0, " p2: ", p1, " Error: ", abs(pn - p) / abs(pn))
    print("Raíz: ",pn)
    return pn

