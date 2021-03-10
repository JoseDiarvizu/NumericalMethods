from sympy.plotting import plot
from sympy import *
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
def div(x,fx,it):
    global mat
    fxN = []
    for i in range(0,len(fx)-1):
        if i+it < len(x):
            fxN.append( (fx[i+1] - fx[i])/(x[i+it] - x[i]) )
        #print(i,i+it)
    print(fxN)
    mat.append(fxN)
    return fxN

def difDiv(x,fx):
    global mat
    mat = []
    print()
    fxNuevo = 2
    c = 1
    aN = [fx[0]]
    while len(fx) > 1:
        print("Diferencia dividida #",c)
        fx = div(x,fx,c)
        aN.append(fx[0])
        c+=1
    #print("A= ",aN)
    print()
    expresion = 1
    sumaExp = aN[0]
    xi = symbols("x")
    for i in range(1,len(aN)):
        expresion*=aN[i]
        for j in range(i):
            expresion*=(xi-x[j])
        sumaExp+=expresion
        expresion=1
    print("Polinomio progresivo: ")
    pprint(sumaExp.expand())
    strMat = printMat(mat)
    return sumaExp,strMat

x = [0,1,2,3]
fx = [1,0,1,10]
'''
punto = 0.5
print("P(7.5)", sumaExp.subs(xi,punto))
'''