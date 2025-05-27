from error import mensaje_error
def buscar_pacientes(matriz):
    if matriz != []:
        historia_clinica = input("Ingrese codigo de Historia Clinica: ")
        flag = False

        if historia_clinica.isdigit():
            historia_clinica = int(historia_clinica)
            for i in range(len(matriz)):
                if matriz[i][0] == historia_clinica:
                    print(f"HC: {historia_clinica} \n"
                        f"Nombre: {matriz[i][1]} \n"
                        f"Edad: {matriz[i][2]} \n"
                        f"Diagnostico: {matriz[i][3]} \n"
                        f"Cantidad de dias de internacion: {matriz[i][4]} \n")
                    flag = True
                    return i
            
            if flag == False:
                mensaje_error(3)


