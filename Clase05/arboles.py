# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:17:00 2022

@author: maria
"""
import csv

#Ejercicio 5.15: Lectura de todos los árboles


archivo = '../Data/arbolado-en-espacios-verdes.csv'

def leer_arboles(nombre_archivo):
    
    with open(nombre_archivo, 'rt', encoding = 'utf8') as f:
        arboleda = []
        rows = csv.reader(f)
        headers = next(rows)
        headers
        row = next(rows)
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
       
        for row in rows:
            arbol = {name: func(val) for name, func, val in zip(headers, types, row)}
            arboleda.append(arbol)
            
        return arboleda

arboleda = leer_arboles(archivo)

   
#%%
#Ejercicio 5.16: Lista de altos de Jacarandá

H=[arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"]
H

#%%
#Ejercicio 5.17: Lista de altos y diámetros de Jacarandá.

altura_diametro = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
altura_diametro

#%%
#Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
diccionario = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
diccionario

#%%
#Ejercicio 6.10: Histograma de altos de Jacarandás

import os
import matplotlib.pyplot as plt

os.path.join('..','Data', 'arbolado-en-espacios-verdes.csv')
arboledad = leer_arboles(archivo)
altos = H
plt.hist(altos, bins=10 )

#Cambiar xy!!!

#%%

#def scatter_hd(lista_de_pares):
    
