# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:48:13 2022

@author: maria
"""

#Ejercicio 9.6: Lectura y seleccion

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

print(df.columns)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]
df_lineal.head()


mas_frecuentes= df_lineal['nombre_cientifico'].value_counts().head(10)
print(mas_frecuentes) #10 especies mas frecuentes

#%%
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
df_lineal_seleccion.head(20)

#%%
#Ejercicio 9.7:Boxplots

df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#Ejemplo de pairplot

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
#!!!! por que no muestra ancho_acera?? porque faltan valores???

#%%