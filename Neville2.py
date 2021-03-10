import math
#fx = [7.7339648,7.1997568,6.9761536,6.320844799999998]

#polinomio = input("Dame el polinomio pliiiis: ")


xk = []
fx = []
matriz = []
def Neville(xk,fx,puntoEval,n):
    matriz = []
    for i in range(n + 1):
        matriz.append([])
        for j in range(n + 2):
            matriz[i].append(0)
    for i in range(n + 1):
        x = matriz[i][0]
        matriz[i][1] =fx[i]
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            matriz[j][i + 2] = ((puntoEval - xk[j]) * matriz[j - 1][i + 1] - (puntoEval - xk[j - i - 1]) * matriz[j][i + 1]) / (
                        xk[j - i - 1] - xk[j])
    x = puntoEval
    d=""
    for i in range(n + 1):
        for j in range(n + 2):
            if matriz[i][j] is 0:
                d+="        "
            else:
                d += str("%.5f"%matriz[i][j]) + "      "
        d+="\n"
    print(d)
    print("Raiz: ", matriz[n][n + 1])
    d+="\nRaiz: "+str(matriz[n][n + 1])
    return d

