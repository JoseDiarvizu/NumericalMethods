import numpy as np
def swap(a,b):
    return b,a
n = int(input("Ingrese el tamaño de su matriz cuadrada"))
a = np.zeros(shape=(n,n))
id = np.zeros(shape=(n,n))
for i in range(n-1):
    for j in range(i,i+1):
        id[i][j]= 1.0
vector=[[1,0,0],[2,0,0],[3,0,0]]
id[n-1][n-1] = 1
print("Ingrese los coeficientes")
for i in range(n):
    for j in range(n):
        a[i][j]=float(input())

for i in range (n-1):
    for j in range(i,i+1):
        if a[i][j] == 0.0:
            cont = i
            while a[cont][j] == 0.0:
                cont+=1
            for o in range(len(a[i])):
                aux = a[i][o]
                a[i][o] = a[cont][o]
                a[cont][o]=aux

                auxID = id[i][o]
                id[i][o] = id[cont][o]
                id[cont][o] = auxID

                auxVec = vector[i][o]
                vector[i][o] = vector[cont][o]
                vector[cont][o] = auxVec
        aux = a[i][j]
        for o in range(0,n):
            a[i][o] = a[i][o] * (1/aux)
            id[i][o] = id[i][o] * (1/aux)
            vector[i][o] = vector[i][o] * (1 / aux)

        for x in range(i+1,n):
            num = a[x][j]/a[i][j]
            for o in range(0,len(a[i])):
                a[x][o] =(a[i][o]*-num) + a[x][o]
                id[x][o] = (id[i][o] * -num) + id[x][o]
                vector[x][o] = (vector[i][o] * -num) + vector[x][o]


aux = a[n-1][n-1]
for i in range (n):
       a[n-1][i] = a[n-1][i] * (1/aux)
       id[n-1][i] = id[n-1][i] * (1/aux)
       vector[n - 1][i] = vector[n - 1][i] * (1 / aux)
print("E L I M I N A C I O N  G A U S S I A N A")
print("––––A––––")
print(a)
print("––––ID––––")
print(id)
for i in range(n-1,0,-1):
    for j in range(i,i+1):
        for x in range(i-1,-1,-1):
            num = a[x][j]/a[i][j]
            for o in range(n-1,-1,-1):
                a[x][o] =(a[i][o]*-num) + a[x][o]
                id[x][o] = (id[i][o] * -num) + id[x][o]
                vector[x][o] = (vector[i][o] * -num) + vector[x][o]
print("\nG A U S S - J O R D A N")
print("––––A––––")
print(a)
print("––––A^-1––––")
print(id)
print(vector)
'''
from tkinter import *
import numpy as np
root = Tk(  )
l=[]
a = [[0 for x in range(3)] for x in range(3)]
for i in range(3):
    for j in range(3):
        a[i][j]= Entry(root, text='R%s/C%s'%(i,j),borderwidth=1,width=5 )
print(a)
for r in range(3):
   for c in range(3):
      a[r][c].grid(row=r,column=c)
root.mainloop(  )







wi = 8
ti = 0
b=600
h = 20
f = "-0.006*((64.2)**(1/2))*(y**(1/2)/(y**(2) ))"
print(eulermodificado(f,wi,ti,h,b))



import tkinter as tk
from tkinter import ttk
import tktable
root = tk.Tk()
container = ttk.Frame(root)
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
                   rows=15,
                   cols=4,
                   colwidth=20)
columns = ['Breed', 'Price', 'Location', 'Age']
#### LIST OF LISTS DEFINING THE ROWS AND VALUES IN THOSE ROWS ####
values = [['Doodle', '1500', 'Chicago', '1'],
          ['Pug', '700', 'Kansas City', '2'],
          ['Westie', '1000', 'Lincoln', '1'],
          ['Aoodle', '900', 'Atlanta', '2'], ['Poodle', '900', 'Atlanta', '2']]
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
tb.pack()



container.pack(fill="both")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()










import tkinter as tk
import tktable

def table_test():
    #### DEFINES THE INTERFACE ####
    master = tk.Tk()
    master.geometry('500x200+250+200')
    master.title('Dogs')
    #### DEFINING THE TABLE ####
    tb = tktable.Table(master,
                       state='disabled',
                       width=50,
                       titlerows=1,
                       rows=15,
                       cols=4,
                       colwidth=20)
    columns = ['Breed','Price','Location','Age']
    #### LIST OF LISTS DEFINING THE ROWS AND VALUES IN THOSE ROWS ####
    values = [['Doodle','1500','Chicago','1'],
              ['Pug','700','Kansas City','2'],
              ['Westie','1000','Lincoln','1'],
              ['Aoodle','900','Atlanta','2'],['Poodle','900','Atlanta','2']]
    #### SETS THE DOGS INTO THE TABLE ####
    #### VVVVVVVVVVVVVVVVVVVVVVVVVVV ####
    #DEFINING THE VAR TO USE AS DATA IN TABLE
    var = tktable.ArrayVar(master)
    row_count=0
    col_count=0
    #SETTING COLUMNS
    for col in columns:
        index = "%i,%i" % (row_count,col_count)
        var[index] = col
        col_count+=1
    row_count=1
    col_count=0
    #SETTING DATA IN ROWS
    for row in values:
        for item in row:
            print(item)
            index = "%i,%i" % (row_count,col_count)
            ## PLACING THE VALUE IN THE INDEX CELL POSITION ##
            var[index] = item
            #### IGNORE THIS IF YOU WANT, JUST SETTING SOME CELL COLOR ####
            try:
                if int(item) > 999:
                    tb.tag_cell('green',index)
            except:
                pass
            ###############################################################
            col_count+=1
        col_count=0
        row_count+=1
    #### ABOVE CODE SETS THE DOG INTO THE TABLE ####
    ################################################
    #### VARIABLE PARAMETER SET BELOW ON THE 'TB' USES THE DATA DEFINED ABOVE ####
    tb['variable'] = var
    tb.pack()
    #tb.tag_cell('green',index)
    #tb.tag_configure('green', background='green')
    #### MAINLOOPING ####
    tk.mainloop()
table_test()
'''