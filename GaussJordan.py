import numpy as np
def swap(a,b):
    return b,a

def inversaGJ(a,n):
    id = np.zeros(shape=(n,n))
    for i in range(n-1):
        for j in range(i,i+1):
            id[i][j]= 1.0
    id[n-1][n-1] = 1

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

            aux = a[i][j]
            for o in range(0,n):
                a[i][o] = a[i][o] * (1/aux)
                id[i][o] = id[i][o] * (1/aux)
            for x in range(i+1,n):
                num = a[x][j]/a[i][j]
                for o in range(0,len(a[i])):
                    a[x][o] =(a[i][o]*-num) + a[x][o]
                    id[x][o] = (id[i][o] * -num) + id[x][o]

    aux = a[n-1][n-1]
    for i in range (n):
           a[n-1][i] = a[n-1][i] * (1/aux)
           id[n-1][i] = id[n-1][i] * (1/aux)
    for i in range(n-1,0,-1):
        for j in range(i,i+1):

            for x in range(i-1,-1,-1):
                num = a[x][j]/a[i][j]
                for o in range(n-1,-1,-1):
                    a[x][o] =(a[i][o]*-num) + a[x][o]
                    id[x][o] = (id[i][o] * -num) + id[x][o]
    return id




def solucionGJ(a,vectorA,n):
    vector= np.zeros(shape=(n,n))
    for i in range(n):
        vector[i][0]= vectorA[i]

    id = np.zeros(shape=(n,n))
    for i in range(n-1):
        for j in range(i,i+1):
            id[i][j]= 1.0
    id[n-1][n-1] = 1

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

                    auxVec = vector[i][o]
                    vector[i][o] = vector[cont][o]
                    vector[cont][o] = auxVec

            aux = a[i][j]
            for o in range(0,n):
                a[i][o] = a[i][o] * (1/aux)
                vector[i][o] = vector[i][o] * (1 / aux)
            for x in range(i+1,n):
                num = a[x][j]/a[i][j]
                for o in range(0,len(a[i])):
                    a[x][o] =(a[i][o]*-num) + a[x][o]
                    vector[x][o] = (vector[i][o] * -num) + vector[x][o]

    aux = a[n-1][n-1]
    for i in range (n):
           a[n-1][i] = a[n-1][i] * (1/aux)
           vector[n - 1][i] = vector[n - 1][i] * (1 / aux)
    for i in range(n-1,0,-1):
        for j in range(i,i+1):
            for x in range(i-1,-1,-1):
                num = a[x][j]/a[i][j]
                for o in range(n-1,-1,-1):
                    a[x][o] =(a[i][o]*-num) + a[x][o]
                    vector[x][o] = (vector[i][o] * -num) + vector[x][o]
    resVector=[]
    for i in range(n):
        resVector.append(vector[i][0])
    return resVector

def solucionInversa(a,vector,n):
    inver= np.zeros(shape=(n,n))
    inver = inversaGJ(a,n)
    resultado = inver.dot(vector)
    return resultado
