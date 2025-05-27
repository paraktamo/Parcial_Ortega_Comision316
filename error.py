
def mensaje_error(codigo):
    match codigo:
        case 1:
            print("No hay pacientes cargados en nuestra base de datos")
        case 2:
            print("Dato inválido. Ingreselo nuevamente.")
        case 3:
            print("No hay coincidencias")