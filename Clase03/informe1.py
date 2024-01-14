

import csv
########################
#LISTA DE TUPLAS
########################

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        return camion 



archivo = '../Data/camion.csv'

camion = leer_camion(archivo)
print(camion)

#total = 0.0
#for s in camion:
 #   total += s[1]*s[2]


total = 0.0
for nombre, cajones, precio in camion:
    total +=cajones *precio
print(total)

#################################################3
#LISTAS DE DICCIONARIOS
###################################################
"""import csv
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



archivo = '../Data/camion.csv'

camion = leer_camion(archivo)

from pprint import pprint 
pprint(camion)

total = 0.0
for s in camion:
    total += s["Cajones"]*s["Precio"]


print(total)"""
