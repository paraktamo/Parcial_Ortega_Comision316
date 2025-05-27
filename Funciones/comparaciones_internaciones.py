

def paciente_con_mas_dias(matriz):
    if matriz != []:
        mas_dias = [0, "", 0 , "", 0]

        for i in range(len(matriz)):
            if matriz[i][4] > mas_dias[4]:
                mas_dias = matriz[i]

        print(f"HC: {mas_dias[0]} \n"
            f"Nombre: {mas_dias[1]} \n"
            f"Edad: {mas_dias[2]} \n"
            f"Diagnostico: {mas_dias[3]} \n"
            f"Cantidad de dias de internacion: {mas_dias[4]} \n")
        


def paciente_con_menos_dias(matriz):
    if matriz != []:
        menos_dias = matriz[0]

        for i in range(len(matriz)):
            if matriz[i][4] < menos_dias[4]:
                menos_dias = matriz[i]

        print(f"HC: {menos_dias[0]} \n"
            f"Nombre: {menos_dias[1]} \n"
            f"Edad: {menos_dias[2]} \n"
            f"Diagnostico: {menos_dias[3]} \n"
            f"Cantidad de dias de internacion: {menos_dias[4]} \n")


def paciente_internado_hace(matriz):
    if matriz != []:
        dias = 5
        internados_hace_mas_de = []

        for i in range(len(matriz)):
            if matriz[i][4] > dias:
                internados_hace_mas_de += [matriz[i]]
        
        print(len(internados_hace_mas_de))

