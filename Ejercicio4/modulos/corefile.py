import json 
import os
BASE="Ejercicio4/data/"
#verifica si el json data existe y si no lo crea
def checkFile(archivo:str,data):
    if(os.path.isfile(BASE+ archivo)):
        with open(BASE + archivo ,"r") as bw:
            data = json.load(bw)
            return data
    else:
        with open(BASE+archivo ,"w") as bw:
            json.dump(data,bw,indent=4)
            return data


#Actualizar cualquier informacion      
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'r+') as fw:
        json.dump(data,fw,indent=4)
        fw.truncate()