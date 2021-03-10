import math
from sympy import *
def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res
def construir(fx,x):
    xi=symbols('x')
    prodL = 1
    prodC = 1
    ld = []
    lc = []
    expresion = " "
    for i in range(len(x)):
        for j in range(len(x)):
            if i is not j:
                prodL *= (x[i] - x[j])
                prodC *= (xi - x[j])
        ld.append(prodL)
        lc.append(prodC)
        prodL = 1
        prodC = 1
    lk = []
    for i in range(len(lc)):
        lk.append((lc[i] / ld[i]).expand())
    px = []
    suma = 0
    for i in range(len(fx)):
        eval = fx[i] * lk[i]
        px.append(eval)
        suma+=eval
    return suma,lk

def f(x):
    aux = []
    for i in range( len( x ) ):
        aux.append(math.cos(x[i]))
    return aux

''''
#MAIN
x = [0,4,8,12,16,20,24]

#print("x: ",x)
fx = [1.7923,1.5676,1.3874,1.2396,1.1168,1.0105,0.9186]
#print("cos x : ",fx)
l,lk = construir(fx,x)
print("Lk = ", lk)
print("P(0.22) = ")
pprint(l.expand())
'''



