import os

def menuss(usuarios:dict):
    isrun = True
    while isrun:
        os.system('cls')
        opciones = ["1","2"]
        print('1. registrar usuario\n2. salir')
        op = input('Seleccione una opcion : ')
        if op not in opciones:
            print('Seleccione una opcion valida')
            os.system('pause')
            menuss()
        else:
            pass
        if op == "1":
            id = input('Ingrese el id del usuario : ')
            nombres = input('Ingrese los nombres del usuario : ')
            apellidos = input('Ingrese los apellidos del usuario : ')
            direccion = input('Ingrese la direccion del usuario : ')
            ciudad = input('Ingrese la ciudad del usuario : ')
            longitud = input('Ingrese la longitud : ')
            latitud = input('ingrese la latitud : ')
            email = input('Ingrese el email del usuario : ')
            edad = input('Ingrese la edad del usuario : ')
            ocupacion = input('Ingrese la ocupacion : ')
            registro = {
                "id":id,
                "nombres":nombres,
                "apellidos":apellidos,
                "ubicacion":{
                    "direccion":direccion,
                    "ciudad":ciudad,
                    "longitud":longitud,
                    "latitud":latitud
                },
                "email":email,
                "edad":edad,
                "ocupacion":ocupacion
            }
            usuarios.update({id:registro})
            print(usuarios)
            os.system('pause')
            menuss(usuarios)
        if op == "2":
            isrun = False
