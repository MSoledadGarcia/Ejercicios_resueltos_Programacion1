

import csv
def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {
                "Nombre" : row[0],
                "Cajones" :  int(row[1]),
                "Precio" : float(row[2])
            }
            camion.append(lote)
        return camion 


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
    


 
def balance (archivo_precios, archivo_camion):
    camion = leer_camion(archivo_camion)
    venta = leer_precios(archivo_precios)
    gasto = 0.0
    ganancia = 0.0
  
    for d in camion:
        gasto += d["Cajones"]* d["Precio"]
        ganancia += venta[d["Nombre"]]*d["Cajones"]
    diferencia = ganancia - gasto
       
    return print(round(diferencia, 2))
   
         
 
archivo_camion= "../Data/camion.csv"
archivo_precios = "../Data/precios.csv"

       
balance(archivo_precios, archivo_camion)


     