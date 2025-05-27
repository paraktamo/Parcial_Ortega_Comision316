from listado_pacientes import lista_pacientes
from validaciones import validacion_contenido_pacientes
from Funciones.carga_pacientes import cargar_pacientes
from Funciones.mostrar_pacientes import mostrar
from Funciones.buscar_pacientes import buscar_pacientes
from Funciones.ordenar_pacientes import ordenar_pacientes_x_HC
from Funciones.comparaciones_internaciones import *
from Funciones.promedio import promedio_dias_internacion

menu = "Sistema de Gestión de Clínica La Fuerza \n"  \
    "1. Cargar pacientes \n" \
    "2. Mostrar todos los pacientes\n" \
    "3. Buscar pacientes por número de Historia Clinica\n" \
    "4. Ordenar pacientes por número de historia clínica\n" \
    "5. Mostrar paciente con más días de internación\n" \
    "6. Mostrar paciente con menos días de internación\n" \
    "7. Cantidad de pacientes con más de 5 días de internación\n" \
    "8. Promedio de días de internación de todos los pacientes\n" \
    "9. Salir\n"

def mostrar_menu():
    opcion = input(menu)
    while opcion:
        if opcion.isdigit() and 1 <= int(opcion) <= 9:
            opcion = int(opcion)
            return opcion
        else:
            print("Opción no válida")
            opcion = input(menu)

def opcion_menu():
    while True:
        opcion_elegida_controlada = mostrar_menu()
        match opcion_elegida_controlada:
            case 1:
                validacion_contenido_pacientes()
                cargar_pacientes(lista_pacientes)
            case 2:
                validacion_contenido_pacientes()
                mostrar(lista_pacientes)
            case 3:
                validacion_contenido_pacientes()
                buscar_pacientes(lista_pacientes)
            case 4:
                validacion_contenido_pacientes()
                print(ordenar_pacientes_x_HC(lista_pacientes))
            case 5:
                validacion_contenido_pacientes()
                paciente_con_mas_dias(lista_pacientes)
            case 6:
                validacion_contenido_pacientes()
                paciente_con_menos_dias(lista_pacientes)
            case 7:
                validacion_contenido_pacientes()
                paciente_internado_hace(lista_pacientes)
            case 8:
                validacion_contenido_pacientes()
                promedio_dias_internacion(lista_pacientes)
            case 9:
                print("Gracias por usar nuestro portal")
                break


opcion_menu()