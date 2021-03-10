from sympy import *
import numpy
mat=[]
def printMat(mat):
    strMat=""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
                print("%.12f"%mat[i][j],end="       ")
                strMat+= str("%.12f"%mat[j][i])+"       "
        strMat+="\n"
        print()
    return strMat
def div(x,fx,it,dfx):
    global mat
    fxN = []
    for i in range(0,len(fx)-1):
        if i+it < len(x):
            if x[i+it] is x[i]:
                fxN.append(dfx[i])
            else:
                fxN.append( (fx[i+1] - fx[i])/(x[i+it] - x[i]) )
        #print(i,i+it)
    print(fxN)
    mat.append(fxN)
    return fxN

def HermiteAl(x,fx,dfx):
    global mat
    mat = []
    c = 1
    aN = [fx[0]]
    while len(fx) > 1:
        print("Diferencia dividida #",c)
        fx = div(x,fx,c,dfx)
        aN.append(fx[0])
        c+=1
    print("A= ",aN)
    print()
    expresion = 1
    sumaExp = aN[0]
    xi = symbols("x")
    for i in range(1,len(x)):
        expresion*=aN[i]
        for j in range(i):
            expresion*=(xi-x[j])
        sumaExp+=expresion
        expresion=1
    print("Polinomio progresivo: ",sumaExp.expand())
    SMatriz = printMat(mat)
    punto = 30
    print("P(",punto,")", sumaExp.subs(xi,punto))
    print(aN[len(aN)-2])

#x = [0.2500,0.2500,0.3750,0.3750,0.5000,0.5000,0,0,0.1250,0.1250]
#x = [0,0,0.1250,0.1250,0.2500,0.2500,0.3750,0.3750,0.5000,0.5000]
#x = [0.1250,0.1250,0.2500,0.2500,0.3750,0.3750,0.5000,0.5000,0,0]
#x = [20,25,40,50,55,60]

#fx = [7.7880,7.7880,4.8599,4.8599,0.0000,0.0000,0,0,6.2402,6.2402]
#fx = [0,0,6.2402,6.2402,7.7880,7.7880,4.8599,4.8599,0.0000,0.0000]
#fx = [6.2402,6.2402,7.7880,7.7880,4.8599,4.8599,0.0000,0.0000,0,0]
#fx = [18,50,33,48,80,60]
#dfx = [7.589,7.589,-8.953,-8.953,-5.785,-5.785,-3.765,-3.765,6.2326,6.2326]
#dfx = [-8.953,-8.953,-5.785,-5.785,-3.765,-3.765,6.2326,6.2326,7.589,7.589]
#dfx = [0.219,0.789,-0.215,2.125,-2.97,1.105]


#mat = HermiteAl(x,fx,dfx)
#string=printMat(mat)
#print()
#print()
#print(string)
