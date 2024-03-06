import os
import modulos.corefile as cf
import modulos.menus as mn
productos = {}
inventario = cf.CheckFile(productos,"productos.json")

if __name__ == "__main__":
    mn.menuss(inventario)