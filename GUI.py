from tkinter import  *
import tkinter as tk
from tkinter import ttk
from sympy import *
from Bisección import Bi
from Secante import Secante
from PF import FP
import numpy as np
from sympy.plotting import plot
from PIL import ImageTk
import matplotlib.pyplot as plt
from NR import nR
from Horner import Horner
from InterpolacionLagrange import construir
from Hermite import Hermite
from HermiteAlternativo import HermiteAl
from DifDiv import difDiv
from Müller import MullerMain
from Neville2 import Neville
from DiferenciacionNumerica import centro, extremos, centro5, extremos5,fp
from IntegracionNumerica import n1,n2,n3,n4,PMedioN0,PMedioN1,PMedioN2,PMedioN3
from IntegracionNumericaCompuesta import trapecio, puntomedio, simpson
from Euler import euler,eulermodificado, heun,puntomedioED,rungekutta
from determinante import DeterminanteCofactor
from GaussJordan import inversaGJ, solucionGJ,solucionInversa
import tktable

#MNuméricpos
longitud=0
def calcularBiseccion():
    resultado.delete(0,len(resultado.get()))
    a = float(puntoA.get())
    b = float(puntoB.get())
    f = tf.get()
    tol = float(tolerancia.get())
    res = Bi(a,b,f,tol)
    resultado.insert(0,str(res))
def calcularPF():
    PFresultado.delete(0,len(PFresultado.get())-1)
    a = float(PFpuntoA.get())
    b = float(PFpuntoB.get())
    f = tf.get()
    tol = float(PFtolerancia.get())
    res = FP(a,b,tol,f)
    PFresultado.insert(0,str(res))
def calcularSEC():
    SECresultado.delete(0, len(SECresultado.get()) - 1)
    a = float(SECpuntoA.get())
    b = float(SECpuntoB.get())
    f = tf.get()
    tol = float(SECtolerancia.get())
    res = Secante(a, b, tol, f)
    SECresultado.insert(0, str(res))
def calcularNR():
    NRresultado.delete(0, len(NRresultado.get()) - 1)
    a = float(NRpuntoA.get())
    f = tf.get()
    tol = float(NRtolerancia.get())
    res = nR(a, tol, f)
    NRresultado.insert(0, str(res))
def calcularHOR():
    HORresultado.delete('1.0', END)
    a = convertirALista(HORCoef.get())
    n = int(HORn.get())+1
    x0 = float(HORx0.get())
    tol = float(HORtol.get())
    res = Horner(n, a, x0,tol)
    print("–––––––––——--––––––––––––––")
    print(res)
    print("–––––––––——--––––––––––––––")
    HORresultado.insert(END, str(res))

def calcularLG():
    LGresultado.delete('1.0', END)
    if LGfx.winfo_ismapped():
        x = convertirALista(LGx.get())
        fx = convertirALista(LGfx.get())
    else:
        func = tf.get()
        x = convertirALista(LGx.get())
        fx = []
        for i in range(len(x)):
            fx.append(evaluar(func, x[i]))
    p, lk = construir(fx, x)
    LGresultado.insert(END,"-------------------------------------------------Polinomio-------------------------------------------------\n " + str(p.expand()) + "\n")
    LGresultado.insert(END,"\n-----------------------------------------------------Lk-----------------------------------------------------\n " + str(lk))

    evaluacion = "P(" + str(LGpuntoEval.get()) + ") = " + str(evaluar(p, float(LGpuntoEval.get())))
    LGresultado.insert(END,
                        "\n-----------------------------------------------------EVALUACION-----------------------------------------\n " + str(
                            evaluacion) + "\n")
    xi = symbols('x')
    xx = np.linspace(-10, 10, 1000)
    yy = lambdify(xi, p)(xx)
    plt.plot(xx, np.transpose(yy))
    # plt.plot(raiz, 0, 'bo')
    plt.show()

def calcularHER():
    HERresultado.delete('1.0', END)
    if HERfx.winfo_ismapped():
        x=convertirALista(HERx.get())
        fx=convertirALista(HERfx.get())
        dfx=convertirALista(HERdfx.get())
    else:
        func = tf.get()
        x = convertirALista(HERx.get())
        fx = []
        dfx = []
        for i in range(len(x)):
            fx.append(evaluar(func,x[i]))
            dfx.append(evaluar(derivar(func,1),x[i]))
    lk,h,hcir,polinomio=Hermite(x,fx,dfx)
    HERresultado.insert(END,"-------------------------------------------------Polinomio-------------------------------------------------\n " + str(sympify(polinomio).expand())+"\n")
    HERresultado.insert(END,
                           "-----------------------------------------------------Lk-----------------------------------------------------\n " + str(
                               lk)+"\n")
    HERresultado.insert(END,
                            "-----------------------------------------------------H-----------------------------------------------------\n " + str(
                                h) + "\n")
    HERresultado.insert(END,
                            "-----------------------------------------------------HCIR--------------------------------------------------\n " + str(
                                hcir) + "\n")
    evaluacion = "P("+str(HERpuntoEval.get())+") = "+str(evaluar(polinomio,float(HERpuntoEval.get())))
    HERresultado.insert(END,
                            "-----------------------------------------------------EVALUACION-----------------------------------------\n " + str(
                                evaluacion) + "\n")
    xi = symbols('x')
    xx = np.linspace(-10, 10, 1000)
    yy = lambdify(xi, sympify(polinomio))(xx)
    plt.plot(xx, np.transpose(yy))
    # plt.plot(raiz, 0, 'bo')
    plt.show()

def calcularHERAL():
    HERALresultado.delete('1.0', END)
    if HERALfx.winfo_ismapped():
        x = convertirALista(HERALx.get())
        fx = convertirALista(HERALfx.get())
        dfx =  convertirALista(HERALdfx.get())
    else:
        func = tf.get()
        x = convertirALista(HERALx.get())
        fx = []
        dfx = []
        for i in range(len(x)):
            fx.append(evaluar(func, x[i]))
            dfx.append(evaluar(derivar(func, 1), x[i]))
    matriz,polinomio = HermiteAl(x,fx,dfx)
    HERALresultado.insert(END,
                        "-------------------------------------------------Polinomio-------------------------------------------------\n " + str(
                            sympify(polinomio).expand()) + "\n")
    HERALresultado.insert(END,
                        "-------------------------------------------------Diferencias divididas-------------------------------------------------\n"+matriz+"\n")
    evaluacion = "P(" + str(HERALpuntoEval.get()) + ") = " + str(evaluar(polinomio, float(HERALpuntoEval.get())))
    HERALresultado.insert(END,
                        "-----------------------------------------------------EVALUACION-----------------------------------------\n " + str(
                            evaluacion) + "\n")
    xi = symbols('x')
    xx = np.linspace(-10, 10, 1000)
    yy = lambdify(xi, sympify(polinomio))(xx)
    plt.plot(xx, np.transpose(yy))
    # plt.plot(raiz, 0, 'bo')
    plt.show()

