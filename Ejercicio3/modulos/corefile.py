import json
import os
BASE = "Ejercicio3/data/"
def CheckFile(producto,data:str):
    if(os.path.isfile(BASE+ data)):
        with open(BASE + data ,"r") as bw:
            producto = json.load(bw)
            return producto
    else:
        with open(BASE+data ,"w") as bw:
            json.dump(data,bw,indent=4)



def UpdateFile(archivo,data):
    with open(BASE+ archivo,'r+') as fw:
        json.dump(data,fw,indent=4)
        fw.truncate()


        
