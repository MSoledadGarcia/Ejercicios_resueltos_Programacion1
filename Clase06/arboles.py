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
len(altura_diametro)

#%%
#Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#diccionario = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
#diccionario


def medidas_de_especies(especies,arboleda):
    diccionario = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return diccionario


medidas= medidas_de_especies(especies,arboleda)
medidas

#%%
#Ejercicio 6.10: Histograma de altos de Jacarandás

import os
import matplotlib.pyplot as plt

os.path.join('..','Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(archivo)
altos = H
plt.hist(altos, bins=10, color="lightcoral")
plt.title("Alturas de Jacarandá en la Ciudad de Buenos Aires")
plt.xlabel('Altura (m)')
plt.ylabel("Cantidad de ejemplares")




#%%
#Ejercicio 6.11: Scatterplot (diámetro vs alto) de Jacarandás

import numpy as np
import matplotlib.pyplot as plt


a_d = np.array(altura_diametro)
a = a_d[0:, 0]
a
d = a_d[0:,1]
d

def scatter_hd(x,y):
    plt.scatter(x, y, marker = "*", c= "y", alpha= 0.45)
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlabel("Diámetro (cm)")
    plt.ylabel("Alto (m)")
    return plt.show
    
scatter_hd(d,a) 

#%%
#Ejercicio 6.12: Scatterplot para diferentes especies

import os
import matplotlib.pyplot as plt
import numpy as np

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

#Eucalipto

eucalipto = np.array(medidas["Eucalipto"])
eucalipto_a = eucalipto[0:,0]
eucalipto_d = eucalipto[0:,1] 

plt.scatter(eucalipto_a, eucalipto_d, marker="D", c= "forestgreen", alpha= 0.45 )
plt.title("Relación altura-diámetro para Eucalipto")
plt.ylabel("Diámetro (cm)")
plt.xlabel("Alto (m)")
plt.xlim(0,50) 
plt.ylim(0,200)
#Palo Borracho Rosado
#%%
palo_borr = np.array(medidas["Palo borracho rosado"])
palo_borr_a = palo_borr[0:,0]
palo_borr_d = palo_borr[0:,1] 

plt.scatter(palo_borr_a, palo_borr_d, marker="2", c="sienna", alpha=0.5 )
plt.title("Relación altura-diámetro para Palo Borracho")
plt.ylabel("Diámetro (cm)")
plt.xlabel("Alto (m)")
plt.xlim(0,25) 
plt.ylim(0,100)
#%%

#Jacarandá
jacaranda = np.array(medidas["Jacarandá"])
jacaranda_a = jacaranda[0:,0]
jacaranda_d = jacaranda[0:,1] 

plt.scatter(jacaranda_a, jacaranda_d, marker=">", c="y", alpha = 0.6)
plt.title("Relación altura-diámetro para Jacarandá")
plt.ylabel("Diámetro (cm)")
plt.xlabel("Alto (m)")
plt.xlim(0,30) 
plt.ylim(0,100)