def calcularDIF():
    DIFresultado.delete('1.0', END)
    if DIFfx.winfo_ismapped():
        x = convertirALista(DIFx.get())
        fx = convertirALista(DIFfx.get())
        print("x", x)
        print("fx", fx)
    else:
        func = tf.get()
        x = convertirALista(DIFx.get())
        fx = []
        for i in range(len(x)):
            fx.append(evaluar(func, x[i]))
    print("x",x)
    print("fx",fx)
    polinomio,matriz=difDiv(x,fx)
    DIFresultado.insert(END,
                          "-------------------------------------------------Polinomio-------------------------------------------------\n " + str(
                              sympify(polinomio).expand()) + "\n")
    DIFresultado.insert(END,
                          "-------------------------------------------------Diferencias divididas-------------------------------------\n" + matriz + "\n")
    evaluacion = "P(" + str(DIFpuntoEval.get()) + ") = " + str(evaluar(polinomio, float(DIFpuntoEval.get())))
    DIFresultado.insert(END,
                          "-----------------------------------------------------EVALUACION-----------------------------------------\n " + str(
                              evaluacion) + "\n")
    xi = symbols('x')
    xx = np.linspace(-10, 10, 1000)
    yy = lambdify(xi, sympify(polinomio))(xx)
    plt.plot(xx, np.transpose(yy))
    # plt.plot(raiz, 0, 'bo')
    plt.show()

def calcularMUL():
    cf = []
    DIFresultado.delete('1.0', END)
    n = int(MULn.get())
    cf = convertirALista(MULCoef.get())
    x = convertirALista(MULx0.get())
    tol = float(MULtol.get())
    res = MullerMain(n,cf,x,tol)
    MULresultado.insert(END,
                        "-------------------------------------------------Raíces-------------------------------------------------\n " +res + "\n")
def calcularNEV():
    NEVresultado.delete('1.0', END)
    if NEVfx.winfo_ismapped():
        x = convertirALista(NEVx.get())
        fx = convertirALista(NEVfx.get())
        n = int(NEVn.get())
        punto = float(NEVPunto.get())
    else:
        func = tf.get()
        x = convertirALista(NEVx.get())
        fx=[]
        fx = []
        for i in range(len(x)):
            fx.append(evaluar(func, x[i]))
        n = int(NEVn.get())
        punto = float(NEVPunto.get())
    res = Neville(x, fx, punto, n)
    NEVresultado.insert(END,
                        "-------------------------------------------------Raíz-------------------------------------------------\n " + res + "\n")
def calcularDN():
    res=""
    valor = varDifNum.get()
    DNresultado.delete(0, END)
    pos= int(DNposicion.get())
    if DNfx.winfo_ismapped():
        x = convertirALista(DNx.get())
        fx = convertirALista(DNfx.get())
    else:
        func = tf.get()
        x = convertirALista(DNx.get())
        fx = []
        for i in range(len(x)):
            fx.append(evaluar(func, x[i]))
    try:
        if valor == 1:
            res = centro(x,fx,pos)
        elif valor == 2:
            res = extremos(x,fx,pos)
        elif valor == 3:
            res = centro5(x,fx,pos)
        elif valor == 4:
            res = extremos5(x,fx,pos)
        elif valor == 5:
            res = fp(x,fx,pos)
        print("Res:",res)
    except:
        res="Revise su entrada, por favor"
    DNresultado.insert(END, str(res) + "\n")

def calcularIN():
    INresultado.delete(0,len(INresultado.get()))
    exp = tf.get()
    x0 = float(INx0.get())
    x1 = float(INx1.get())
    res=0.0
    if varIntegNum.get() == 1:
        text = str(menuIN.get())
        if text == "Grado 1":
            res = n1(exp,x0,x1)
        elif text =="Grado 2":
            res = n2(exp, x0, x1)
        elif text =="Grado 3":
            res = n3(exp, x0, x1)
        elif text == "Grado 4":
            res = n4(exp,x0,x1)
        elif text == "Punto medio (º1)":
            res = PMedioN0(exp,x0,x1)
        elif text == "Punto medio (º2)":
            res = PMedioN1(exp, x0, x1)
        elif text == "Punto medio (º3)":
            res = PMedioN2(exp, x0, x1)
        elif text == "Punto medio (º4)":
            res = PMedioN3(exp, x0, x1)
    elif varIntegNum.get() ==2:
        text = str(menuINC.get())
        if text == "Trapecio":
            res = trapecio(exp,x0,x1)
        elif text == "Simpson":
            res = simpson(exp,x0,x1)
        elif text == "Punto medio":
            res = puntomedio(exp,x0,x1)
    INresultado.insert(END,str(res))

def calcularED():
    try:
        EDlabelRes.config(text="Resultado")
        ecuacion = tf.get()
        wi = float(EDwi.get())
        ti = float(EDti.get())
        b = float(EDLimSup.get())
        h = float(EDh.get())
        text = str(menuED.get())
        if text =="Euler":
            res = euler(ecuacion,wi,ti,h,b)
        elif text == "Euler modificado":
            res = eulermodificado(ecuacion,wi,ti,h,b)
        elif text == "Heun":
            res = heun(ecuacion,wi,ti,h,b)
        elif text == "Punto medio":
            res = puntomedioED(ecuacion,wi,ti,h,b)
        elif text == "Runge Kutta":
            res = rungekutta(ecuacion,wi,ti,h,b)
    except:
        EDlabelRes.config(text = "Revise sus entradas")
    frame = tk.Frame(frameED)
    container = ttk.Frame(frame)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    tb = tktable.Table(scrollable_frame,
                       state='disabled',
                       width=50,
                       titlerows=1,
                       rows=len(res)+1,
                       cols=4,
                       colwidth=20)
    columns = ['i', 'ti', 'wi', 'f(ti,wi)']
    #### LIST OF LISTS DEFINING THE ROWS AND VALUES IN THOSE ROWS ####
    values = res
    #### SETS THE DOGS INTO THE TABLE ####
    #### VVVVVVVVVVVVVVVVVVVVVVVVVVV ####
    # DEFINING THE VAR TO USE AS DATA IN TABLE
    var = tktable.ArrayVar(scrollable_frame)
    row_count = 0
    col_count = 0
    # SETTING COLUMNS
    for col in columns:
        index = "%i,%i" % (row_count, col_count)
        var[index] = col
        col_count += 1
    row_count = 1
    col_count = 0
    # SETTING DATA IN ROWS
    for row in values:
        for item in row:
            print(item)
            index = "%i,%i" % (row_count, col_count)
            ## PLACING THE VALUE IN THE INDEX CELL POSITION ##
            var[index] = item
            #### IGNORE THIS IF YOU WANT, JUST SETTING SOME CELL COLOR ####
            try:
                if int(item) > 999:
                    tb.tag_cell('green', index)
            except:
                pass
            ###############################################################
            col_count += 1
        col_count = 0
        row_count += 1
    #### ABOVE CODE SETS THE DOG INTO THE TABLE ####
    ################################################
    #### VARIABLE PARAMETER SET BELOW ON THE 'TB' USES THE DATA DEFINED ABOVE ####
    tb['variable'] = var
    tb.pack(fill="both")
    container.pack(fill="both")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    frame.place(relx=0.10,rely=0.5,relheight=0.5,relwidth=0.75)
    root.mainloop()
