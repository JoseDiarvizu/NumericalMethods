from sympy import *
def fx(exp, ti,wi):
    y = symbols('y')
    t = symbols('t')
    res1 = sympify(exp).subs(t, ti)
    res = sympify(res1).subs(y, wi).evalf()
    return res

def euler(ed,wi,ti,h,b):
    i=0
    l=[]
    li=[]
    li.append(i)
    li.append(ti)
    li.append(wi)
    li.append(fx(ed, ti, wi))
    l.append(li)
    print("i","   ti      ","wi      ","f(ti,wi)")
    print(i, "%.6f"%ti,"%.6f"% wi, "%.6f"%fx(ed, ti, wi))
    while(ti<=b):
        li = []
        i+=1
        wiN = wi + (h * fx(ed, ti, wi))
        tiAux = ti+h
        print(i,"%.6f"%tiAux, "%.6f"%wiN,"%.6f"%fx(ed, tiAux, wiN) )
        li.append(i)
        li.append(tiAux)
        li.append(wiN)
        li.append(fx(ed, tiAux, wiN))
        wi = wiN
        ti += h
        l.append(li)
    return l

def eulermodificado(f,wi,ti,h,b):
    i=0
    l = []
    while(ti<=b):
        li=[]
        li.append(i)
        li.append(ti)
        li.append(wi)
        li.append(fx(f,ti,wi))
        print("i",i,"TI",ti, "WI",wi,"FX",fx(f,ti,wi))
        wiN = wi + (h/2) * (fx(f,ti,wi)+ fx(f,ti, wi + h*fx(f,ti,wi) ) )
        ti+=h
        wi = wiN
        i+=1
        l.append(li)
    return l

def heun(f,wi,ti,h,b):
    i=0
    l=[]
    while(ti<=b):
        li=[]
        li.append(i)
        li.append(ti)
        li.append(wi)
        li.append(fx(f,ti,wi))
        print("TI",ti, "WI",wi,"FX",fx(f,ti,wi))
        wiN = wi + (h/4) * (fx(f,ti,wi)+ 3*fx(f,ti, wi + (2/3)*h*fx(f,ti,wi) ) )
        ti+=h
        wi = wiN
        i+=1
        l.append(li)
    return l

def puntomedioED(f,wi,ti,h,b):
    i=0
    l=[]
    while(ti<=b):
        li=[]
        li.append(i)
        li.append(ti)
        li.append(wi)
        li.append(fx(f,ti,wi))
        print("TI",ti, "WI",wi,"FX",fx(f,ti,wi))
        wiN = wi + h * fx( f,ti,wi+(h/2)*fx(f,ti,wi))
        ti+=h
        wi = wiN
        i+=1
        l.append(li)
    return l

def rungekutta(f,wi,ti,h,b):
    i=0
    l=[]
    while(ti<=b):
        li=[]
        li.append(i)
        li.append(ti)
        li.append(wi)
        li.append(fx(f,ti,wi))
        print("TI",ti, "WI",wi,"FX",fx(f,ti,wi))
        k1 = h*fx(f,ti,wi)
        k2 = h*fx(f,ti,wi+(1/2)*k1)
        k3 = h*fx(f,ti,wi+(1/2)*k2)
        k4 = h*fx(f,ti,wi+k3)
        wiN = wi + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        ti+=h
        wi = wiN
        i+=1
        l.append(li)
    return l

'''
Codigos prueba e inputs prueba

wi = 8
ti = 0
b=600
h = 20
f = "-0.006*((64.2)**(1/2))*(y**(1/2)/(y**(2) ))"
print(eulermodificado(f,wi,ti,h,b))



ti = 1
wi = -1
h = 0.05
b=2
ed = input()
res =  euler(ed,wi,ti,h,b)
print(euler(ed,wi,ti,h,b))
print(len(res))

ti = 1
wi = -1
h = 0.05
b=2
ed = input()
print(euler(ed,wi,ti,h,b))


x=[]
fx=[]
x.append(l[10][1])
x.append(l[11][1])
fx.append(l[10][2])
fx.append(l[11][2])
suma,lk=construir(fx,x)
xi = symbols("x")
punto = 0
print("i)",suma.subs(xi,punto))
x=[]
fx=[]
x.append(l[11][1])
x.append(l[12][1])
fx.append(l[11][2])
fx.append(l[12][2])
suma,lk=construir(fx,x)
xi = symbols("x")
punto = 1.55
print("ii)",suma.subs(xi,punto))
x=[]
fx=[]
x.append(l[19][1])
x.append(l[20][1])
fx.append(l[19][2])
fx.append(l[20][2])
suma,lk=construir(fx,x)
xi = symbols("x")
punto = 1.978
print("iii)",suma.subs(xi,punto))
print(l)
'''