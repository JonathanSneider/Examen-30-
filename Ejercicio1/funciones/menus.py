import os
def menuss():
    runmenus = True
    while runmenus:
        os.system('cls')
        opciones = ["1","2","3","4","5"]
        print('1. Convertir de pesos a dolares\n2. convertir de pesos a euros\n3. convertir de euros a pesos\n4. convertir de pesos a yenes\n5. salir')
        op = input('Seleccione una opcion : ')
        if op not in opciones:
            print('Seleccione una opciones valida')
            os.system('pause')
            menuss()
        else:
            pass
        os.system('cls')
        if op == "1":
            try:
                valor = float(input('Ingrese el valor a pesos que desee convertir a dolares : '))
            except ValueError:
                print('Ingrese un valor valido')
                os.system('pause')
                menuss()
            else:
                pass
            resultado = (valor/3944)
            print(f'{valor} pesos son en total {resultado} dolares')
            os.system('pause')
            continue
        if op == "2":
            try:
                valor = float(input('Ingrese el valor a pesos que desee convertir a euros : '))
            except ValueError:
                print('Ingrese un valor valido')
                os.system('pause')
                menuss()
            else:
                pass
            resultado = (valor/4279)
            print(f'{valor} pesos son en total {resultado} euros')
            os.system('pause')
            continue
        if op == "3":
            try:
                valor = float(input('Ingrese el valor a euros que desee convertir a pesos : '))
            except ValueError:
                print('Ingrese un valor valido')
                os.system('pause')
                menuss()
            else:
                pass
            resultado = (valor*4279)
            print(f'{valor} euros son en total {resultado} pesos')
            os.system('pause')
            continue
        if op == "4":
            try:
                valor = float(input('Ingrese el valor a pesos que desee convertir a yenes : '))
            except ValueError:
                print('Ingrese un valor valido')
                os.system('pause')
                menuss()
            else:
                pass
            resultado = (valor/26.30)
            print(f'{valor} pesos son en total {resultado} yenes')
            os.system('pause')
            continue
        if op == "5":
            runmenus = False