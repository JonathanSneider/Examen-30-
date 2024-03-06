import os
import modulos.corefile as cf

def menuss(inventario:dict):
    os.system('cls')
    isrun = True
    while isrun:
        opciones = ["1","2"]
        print('1. registrar producto\n2. salir')
        op = input('Seleccione una opcion : ')
        os.system('cls')
        if op not in opciones:
            print('Seleccione una opcion correcta')
            os.system('pause')
            menuss(inventario)
        else:
            pass
        if op == "1":
            os.system('cls')
            id = input('Ingrese la id del producto : ')
            if id in inventario:
                print('Esta id ya se encuentra registrada')
                os.system('pause')
                menuss(inventario)
            nombre = input('Ingrese el nombre del producto : ')
            valorUnitario = input('Ingrese el valor unitario del producto : ')
            stockmin = input('Ingrese el stock minimo del producto : ')
            stockmax = input('Ingrese el stock max del producto : ')
            inventarioo = {
                "id":id,
                "nombre":nombre,
                "valorUnitario":valorUnitario,
                "stockmin":stockmin,
                "stockmax":stockmax,
            }
            inventario.update({id:inventarioo})
            cf.UpdateFile("productos.json",inventario)
            menuss(inventario)
        if op == "2":
            isrun = False