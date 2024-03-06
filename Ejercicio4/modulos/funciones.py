import os
import modulos.corefile as cf
from tabulate import tabulate
def resgempleado(registro):
    os.system('cls')
    id = input('Ingrese el id del empleado : ')
    if id in registro:
        print('el id ya se encuentra registrado')
        os.system('pause')
        resgempleado(registro)
    else:
        pass
    nombre = input('Ingrese el nombre del empleado : ')
    cargos = [["1. Almacenista,"],["2. Jefe IT"],["3. Administrador"],["4. Mensajero"],["5. Gerente"]]
    print(tabulate(cargos, tablefmt="grid"))
    opc = input('Seleccione una opcion : ')
    if opc == "1":
        cargo = "Almacenista"
    elif opc == "2":
        cargo = "Jefe IT"
    elif opc == "3":
        cargo = "Administrador"
    elif opc == "4":
        cargo = "Mensajero"
    elif opc == "5":
        cargo = "Gerente"
    else:
        print('Seleccione una opcion valida')
        os.system('pause')
        return
    try:
        Salario = float(input('Ingrese el salario del empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    empleado = {
        "id":id,
        "nombre":nombre,
        "cargo":cargo,
        "salario":Salario,
    }
    colillas = {
        "id":id,
        "Colillas":{}
    }
    registro["EmpladosNomina"].update({id:colillas})
    registro["Empleados"].update({id:empleado})
    cf.UpdateFile("nominas.json", registro)


def calcularnomina(nomina):
    os.system('cls')
    id = input('Ingrese el id del empleado : ')
    if id not in nomina['Empleados']:
        print('La id del empleado no esta registrada')
        os.system('pause')
        return
    else:
        pass
    try:
        diastrabajados = float(input('Ingrese los dias trabajados por el empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    try:
        horasExtra = float(input('Ingrese las horas extras trabajadas por el empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    try:
        valorDia = float(input('Ingrese el valor trabajado por dia el empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    try:
        descuentoxcafeteria = float(input('Ingrese el descuento por cafeteria del empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    try:
        descuentoxprestamo = float(input('Ingrese el descuento por cuota de prestamo empleado : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    mesPagado = input('Ingrese el mes pagado : ')
    dia = input('Ingrese el dia de la fecha de pago : ')
    mes = input('Ingrese el mes de la fecha de pago : ')
    año = input('Ingrese el año de la fecha de pago : ')
    fechaPago = (f'{dia}/{mes}/{año}')
    sueldobase = (diastrabajados*valorDia)
    valorhorasex = (horasExtra*5500)
    totalapagar = ((diastrabajados*valorDia) + (horasExtra*5500) - (descuentoxcafeteria + descuentoxprestamo))
    cod = str(len(nomina['EmpladosNomina']['Colillas'])+1).zfill(3)
    colilla = {
        "id":id,
        "mespagado":mesPagado,
        "fechapago":fechaPago,
        "sueldobase":sueldobase,
        "valorTotalHrasExtra":valorhorasex,
        "cuotaPrestamo":descuentoxprestamo,
        "descuentoXcafeteria":descuentoxcafeteria,
        "totalapagar":totalapagar

    }
    os.system('cls')
    print(f'El total a pagar por el concepto de nomina al empleado es de {totalapagar}')
    os.system('pause')
    nomina['EmpladosNomina'][id]["Colillas"].update({cod:colilla})
    cf.UpdateFile("nominas.json", nomina)

def buscarsolillas(nomina):
    id = input('Ingrese el id del empleado : ')
    if id not in nomina['Empleados']:
        print('La id del empleado no esta registrada')
        os.system('pause')
        return
    else:
        pass
    comillas = nomina['EmpladosNomina']['Colillas'][id]
    lista =[]
    print(comillas)