def calcularID():
    n = int(IDmatSize.get())
    a = np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            a[i][j] = float(matrizID[i][j].get())
    if menuID.get()=="Matriz inversa":
        IDlabelResDet.place_forget()
        IDResDet.place_forget()
        det = DeterminanteCofactor(a)
        if det == 0.0:
            IDlabelResDet.place(relx=0.63, rely=0.3)
            IDlabelResDet.config(text="La matriz es no invertible")
            return
        res = inversaGJ(a,n)
        create_window3(res,n)
    elif menuID.get()=="Determinante":
        print(a)
        res = DeterminanteCofactor(a)
        IDResDet.delete(0,len(IDResDet.get()))
        IDlabelResDet.place(relx=0.63,rely=0.3)
        IDlabelResDet.config(text="Resultado: ",font="Verdana 14 bold")
        IDResDet.place(relx=0.77,rely=0.3,relwidth=0.1)
        IDResDet.insert(END,str(res))
def calcularSL():
    try:
        n = int(IDmatSize.get())
        a = np.zeros(shape=(n, n))
        vector = convertirALista(SLVector.get())
        for i in range(n):
            for j in range(n):
                a[i][j] = float(matrizID[i][j].get())
        if menuSL.get()=="Gauss-Jordan":
            print("Mat",a)
            print("Vec",vector)
            res = solucionGJ(a,vector,n)
            print(res)
            SLresultado.delete('1.0',END)
            for i in range(len(res)):
                #str(" %.6f  " % extremos5(x, fx, 0))
                SLresultado.insert(END,"X"+str(i)+"= "+str("%.6f"%res[i])+"\n")
                SLresultado.place(relx=0.67,rely=0.3)
        if menuSL.get() == "Solución por inversa":
            res = solucionInversa(a, vector, n)
            print(res)
            SLresultado.delete('1.0', END)
            for i in range(len(res)):
                # str(" %.6f  " % extremos5(x, fx, 0))
                SLresultado.insert(END, "X" + str(i) + "= " + str("%.6f" % res[i]) + "\n")
                SLresultado.place(relx=0.67, rely=0.3)
    except:
        SLresultado.insert(END, "Revise sus entradas"+ "\n")
        SLresultado.place(relx=0.67, rely=0.3)

def genMatID():
    subFrameID.place_forget()
    n = int(IDmatSize.get())
    valor = int(varSL.get())
    for i in range(8):
        for j in range(8):
            matrizID[i][j].delete(0, len(matrizID[i][j].get()))
            matrizID[i][j].grid_forget()
    print(matrizID)
    for r in range(n):
        for c in range(n):
            matrizID[r][c].grid(row=r, column=c)
    if valor ==1:
        menuSL.place_forget()
        calcSL.place_forget()
        SLlabelVector.place_forget()
        SLVector.place_forget()
        menuID.place(relx=0.5, rely=0.2)
        calcID.place(relx=0.77, rely=0.2)
        subFrameID.place(relx=0.1,rely=0.3)
    elif valor == 2:
        menuID.place_forget()
        calcID.place_forget()
        menuSL.place(relx=0.5, rely=0.2)
        calcSL.place(relx=0.77, rely=0.2)
        subFrameID.place(relx=0.1,rely=0.4)
        SLlabelVector.place(relx=0.05,rely=0.3)
        SLVector.delete(0,END)
        SLVector.place(relx=0.15,rely=0.3)



#fin de MNuméricos

#------------------------MÉTODOS--------------------------------
def convertirALista(string):
    l=[]
    num = ""
    for i in range(len(string)):
        if string[i] is ',':
            l.append(float(num))
            num = ""
        else:
            num += string[i]
    l.append(float(num))
    return l
def derivar(f,n=1):
    df = sympify(f)
    aux = df
    i = 0
    while i<n:
        df = Derivative(aux).doit()
        aux = df
        i+=1
    return aux
def evaluar(exp, a):
    x = symbols('x')
    res = sympify(exp).subs(x, a)
    return res
def graficar():
    f = sympify(tf.get())
    x = symbols('x')
    equation = f
    xx = np.linspace(-10, 10, 1000)
    yy = lambdify(x, equation)(xx)
    plt.plot(xx, np.transpose(yy))
    #plt.plot(raiz, 0, 'bo')
    plt.show()

def cerrarFrame():
    if frameB.winfo_ismapped():
        frameB.place_forget()
    elif framePF.winfo_ismapped():
        framePF.place_forget()
    elif frameSEC.winfo_ismapped():
        frameSEC.place_forget()
    elif frameNR.winfo_ismapped():
        frameNR.place_forget()
    elif frameHOR.winfo_ismapped():
        frameHOR.place_forget()
    elif frameLG.winfo_ismapped():
        frameLG.place_forget()
    elif frameHER.winfo_ismapped():
        frameHER.place_forget()
    elif frameHERAL.winfo_ismapped():
        frameHERAL.place_forget()
    elif frameDIF.winfo_ismapped():
        frameDIF.place_forget()
    elif frameMUL.winfo_ismapped():
        frameMUL.place_forget()
    elif frameNEV.winfo_ismapped():
        frameNEV.place_forget()
    elif frameDN.winfo_ismapped():
        frameDN.place_forget()
    elif frameIN.winfo_ismapped():
        frameIN.place_forget()
    elif frameED.winfo_ismapped():
        frameED.place_forget()
    elif frameID.winfo_ismapped():
        frameID.place_forget()
    else:
        pass
def create_window():
    window = tk.Toplevel(root)
    img = ImageTk.PhotoImage(file="instrucciones.jpg")
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()
def create_window2():
    window = tk.Toplevel(root)
    img = ImageTk.PhotoImage(file="acerca.jpg")
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()
def create_window3(A,n):
    window = tk.Toplevel(root)
    n = len(A[0])
    a = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = Entry(window, borderwidth=1, width=10)
            a[i][j].insert(END, str(A[i][j]))
    for r in range(n):
        for c in range(n):
            a[r][c].grid(row=r, column=c)
    window.mainloop()
def biseccion():
    cerrarFrame()
    frameB.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def secante():
    cerrarFrame()
    frameSEC.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def pf():
    cerrarFrame()
    framePF.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def nr():
    cerrarFrame()
    frameNR.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def horner():
    cerrarFrame()
    frameHOR.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def lagrange():
    cerrarFrame()
    frameLG.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def hermite():
    cerrarFrame()
    frameHER.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def hermiteAL():
    cerrarFrame()
    frameHERAL.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def difdiv():
    cerrarFrame()
    frameDIF.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def muller():
    cerrarFrame()
    frameMUL.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def neville():
    cerrarFrame()
    frameNEV.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def difn():
    DNfx.delete(0, len(DNfx.get()))
    DNx.delete(0, len(DNx.get()))
    DNresultado.delete(0,END)
    DNposicion.delete(0,len(DNposicion.get()))
    insertarFxDN.place(relx=0.46, rely=0.2)
    DNlabelFX.place_forget()
    DNfx.place_forget()
    cerrarFrame()
    nombre =""
    valor =int(varDifNum.get())
    if valor ==1:
        nombre="Centro (3 puntos)"
    elif valor == 2:
        nombre = "Extremo (3 puntos)"
    elif valor == 3:
        nombre = "Centro (5 puntos)"
    elif valor ==4:
        nombre = "Extremos (5 puntos)"
    elif valor ==5:
        nombre = "Segunda derivada"
    print(nombre)
    DNlabel.config(text=nombre)
    frameDN.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def integNum():
    cerrarFrame()
    #tf.delete(0,len(tf.get()))
    INx0.delete(0,len(INx0.get()))
    INx1.delete(0,len(INx1.get()))
    INresultado.delete(0,len(INresultado.get()))
    print(varIntegNum.get())
    frameIN.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
    if varIntegNum.get()==1:
        INlabel.config(text="Integración numérica")
        menuINC.place_forget()
        menuIN.place(relx=0.55, rely=0.2)
    if varIntegNum.get()==2:
        INlabel.config(text="Integración numérica compuesta")
        menuIN.place_forget()
        menuINC.place(relx=0.55, rely=0.2)
