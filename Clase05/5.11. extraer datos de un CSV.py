# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:33:04 2022

@author: maria
"""

#Ejercicio 5.11: Extraer datos de un archivo CSV
import csv
f = open ('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
headers

select = ['nombre', 'cajones', 'precio']
select

indices = [headers.index(ncolumna) for ncolumna in select]
indices

row =next(rows)
record = {ncolumna:row[index] for ncolumna, index in zip(select,indices)}
record #COMPRENSION DE DICCIONARIO

camion = [{ncolumna:row[indes] for ncolumna,index in zip(select, indices)} for row in rows]
camion
