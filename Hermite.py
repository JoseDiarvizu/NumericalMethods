from sympy import *
from sympy.plotting import plot

def evaluar(exp):
    x = symbols('x')
    res = sympify(exp)
    return res

import math
def construir(fx,x):
    prodL = 1
    prodC = 1
    ld = []
    lc = []
    expresion = " "
    xi = symbols('x')
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
        lk.append(lc[i] / ld[i])
    px = []
    '''
    suma = 0
    for i in range(len(fx)):
        eval = fx[i] * lk[i]
        px.append(eval)
        suma+=eval
    '''
    return lk

def Hermite(x,fx,dfx):
    hcirString=""
    lkString=""
    hString=""
    lk = construir(fx,x)
    h=[]
    hCircunflejo = []
    xk = symbols('x')
    for i in range(len(x)):
        h.append( ( 1-(2*(xk -x[i]))*(Derivative(lk[i]).doit().subs("x",x[i])) ) * lk[i]**2)
        hCircunflejo.append( (xk-x[i])*(lk[i])**2 )

    print("---------LK---------")
    for i in range(len(lk)):
        pprint(lk[i].expand())
        lkString+= str(lk[i].expand())+"\n"

    print("---------H---------")
    for i in range(len(h)):
        pprint(h[i].expand())
        hString += str(h[i].expand())+"\n"
    print("---------HCircunflejo---------")
    for i in range(len(hCircunflejo)):
        pprint(hCircunflejo[i].expand())
        hcirString+= str(hCircunflejo[i].expand())+"\n"

    print("---------POLINOMIO---------")
    polinomio = 0
    for i in range(len(x)):
        polinomio+= (fx[i] * h[i]) + (dfx[i]*hCircunflejo[i])
    pprint(polinomio.expand())
    punto = 7.5
    print("P(",punto,"): ",polinomio.subs("x",punto))
    return lkString,hString,hcirString,polinomio
#MAIN


'''
x = [0,4,8,12,16,20,24]
fx = [1.7923,1.5676,1.3874,1.2396,1.1168,1.0105,0.9186]
dfx = [-0.0156,-0.0958,-0.1015,-0.0632,-.0456,-.0323,-.0308]
lk,h,hc,polinomio=Hermite(x,fx,dfx)

print("Lk",lk)
print("h",h)
print("hc",hc)
print("polinomio",polinomio)
'''




