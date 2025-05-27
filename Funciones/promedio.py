
def promedio_dias_internacion(matriz):
    if matriz != []:
        promedio_lista = []
        contador = 0

        for i in range(len(matriz)):
            promedio_lista += [matriz[i][4]]

        cantidad_elementos = len(promedio_lista)

        for i in range(cantidad_elementos):
            contador += promedio_lista[i]

        promedio_final = contador // cantidad_elementos

        print(f"Promedio de dias de internacion {promedio_final}")

        

            
