import cmath
import math
cadenaMul=""
def f(cf,n,x):
    suma = 0
    for i in range(n):
        suma+=cf[i]*pow(x,n-i)
    suma+=cf[n]
    return suma

def a(x0,x1,x2,cf,n):
    return ( (x1 - x2) * (f(cf,n,x0) - f(cf,n,x2)) - (x0-x2) * (f(cf,n,x1) - f(cf,n,x2)) ) / ( (x0-x2) * (x1-x2) * (x0-x1))
def b(x0,x1,x2,cf,n):
    return ( pow((x0 - x2),2) * (f(cf,n,x1) - f(cf,n,x2)) - pow((x1-x2),2) * (f(cf,n,x0) - f(cf,n,x2)) ) / ( (x0-x2) * (x1-x2) * (x0-x1))
def c(x2,cf,n):
    return f(cf,n,x2)
def error(x3,x2):
    return (abs(x3-x2)/abs(x3))
def horner(cf,n,x3):
    aux = []
    aux.append(cf[0])
    for i in range(1,n):
        aux.append(x3*aux[i-1]+cf[i])
    return aux
def Muller(x0,x1,x2,cf,n,TOL):
    x3 = 0
    e = 1
    while(e>TOL):
        A = a(x0, x1, x2,cf,n)
        B = b(x0, x1, x2,cf,n)
        C = c(x2,cf,n)
        discriminante = cmath.sqrt( pow(B,2) - (4*A*C) )
        x3 = x2 - (2*C)/(B+(B/abs(B))*discriminante)
        x0 = x1
        x1 = x2
        x2 = x3
        e = error(x2, x1)
       # print(e)
    cf=horner(cf,n,x3)
    return x3,cf
def chicharronera(a,b,c):
    global cadenaMul
    raiz1 = (-b+cmath.sqrt((b*b) - (4*a*c)))/(2*a)
    raiz2 = (-b - cmath.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("X1 es: ",raiz1)
    print("X2 es: ", raiz2)
    cadenaMul+="X1 es: "+str(raiz1)+"\n"
    cadenaMul += "X2 es: " + str(raiz2) + "\n"
def MullerMain(n,cf,xs,TOL):
    global cadenaMul
    cadenaMul=""
    c1=0
    c2=1
    c3=2
    while(len(cf)-1 > 2):
       #print(xs[c1][0],xs[c1][1],xs[c1][2])
       x3 , cf = Muller(xs[c1], xs[c2], xs[c3], cf, n,TOL)
       c1+=3
       c2+=3
       c3+=3
       print("Raiz = ",x3)
       cadenaMul+="Raiz = "+str(x3)+"\n"
       n-=1
    chicharronera(cf[0],cf[1],cf[2])
    return cadenaMul
'''
n=5
x=[1,2,3,1,2,3,1,2,3]
coef=[1,2,3,4,5,6]
MullerMain(n,coef,x)
#xi=[[None]*3]*(n-2)
'''