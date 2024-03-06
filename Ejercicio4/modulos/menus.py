import os
import modulos.corefile as cf

def menus():
    os.system('cls')
    opciones = ["1","2","3","4"]
    print('1. Registrar empleado \n2. Calcular valor a pagar por concepto de nomina\n3. Consultar colilla de pago de un empleado\n4. salir')
    op = input('Seleccione una opcion : ')
    if op not in opciones:
        print('Ingrese una opcion valida : ')
        os.system('pause')
        menus()
    else:
        return op
