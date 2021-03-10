import cmath
cadena=""
def chicharronera(a,b,c):
    global cadena
    raiz1 = (-b+cmath.sqrt((b*b) - (4*a*c)))/(2*a)
    raiz2 = (-b - cmath.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("X1 es: ",raiz1)
    print("X2 es: ", raiz2)
    cadena+=str("X1 es: "+ str(raiz1)+"\n")
    cadena+=str("X2 es: "+ str(raiz2)+"\n")
def newton(a,x0,n,TOL):
    global cadena
    tol = 1
    print("Coeficientes del polinomio: ",a,"Grado: ",n-1)
    cadena+=str("Coeficientes del polinomio: de grado "+str(n-1)+"\n"+" "+str(a))+"\n"

    while(tol>TOL):
        b=[]
        c=[]
        b.append(a[0])
        c.append(a[0])
        for i in range(1, n):
            b.append(a[i] + x0 * b[i - 1])
            c.append(b[i] + x0 * c[i - 1])
        pn = x0 - (b[n-1]/c[n-2])
        tol = abs(pn-x0) /abs(pn)
        x0 = pn
    print("\nRaiz: ",x0)
    cadena+=str("Raiz: "+str(x0)+"\n")
    b.pop()
    return b;
def Horner(n, a, x0,TOL):
    global cadena
    cadena = ""
    while(n>3):
        a = newton(a,x0,n,TOL)
        n-=1
        #print(a,n)
    print("Coeficientes del polinomio: ",a,"Grado: ",n-1)
    cadena+=str("Coeficientes del polinomio: de grado "+str(n-1)+"\n"+" "+str(a))+"\n"
    chicharronera(a[0],a[1],a[2])
    return cadena
'''
a=[1,2,3,4]
Horner(4,a,1.5)
print("_________")
print(cadena)
'''