# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:42:51 2022

@author: maria
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0] : fila[0],
                encabezado[1] : int(fila[1]),
                encabezado[2] : float(fila[2])
            }
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
#estoy reemplazando los elementos de la lista 
