from sympy import *
def derivar(f,n=1):
    df = sympify(f)
    aux = df
    i = 0
    while i<n:
        df = Derivative(aux).doit()
        aux = df
        i+=1
    return aux
def f(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res

def n1(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 1
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("x= ", x)
    print(h)
    expresion = (h/2)*( f(p,x[0]) + f(p,x[1]))
    print("Integral= ", expresion)
    d = f(derivar(p, 2), 1)
    error = ((h ** 3) / 12) * d
    print("Error", error)
    return expresion

def n2(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 2
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("x= ", x)
    print(h)
    expresion = (h / 3) * (f(p, x[0]) + 4*f(p, x[1]) + f(p,x[2]))
    print("Integral= ", expresion)
    d = f(derivar(p, 4), 1)
    error = ((h ** 5) / 90) * d
    print("Error", error)
    return expresion

def n3(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 3
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("x= ", x)
    print(h)
    expresion = ((3*h)/ 8) * (f(p, x[0]) + 3 * f(p, x[1]) + 3*f(p, x[2]) + f(p, x[3]))
    print("Integral= ", expresion)
    d = f(derivar(p, 4), 1)
    error = ((3*h ** 5) / 80) * d
    print("Error", error)
    return expresion

def n4(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 4
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("x= ", x)
    print(h)
    expresion = ((2*h/45))*( 7*f(p,x[0]) + 32*f(p,x[1]) + 12*f(p,x[2]) + 32*f(p,x[3]) + 7*f(p,x[4])) #- ((8*h**7)/945) * 720
    print("Integral= ", expresion)
    d= f(derivar(p,6),1)
    error = ((8 * h ** 7) / 945)*d
    print("Error", error)
    return expresion

def PMedioN0(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 2
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("X= ", x)
    print("H= ",h)
    expresion = (2*h)*f(p,x[0]+h)
    print("Integral= ", expresion)
    d = f(derivar(p, 2), 1)
    error = ((h ** 3) / 3) * d
    print("Error", error)
    return expresion

def PMedioN1(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 3
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("X= ", x)
    print("H= ",h)
    expresion = ((3*h)/2)*(f(p,x[1]) + f(p,x[2]))
    print("Integral= ", expresion)
    d = f(derivar(p, 2), 1)
    error = ((3*h ** 3) / 4) * d
    print("Error", error)
    return expresion

def PMedioN2(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 4
    while n != x1:
        x.append(n)
        n += h
    x.append(n)
    print("X= ", x)
    print("H= ",h)
    expresion = ((4*h)/3)*(2*f(p,x[1]) - f(p,x[2]) + 2*f(p,x[3]))
    print("Integral= ", expresion)
    d = f(derivar(p, 4), 1)
    error = ((14*h ** 5) / 45) * d
    print("Error", error)
    return expresion

def PMedioN3(p,x0,x1):
    x = []
    n = x0
    h = (x1 - x0) / 5
    while n < x1:
        x.append(n)
        n += h
    x.append(n)
    print("X= ", x)
    print("H= ", h)
    expresion = ((5*h)/24)*(11*f(p,x[1]) + f(p,x[2]) + f(p,x[3]) + 11*f(p,x[4]))
    print("Integral= ", expresion)
    d = f(derivar(p, 4), 1)
    error = ((95*h ** 5) / 144) * d
    print("Error", error)
    return expresion

#Main
'''
pol=input("Deme su funcion: ")
print("******INTEGRAL DE 1 A 5.5:******")
print("--------------N1------------")
P1_1= n1(pol,1,5.5)
print("--------------N2------------")
P1_2=n2(pol,1,5.5)
print("--------------N3------------")
P1_3 = n3(pol,1,5.5)
print("--------------N4------------")
P1_4=n4(pol,1,5.5)

print("******INTEGRAL DE 5.5 A 10:******")
print("--------------N1------------")
P2_1=n1(pol,5.5,10)
print("--------------N2------------")
P2_2=n2(pol,5.5,10)
print("--------------N3------------")
P2_3=n3(pol,5.5,10)
print("--------------N4------------")
P2_4=n4(pol,5.5,10)

print("SUMA DE INTEGRALES: ")
print("--------------N1------------")
print(P1_1+P2_1)
print("--------------N2------------")
print(P1_2+P2_2)
print("--------------N3------------")
print(P1_3+P2_3)
print("--------------N4------------")
print(P1_4+P2_4)


print()
print("Newton Cotes: ")

print("******INTEGRAL DE 1 A 5.5:******")
print("--------------N0------------")
M1_1 = PMedioN0(pol,1,5.5)
print("--------------N1------------")
M1_2 =PMedioN1(pol,1,5.5)
print("--------------N2------------")
M1_3 =PMedioN2(pol,1,5.5)
print("--------------N3------------")
M1_4 =PMedioN3(pol,1,5.5)

print("******INTEGRAL DE 5.5 A 10:******")
print("--------------N0------------")
M2_1 = PMedioN0(pol,5.5,10)
print("--------------N1------------")
M2_2 =PMedioN1(pol,5.5,10)
print("--------------N2------------")
M2_3 =PMedioN2(pol,5.5,10)
print("--------------N3------------")
M2_4 =PMedioN3(pol,5.5,10)

print("SUMA DE INTEGRALES: ")
print("--------------N0------------")
print(M1_1+M2_1)
print("--------------N1------------")
print(M1_2+M2_2)
print("--------------N2------------")
print(M1_3+M2_3)
print("--------------N3------------")
print(M1_4+M2_4)
'''