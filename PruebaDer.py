from Bisección import Bi
import math
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
def fx(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a).evalf()
    return res
def trapecio(f,a,b):
    print("--------------------TRAPECIO--------------------")
    pc = []
    ddf = derivar(f,2)
    pprint(ddf)
    dddf = derivar(ddf,1)
    pprint(dddf)
    raiz = Bi(1.7,2.5,dddf)
    pc.append(a)
    pc.append(b)
    pc.append(raiz)
    max = -999999
    for i in range(len(pc)):
        if(abs(fx(ddf,pc[i])) > max):
            max = fx(ddf,pc[i])
    print("MAXIMO: ",max)
    h = sqrt( (12*10**-4) / (max*(b-a)) )
    print("H: ",h)
    n = (b-a)/h
    print("N: ",ceiling(n))
    suma=0
    for i in range(0,int(n)+1):
        xi=a+i*h
        fi = fx(f,xi)
        suma += fi
    suma = suma *2
    integral = (h/2) * ( fx(f,a) + suma + fx(f,b))
    print("Integral: ",integral)

def simpson(f,a,b):
    print("--------------------SIMPSON--------------------")
    pc = []
    ddf = derivar(f, 4)
    pprint(ddf)
    dddf = derivar(ddf, 1)
    pprint(dddf)
    raiz = Bi(1.7, 2.5, dddf,0.00001)
    pc.append(a)
    pc.append(b)
    pc.append(raiz)
    max = -999999
    for i in range(len(pc)):
        if (abs(fx(ddf, pc[i])) > max):
            max = fx(ddf, pc[i])
    print("MAXIMO: ", max)
    h = pow( ((180*10**-4) / (max*(b-a)) ),1/4)
    print("H: ",h)
    n = (b - a) / h
    print("N: ", ceiling(n))
    suma = 0
    xi=[]

    for i in range(0,int(n),2):
        suma+=fx(f,a+i*h)
        #print(fx(f,a+i*h))
    print()
    suma = suma * 4
    suma2 = 0
    for i in range(1,int(n)+1,2):
        suma2+=fx(f,a+i*h)
        #print(fx(f,a+i*h))
    suma2 = suma2 * 2

    #print(suma)
    #print(suma2)
    integral = (h/3) * (fx(f,a) + suma + suma2 +fx(f,b))
    print("Integral: ",integral)
def pm(f,a,b):
    print("--------------------PM--------------------")
    pc = []
    ddf = derivar(f, 2)
    pprint(ddf)
    dddf = derivar(ddf, 1)
    pprint(dddf)
    raiz = Bi(1.7, 2.5, dddf)
    pc.append(a)
    pc.append(b)
    pc.append(raiz)
    max = -999999
    for i in range(len(pc)):
        if (abs(fx(ddf, pc[i])) > max):
            max = fx(ddf, pc[i])
    print("MAXIMO: ", max)
    h = pow(((6 * 10 ** -4) / (max * (b - a))), 1 / 2)
    print("H: ", h)
    n = ((b - a) / h) - 2
    print("N: ", ceiling(n))
    suma=0

    for i in range(1,(n//2)+2):
        suma += fx(f,a+(2*i+1)*h)
    integral = 2*h*suma
    print(integral)

func = input("Ingrese su función: ")
print("Ingrese sus límites")
a = 0
b = 30

simpson(func,a,b)

'''
from sympy import *
def evaluar(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a).evalf()
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
f="-2.02236319728905e-5*x**9 + 0.0010405902303646*x**8 - 0.0218756663126469*x**7 + 0.243041247850591*x**6 - 1.53829559927041*x**5 + 5.5081205113346*x**4 - 10.0953089386401*x**3 + 7.16190803747486*x**2 + 75.0*x"
f=derivar(f,1)
print(f)
print(evaluar(f,7))
'''