def eedd():
    cerrarFrame()
    EDwi.delete(0,len(EDwi.get()))
    EDti.delete(0, len(EDwi.get()))
    frameED.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
    if varED.get() == 1:
        EDlabel.config(text="PVI")
def sl():
    cerrarFrame()
    calcSL.place_forget()
    menuSL.place_forget()
    SLVector.place_forget()
    SLlabelVector.place_forget()

    calcID.place_forget()
    menuID.place_forget()
    IDlabelResDet.place_forget()
    IDResDet.place_forget()
    SLresultado.place_forget()
    if varSL.get() == 1:
        IDlabel.config(text="Inversa/Determinante")
    if varSL.get()==2:
        IDlabel.config(text="Solución de sistemas")
    for i in range(8):
        for j in range(8):
            matrizID[i][j].delete(0, len(matrizID[i][j].get()))
            matrizID[i][j].grid_forget()
    frameID.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def det():
    cerrarFrame()
    frameID.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
def insertFXLG():
    insertarFxLG.place_forget()
    LGlabelFX.place(relx=0.46, rely=0.2)
    LGfx.place(relx=0.59,rely=0.2)
def insertFxHER():
    insertarFxHER.place_forget()
    HERlabelFX.place(relx=0.46, rely=0.2)
    HERfx.place(relx=0.59, rely=0.2)
    HERlabeldFX.place(relx=0.46,rely=0.27)
    HERdfx.place(relx=0.59,rely=0.27)
def insertFxHERAL():
    insertarFxHERAL.place_forget()
    HERALlabelFX.place(relx=0.46, rely=0.2)
    HERALfx.place(relx=0.59, rely=0.2)
    HERALlabeldFX.place(relx=0.46,rely=0.27)
    HERALdfx.place(relx=0.59,rely=0.27)
def insertFxDIF():
    insertarFxDIF.place_forget()
    DIFlabelFX.place(relx=0.46, rely=0.2)
    DIFfx.place(relx=0.59, rely=0.2)
def insertXMUL():
    MULlabelx0.place(relx=0.55,rely=0.3)
    MULx0.place(relx=0.59,rely=0.3)
    grado = int(MULn.get())
    if grado > 3:
        valores = str( (grado - 2) *3 )
    else:
        valores = str("3")
    texto = "Inserte "+valores+" valores de X"
    notaMUL = Label(frameMUL,text=texto,font='Verdana 12 bold italic')
    notaMUL.place(relx=0.59,rely=0.4)
    calcMUL.place(relx=0.21, rely=0.48)
def insertFXNEV():
    insertarFxNEV.place_forget()
    NEVlabelFX.place(relx=0.46, rely=0.2)
    NEVfx.place(relx=0.59, rely=0.2)
def insertFXDN():
    insertarFxDN.place_forget()
    DNlabelFX.place(relx=0.46, rely=0.2)
    DNfx.place(relx=0.59, rely=0.2)
def ocultarMetodos():
    R1.place_forget()
    R2.place_forget()
    R3.place_forget()
    R4.place_forget()
    R5.place_forget()
    R6.place_forget()
    R7.place_forget()
    R8.place_forget()
    R9.place_forget()
    R10.place_forget()
    R11.place_forget()
    R12.place_forget()
    R13.place_forget()
    R14.place_forget()
    R15.place_forget()
    R16.place_forget()
    R17.place_forget()
    R18.place_forget()
    R19.place_forget()
    R20.place_forget()
    R21.place_forget()
def callbackFunc(event):
    opcion = menu.get()
    ocultarMetodos()
    if opcion == "Raíces":
        R1.place(relx=0.0, rely=0.15)
        R2.place(relx=0.0, rely=0.2)
        R3.place(relx=0.0, rely=0.25)
        R4.place(relx=0.25, rely=0.15)
        R5.place(relx=0.25, rely=0.2)

    elif opcion == "Interpolación":
        R6.place(relx=0.0, rely=0.15)
        R7.place(relx=0.0, rely=0.2)
        R8.place(relx=0.0, rely=0.25)
        R9.place(relx=0.25, rely=0.15)
        R10.place(relx=0.25, rely=0.2)
        R11.place(relx=0.25, rely=0.25)

    elif opcion == "Diferenciación numérica":
        R12.place(relx=0.0, rely=0.15)
        R13.place(relx=0.0, rely=0.2)
        R14.place(relx=0.0, rely=0.25)
        R15.place(relx=0.25, rely=0.15)
        R16.place(relx=0.25, rely=0.2)

    elif opcion == "Integración numérica":
        R17.place(relx=0.0, rely=0.15)
        R18.place(relx=0.0, rely=0.2)

    elif opcion == "EEDD":
        R19.place(relx=0.0, rely=0.15)

    elif opcion =="Sistemas lineales":
        R20.place(relx=0.0, rely=0.15)
        R21.place(relx=0.0, rely=0.2)
#------------------------FIN DE MÉTODOS--------------------------------

HEIGHT = 700
WIDTH = 900
root = tk.Tk()
label = Label(root,text="Métodos numéricos")
label.config(font=("Verdana", 44))
label.pack()

