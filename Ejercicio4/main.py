import modulos.corefile as cf
import modulos.funciones as fn
import modulos.menus as mn
dataa = {
    'Empleados':{},
    'EmpladosNomina':{},
}
nomina = cf.checkFile("nominas.json",dataa)
if __name__ == "__main__":
    isrun = True
    while isrun:
        op = mn.menus()
        if op == "1":
            isrun1 = True
            while isrun1:
                fn.resgempleado(nomina)
                rta1 = 'x'
                while (rta1 not in ['S','s','']):
                    rta1 = input('Desea registrar otro empleado Si(S/s) Enter(No) :')
                    isrun1 = bool(rta1)
        if op == "2":
            isrun2 = True
            while isrun2:
                fn.calcularnomina(nomina)
                rta2 = 'x'
                while (rta2 not in ['S','s','']):
                    rta2 = input('Desea saber la nomina de otro empleado Si(S/s) Enter(No) :')
                    isrun2 = bool(rta2)
        if op == "3":
            pass
        if op == "4":
            isrun = False
