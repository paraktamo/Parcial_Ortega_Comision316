from error import mensaje_error
from listado_pacientes import lista_pacientes

def validacion_entrada_numero(entero: int) -> bool: 
    return entero.isdigit()

def validacion_contenido_pacientes():
    if lista_pacientes == []:
        mensaje_error(1)

def validacion_string(entrada):
    return entrada != ""
