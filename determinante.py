def matrizDzeros(filas, columnas):
    M = []
    while len(M) < filas:
        M.append([])
        while len(M[-1]) < columnas:
            M[-1].append(0.0)
    return M
def copiarMatriz(M):
    filas = len(M)
    columnas = len(M[0])
    MC = matrizDzeros(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            MC[i][j] = M[i][j]
    return MC

def DeterminanteCofactor(A, sumaFinal=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for column in indices:
        subMatriz = copiarMatriz(A)
        subMatriz = subMatriz[1:]
        height = len(subMatriz)
        for i in range(height):
            subMatriz[i] = subMatriz[i][0:column] + subMatriz[i][column + 1:]
        signo = (-1) ** (column % 2)  # F)
        subDeterminante = DeterminanteCofactor(subMatriz)
        sumaFinal += signo * A[0][column] * subDeterminante
    return sumaFinal


