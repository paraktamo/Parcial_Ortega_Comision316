

def ordenar_pacientes_x_HC(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            for j in range(len(matriz)-i-1):
                if matriz[j][0] > matriz[j+1][0]:
                    aux = matriz[j+1]
                    matriz[j+1] = matriz[j]
                    matriz[j] = aux
        return matriz

