from sympy import *

def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res
def derivar(f,n=1):
    df = sympify(f)
    aux = df
    i = 0
    while i<n:
        df = Derivative(aux).doit()
        aux = df
        i+=1
    return aux

def nR(x,tol,f):
    deriv = derivar(f,1)
    h = fx(f,x) / fx(deriv,x)
    while abs(h) >= 0.0001:
        h = h = fx(f,x) / fx(deriv,x)
        x = x - h
    return x