canva = tk.Canvas(root,height = HEIGHT, width=WIDTH,bg="black")
canva.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "Mates.jpg")
canva.create_image(10, 10, image = image, anchor = NW)
#canva.pack()
frame = tk.Frame(root,bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

#------------------------PARTE DE INPUT------------------------
label1 = Label(frame,text="Introduzca su función aquí")
label1.config(font=("Verdana",22))
label1.pack()
tf = tk.Entry(frame, text = "texto",width=WIDTH)
tf.pack()
graficar = Button(frame,text="Muéstrame la gráfica",command=graficar)
graficar.place(relx=0.37, rely=0.1)
button = Button(frame,text="¿No sabes cómo introducir tu función?",command=create_window)
button.pack(anchor = "e")
menu = ttk.Combobox(frame,values=["Raíces","Interpolación","Diferenciación numérica","Integración numérica","EEDD","Sistemas lineales"], state="readonly")
menu.bind("<<ComboboxSelected>>", callbackFunc)
menu.place(relx=0.0,rely=0.1)
acercaDe =Button(frame, text="Acerca de:",command=create_window2,font="Verdana 15 bold")
acercaDe.place(relx=0.84,rely=0.955)
#------------------------FIN PARTE INPUT------------------------

#------------------------METODOS GUI------------------------------
var = IntVar()
varDifNum = IntVar()
varIntegNum = IntVar()
varED = IntVar()
varSL = IntVar()
varDet = IntVar()
R1 = Radiobutton(frame, text="Bisección", variable=var, value=1,command=biseccion)
R2 = Radiobutton(frame, text="Posición falsa",variable=var, value=2,command=pf)
R3 = Radiobutton(frame, text="Secante",variable=var, value=3,command=secante)
R4 = Radiobutton(frame, text="Newton Raphson",variable=var, value=4,command=nr)
R5 = Radiobutton(frame, text="Horner",variable=var, value=5,command=horner)
R6 = Radiobutton(frame, text="Lagrange",variable=var, value=6,command=lagrange)
R7 = Radiobutton(frame, text="Hermite",variable=var, value=7,command=hermite)
R8 = Radiobutton(frame, text="Hermite Alternativo",variable=var, value=8,command=hermiteAL)
R9 = Radiobutton(frame, text="Diferencias Divididas",variable=var, value=9,command=difdiv)
R10 = Radiobutton(frame, text="Müller",variable=var, value=10,command=muller)
R11 = Radiobutton(frame, text="Neville",variable=var, value=11,command=neville)

#DIF NUM
R12 = Radiobutton(frame, text="Centro (3 puntos)",variable=varDifNum, value=1,command=difn)
R13 = Radiobutton(frame, text="Extremos (3 puntos)",variable=varDifNum, value=2,command=difn)
R14 = Radiobutton(frame, text="Centro (5 puntos)",variable=varDifNum, value=3,command=difn)
R15 = Radiobutton(frame, text="Extremos (5 puntos)",variable=varDifNum, value=4,command=difn)
R16 = Radiobutton(frame, text="Segunda derivada",variable=varDifNum, value=5,command=difn)
#FIN DIF NUM

#INTEG NUM
R17 = Radiobutton(frame,text="Integración numérica",variable=varIntegNum,value = 1,command=integNum)
R18 = Radiobutton(frame,text="Integración numérica compuesta",variable=varIntegNum,value = 2,command=integNum)
#FIN INTEG NUM

#EEDD
R19 = Radiobutton(frame, text="PVI", variable=varED,value=1,command=eedd)
#FIN EEDD

#SISTEMAS LINEALES
R20 = Radiobutton(frame, text="Inversa/Determinante", variable=varSL,value=1,command=sl)
R21 = Radiobutton(frame, text="Soulcion de sistemas", variable=varSL,value=2,command=sl)
#FIN SISTEMAS LINEALES

#------------------------FIN METODOS GUI------------------------------

#FRAMES METODOS

#BISECCION
#frame
frameB = tk.Frame(root,bg='white')
#frameB.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#lables
labelBis = Label(frameB, text = "Bisección",width=WIDTH,bg="black",fg="white")
labelBis.config(font=("Verdana",22))
labelA =Label(frameB,text="A: ")
labelB =Label(frameB,text="B: ")
labelTol = Label(frameB,text="Tolerancia: ")
labelRes = Label(frameB,text="Resultado: ",font='Verdana 12 bold')
#fin labels

#entry
puntoA = Entry(frameB)
puntoB = Entry(frameB)
tolerancia = Entry(frameB)
resultado = Entry(frameB)
#finEntry

#buttons
calcB = Button(frameB,text="Calcular",command=calcularBiseccion)
#fin buttons

#Place
labelBis.pack()
labelA.place(relx=0.1, rely=0.2)
puntoA.place(relx=0.15, rely=0.2)
labelB.place(relx=0.1, rely=0.3)
puntoB.place(relx=0.15, rely=0.3)
labelTol.place(relx=0.46,rely=0.2)
tolerancia.place(relx=0.58,rely=0.2)
labelRes.place(relx=0.46,rely=0.3)
resultado.place(relx=0.58,rely=0.3)
calcB.place(relx=0.15,rely=0.4)
#FinPlace
#FIN BISECCION

#POSICION FALSA
#frame
framePF = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcPF = Button(framePF,text="Calcular",command=calcularPF)
#fin button

#lables
PFlabel = Label(framePF, text = "Posición Falsa",width=WIDTH,bg="black",fg="white")
PFlabel.config(font=("Verdana",22))
PFlabelA =Label(framePF,text="A: ")
PFlabelB =Label(framePF,text="B: ")
PFlabelTol = Label(framePF,text="Tolerancia: ")
PFlabelRes = Label(framePF,text="Resultado: ",font='Verdana 12 bold')
#fin labels

#entry
PFpuntoA = Entry(framePF)
PFpuntoB = Entry(framePF)
PFtolerancia = Entry(framePF)
PFresultado = Entry(framePF)
#finEntry

#Place
PFlabel.pack()
PFlabelA.place(relx=0.1, rely=0.2)
PFpuntoA.place(relx=0.15, rely=0.2)
PFlabelB.place(relx=0.1, rely=0.3)
PFpuntoB.place(relx=0.15, rely=0.3)
PFlabelTol.place(relx=0.46,rely=0.2)
PFtolerancia.place(relx=0.58,rely=0.2)
PFlabelRes.place(relx=0.46,rely=0.3)
PFresultado.place(relx=0.58,rely=0.3)
calcPF.place(relx=0.15,rely=0.4)
#FinPlace
#FIN POSICION FALSA

#SECANTE
#frame
frameSEC = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcSEC = Button(frameSEC,text="Calcular",command=calcularSEC)
#fin button

#lables
SEClabel = Label(frameSEC, text = "Secante",width=WIDTH,bg="black",fg="white")
SEClabel.config(font=("Verdana",22))
SEClabelA =Label(frameSEC,text="A: ")
SEClabelB =Label(frameSEC,text="B: ")
SEClabelTol = Label(frameSEC,text="Tolerancia: ")
SEClabelRes = Label(frameSEC,text="Resultado: ",font='Verdana 12 bold')
#fin labels

#entry
SECpuntoA = Entry(frameSEC)
SECpuntoB = Entry(frameSEC)
SECtolerancia = Entry(frameSEC)
SECresultado = Entry(frameSEC)
#finEntry

#Place
SEClabel.pack()
SEClabelA.place(relx=0.1, rely=0.2)
SECpuntoA.place(relx=0.15, rely=0.2)
SEClabelB.place(relx=0.1, rely=0.3)
SECpuntoB.place(relx=0.15, rely=0.3)
SEClabelTol.place(relx=0.46,rely=0.2)
SECtolerancia.place(relx=0.58,rely=0.2)
SEClabelRes.place(relx=0.46,rely=0.3)
SECresultado.place(relx=0.58,rely=0.3)
calcSEC.place(relx=0.15,rely=0.4)
#FinPlace
#FIN SECANTE

#NEWTON RAPHSON
#frame
frameNR = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcNR = Button(frameNR,text="Calcular",command=calcularNR)
#fin button

#lables
NRlabel = Label(frameNR, text = "Newton Raphson",width=WIDTH,bg="black",fg="white")
NRlabel.config(font=("Verdana",22))
NRlabelA =Label(frameNR,text="A: ")
NRlabelTol = Label(frameNR,text="Tolerancia: ")
NRlabelRes = Label(frameNR,text="Resultado: ",font='Verdana 12 bold')
#fin labels

#entry
NRpuntoA = Entry(frameNR)
NRtolerancia = Entry(frameNR)
NRresultado = Entry(frameNR)
#finEntry

#Place
NRlabel.pack()
NRlabelA.place(relx=0.1, rely=0.2)
NRpuntoA.place(relx=0.15, rely=0.2)
NRlabelTol.place(relx=0.46,rely=0.2)
NRtolerancia.place(relx=0.58,rely=0.2)
NRlabelRes.place(relx=0.46,rely=0.3)
NRresultado.place(relx=0.58,rely=0.3)
calcNR.place(relx=0.15,rely=0.3)
#FinPlace
#FIN NEWTON RAPHSON


#HORNER
#frame
frameHOR = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcHOR = Button(frameHOR,text="Calcular",command=calcularHOR)
#fin button

#lables
HORlabel = Label(frameHOR, text = "Horner",width=WIDTH,bg="black",fg="white")
InstruccionHor = Label(frameHOR, text="Introduce los coeficientes separados por comas:\n a0,a1,a2,....,aN")
HORlabel.config(font=("Verdana",22))
HORlabelN =Label(frameHOR,text="N: ")
HORlabelCoef = Label(frameHOR,text="Coeficientes: ")
HORlabelRes = Label(frameHOR,text="Resultado: ",font='Verdana 16 bold')
HORlabelx0 = Label(frameHOR,text="X0")
HORtolLabel = Label(frameHOR,text="Tolerancia")
#fin labels

var = StringVar()
#entry
HORn = Entry(frameHOR)
HORCoef = Entry(frameHOR)
HORresultado = Text(frameHOR)
HORresultado.config(font=("Verdana",12))
HORx0 = Entry(frameHOR)
HORtol = Entry(frameHOR)
#finEntry

#Place
HORlabel.pack()
HORlabelN.place(relx=0.1, rely=0.2)
HORn.place(relx=0.15, rely=0.2)
HORlabelCoef.place(relx=0.46,rely=0.2)
InstruccionHor.place(relx=0.46,rely=0.3)

HORtolLabel.place(relx=0.46,rely=0.4)
HORtol.place(relx=0.59,rely=0.4)

HORCoef.place(relx=0.59,rely=0.2)

HORlabelRes.place(relx=0.44,rely=0.5)
HORresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
calcHOR.place(relx=0.15,rely=0.3)
HORlabelx0.place(relx=0.1, rely=0.4)
HORx0.place(relx=0.15, rely=0.4)
#FinPlace
#FIN HORNER

#---------------LAGRANGE---------------
#frame
frameLG = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcLG = Button(frameLG,text="Calcular",command=calcularLG)
insertarFxLG = Button(frameLG,text="¿No tienes tu función?",command=insertFXLG)
#fin button

#lables
LGlabel = Label(frameLG, text = "Lagrange",width=WIDTH,bg="black",fg="white")
LGinstrucciones = Label(frameLG,text="Introducir X y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
LGlabel.config(font=("Verdana",22))
LGlabelX =Label(frameLG,text="X: ")
LGlabelFX = Label(frameLG,text="Fx: ")
LGlabelRes = Label(frameLG,text="Resultado: ",font='Verdana 16 bold')
LGlabelpuntoEval = Label(frameLG,text="Punto: ")
#fin labels

#entry
LGx = Entry(frameLG)
LGfx = Entry(frameLG)
LGresultado = Text(frameLG,font='Verdana 13 bold')
LGresultado.config(font=("Verdana",12))
LGpuntoEval=Entry(frameLG)
#finEntry

#Place
LGlabel.pack()
LGlabelX.place(relx=0.1, rely=0.2)
LGx.place(relx=0.15, rely=0.2)
insertarFxLG.place(relx=0.46,rely=0.2)
#LGlabelFX.place(relx=0.46,rely=0.2)
#LGfx.place(relx=0.59,rely=0.2)
LGlabelRes.place(relx=0.44,rely=0.5)
LGresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
calcLG.place(relx=0.46,rely=0.3)
LGinstrucciones.place(relx=0.15, rely=0.1)
LGlabelpuntoEval.place(relx=0.07, rely=0.3)
LGpuntoEval.place(relx=0.15, rely=0.3)
#FinPlace
#---------------FIN LAGRANGE---------------

#---------------HERMITE---------------
#frame
frameHER = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcHER = Button(frameHER,text="Calcular",command=calcularHER)
insertarFxHER = Button(frameHER,text="¿No tienes tu función?",command=insertFxHER)
#fin button

#lables
HERlabel = Label(frameHER, text = "Hermite",width=WIDTH,bg="black",fg="white")
HERinstrucciones = Label(frameHER,text="Introducir X, dFX y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
HERlabel.config(font=("Verdana",22))
HERlabelX =Label(frameHER,text="X: ")
HERlabelFX = Label(frameHER,text="Fx: ")
HERlabeldFX = Label(frameHER,text="dFx: ")
HERlabelRes = Label(frameHER,text="Resultado: ",font='Verdana 16 bold')
HERlabelpuntoEval = Label(frameHER,text="Punto: ")
#fin labels

#entry
HERx = Entry(frameHER)
HERfx = Entry(frameHER)
HERdfx = Entry(frameHER)
HERresultado = Text(frameHER,font='Verdana 13 bold')
HERresultado.config(font=("Verdana",12))
HERpuntoEval = Entry(frameHER)
#finEntry

#Place
HERlabel.pack()
HERlabelX.place(relx=0.1, rely=0.2)
HERx.place(relx=0.15, rely=0.2)
insertarFxHER.place(relx=0.46,rely=0.2)
HERlabelRes.place(relx=0.44,rely=0.5)
HERresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
calcHER.place(relx=0.15,rely=0.35)
HERinstrucciones.place(relx=0.15, rely=0.1)
HERlabelpuntoEval.place(relx=0.07,rely=0.27)
HERpuntoEval.place(relx=0.15,rely=0.27)
#FinPlace
#---------------FIN HERMITE---------------


#---------------HERMITE ALTERNATIVO---------------
#frame
frameHERAL = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcHERAL = Button(frameHERAL,text="Calcular",command=calcularHERAL)
insertarFxHERAL = Button(frameHERAL,text="¿No tienes tu función?",command=insertFxHERAL)
#fin button

#lables
HERALlabel = Label(frameHERAL, text = "Hermite Alternativo",width=WIDTH,bg="black",fg="white")
HERALinstrucciones = Label(frameHERAL,text="Introducir X, dFX y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
HERALlabel.config(font=("Verdana",22))
HERALlabelX =Label(frameHERAL,text="X: ")
HERALlabelFX = Label(frameHERAL,text="Fx: ")
HERALlabeldFX = Label(frameHERAL,text="dFx: ")
HERALlabelRes = Label(frameHERAL,text="Resultado: ",font='Verdana 16 bold')
HERALlabelpuntoEval = Label(frameHERAL,text="Punto: ")
#fin labels

#entry
HERALx = Entry(frameHERAL)
HERALfx = Entry(frameHERAL)
HERALdfx = Entry(frameHERAL)
HERALresultado = Text(frameHERAL,font='Verdana 13 bold')
HERALresultado.config(font=("Verdana",12))
HERALpuntoEval = Entry(frameHERAL)
#finEntry

#Place
HERALlabel.pack()
HERALlabelX.place(relx=0.1, rely=0.2)
HERALx.place(relx=0.15, rely=0.2)
insertarFxHERAL.place(relx=0.46,rely=0.2)
HERALlabelRes.place(relx=0.44,rely=0.5)
HERALresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
calcHERAL.place(relx=0.15,rely=0.35)
HERALinstrucciones.place(relx=0.15, rely=0.1)
HERALlabelpuntoEval.place(relx=0.07,rely=0.27)
HERALpuntoEval.place(relx=0.15,rely=0.27)
#FinPlace
#---------------FIN HERMITE ALTERNATIVO---------------

#----------------DIFERENCIAS DIVIDIDAS----------------
#frame
frameDIF = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcDIF = Button(frameDIF,text="Calcular",command=calcularDIF)
insertarFxDIF = Button(frameDIF,text="¿No tienes tu función?",command=insertFxDIF)
#fin button

#lables
DIFlabel = Label(frameDIF, text = "Diferencia Divididas",width=WIDTH,bg="black",fg="white")
DIFinstrucciones = Label(frameDIF,text="Introducir X y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
DIFlabel.config(font=("Verdana",22))
DIFlabelX =Label(frameDIF,text="X: ")
DIFlabelFX = Label(frameDIF,text="Fx: ")
DIFlabelRes = Label(frameDIF,text="Resultado: ",font='Verdana 16 bold')
DIFlabelpuntoEval = Label(frameDIF,text="Punto: ")
#fin labels

#entry
DIFx = Entry(frameDIF)
DIFfx = Entry(frameDIF)
DIFresultado = Text(frameDIF,font='Verdana 13 bold')
DIFresultado.config(font=("Verdana",12))
DIFpuntoEval = Entry(frameDIF)
#finEntry

#Place
DIFlabel.pack()
DIFlabelX.place(relx=0.1, rely=0.2)
DIFx.place(relx=0.15, rely=0.2)
insertarFxDIF.place(relx=0.46,rely=0.2)
DIFlabelRes.place(relx=0.44,rely=0.5)
DIFresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
calcDIF.place(relx=0.15,rely=0.35)
DIFinstrucciones.place(relx=0.15, rely=0.1)
DIFlabelpuntoEval.place(relx=0.07,rely=0.27)
DIFpuntoEval.place(relx=0.15,rely=0.27)
#FinPlace
#--------------FIN DIFERENCIAS DIVIDIDAS--------------

#---------------------MULLER--------------------------
#frame
frameMUL = tk.Frame(root,bg='white')
#framePF.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
#fin frame

#buttons
calcMUL = Button(frameMUL,text="Calcular",command=calcularMUL,font="Verdana 12 bold")
insertarXMUL = Button(frameMUL,text="Introducir valores de X",command=insertXMUL)
#fin button

#lables
MULinstrucciones = Label(frameMUL,text="Introducir X y Coeficientes sepraradas por coma, por favor.",font='Verdana 16 bold')
MULlabel = Label(frameMUL, text = "Müller",width=WIDTH,bg="black",fg="white")
MULlabel.config(font=("Verdana",22))
MULlabelN =Label(frameMUL,text="N: ")
MULlabelCoef = Label(frameMUL,text="Coeficientes: ")
MULlabelRes = Label(frameMUL,text="Resultado: ",font='Verdana 16 bold')
MULlabelx0 = Label(frameMUL,text="X: ")
MULlabeltol = Label(frameMUL,text="Tolerancia: ")

#fin labels

var = StringVar()
#entry
MULn = Entry(frameMUL)
MULCoef = Entry(frameMUL)
MULresultado = Text(frameMUL)
MULresultado.config(font=("Verdana",12))
MULx0 = Entry(frameMUL)
MULtol = Entry(frameMUL)
#finEntry

#Place
MULinstrucciones.place(relx=0.15, rely=0.1)
MULlabel.pack()
MULlabelN.place(relx=0.1, rely=0.2)
MULn.place(relx=0.15, rely=0.2)
MULlabelCoef.place(relx=0.46,rely=0.2)
MULCoef.place(relx=0.59,rely=0.2)
MULlabelRes.place(relx=0.44,rely=0.5)
MULresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
#calcMUL.place(relx=0.59,rely=0.3)
#MULlabelx0.place(relx=0.1, rely=0.4)
#MULx0.place(relx=0.15, rely=0.4)
insertarXMUL.place(relx=0.15, rely=0.4)
MULlabeltol.place(relx=0.04, rely=0.3)
MULtol.place(relx=0.15, rely=0.3)
#FinPlace
#---------------------FIN MULLER--------------------------

#---------------------NEVILLE---------------------
#frame
frameNEV = tk.Frame(root,bg='white')
#fin frame

#buttons
calcNEV = Button(frameNEV,text="Calcular",command=calcularNEV)
insertarFxNEV = Button(frameNEV,text="¿No tienes tu función?",command=insertFXNEV)
#fin button

#lables
NEVlabel = Label(frameNEV, text = "Neville",width=WIDTH,bg="black",fg="white")
NEVinstrucciones = Label(frameNEV,text="Introducir X y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
NEVlabel.config(font=("Verdana",22))
NEVlabelX =Label(frameNEV,text="X: ")
NEVlabelFX = Label(frameNEV,text="Fx: ")
NEVlabelRes = Label(frameNEV,text="Resultado: ",font='Verdana 16 bold')
NEVlabelPunto = Label(frameNEV,text="Punto")
NEVLabelN = Label(frameNEV,text="N: ")

#fin labels

#entry
NEVx = Entry(frameNEV)
NEVfx = Entry(frameNEV)
NEVresultado = Text(frameNEV,font='Verdana 13 bold')
NEVresultado.config(font=("Verdana",12))
NEVPunto = Entry(frameNEV)
NEVn = Entry(frameNEV)
#finEntry

#Place
NEVlabel.pack()
NEVlabelX.place(relx=0.1, rely=0.2)
NEVx.place(relx=0.15, rely=0.2)
insertarFxNEV.place(relx=0.46,rely=0.2)
#NEVlabelFX.place(relx=0.46,rely=0.2)
#NEVfx.place(relx=0.59,rely=0.2)
NEVlabelRes.place(relx=0.44,rely=0.5)
NEVresultado.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.4)
NEVlabelPunto.place(relx=0.08,rely=0.28)
NEVPunto.place(relx=0.15,rely=0.28)
calcNEV.place(relx=0.46,rely=0.3)
NEVinstrucciones.place(relx=0.15, rely=0.1)
NEVLabelN.place(relx=0.09,rely=0.36)
NEVn.place(relx=0.15,rely=0.36)
#FinPlace
#---------------------FIN NEVILLE---------------------


#---------------------DIFERENCIACION NUMERICA---------------------

#frame
frameDN = tk.Frame(root,bg='white')
#fin frame

#buttons
calcDN = Button(frameDN,text="Calcular",command=calcularDN)
insertarFxDN = Button(frameDN,text="¿No tienes tu función?",command=insertFXDN)
#fin button

#lables
DNlabel = Label(frameDN,text="",width=WIDTH,bg="black",fg="white")
DNinstrucciones = Label(frameDN,text="Introducir X y FX sepraradas por coma, por favor.",font='Verdana 16 bold')
DNlabel.config(font=("Verdana",22))
DNlabelX =Label(frameDN,text="X: ")
DNlabelFX = Label(frameDN,text="Fx: ")
DNlabelRes = Label(frameDN,text="Resultado: ",font='Verdana 12 bold')
DNlabelposicion = Label(frameDN,text="Posición")
#fin labels

#entry
DNx = Entry(frameDN)
DNfx = Entry(frameDN)
DNresultado = Entry(frameDN)
DNposicion = Entry(frameDN)
#finEntry

#Place
DNlabel.pack()
DNlabelX.place(relx=0.1, rely=0.2)
DNx.place(relx=0.15, rely=0.2)
insertarFxDN.place(relx=0.46,rely=0.2)
#DNlabelFX.place(relx=0.46,rely=0.2)
#DNfx.place(relx=0.59,rely=0.2)
DNlabelRes.place(relx=0.05,rely=0.4)
DNresultado.place(relx=0.15,rely=0.4)
calcDN.place(relx=0.46,rely=0.3)
DNinstrucciones.place(relx=0.15, rely=0.1)
DNlabelposicion.place(relx=0.05,rely=0.3)
DNposicion.place(relx = 0.15, rely=0.3)
#FinPlace

#---------------------FIN DIF NUMERICA---------------------

#-------------------INTEGRACION NUMERICA-------------------
#frame
frameIN = tk.Frame(root,bg='white')
#fin frame

#buttons
calcIN = Button(frameIN,text="Calcular",command=calcularIN)
#fin button

#lables
INlabel = Label(frameIN,text="",width=WIDTH,bg="black",fg="white")
INlabel.config(font=("Verdana",22))
INinstrucciones = Label(frameIN,text="No olvide introducir su función en el recuadro superior y los límites en x1 y x0",font='Verdana 16 bold')

INlabelX0 = Label(frameIN,text="X0: ")
INlabelX1 = Label(frameIN,text="X1: ")
INlabelRes = Label(frameIN,text="Resultado: ",font='Verdana 12 bold')
INlabelFormula = Label(frameIN,text="Fórmula: ")
#fin labels
menuIN = ttk.Combobox(frameIN)
#entry
INx0 = Entry(frameIN)
INx1 = Entry(frameIN)
INresultado = Entry(frameIN)
#finEntry
menuIN = ttk.Combobox(frameIN,
                      values=["Grado 1", "Grado 2", "Grado 3", "Grado 4", "Punto medio (º1)", "Punto medio (º2)",
                              "Punto medio (º3)", "Punto medio (º4)"], state="readonly")
menuINC = ttk.Combobox(frameIN, values=["Trapecio", "Simpson", "Punto medio"], state="readonly")

#Place
INlabel.pack()
INlabelX0.place(relx=0.05,rely=0.2)
INx0.place(relx=0.10, rely=0.2,relwidth = 0.1)
INlabelX1.place(relx=0.25,rely=0.2)
INx1.place(relx=0.30, rely=0.2,relwidth = 0.1)
INlabelFormula.place(relx=0.45,rely=0.2)
calcIN.place(relx=0.10,rely=0.3)

INlabelRes.place(relx=0.43,rely=0.3)
INresultado.place(relx=0.55,rely=0.3)

INinstrucciones.place(relx=0.05, rely=0.1)
#INlabelFormula.place(relx=0.05,rely=0.3)
#FinPlace

#---------------------FIN INTEGRACIÓN NUMÉRICA------------------

#---------------------ECUACIONES DIFERENCIALES------------------

#frame
frameED = tk.Frame(root,bg='white')
#fin frame

#buttons
calcED = Button(frameED,text="Calcular",command=calcularED)
#fin button

#lables
EDlabel = Label(frameED,text="",width=WIDTH,bg="black",fg="white")
EDlabel.config(font=("Verdana",22))
EDinstrucciones = Label(frameED,text="No olvide introducir su función en el recuadro superior, las condiciones iniciales, el límite superior y la h",font='Verdana 12 bold')

EDlabelwi = Label(frameED,text="Wi: ")
EDlabelti = Label(frameED,text="Ti: ")
EDlabelRes = Label(frameED,text="Resultado: ",font='Verdana 14 bold')
EDlabelFormula = Label(frameED,text="Fórmula: ")
EDlabelLimSup = Label(frameED, text="Límite superior")
EDlabelH = Label(frameED, text="H:")
#FIN labels
#entry
EDwi = Entry(frameED)
EDti = Entry(frameED)
EDLimSup = Entry(frameED)
EDh = Entry(frameED)
#FINEntry


menuED = ttk.Combobox(frameED,
                      values=["Euler","Euler modificado","Heun","Punto medio","Runge Kutta"], state="readonly")
menuED.place(relx=0.15, rely=0.3)

#Place
EDlabel.pack()

EDlabelwi.place(relx=0.05,rely=0.2)
EDwi.place(relx=0.10, rely=0.2,relwidth = 0.1)

EDlabelti.place(relx=0.25,rely=0.2)
EDti.place(relx=0.30, rely=0.2,relwidth = 0.1)

EDlabelFormula.place(relx=0.05,rely=0.3)
calcED.place(relx=0.43,rely=0.3)

EDlabelRes.place(relx=0.4,rely=0.4)

EDinstrucciones.place(relx=0.025, rely=0.1)

EDlabelLimSup.place(relx=0.45,rely=0.2)
EDLimSup.place(relx=0.60, rely=0.2,relwidth=0.1)

EDlabelH.place(relx=0.72,rely=0.2)
EDh.place(relx=0.75, rely=0.2,relwidth=0.08)
#EDlabelFormula.place(relx=0.05,rely=0.3)
#FIN Place
#---------------------FIN ECUACIONES DIFERENCIALES------------------

#---------------------SISTEMAS LINEALES---------------------------

#-----Inversa/Determinante--------

#frame
frameID = tk.Frame(root,bg='white')
subFrameID = tk.Frame(frameID)
#fin frame

matrizID = [[0 for x in range(8)] for x in range(8)]
for i in range(8):
    for j in range(8):
        matrizID[i][j] = Entry(subFrameID, borderwidth=1, width=5)

SLresultado = Text(frameID,font='Verdana 15 bold')
#buttons
calcID = Button(frameID,text="Calcular",command=calcularID)
calcSL = Button(frameID,text="Calcular solución",command=calcularSL)
generarMatID = Button(frameID,text="Generar",command=genMatID)
#fin button

#lables
IDlabel = Label(frameID,text="",width=WIDTH,bg="black",fg="white")
IDlabel.config(font=("Verdana",22))
IDinstrucciones = Label(frameID,text="Introduzca el tamaño de su matriz cuadrada (máximo 8)",font='Verdana 14 bold')
IDlabelmatSize = Label(frameID,text="Tamaño de la matriz: ")
IDlabelResDet = Label(frameID,text="Resultado : ",font='Verdana 14 bold')

SLlabelVector = Label(frameID,text="Vector: ")
#FIN labels

#entry
IDmatSize = Entry(frameID)
IDResDet = Entry(frameID,width=65)

SLVector = Entry(frameID)
#FINEntry

menuID = ttk.Combobox(frameID,values=["Determinante","Matriz inversa"], state="readonly")
menuSL = ttk.Combobox(frameID,values=["Gauss-Jordan","Solución por inversa"], state="readonly")
#menuID.place(relx=0.15, rely=0.3) -- menu: inv/det

#Place
IDlabel.pack()
IDlabelmatSize.place(relx=0.05,rely=0.2)
IDmatSize.place(relx=0.25, rely=0.2,relwidth = 0.1)
generarMatID.place(relx=0.38, rely=0.2)

IDinstrucciones.place(relx=0.025, rely=0.1)
#calcID.place(relx=0.43,rely=0.3) -- boton calcular inv/det
#FIN Place

#-----FIN Inversa/Determinante----



#-------Sol. de sistemas----------
#-------FIN Sol. de sistemas------

#---------------------FIN SISTEMAS LINEALES------------------------


#------------------------------------------------------------FIN FRAMES METODOS----------------------------------------------------------------

root.mainloop()