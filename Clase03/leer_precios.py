import csv
from pprint import pprint 
archivo = "../Data/precios.csv" 
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, "r")
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]]=float(row[1])

        except IndexError: 
            pass
    f.close()
    return precios
    

    """fruta = input("Ingrese nombre de fruta/verdura: ")
     
    if fruta in precios:
        
        return print(precios[fruta])
    else:
        print("Esa fruta/verdura no está en la lista")

   
    f.close()"""

precio = leer_precios(archivo)
pprint(precio)




