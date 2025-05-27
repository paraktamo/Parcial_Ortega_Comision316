
def mostrar(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            print(f"Paciente N°: {matriz[i][0]} . Nombre: {matriz[i][1]} . Edad: {matriz[i][2]} . Diagnóstico: {matriz[i][3]} . Cantidad de días de internación: {matriz[i][4]} \n")
