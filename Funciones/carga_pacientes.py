from error import mensaje_error
from validaciones import validacion_string

def cargar_pacientes(lista):
    cantidad_pacientes_a_ingresar = input("Cantidad de pacientes a ingresar: ")

    while not cantidad_pacientes_a_ingresar.isdigit():
        mensaje_error(2)
        cantidad_pacientes_a_ingresar = input("Cantidad de pacientes a ingresar: ")

    cantidad_pacientes_a_ingresar = int(cantidad_pacientes_a_ingresar)
    
    for i in range(cantidad_pacientes_a_ingresar):
        codigo = input("Codigo: ")
        while not codigo.isdigit():
            mensaje_error(2)
            codigo = input("Codigo: ")
        codigo = int(codigo)
        
        nombre = input("Nombre: ")
        while not validacion_string(nombre):
            mensaje_error(2)
            nombre = input("Nombre: ")

        edad = input("Edad: ")
        while not edad.isdigit():
            mensaje_error(2)
            edad = input("Edad: ")
        edad = int(edad)

        diagnostico = input("Diagnóstico: ")
        while not validacion_string(diagnostico):
            mensaje_error(2)
            diagnostico = input("Diagnóstico: ")

        dias_internacion = input("Dias de Internación: ")
        while not dias_internacion.isdigit():
            mensaje_error(2)
            dias_internacion = input("Dias de Internación: ")
        dias_internacion = int(dias_internacion)

        lista += [[codigo, nombre, edad, diagnostico, dias_internacion]]

        print(f"Se ha ingresado \n"
            f"Codigo: {codigo} \n" \
            f"Nombre: {nombre} \n" \
            f"Edad: {edad} \n" \
            f"Diagnóstico: {diagnostico} \n" \
            f"Dias de Internación: {dias_internacion}")
        
    print("Carga Exitosa")
    print(lista)
    